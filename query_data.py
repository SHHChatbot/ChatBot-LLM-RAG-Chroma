import argparse
from dataclasses import dataclass
from langchain.vectorstores.chroma import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain_openai import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
import requests
import io
import os
import PIL.Image

CHROMA_PATH = "chroma"
PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

API_URL = "https://api-inference.huggingface.co/models/SaiRaj03/Text_To_Image"
HEADERS = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}
TRANSLATION_API_URL1 = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-fr"
TRANSLATION_API_URL = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-fr-en"


# Initialize a counter to keep track of the number of generated images
image_counter = 1

def generate_image(text):
    global image_counter
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": text})
    if response.status_code == 200:  # Check if the API call was successful
        try:
            image_bytes = response.content
            if image_bytes:  # Check if image bytes are not empty
                image = PIL.Image.open(io.BytesIO(image_bytes))
                # Save the image with a unique filename based on the counter
                filename = f"generated_image_{image_counter}.jpg"
                filepath = os.path.join("images", filename)
                image.save(filepath)
                print(f"Image '{filename}' saved successfully.")
                image_counter += 1
            else:
                print("Error: Empty image bytes received.")
        except PIL.UnidentifiedImageError:
            print("Error: Unsupported image format.")
    else:
        print("Error:", response.text)



def translate_to_french(text):
    chunk_size = 100  # Define the chunk size
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]  # Split text into chunks
    translated_chunks = []
    for chunk in chunks:
        response = requests.post(TRANSLATION_API_URL1, headers=HEADERS, json={"inputs": chunk})
        translated_text = response.json()
        if translated_text and isinstance(translated_text, list) and "translation_text" in translated_text[0]:
            translated_chunks.append(translated_text[0]["translation_text"])  # Extract translation from response
    return " ".join(translated_chunks)  # Combine translated chunks into a single string

def translate_to_english(text):
    response = requests.post(TRANSLATION_API_URL, headers=HEADERS, json={"inputs": text})
    translated_text = response.json()
    if translated_text and isinstance(translated_text, list) and "translation_text" in translated_text[0]:
        return translated_text[0]["translation_text"]
    else:
        return None



def chat_with_bot():
    # Add your OpenAI API key here
    openai_api_key = "YOUR_OPENAI_KEY"

    # Prepare the DB.
    embedding_function = OpenAIEmbeddings(openai_api_key=openai_api_key)
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    print("Welcome to the Chatbot! Type 'quit' to exit.")

    while True:
        user_input_fr = input("Vous: ").strip()  # Prompt the user in French

        if user_input_fr.lower() == "quit":
            print("Au revoir!")
            break

        # Translate user input from French to English
        user_input_en = translate_to_english(user_input_fr)

        if user_input_en is None:
            print("Erreur lors de la traduction.")
            continue

        # Search the DB.
        results = db.similarity_search_with_relevance_scores(user_input_en, k=3)
        if len(results) == 0 or results[0][1] < 0.7:
            print("Impossible de trouver des résultats correspondants.")
            continue

        context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        prompt = prompt_template.format(context=context_text, question=user_input_en)

        model = ChatOpenAI(openai_api_key=openai_api_key)
        response = model.invoke(prompt)

        # Extracting content from response
        content = response.content

        # Translate the response to French
        translated_response = translate_to_french(content)

        print("Bot (French):", translated_response)

        # Generate an image based on the bot's response
        generate_image(content)

if __name__ == "__main__":
    chat_with_bot()