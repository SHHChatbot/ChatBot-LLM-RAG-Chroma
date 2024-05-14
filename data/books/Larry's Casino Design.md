<a name="br1"></a> 

Leisure Suit Larry’s

Casino

Game Design Document

Copyright 1997 by Al Lowe

for Sierra On-Line, Inc.



<a name="br2"></a> 

Leisure Suit Larry’s Casino Design Document

Page 2

Copyright 1997 by Al Lowe

Table of Contents

Table of Contents.........................................................................................................................................................2

Overview.......................................................................................................................................................................3

Off-Line Versus On-Line Play ...............................................................................................................................4

The Games..............................................................................................................................................................5

Spending Your Winnings .......................................................................................................................................6

Marketing.....................................................................................................................................................................7

Scene-By-Scene Description........................................................................................................................................8

0's, Miscellaneous Animation.................................................................................................................................8

1000\. User Interface.......................................................................................................................................................... 8

2000\. SIGS User Interface ................................................................................................................................................ 9

3000\. Cards, Chips, Gambling Pieces............................................................................................................................... 9

5000\. Characters' Personas................................................................................................................................................ 9

7000\. Leisure Suit Larry ................................................................................................................................................. 13

100's, Opening......................................................................................................................................................14

100\. Sierra Screen & Video ............................................................................................................................................ 14

110\. Larry Casino Title Screen ....................................................................................................................................... 14

150\. World Map.............................................................................................................................................................. 14

200's, Hotel Room................................................................................................................................................14

210\. The Closet............................................................................................................................................................... 15

220\. Hot Tub................................................................................................................................................................... 16

230\. CYBERLARRY 2000.............................................................................................................................................. 16

270\. Mirror...................................................................................................................................................................... 16

300’s, Casino........................................................................................................................................................17

300\. Casino Lobby.......................................................................................................................................................... 17

310\. Casino Floor, Inner Circle....................................................................................................................................... 18

320\. Casino Floor, Outer Circle...................................................................................................................................... 18

340\. Elevators ................................................................................................................................................................. 18

350\. Restaurants.............................................................................................................................................................. 19

360\. Bars......................................................................................................................................................................... 19

370\. Gift Shop................................................................................................................................................................. 19

380\. Hotel Front Desk..................................................................................................................................................... 20

390\. Quiki-Wed Wedding Chapel................................................................................................................................... 20

391\. Quiki-Wed Wedding Chapel Wedding ................................................................................................................... 20

400-600's, Casino Games .....................................................................................................................................20

400\. Poker....................................................................................................................................................................... 20

450\. Blackjack ................................................................................................................................................................ 20

500\. Craps....................................................................................................................................................................... 20

550\. Roulette................................................................................................................................................................... 20

600\. Wheel of Fortune .................................................................................................................................................... 20

700's, Slots............................................................................................................................................................21

700\. Slots Long Shot....................................................................................................................................................... 21

710\. Slots, A.................................................................................................................................................................... 21

720\. Slots, B.................................................................................................................................................................... 21

730\. Slots, C.................................................................................................................................................................... 21

740\. Slots, D.................................................................................................................................................................... 21

800's, Party Games ...............................................................................................................................................21

800\. Say What?!.............................................................................................................................................................. 23

810\. The Bottom Line..................................................................................................................................................... 24

820\. Pickup Master ......................................................................................................................................................... 26

830\. Larry's Comedy Club .............................................................................................................................................. 27

Sound ..........................................................................................................................................................................30

Miscellaneous .............................................................................................................................................................31



<a name="br3"></a> 

Leisure Suit Larry’s Casino Design Document

Page 3

Copyright 1997 by Al Lowe

Overview

History

Eight years ago, a modem-based multi-player adventure game called LarryLand was the impetus behind the

birth of INN. After six months of waiting for a working multi-player graphic adventure game engine, the project was

dropped. Three years later, INN implemented a shadow of the original design creating a Larry-theme casino with

adult on-line chat, but little more. Still, for its time, it was extremely popular.

Today

Using the existing Hoyle’s Casino code base as a starting point for a totally new product, Larry’s Casino in-

cludes all the Hoyle’s stand-alone gambling games, but with total Internet involvement. It doesn’t require Internet

access, but is more fun with it. It creates a fantasy world emphasizing Larry’s two key ingredients: humor and sexual

titillation.

Gamble in a safe, anonymous environment where adults can be as naughty or nice as they like, act out their fan-

tasies, and play the role of their favorite character from a Larry game (even cross-dressing if they like). Meet other

people, gamble, chat, even share your hotel room with them. Nothing hard-core nor pornographic, just funny, silly,

slapstick, good-natured adult fun. It is aimed at an audience Hoyle’s has missed completely.

The key concept here is to “keep it simple.” While it would be fun to create avatars, wander around through a

third-person virtual world like The Realm, going from casino to disco to hot tub, gambling, drinking, chatting, danc-

ing, swimming, hot-tubbing, etc., and make every participant’s every attribute completely tweakable, it’s just not

viable economically. Larry’s Casino takes a more conservative, first-person approach, one that includes all the

Hoyle games and adds Internet chat everywhere, in all the games, in bars, clubs, and hotel rooms.

Financial Model

Larry’s Casino combines the battle.net “pay once up front” retail model with the “interstitial” advertising of

Berkeley’s Jack games. The casino games themselves are ad-free, since they are included in the purchase price. The

four additional “party games” do contain ads, since they’re not part of the casino per se. We should be able to get

national advertisers to sponsor various tournaments, i.e. the “Jack Daniels Poker Quest,” the “Chevrolet Blackjack”

challenge, etc.

Theme

Once again, Leisure Suit Larry’s life seems too good to be true: lucky Larry is picked “at random” to create and

“front” a casino. He even gets to create it in “his image.” Imagine how Larry would decorate if he had millions of

dollars to spend? He makes regular appearances in his homage du weirdness. Only after much conversation with on-

line Larry will players eventually learn the truth: once again, Larry is merely the stooge, a puppet fronting “his” ca-

sino for its mob owners.

One running gag here is Larry seems to be the casino’s only employee. He hosts every game, works every

counter, sells every ticket, changes every dollar. He’s not the only employee, of course, but it seems that way. He

scurries into every scene shortly after you do.

Goals

Our goals are fun, gambling, chat, harmless sex, and humor. In addition, we want to balance the importance of

on-line and off-line play; provide a reason for winning; provide consequences for losing, provide a fun way to obtain

additional funds; provide Internet play for all the games; completely integrate SIGS into all the games; and stream-

line the method of moving between games.



<a name="br4"></a> 

Leisure Suit Larry’s Casino Design Document

Page 4

Copyright 1997 by Al Lowe

Off-Line Versus On-Line Play

Off-Line

Off-line play is functionally the same as the current Hoyle’s Casino. You can play any of Hoyle’s five games:

blackjack, poker, craps, roulette, or slots, plus two new games: wheel of fortune and on-track race betting. You play

as a character from a previous Larry game and against other characters from previous games. Off-line winnings do

not transfer to on-line play; they are only practice. You can have all the money you want, with “unlimited refills,”

but you are always reminded this is practice only. It is unusable in the on-line only hotel, restaurants, gift shop, etc.

Larry’s Casino offers no instructional play. It only corrects you when you make mistakes. It prompts you for

bets as necessary. It does not teach strategy. Larry serves as your (just barely off-screen) dealer, complete with his

own personal Larryesque dealer-type remarks.

Since all the casino games are played at gambling tables built inside hot tubs, and everyone must disrobe before

entering the hot tub, everyone gambles naked! But since we never see anyone transition into or out of a tub, there’s

no nudity.

Preparation

The game begins in your room. In order to leave your room, you must “get dressed” by going to your closet and

selecting a persona from the collection of favorite characters from old Larry games. You can see yourself in the

bathroom mirror, but only from the chest up as none of the personas have full bodies (to cut down on the amount of

animation). Since we only see them from the chest up, our investment is in facial emotion and expressions. Once

“dressed,” you can access the map and head “downstairs” to the casino proper. You have free reign of the entire

casino, although certain aspects of the game make no sense off-line, and thus require you to “sign on” first.

On-Line

Preparation

You prepare just as you do for single-player, off-line mode. Pick a persona before leaving your room, access the

map, go down the elevator, enter the casino, move to the gaming table of your choice.

Accessing the Games

You use the map to leave your room. You access the map by right-clicking the mouse to bring up a pop-up

menu just as in Leisure Suit Larry 7: Love for Sail! In many parts of the game, you may also point and click your

way through pictures.

As seemingly the casino’s sole employee, Larry appears throughout the game and is the only character with

whom you may interact. He has many lines of dialogue, some reminiscing about when your character met him in a

previous game. We keep track of each player’s conversations with Larry to prevent repetition. Other roaming char-

acters (waitresses, cigar girls, photographers, etc.) are generic and non-interactive.

Regardless, when you stop moving around and finally click on a gaming table, you are placed in the hot tub and

the game begins. At any time, you can choose “Internet play” from the right-click menu to go on-line. You are then

presented with the SIGS interface, positioned to begin the type of game you previously chose. Do the SIGS thing,

get up a group to play, and when you return, you are all naked in the bubbling waters of the hot tub, at the gambling

table for your particular game. You can’t see yourself (other than your toes) or Larry, who is always the dealer, but

you can see four of your opponents.

On-line chat uses comic book-style cartoon balloons to indicate who said what. You can change the colors of

your text and bubble background.

Winnings, Busting & Finances

Larry’s Casino has a real on-line economy, with ways to win, lose, earn and spend Larrybucks. You begin with

a few Larrybucks and get to keep what you win. Or, if you go bust, you must use the “party games” (described be-

low) to earn another stake. Your account balance is saved on our server between on-line sessions. Spend your



<a name="br5"></a> 

Leisure Suit Larry’s Casino Design Document

Page 5

Copyright 1997 by Al Lowe

Larrybucks on gifts, drinks, and enhanced chat areas: bars, clubs, hotel rooms, penthouse, dinners, even a wedding

in the Chapel O’ Love, starring Larry doing his best (goofiest) Elvis impersonation.

You can purchase gifts at the casino gift shop before you enter the game. Then, once you are connected through

SIGS, you can give presents from your Inventory to the other characters at your table.

You can invite the other characters to “private” chat areas, like bars, restaurants, and your room (although per-

haps you should pop for an upgraded room first).

The Games

Six Casino Games

All casino table games are functionally like Hoyle’s, but with a more realistic perspective and animated charac-

ters sitting across from you…naked. (Of course, since everyone is in water to their chest, you can’t see anything.)

The games include Blackjack, Poker, Craps, Roulette, Wheel of Fortune. The weird Nude JetSki Racing betting is

handled differently (or maybe not at all, if we run out of time).

Four Party Games

All four party games (Say What?!, The Bottom Line, Pickup Master, and Larry’s Comedy Club) are on-line,

chatty, text-based, self-authoring, self-scoring games inspired by Berkeley’s Acrophobia. They all make use of

(Berkeley’s YDKJ-style) interstitial advertising. Party game participants award Larrybucks to each game’s winner

with no money coming out of their pockets. There is no betting. There is a minimum of two players and a maximum

limited only by how many text entries each game can simultaneously display on-screen. Players can enter, leave,

and/or reenter games between rounds. They get to keep any Larrybucks accumulated even if they leave before the

end of the game.

Larry’s Comedy Club

…is an interactive, on-line, joke-telling contest. Each player has 60 seconds to type in a joke, which is stored

and then fed back to the group to vote on. The other players then award each joke Larrybucks as they see fit. To

prevent offending sensitive Larry players, there are three different rooms featuring varied levels of cleaniness: a tiny

“Sunday School Clean Room,” a nightclub-sized “Club Risqué,” and the Kingdome of comedy, “Raunchy Dome.”

The Bottom Line

…is an interactive, on-line, story writing game. Each player has 60 seconds to write the first line of a story. The

computer collects all the lines and when the time is up, displays all the lines. Everyone votes on which line they

want to keep. The winning line gets Larrybucks. The story then continues on, until everyone is tired of writing or

they agree to an ending. Results can be saved as a text file on the users’ hard disks. The best stories will, of course,

be submitted for storage in our on-line archives, perhaps even published as a book, The Leisure Suit Larry Stories:

On-Line and Stupid!

Pickup Master

…is an interactive, on-line, pickup line contest. Each player has 60 seconds to submit a topic, the computer col-

lects everyone’s topics and when time is up, offers one topic. Everyone then has another 60 seconds to type in a

pick-up line relating to that topic. When time is up, all the pick-up lines are displayed and everyone votes for the

best line. The winning line gets Larrybucks. All lines become the property of Al Lowe, who promises to use the best

ones in future Larry adventure games.

Say What?!

…is an interactive, on-line, word definition game. Each player has 60 seconds to type in a real word and its real

definition. The computer collects everyone’s words and definitions and when time is up, presents one of the submit-

ted words. Everyone then has another 60 seconds to type in his best fake definition of that word. The computer

collects all the definitions and when time is up, displays the word and all the submitted fake definitions plus the real



<a name="br6"></a> 

Leisure Suit Larry’s Casino Design Document

Page 6

Copyright 1997 by Al Lowe

definition. Everyone votes on which definition they think is the real one. The definition with the most votes wins

Larrybucks. The real definition is then displayed, but gets no reward, unless it was the high vote receiver.

Spending Your Winnings

Since on-line players need something to do with their winnings, we provide a variety of settings. Of course, you

and I know they are merely accessing areas that have been on their CD-ROMs all along.

There are three bar chat areas, where you can buy drinks for your friends while chatting. Of course, Larry is the

only waiter. There are also three restaurant chat areas, for private or group food and chat. The bars and the restau-

rants come in three quality levels: cheap, nicer, and plush. The difference? Primarily on-screen graphics and the

number of Larrybucks stuff costs in each area.

When you win at the gaming tables, you can “toke” the dealer.

Cigarette girls roam the tables selling “inhale-only” smokes, which offend no one (and require no expensive

animation).

A gift shop sells a variety of objects that enter your inventory. Later, while you’re gambling on-line, you may

give these gifts to others at your table.

The hotel’s front desk sells you upgraded hotel rooms that you get to keep and are then available for private

“chat sessions” with your guests.

A wedding chapel is available (for many Larrybucks) where you can stage an “on-line marriage,” valid for at

least the night, by Leisure Suit Larry impersonating an Elvis impersonator.



<a name="br7"></a> 

Leisure Suit Larry’s Casino Design Document

Page 7

Copyright 1997 by Al Lowe

Marketing

Box Points

•

•

•

•

•

•

•

Leisure Suit Larry humor

Gambling

Internet play

New CYBERFACE 2000 Chat

Recall LarryLand for those who remember

Larry is your on-screen host

You are your favorite character from Larry game

Differences From Hoyle’s Casino

•

•

•

•

More fun

All games play on-line

Internet play designed in from beginning

Leisure Suit Larry’s risqué humor and mild titillation plus Internet casino play and on-line chat says “Fun!”

Selling Points

•

•

•

•

•

•

•

Gambling off-line, or with others on the Internet

Be the character you enjoyed.

A fantasy world for adults only

CYBERFACE 2000 Chat while you gamble on-line

Win a fortune, then adjourn to a private room with your special someone

Live the Leisure Suit Larry experience. (Or better yet, don’t!)

Visit the wedding chapel and get hitched (for the evening) by Larry doing his Elvis impersonation.

Goals

•

•

Reach a new market that probably doesn’t buy Hoyle’s

Leverage off our installed base of Larry fans

Questions

1\. How are the interstitial ads updated?

2\. How are the ads scheduled?

3\. Are there time limits?

4\. Do we sell time in 5-second multiples? Or have fixed time periods like 10, 15, 20 or 30 seconds?

5\. Who manages the money, times, graphics, etc.?



<a name="br8"></a> 

Leisure Suit Larry’s Casino Design Document

Page 8

Copyright 1997 by Al Lowe

Scene-By-Scene Description

0's, Miscellaneous Animation

1000\. User Interface

The 1000 numbers include everything that is shared globally: menus, cursors, icons, etc.

Menus

Rock Hard

Map

Internet play

The right-click menu will contain at least the following items (more will probably follow as

we discover what I’ve forgotten!).

My Stuff… Title Bar

Options…

Help

Exit

This only says “Rock Hard” if that’s the player’s chosen persona.

Map

Takes you to the Map without leaving the current scene so in case you cancel while on the

Map, you’ll still be exactly where you were. While in the Map, this menu item changes to “Return from Map.”

Internet play

Takes you to SIGS. If you are not in a game, lets you select the game in SIGS, then takes you there. If you are

already gambling, you remain in your chosen game. When you return, your on-line sign-up mates are there with

you.

Stuff…

Stuff

Opens a hierarchical menu off the side listing all the “stuff” you have in Inventory,

which at the very least includes money and probably other things you’ve bought or been

given. Left-clicking on one of the items expands another layer of menu of verbs that in-

cludes “give” if the item is “giftable.” Give then has a sub-menu that lists all the people in

your immediate “chat area.”

Money $5000.00

Cigars

3

2

Condoms

Disinfectant

Roses

1

12

Options…

Goes to a tabbed dialog with all the choices in Hoyle’s “Controls” dialog, except “Attitude.” Added to the

Hoyle’s collection will be individual tabs for each of the games, allowing players to customize everything we think

may ever be annoying. (For examples, see Office ’97’s “Tools | Options” menu item.) Each game’s specifics are

under that game. Going to Options from within a game opens to that game’s sheet. Going to Options from anywhere

else opens to the General sheet. Here are just a few of the many items available to futz with:

Text color (of text you send to others)

Background color (of text you send to others)

Reading speed (for others’ cartoon bubbles)

Help

Takes you to the standard Windows Help system, and Al’s rip-off of Hoyle’s help system.

Exit

Sure, ask ‘em to confirm, but if they do, don’t display a commercial, just get the hell out!

Chat Bubble

Chat is displayed inside a rounded-corner rectangle, with one corner replaced with a comma shape leading from

the persona’s mouth. Bubbles scale to fit the text typed. The left personas’ bubbles go to the right, while the right

personas’ bubbles go to the left; the inner personas’ bubbles go above, while the outer personas’ bubbles go below.

Each bubble attempts to not cover other bubbles, although that seems impossible. Keep them gracefully shaped and

proportionate (i.e., approximately 3x5 proportions), rather than rigid and within fixed boundaries.



<a name="br9"></a> 

Leisure Suit Larry’s Casino Design Document

Page 9

Copyright 1997 by Al Lowe

Players can set their text and background color preferences, which is stored in their preferences file on their

hard drive.

CYBERFACE 2000

A 3x3 grid (remember CyberSniff 2000 of Larry 7?) of emotions is displayed beside our chat’s typing input.

Every character shares the same CYBERFACE 2000, it does not vary with the personality. The grid contains icons

representing 8 emotions, with the center square indicating “normal” or “nothing” (the default). If you actually type

any of the corresponding emoticons, the corresponding CYBERFACE 2000 button is automatically depressed for

you. Or, you can click an emotion on the grid. When the player presses Enter or the Send button, the text is sent with

a header containing the corresponding emotion. The other members of the chat group then see our player’s persona’s

corresponding loop do an end of loop, remain until the message’s chat bubble disappears, then do a beginning of

loop back to normal.

\#

1

2

3

4

5

6

7

8

9

Emoticon

:) :-)

<g> rofl lol

3:| 3:-|

:( :-(

:O :-O

\8) 8-)

;) ;-)

:P :-P

Description

Smile

Laugh

thinking hard

Frown

Shocked

Surprise

Wink

tongue out, rude, Bronx cheer, etc.

nothing, normal, no emotion (center button)

2000\. SIGS User Interface

Since all of the SIGS interface is shared by multiple areas, dump all the SIGS crap here.

3000\. Cards, Chips, Gambling Pieces

The 3000 section is for gaming pieces used in multiple areas. Objects that are not shared are numbered with

their respective rooms.

5000\. Characters' Personas

Each character has a background bitmap that includes all of the visible portion of their body, eye blinks, 8 loops

of different facial expressions/emotions, two loops of bubble animation to hide their, ahem, inflexible body angle,

and at least one fidget loop where they do something representative of their character. Each of the emotion loops

covers the minimal portion of the face necessary. The first 8 numbers correspond to the positions on the

CYBERFACE 2000 grid displayed during chat typing.

Persona loops are numbered as follows:

0

background bitmap

1-8 see CYBERFACE 2000 above

eye blinks

9

10 bubbles, inside angle

11 bubbles, outside angle

12 fidget 1, etc.

13 fidget 2, etc.

In single player mode, each casino game shows four random, unique characters from the set of twenty available.

Characters speak one at a time, never interrupting each other. Each head chooses an appropriate message from its



<a name="br10"></a> 

Leisure Suit Larry’s Casino Design Document

Page 10

Copyright 1997 by Al Lowe

own message file. In Multi-Player mode, display as many heads as there are players in the game, filling from the

center out (from left-to-right: 2, 3, 1, 4). Heads respond to player control, based on typed (or clicked) emoticons.

The following characters have personas. The Leisure Suit Larry game(s) in which they appeared are inside pa-

renthesis.

Women

~~5000~~ ~~Passionate Patti (2,3,5)~~

~~Patti is not young any more, worldly wise, hip, happening, in other words, she’s everything Larry is not. She~~

~~only plays famous airport hotel cocktail lounges because that’s where the businessmen are.~~

~~Our next selection is the hip, the happ’ning, Passionate Patti, who played a starring role in “Leisure Suit Larry~~

~~5: Passionate Patti Does a Little Undercover Work.” If you choose to play as Patti, expect nothing but the finest.~~

~~Expect traveling salesmen to hustle you everywhere. Expect the world, but, of course, as with everything else in life,~~

~~you’ll probably just end up disappointed. I know I am, working here in the God-forsaken studio. Reading these same~~

~~lines over and over, just waiting for the sweet bird of death to fly me away to a better place, a place, (REALIZE~~

~~MIKE IS LIVE) (ENTHUSIASTICALLY AGAIN) a place for you to have loads of fun is: Leisure Suit Larry’s Ca-~~

~~sino. Just select Passionate Patti and head downstairs. (QUIETLY) A small charge will be subtracted from your~~

~~winnings.~~

5100 Drew Baringmore (7)

Beautiful, young, intelligent, perpetually-naked aeronautical industry leader biographer nudist, Drew spends as

much time as possible naked. She’s completely comfortable with her body, her nudity, and her many abilities.

Next up is the beautiful, young, intelligent, perpetually-naked aeronautical industry leader biographer nudist,

Drew Baringmore! As you must remember from “LEISURE Suit Larry 7: Love for Sail!”, Drew spends as much of

her time as possible naked, so if you choose to become Drew, you’ll fit right in downstairs in Larry’s Casino. I

really loved how Drew got the best of Larry, leading him along, teasing him, making him think he was going to get

lucky, before… Oh, wait. Was that Drew? Or was it…every other woman in any Leisure Suit Larry game!! Well, if

you choose Drew, you’ll pick at least one winner tonight, that’s for sure!

5200 Cavaricchi Vuarnet (6)

Beautiful young bisexual aerobics instructor, with a great body, short hair with lots of mousse, a tough, no non-

sense girl with well-defined muscles, hard. She’s more than willing to meet Larry tit-for-tat.

Well now, who have we next to offer your shopping pleasure? Oh, this must be the one you want! Tired of be-

ing hit on by men? How about this persona? Ready for a woman that’s not just another pretty face? Consider this

little number right here. Cavaricchi Vuarnet. Cav was featured in “Leisure Suit Larry 6: Shape Up or Ship Out!” As

poor Larry found out, she enjoys hitting on the girls herself. She was more than willing to meet Larry tit-for-tat. This

beautiful young bisexual aerobics instructor has a great body and rock-hard, perfectly-defined muscles. Yes, Cava-

ricchi is one tough, no-nonsense woman. You won’t go wrong with her. Just press the “BUY” button now and be

Cav tonight!

5300 Annette Boning (7)

A mysterious, dark-haired, film noire woman of the night. A gold-digger who married old Mr. Boning, never

realizing his name referred to his sexual appetite. She’s dressed in a classy 40’s black suit, with a large black floppy

hat. She wanted someone willing (or stupid enough) to commit murder…and she’ll do anything to get him.

Moving now to a mysterious woman of the night, the beautiful Annette Boning. Annette was that dark-haired,

film noire woman in “Leisure Suit Larry 7: Love for Sail!” Well, sure maybe in the game she was not such a nice

girl…actually she was a gold-digger who only married poor old Mr. Boning for his money! But the laugh was on

her. She never realized the old boy’s name referred to his prodigious sexual appetite. She tried to get Larry to com-

mit murder for her, but fortunately Larry was too clumsy to even get started. Now just take a look at her here. Isn’t

she lovely? Well, of course, here she looks kind of naked, but usually she looks a lot classier. She usually dresses in

a classic 1940’s black suit, and she loves to wear those big black floppy hats. So pick Annette. Enjoy your evening.

People are dying to meet you!



<a name="br11"></a> 

Leisure Suit Larry’s Casino Design Document

Page 11

Copyright 1997 by Al Lowe

~~5400~~ ~~Kalalau (3)~~

~~Hawaiian beauty. Larry 3 has such primitive graphics, you may as well start from scratch on this one.~~

~~Oh, you remember Kalalau, don’t you? From that famous first appearance in “Leisure Suit Larry 2: Goes Look-~~

~~ing for Love (in Several Wrong Places)” where she was standing in the surf, naked to the waist, until that fateful~~

~~opening scene in “Leisure Suit Larry 3: Passionate Patti in Pursuit of the Pulsating Pectorals,” Kalalau was Larry’s~~

~~first true love. She was the lovely native island beauty, the daughter of royalty, for whose hand Larry was willing to~~

~~do anything, even learn assembly language. And for what? A few months of what Larry thought was bliss, only to~~

~~discover she had left him for another woman! Still, you don’t have to worry. It’s only a persona to you. Choose~~

~~Kalalau,~~  ~~and really enjoy soaking in those gambling hot tubs downstairs!~~

~~5500~~ ~~Jamie Lee Coitus (7)~~

~~Twenty years ago, she was a Bayonne prom queen beautiful enough to become a Paris runway model who then~~

~~became a leading haute couture designer. She’s well-preserved, still gorgeous and desirable…until you hear her~~

~~voice. An aggressive, forceful, successful East Coast businesswoman with too much gold jewelry, not real bright,~~

~~but able to work her way around anything. She looks great, but sounds like Fran Dresher, only worse!~~

~~A few years ago, she was a Bayonne prom queen beautiful enough to become a Paris fashion model. She then~~

~~became a leading haute couture designer, eventually taking control of the entire company. She’s well-preserved, still~~

~~gorgeous and desirable…just don’t ask about her voice. She’s aggressive and forceful, maybe a little too much jew-~~

~~elry, but Jamie Lee Coitus can work her way around anything. She was in “Leisure Suit Larry 7: Love for Sail!” but~~

~~more important, she’s ready and willing to be you tonight. Or is that vice versa? Anyhoo, Jamie would be a great~~

~~choice for your very own persona tonight. Try her. Gowaan!~~

~~5600~~ ~~Chi~~ ~~Chi~~ ~~Lambada (5)~~

~~Miami-based Latin-American lambada-dancing former gymnast/dental hygienist. New in country. Willing to~~

~~"pay" for~~  ~~her green card in merchandise! Hot-blooded Latino.~~

~~Oh, folks, this next persona is one of my favorites. Remember that great scene in “Leisure Suit Larry 5: Pas-~~

~~sionate Patti Does a Little Undercover Work.” In Miami? With that sexy Latin-American lambada-dancing former~~

~~gymnast turned dental hygienist, Chi~~ ~~Chi~~ ~~Lambada? While she may have been new to this country then, by now~~

~~she’s yours tonight. If you’ve always dreamed of being a hot-blooded Latino, or if you just stop channel surfing~~

~~when you get to those Galavision variety shows, Chi Chi’s for you! Hit the BUY button now. You may have to sleep~~

~~late in the morning, but what the hell. Life’s too short, eh?~~

5700 Captain Thygh (7)

Swedish, blond, forceful, powerful, and demanding, she expects utmost discipline, instant response to her every

order, and utter loyalty. She runs a weekly contest for her male passengers where the winner gets to spend the fol-

lowing week “cruising on her!”

Uh, oh. Ten- hut! All hands on deck. You’ll wish your hands were on THIS deck. Captain Thygh was the ulti-

mate goal gal of “Leisure Suit Larry 7: Love for Sail!” If you ever wanted to be forceful, Swedish, blond, powerful,

and demanding, if you expect the utmost discipline from your passengers, their instant response to your every order,

if you want utter loyalty from “your crew,” well, this is your persona! Remember? Captain Thygh was the skipper of

the PMS Bouncy. She ran the weekly contest for her male passengers where the winner got to spend the following

week “cruising on the Captain!” Yes, if you can’t wait for people to snap to when you enter the casino, hit the BUY

button now.

~~5800~~ ~~Shamara Payne (6,7)~~

~~Shamara is a successful career woman of the 80s with an extraordinarily high opinion of herself, bouncing back~~

~~from her divorce, through with men, tired of material possessions (since she owns two of everything!) and is search-~~

~~ing for the meaning of life.~~

~~(COOL VOICE) Shamara was the ultimate goal girl in “Leisure Suit Larry 6: Shape Up or Ship Out!” She’s the~~

~~one who sat on her balcony overlooking the sea, searching for the meaning of life, posing questions to Larry and~~

~~then answering them herself. But remember how quickly she turned on poor Larry? Only one night together, and by~~

~~the beginning of “Leisure Suit Larry 7: Love for Sail!” she left handcuffed to a burning bed! Well, if that’s the kind~~

~~of person you are (or maybe that the kind of person you’d like to pretend to be!), then choose Sham Payne right~~



<a name="br12"></a> 

Leisure Suit Larry’s Casino Design Document

Page 12

Copyright 1997 by Al Lowe

~~now. Beluga dreams, but beer budget? Don’t worry. Her price is right. Besides, isn’t it about time you did something~~

~~just for you?~~

5900 Wydoncha Jugg (7)

The daughter half of that hot mother-daughter country-western singing duet, The Juggs. (“Ya know, I’m already

older than Momma was when she had me!”) Wydoncha wrote that country music classic, He’s Got His Daddy’s

Eyes (And His Other Daddy’s Smile). Wydoncha has big red teased hair, a loud mouth, a severe country accent.

Remember that hot mother-daughter country-western singing duet, The Juggs from “Leisure Suit Larry 7: Love

for Sail!”? Well, this little lady right here is Wydoncha Jugg, daughter of Nailmi Jugg and one fun-loving country

girl. Wydoncha wrote that famous country music classic, He’s Got His Daddy’s Eyes (And His Other Daddy’s

Smile). No, you don’t have to sing. In fact, you don’t even have to karaoke. You just have to go downstairs as one

hot young country hayseed. Why don’cha choose Wydoncha? Hey, I made a little joke, there, eh? Well, I’m good.

~~6000~~ ~~Gammie Boysullay (6)~~

~~A receptionist at La Costa Lotta, she’s a real beauty above the counter, great chest, beautiful face, gorgeous~~

~~hair. Larry treated her in the spa’s exclusive Cellulite Drainage Salon so her legs now match the rest, but since she’s~~

~~only seen in this game from the waist up, just use the Larry 6 graphics.~~

~~Oh, ladies and gentlemen, next up tonight is one of my personal favorites, Gammie Boysullay. Remember her?~~

~~She was the receptionist at La Costa Lotta, back in “Leisure Suit Larry 6: Shape Up or Ship Out!” She’s the woman~~

~~with the great body above the counter, a beautiful face, gorgeous hair, but her hips looked like two pigs in a gunny~~

~~sack before our boy Larry treated her in the spa’s exclusive Cellulite Drainage Salon. Now her legs match the rest of~~

~~that fabulous body. Gammie’s not that gammy anymore.~~

~~6100~~ ~~Nailmi Jugg (7)~~

~~The mother half of that famous mother-daughter country-western singing duet, The Juggs. (“Ya know, Honey,~~

~~we’re damn near the same age!”) Nailmi Jugg wrote that country classic, I’ve Got My Panties ‘Round My Ankles~~

~~(And Pain Around My Hea~~rt). ~~Nailmi has big red teased hair over a well-preserved body (“The best money kin buy,~~

~~sugar!”).~~

~~We now offer for your purchasing pleasure the other half, the “mother” half, of that hot mother-daughter coun-~~

~~try-western singing duet, The Juggs as seen in “Leisure Suit Larry 7: Love for Sail!” This little mother has the best~~

~~preserved body in country-western music.~~ ~~Nailmi Jugg wrote that country classic, I’ve Got My Panties ‘Round My~~

~~Ankles (And Pain Around My Heart). Buy Nailmi and get the best-preserved body that money can buy! It ain’t~~

~~growing old gracefully, but you’ll have a hootin’ good time tonight as Nailmi Jugg.~~

6200 Peggy (7)

Peggy is the peg-legged fowl-mouthed deckhand, a stereotypical pirate movie’s nasty old salt, a swashbuckler

with a surly attitude, except she’s not a he. Her peg leg comes complete with interchangeable Rube Goldberg jani-

torial attachments installed on her peg, like a mop, push broom, electric welder, vacuum cleaner, disc sander, floor

waxer.

Oh, man, this next persona is a favorite. I thought Peggy the peg-legged fowl-mouthed deckhand of “Leisure

Suit Larry 7: Love for Sail!” was the funniest character I’ve seen in a long while. Remember her? A stereotypically

nasty old salt, a pirate movie refugee, a swashbuckler with a surly attitude, Peggy only difference was she was not a

he. Her peg leg comes complete with interchangeable janitorial attachments. Yes, if you crave a persona with a defi-

nite difference, try Peggy!

~~6300~~ ~~Hooker (1)~~

~~Gum-chewing, not too bright, happy with the success she’s achieved.~~

Men

6400 Wang (7)

The ship’s carving boy is Half-Chinese and half-Irish, excitable, he mixes both accents, each for part of each

sentence so half of each sentence sounds like Hop Singh, the other half, Peter O’Toole. Responsible for the s’Pork

serving line.



<a name="br13"></a> 

Leisure Suit Larry’s Casino Design Document

Page 13

Copyright 1997 by Al Lowe

You met him in “Leisure Suit Larry 7: Love for Sail!” and learned to love his wacky sense of the absurd. Yes,

of course I’m talking about Wang, the half-Chinese, half-Irish carving boy from the buffet line of the PMS Bouncy.

Just don’t expect to see any s’Pork; he hasn’t served any of that since the terrible “Insane Pig” epidemic!

6500 Dick (7)

Pool boy, surfer dude, Valley boy accent, sun-bleached hair.

Hey, dude! Look who’s here. It’s Dick, that oh so precious pool boy surfer dude who managed the swimming

pool on the PMS Bouncy in “Leisure Suit Larry 7: Love for Sail!” While you may be able to take the boy out of the

Valley, Dick is proof you just can’t the Valley Boy out of the boy! Pour some lemon juice on your hair and head out

to the casino tonight as the coolest dude to ever wipe-out in a hot tub!

6600 Johnson (7)

Big, tough, Travolta look, with Southern good ol’ boy accent, a redneck with an attitude, trained in the Deep

South, with the sensitivity of Andrew Dice Clay but none of the subtlety. Probably dated Brett Butler at a trailer

park outside Macon. A lazy, White Trash attitude. Surly to bed, surly to rise.

Ever dreamed about looking like John Travolta? Well, no, not the “Michael” John Travolta, the Saturday Night

Fever Travolta! Well, now you can. Just hit that BUY button right now and become Johnson, that lovable bartender

from “Leisure Suit Larry 7: Love for Sail!” Tonight you’ll slick back your hair with the best of ‘em! Of course,

you’re going to sound like a little good ol’ boy fresh from a trailer park outside Macon, Georgia, but isn’t that a

small price to pay? Johnson. He’s all you’ve dreamed of. And less.

6700 Peter (7)

The Purser. Prissy, gay conspiracy theorist. Flaming.

Our next selection on CyberShop 2000 is this precious little number from “Leisure Suit Larry 7: Love for Sail!”

Peter, the purser. While Peter may be a little prissy, his conspiracy theories will keep everyone around the table

amused all night long. Not the choice for every man, but for something special tonight, pick a pack of Peter Pursers.

~~6800~~ ~~Rock Hard (6)~~

~~Body builder, maximum buff, not real bright, Larry’s opponent on Stallions.~~  ~~“big & beefy, rich & juicy, thick &~~

~~meaty,” in other words, a human “butt steak.”~~

~~“Leisure Suit Larry 6: Shape Up or Ship Out!”~~

~~6900~~ ~~P. C.~~ ~~Hammer (5)~~

~~Black, sharp, good dresser, hip.~~

~~And now for something completely cool. P. C. Hammer was that world famous rapper in “Leisure Suit Larry 5:~~

~~Passionate Patti Does a Little Undercover Work.” A hip dresser, although that won’t do you much good here at~~

~~Larry’s Casino. Take P. C. and be totally non-P. C.!~~

7000\. Leisure Suit Larry

Larry is not available for you to use as your persona, since he is the star of the show as host of the casino. He

has three main tasks: dealer for every game, clerk behind every counter, and minister of the wedding chapel. He

doesn’t need full walkers, since you see him only as he zips to one of his jobs.

Larry deals every hand in every game, both on-line and off-line. In each case, we see his cartoonish “fast zip”

past the current scene into place.

Larry works behind the counters of the Gift Shop, Front Desk, Cashier, Betting Window. He needs a (one,

shared) talker for all those scenes, as there will be lots of dialogue. He has a fancy entrance loop so that after you

ring the bell for him, you see him enter in as a blur, changing into clothes that reflect this new position.

Larry needs some special loops for his appearance in the chapel when he does his Elvis impersonation.



<a name="br14"></a> 

Leisure Suit Larry’s Casino Design Document

Page 14

Copyright 1997 by Al Lowe

100's, Opening

100\. Sierra Screen & Video

We begin with a video sequence actually shot from a helicopter cruising above the real Las Vegas strip at high

speed, slow enough to let people figure out where they are, but fast enough to not drag. The flight continues right

past the end of the casinos, out into the darkness of the Nevada desert, then a speck of light appears in the distance.

It grows larger and larger until we recognize it as Larry’s Casino. You fly right up to the front of the building, stop-

ping with a close-up of casino’s big neon sign, i.e., 110. Larry Casino Title Screen, below. This entire sequence

must take less than 15 seconds.

Any user action immediately interrupts the sequence and we cut to the Title Screen. Can the title pic and its

animation be loaded in the background while the AVI is playing? If not, how about ahead of the AVI?

Question

Who’s going to build the casino exterior for the opening movie?

110\. Larry Casino Title Screen

This is a full-screen shot of the sign outside the casino. It remains up for 5-10 seconds, while the title music

plays. If there is no user action, the music continues as we roll the credits in the marquee area of the sign. Use Mar-

tino’s faked electric light bulb technique from Love for Sail!’s cook-off. If we’re in the opening sequence, any user

action immediately cuts to 200. Hotel Room, below.

150\. World Map

A right-click of the mouse brings up a menu with the most common game commands, as in Love for Sail! Select

Map and you see this screen, a map of the casino. Move the cursor over an area and (if you can go to that area) the

area will brighten by being lit by a spotlight, the preview window will display a thumbnail, and its name will appear

in the marquee area of the Larry’s Casino sign logo. Click the mouse to immediately go there, or move around some

more to find another place. Areas will not light unless it’s possible to go to them. The perimeter of the map displays

the “return to previous scene” cursor and takes you back to the previous scene.

The shape of the room indicates its function:

°

°

°

°

°

°

°

Main area casino games, slots; each wedge’s color matches the carpet in that area of the casino

Diamonds on-line party games

Clubs

clubs, restaurants

wedding chapel

gift shop, front desk

bars

Hearts

Spades

Circles

Dollar Sign casino cashier, racetrack betting cage

The map also contains a door indicating your (variable) hotel room. It remains a constant shape, although its

thumbnail does change to reflect your current room’s quality.

While in the Map, the “Map” menu item changes to “Leave Map.” Selecting this returns you to the previous

scene, with no changes.

200's, Hotel Room

Room L. S.

All the hotel rooms must include the same items. The art is the primary (only?) difference. This section de-

scribes what exists in all the rooms. All five pictures of each “quality of room” are rendered from the same 3-D

build. Individual differences are described in the 201-205 section below.



<a name="br15"></a> 

Leisure Suit Larry’s Casino Design Document

Page 15

Copyright 1997 by Al Lowe

Functioning like the casino map, the Room L. S. is an overall picture of the room that lets you move between

the other areas listed below. It shows at least a portion of the Hot Tub, CYBERLARRY 2000, and the Interactive

Closet so you can click on them to move to them. For example, click on CYBERLARRY 2000 in this long shot takes

you to 221. Hot Tub, bad news below. Same with the hot tub, closet and door.

If you enter this room with a SIGS “guest,” you’re automatically transported into the hot tub, since otherwise

we have no way of showing the two of you here.

To leave the room and head for the casino without using the map, click near the bottom of the screen, when

your cursor is a bent arrow. You go straight to the elevator. If you haven’t yet chosen a “persona,” you get a text

error message and you go directly to the closet.

201\. Room, bad news

This place is the pits. Two grades below Kane’s Motel. Actually, maybe we should just “sample” Kane’s fur-

nishings! Dress it up as bad as you can, but funny. Make it so bad people want to move on to a classier place.

202\. Room, acceptable

Next grade up. 1-star. Not filthy, not ratty, just not very nice.

203\. Room, comfortable

Embassy Suites? Nice room. Sofa, little balcony, soft lighting.

204\. Room, deluxe

Real disco ball hangs from ceiling, mirrors above bed, magic fingers mattress with slot for quarters. Plush, de-

luxe, spacious, make people think this is the best there is.

205\. Room, extravagant

Huge room, white grand piano in one corner, tremendous view of the front of the casino spread out below you

and Las Vegas lit up way off in the distance, sexy background music, monogrammed robes laid out on your tiger-

skin bedspread, rotating bed, champagne bucket hot tub, mirrors over the bed, etc. Make it way over the top. What

do we care about expense? It’s just art!

210\. The Closet

Before you can go to the casino, you must decide “who to wear!” Come here to pick your on-screen persona

from this interactive video “closet.” Every closet in the hotel has an identical CYBERSHOP 2000 machine hidden in

the closet, its TV screen portraying a bastard derivative of the Home Shopping Network, its plumbing somehow

connected to a central warehouse somewhere else in the hotel for instantaneous deliveries.

All closets, regardless of “room quality,” maintain a consistent “programmer-friendly” usability. The size of the

closet may increase, but it’s only in the background pic. Interface and functionality remain constant. Each closet has

a hint of a mirror to one side which players can click on it to “audition” their current persona’s CYBERFACE 2000

emotions.

Watch the on-screen shopping, listen to the pitchman and browse through torsos until you see one you like. We

offer a variety of characters (both men and women) from previous Leisure Suit Larry games. The machine includes

controls to work the mechanism (left arrow, right arrow, and “Buy”).

The salesman’s voice-over pitch is geared to easy programmability. He chats on and on (in true HSN fashion)

until you press a button to move on. He then immediately reacts to your button press and begins his pitch for the

next persona. When you finally press “Buy” (and you must or you’ll never get out of your room!), the machine re-



<a name="br16"></a> 

Leisure Suit Larry’s Casino Design Document

Page 16

Copyright 1997 by Al Lowe

acts, air hisses, a box flies through the clear plastic piping before appearing in the area near the bottom of the ma-

chine. There’s a short pause before the box disappears. You then immediately go to room 270. Mirror below.

Exiting here returns you to the same hotel room you came from.

The player’s persona choice is saved on disk between sessions so you only have to pick once, not every time

you start up.

The backgrounds are numbered as shown below, but all the buttons and animation are shared with all five.

211\. The Closet, bad news

212\. The Closet, acceptable

213\. The Closet, comfortable

214\. The Closet, deluxe

215\. The Closet, extravagant

220\. Hot Tub

For those intimate chat sessions. Size and quality of fittings can vary, but not the picture’s coordinates. If you

enter your room with an on-line “friend,” the two of you automatically end up here. To the player, it appears he

automatically undressed and entered the hot tub. Shows CYBERLARRY 2000 off to the side, but obviously not us-

able from this angle. Downplay the door, closet, etc. so people don’t think they can just click on them from this pic

to move there. The actual pic displayed varies with the quality of your room, but will be one of the following num-

bers.

221\. Hot Tub Chat, bad news

222\. Hot Tub Chat, acceptable

223\. Hot Tub Chat, comfortable

224\. Hot Tub Chat, deluxe

225\. Hot Tub Chat, extravagant

230\. CYBERLARRY 2000

Every hotel room has a hot tub, and every hot tub comes complete with a CYBERLARRY 2000 installed right

beside it. CYBERLARRY 2000 is an automaton spoof of Larry, only here to tell jokes to any victims foolish enough

to enter the hot tub alone. Even expensive hotel rooms include a CYBERLARRY 2000. We spoof 3D-rendered peo-

ple with a CYBERLARRY that appears to be carved of wood with strings suspending mechanical arms and a hinged

wooden Pinocchio mouth. CYBERLARRY “awakens” amid mechanical creaks and pneumatic wheezing and spouts

jokes, often with bad mechanical skips in playback. All the CYBERLARRY 2000s are identical, regardless of the

quality of your room. (Hey, the casino got ‘em on sale, okay!?)

231\. CYBERLARRY 2000, bad news

232\. CYBERLARRY 2000, acceptable

233\. CYBERLARRY 2000, comfortable

234\. CYBERLARRY 2000, deluxe

235\. CYBERLARRY 2000, extravagant

270\. Mirror

The mirror shows a close-up of your currently selected persona exactly as other players will see you. It’s merely

a preview screen, nothing more. It crops your torso so our limited animation looks acceptable. A fake chat area and a



<a name="br17"></a> 

Leisure Suit Larry’s Casino Design Document

Page 17

Copyright 1997 by Al Lowe

CYBERFACE 2000 panel is displayed in one corner. Clicking it causes your persona (i.e., the character in the mir-

ror) to display the appropriate loop of facial animation. Cycle to the end of loop, put up a cartoon bubble, pause 3

seconds, then cycle back to the beginning.

The bubble’s text says, “Click here to change

your text colors.” Clicking it brings up a dialog box

beside the bubble with two sets of three numbers.

One set of three boxes is labeled “Text,” the other

“Background.” The three boxes in each set are la-

beled “Red,” “Green,” and “Blue.” Each box

contains digits representing the color value and an

up/down arrow pair beside the digits. (Shown to the

left is the one from Word 97, “Format | Back-

ground… | More Colors | Custom” which is kind of

close.) You can type in the numbers, or use the ar-

rows to change them. Arrows auto-repeat at the

current Windows keyboard repeat speed following

the current Windows keyboard delay. Altering the

numbers immediately affects the colors in the bub-

ble. Include buttons for OK, Cancel and Default

(which gives black on white background). OK saves

the colors, which are then sent as part of every sin-

gle chat message’s header.

A possibly easier alternative

may be the dialog shown to the

right, as made famous by Control

Panel | Display | Window text | Color. We could put up two of those, using their Windows colors.

The advantage of this is you could put this the tabbed Options dialog along with all other settings.

Exiting here returns you to the previous room, probably the closet, but possibly your hotel

room.

The backgrounds for the mirror are numbered as shown below, but all the buttons and animation are shared with

all five.

271\. Mirror, bad news

272\. Mirror, acceptable

273\. Mirror, comfortable

274\. Mirror, deluxe

275\. Mirror, extravagant

300’s, Casino

300\. Casino Lobby

Merely a long shot establishing the size and “half-vastness” of the place. Show flashing lights, waterfalls, foun-

tains, elevators “sperming” their way through the plumbing, etc. It just can’t have too much animation, especially

animated electric light bulbs. Shares background sounds with 310 & 320, below.



<a name="br18"></a> 

Leisure Suit Larry’s Casino Design Document

Page 18

Copyright 1997 by Al Lowe

310\. Casino Floor, Inner Circle

A set of continuous, seamed-together, side-scrolling pictures, shot radially outward as if your back was near the

elevators and the casino games were spread out before you. The pictures’ scales, and the tables’ locations, allow

walkers to reasonably move through the scenes.

Click near the top edge of the screen to move forward to the corresponding scene in picture set 320. Casino

Floor, Outer Circle, below. Click on the bottom to go to the elevator. Click left & right to move through the scrol-

ler. Click in the middle of the pic to begin playing one of those games. After passing through SIGS (which also

selects the game’s stakes), you arrive at the actual game’s close-up, described below in 400-600's, Casino Games.

The following list names the casino games in left-to-right, clockwise order, one game per pic.

3101\. Casino Slots

3102\. Casino Blackjack Medium Shot

3103\. Casino Roulette Medium Shot

3104\. Casino Wheel of Fortune Medium Shot

3105\. Casino Poker Medium Shot

3106\. Casino Craps Medium Shot

320\. Casino Floor, Outer Circle

A set of continuous, seamed-together, side-scrolling pictures, shot radially outward as if the casino games were

now behind your back and you are near the outer wall facing it and its doorways leading to the adjoining rooms. The

pictures’ scales, and the tables’ locations, allow walkers to reasonably move through the scenes. Sysops drop-in oc-

casionally to walk around as Larry.

Click near the bottom edge of the screen to move to the corresponding scene in picture set 310. Casino Floor,

Inner Circle, above. Click left & right to move through the scroller. Click a doorway to enter that area. Sometimes

you’ll have to pass through SIGS, which may add additional detail to your selection (i.e., clicking on the Comedy

Club doorway in 323 below takes you to SIGS’s comedy area where you decide on clean, dirty or obscene, which

then sends you to the appropriate Comedy Club). This list shows the entrances to adjoining rooms in left-to-right,

clockwise order. Some pix contain two or more doorways leading to other scenes.

3201\. Casino Front Door

3202\. Gift Shop & Say What?!

3203\. Restaurant, Better & Larry's Comedy Club

3204\. Casino Cashier

3205\. Bar, Cheap

3206\. Quiki-Wed Wedding Chapel

3207\. Bar, Better

3208\. The Bottom Line & Restaurant, Cheap

3209\. Pickup Master & Hotel Front Desk

340\. Elevators

Actually there’s only one elevator, always the same one, coincidentally that one we drew! Most of this pic is a

view out the front of the casino through the elevator’s glass door. The rest contains two buttons and a key card slot.

The upper button is labeled “High Rollers” and the lower “Casino.” When your cursor is over a button, it becomes a

hand. When it passes over the card scanner, it becomes a key card. Clicking takes you to either the penthouse, the

casino, or your current room. You are only allowed entrance to the “HR” area if you have plenty of on-line money.



<a name="br19"></a> 

Leisure Suit Larry’s Casino Design Document

Page 19

Copyright 1997 by Al Lowe

350\. Restaurants

350\. Restaurant, Bad

351\. Restaurant, Better

352\. Restaurant, Classy

These are simple chat areas without much to do but chat and pay for food. Functionally identical, artistically

distinctive. 2-D animated waitresses pass through without stopping. Clicking on one causes her to offer a (silent)

menu of choices with prices on both (multiple?) computers. Click the items you want to buy for yourself. Whoever

clicks on the waitress pays. After a (random) delay, a message box appears, telling you your order has appeared.

Bon appétit! Thank you’s are expected from your guests.

360\. Bars

360\. Bar, Bad

361\. Bar, Better

362\. Bar, Classy

These are simple chat areas without much to do but chat and pay for drinks. Functionally identical, artistically

distinctive. 2-D animated waitresses pass through without stopping. Clicking on one causes her to offer a (silent)

menu of drinks with prices on both (multiple? all?) computers. Click the item you want to buy for yourself. Whoever

clicks on the waitress pays. After a (random) delay, a message box appears, telling you your order has appeared.

Salud! Thank you’s are expected from your guests.

Gary Spinrad’s bar lines

1: Ladies and gentlemen! Take your seats! In just ten minutes, the Fearless Freep will be shot from a cannon, fly

high through the air through a ring of fire and land in a waiting ambulance below!

2: Ladies and gentlemen, your attention please. Will the person who stole the elephant's tutu please return it to the

ringmaster. The elephant ballet cannot go on without it.

3: Ladies and gentlemen, you attention please. A rare Brazillian brain eating monkey has escaped from its cage. If

you see it, please run like hell, then notify hotel staff immediately. Larry's casino assumes no responsibility for those

injured by brain eating monkeys.

1: Hey! Don't forget out to be here a Shooters of the 17th. Otherwise you'll miss the regional championships of the

World Barfight association. Brought to you by Li'l Coldcock Brass Knuckles and Larry's Casino.

2: We have Drink specials every day here at shooters! You buy a drink, we'll make you feel special!

3: Just a reminder! Here at shooters, darts are to be thrown at the dartboards only.

370\. Gift Shop

As you enter this scene, the desk is empty, except for a little bell. Click on the bell to ring it and Larry zips in

from off-screen to wisecrack with you. A visual feast of goods is displayed before you, waiting for your click. Pause

your mouse over an object, and a tooltip appears with the name and price of that object. Click on it, Larry says “Ex-

cellent choice!” and you see a dialog saying, “Purchase %s for $%d?” (objectName, objectPrice) with OK and

cancel buttons. OK makes Larry respond, “Perfect. I’ll add it to your Inventory.” Cancel and he’s disappointed.

Each Inventory object has an ID number. Later, when you click that object on another player, we transmit only that

object’s ID, along with your chat message.

Drinks, food, etc. is handled the same way.

There are about 20 things to purchase, including: Lingerie, Bean Dip, Cigars, Flowers, Candy, Perfume, Jew-

elry, Condoms, Disinfectant, And Even A Marriage License for a wedding in the Quiki-Wed chapel.



<a name="br20"></a> 

Leisure Suit Larry’s Casino Design Document

Page 20

Copyright 1997 by Al Lowe

380\. Hotel Front Desk

As you enter this scene, the desk is empty, except for a little bell. Click on the bell to ring it and Larry zips in

from off-screen to wisecrack with you. He offers you a room, haggles with you over price, then gives you your key

card. All as humorously as possible. The only functionality here is: upgrade your hotel room.

390\. Quiki-Wed Wedding Chapel

Enter this scene alone and there’s nothing to do but leave. But purchase a marriage license in the gift shop,

spread the word among your on-line buddies as to when to show up in the chapel, then come here with another on-

line person and instead of an empty boring room, you get…

391\. Quiki-Wed Wedding Chapel Wedding

Leisure Suit Larry as Elvis impersonator to perform a funny wedding. Essentially a prepared cartoon, with

pauses for on-line chat interjections from the crowd, the room is shown from the wedding couple’s perspective, with

Larry close-up in the foreground, Larry singing “Love Me Tender,” maybe even a cut scene showing Larry doing

his Elvis moves. Free virtual cake for everyone, too!

400-600's, Casino Games

All these games are identical to their Hoyle’s versions, with the few exceptions specified below. In other words,

if something is specified here, it’s different. If it’s ignored, it’s the same. So far, damned near everything is the

same.

400\. Poker

450\. Blackjack

500\. Craps

550\. Roulette

600\. Wheel of Fortune

601 WOF Paddlewheel

Since there is no corresponding Hoyle game, this is the complete spec of WOF.

You sit in a hot tub, with other WOF players. Chat is enabled. Larry prompts everyone to place their bets. Play-

ers drag chips from their chip trays to the table and place them on the rectangle containing the odds they want to

play. When all the bets are placed, Larry says, “All bets are down.” (or some equally vapid line) and we spin the

paddle wheel. Pick some random number as the length of delay before slowdown, start the animation, and when the

random counter hits, start slowing the animation until it stops on some random cell. That becomes the winning num-

ber. (Save the cell number so it becomes the new start of animation.) If they lost, erase his chips and loop back to the

beginning. If they win, display a stack of chips on the table indicating his payoff. He then clicks the “done” button

and we start over.

There are 54 tiles on the wheel, consisting of 6 different types. The 6 types are represented by dollar-bill loo-

kalikes of 1, 2, 5, 10, and 20 dollar bills (with a Larry face, of course), plus a special 40 Larrybuck jackpot bill. The

number on the bill represents the multiple paid back by the casino. The odds are not in the player’s favor.



<a name="br21"></a> 

Leisure Suit Larry’s Casino Design Document

Page 21

Copyright 1997 by Al Lowe

Multiplier # of tiles Odds in 54 Payback

1

2

28

14

6

28

28

30

30

40

40

52%

52%

56%

56%

74%

74%

5

10

20

40

3

2

1

Total:

54

700's, Slots

All the slot machines share one “room” in SIGS. On-line chat appears around the corners of the screen, with the

pointer aimed in random (though consistent by player) directions. Every on-line slots player is in the same game, but

is invisible, just like when you play real slots. Everyone can hear everyone else’s chat. When one wins, all machines

hear the celebration sound, but at reduced volume.

700\. Slots Long Shot

Use the 700’s for common slot machine animation. The actual game animation is one of the numbers below.

Same old Hoyle’s slot machine play, but with goofier graphics and better sound effects.

710\. Slots, A

720\. Slots, B

730\. Slots, C

740\. Slots, D

800's, Party Games

Description

All four party games: Say What?!, The Bottom Line, Pickup Master, and Larry’s Comedy Club. All are on-line,

text-based, self-authoring, self-scoring games with interstitial advertising played to win Larrybucks. There is no

betting. There is a minimum of two players and a maximum limited only by how many text entries each game can

simultaneously display on-screen. Players can enter, leave, and/or reenter games between rounds. They get to keep

any Larrybucks accumulated even if they leave before the end of the game. The chat window is often available.

Visit www.Berzerk.com and play Acrophobia. Let’s style ours after that.



<a name="br22"></a> 

Leisure Suit Larry’s Casino Design Document

Page 22

Copyright 1997 by Al Lowe

Definitions

Text-based means players type in words, phrases, or sentences and submit them to the Casino server. These

strings are collected on the server, presented to the players, and judged by the players. Chat is usually available, ex-

cept during timed dialogs. When a dialog is “Submitted,” chat returns.

Self-authoring means there is no AI. Players do everything; Casino does nothing.

Self-scoring means players’ decisions select who wins, and how many Larrybucks he wins. Casino merely per-

forms game management, communication, and record keeping. Consider Casino the scribe of these games.

Interstitial advertising are on-line ads run during natural pauses in game play, often between rounds. Game

play is never interrupted. Ads appear on TV screens within the visual context of the game. These may look like tele-

vision game show displays.

Common Game Elements

All four party games share:

°

°

°

°

°

°

°

°

°

°

Interstitial ads

Game states

Navigation between text fields

Sound effects

Instruction display

Text length restriction

Time clock

Timer multiples

Text animation

Voice prompts

Interstitial ads are in each game, are displayed on-screen in a provided area that’s within the context of the

scene. Ads last no longer than 30 seconds and may be 10, 15, or 20 seconds long.

Game states are a convenient way of describing: discrete time periods in the game, what happens during each

state, how long each state lasts, what terminates the state, what players do during each state, and what Casino does

during each state.

Navigation between text fields is done by clicking in a target text field or by using Tab to move from field to

field. Tabbing order is always left to right, top to bottom.

All significant actions have sound effects. When you submit a word definition or vote on a winner, you hear

aural feedback.

Instruction display is via voice-over plus abbreviated text in a mock TV screen within the game window. The

TV screen grows and shrinks as needed. Voice-over instructions are tracked by each game and cease when a player

has heard each of them once.

Text length restrictions depend on the field. If you type too many characters, they just stop showing up and

you hear a sound effect.

Time clocks are used to keep gameplay moving. A two-digit, on-screen, countdown timer displays the seconds

remaining in that game state. Each game’s time clock looks and functions identically. Whenever time limits are

specified below, the clock is displayed. An audible tick marks each changing second. When 10 seconds remain, you

hear a short snippet of music which ends when the clock hits zero. If all players have submitted their entries before

the time limit is reached, the time clock speeds up and runs down to zero quickly, still ticking all the way. In accel-

erate mode, the music is silenced. Usually, chat is not available when a time clock is running so players may

concentrate on whatever text they are entering. This may also avoid unfair collaboration.



<a name="br23"></a> 

Leisure Suit Larry’s Casino Design Document

Page 23

Copyright 1997 by Al Lowe

Timer multiples set time limits based on the number of players in a game, i.e., a 10-second multiple means a 9

player game would have 90 seconds. Timer multiples default to 10 seconds, but will be tweaked during play testing.

Provisions will be made to also adjust it by those maintaining the game server.

Text often arrives on-screen via text animation. Instead of just showing the text, we’ll use as many different

ways of making text fun as possible, like zooming, panning, dissolves, fade-ins and outs, vertical and horizontal

scrolling, crawling, melting, and other effects.

Any prompting necessary to the game is displayed on-screen and also read aloud by voice prompts. Major

stages of each game have graphic, text, and aural indicators.

Questions

1\. What happens when we have only two players? Can we keep them from collaborating? Do we want to avoid

collaboration? Will it cause Larrybuck inflation? What if people enter nothing and a buddy votes for it? Do we

care?

2\. Can you vote for your own submissions? If not, it must not be displayed.

3\. What if there’s only one player? He may be waiting for others. Or, people may leave or fall off-line until there

is only one player left. Do we just leave him there?

4\. What are the technical details of the interstitial ads? File format, etc.?

5\. How are interstitial ads programmed?

6\. Who tells the game software what ad is scheduled when?

7\. Will we be able to adjust the timing of each game? If so, will the players or the server people do the adjusting?

Should we build an automatic mechanism that responds to player usage?

800\. Say What?!

…is an interactive, on-line, word definition game. When everyone in a group indicates they are ready to begin,

a timer starts. Each person then has 60 seconds to type in a word. When you hit Enter, nothing appears on-screen,

but instead, Casino collects everyone’s words and waits until the time is up, or everyone has submitted. It then pre-

sents each of the submitted words in sequence. The number of words determines the number of rounds played, one

word per round. In each round, Casino presents one word to all of the players. Everyone has 60-seconds to type in

his best fake definition of that word. Again, when you hit Enter, nothing appears on-screen, but instead, Casino col-

lects everyone’s definitions and waits until the time is up, or everyone has submitted. It then displays all the

definitions, and offers a means to vote. Players vote for the definition they think is the funniest. Each vote awards

the player who submitted that definition a Larrybuck.

There are 6 game states in YDKD! States 3 through 5 are repeated once for each word collected in state 2. Upon

reaching state 6, players may opt to loop back to state 1 for another game.

1\. Gathering

2\. Word Entry

3\. Word Display and Definition Entry

4\. Voting

5\. End of Round

6\. Conclusion

Voice Over Instructions

Welcome to "Say What?!", the new quiz game sensation that’s sweeping the nation! It's that special place where

you and your on-line buddies (or even strangers!) get together for fun and laughs while earning Larrybucks!

Now here's how we play the game. Think up a word that will make for funny phony definitions. When asked,

type it in. Everyone’s word is collected, then fed back one at a time. Each player creates a funny definition for each

word. (It might even be the real definition!). When all the definitions are in, they’re all displayed. Then you give

Larrybucks to the one you like best.

Here’s a few more rules. The Larrybucks you award don’t come out of your bankroll, they’re “on the house,” so

vote freely! You can’t vote for your own definition—that just wouldn’t be right. And you earn Larrybucks even

when you submit a word. So don’t be shy…throw out your best words, your funniest definitions. You just might

make people go, “Say What?!”



<a name="br24"></a> 

Leisure Suit Larry’s Casino Design Document

Page 24

Copyright 1997 by Al Lowe

Game State 1: Gathering

•

When a player is ready to start he or she clicks the “Ready” button. Voice-over harasses those who haven’t

pressed their ready button. To silence such harassment, click the “Waiting for Someone” button.

Chat is available for the duration of this state.

Casino keeps track of who is ready. Players’ names and “Ready” status appear on the TV screen. You can chat

to hurry others along. When all indicators are set, there is an announcement to start, accompanied by music,

sounds effects and voice-over narration.

•

•

•

•

Ads may be run in the TV screen.

This game state lasts until all players have clicked their “Ready” buttons.

Game State 2: Word Entry

•

The player types a single word into the editable text field named “My Word.” The maximum word length is 20

characters. When done, the player clicks the “Submit” button or hits “Enter.”

•

•

The TV displays text instructing the player what to do while audio prompts in a humorous way.

Casino collects everyone’s words. If you haven’t entered a word when time runs out…oh, well. Too bad. There

are just fewer words than players this round.

•

This game state lasts 30 seconds, or until everyone has submitted a word.

Game State 3: Word Display and Definition Entry

•

•

A word is selected and displayed in the order the server received them.

Casino displays the next word accompanied by visuals, sound effects and music. The TV screen tells players to

enter a definition. One of a dozen random voice-over files instructs them how to do it.

The player types a short definition into the field named “My Definition” and clicks “Submit” or hits Enter.

Definitions are limited to 80 characters (or whatever fits considering the number of players and our font).

Casino collects everyone’s definitions

•

•

•

This game state lasts 60 seconds, or until everyone has submitted a word.

Game State 4: Voting

•

•

•

•

•

Casino displays the word plus all the submitted definitions, in the order received.

When the cursor is over a definition, that definition is outlined with a colored line.

Players vote by clicking a definition. The outline is erased, the text is highlighted, and the vote sent to Casino.

Casino collects the votes as they are entered. If you haven’t voted when time runs out…oh, well.

The maximum time limit of this game state is a timer multiple times the number of definitions collected.

Game State 5: End of Round

•

Casino displays the number of Larrybucks the winning player won, his name, and his winning definition. His

Larrybucks are recorded in the casino server database.

•

•

The maximum time limit of this game state is 60 seconds or until everyone clicks “Go Ahead.”

The game then loops to state 3 for the next round, or to state 6 if there are no words left.

Game State 6: Conclusion

•

•

Casino displays each player’s name and winnings, sorted by winnings from high to low.

Players can stay here and chat (and watch ads). When the player clicks “Start New Game,” loop back to state 1

and start gathering a new game. Players, as always, can right-click to go to the Map and head elsewhere.

Chat is available for the duration of this state.

•

•

•

Ads are run in the TV screen.

This game state lasts until the last player leaves.

810\. The Bottom Line

…is an interactive, on-line, story writing game. When everyone in a group indicates they are ready to begin, a

timer starts. Each person then has 60 seconds to write the first line of a story. Casino collects everyone’s lines, waits

until time is up, then displays all the lines, and offers a means to vote. Everyone votes on which line they want to



<a name="br25"></a> 

Leisure Suit Larry’s Casino Design Document

Page 25

Copyright 1997 by Al Lowe

keep. The author of the winning line receives Larrybucks. This process is repeated until everyone is tired of writing

or agree on an ending. At any time, the story can be saved as a text file on your hard disk. Later, stories may be

submitted for storage in our on-line archives, with the best ones published as a book, The Larry Stories, On-Line and

Stupid!

One unique aspect of The Bottom Line is the story window, a separate window which displays the ongoing

story as it’s created, with each line of text color-coded by author. Players may choose the color of their text from a

palette of colors, or leave it in its default color of black-on-white. The authors’ names are listed at the top of the file,

like this:

A Story by

John W. Bobbit

Ken Williams

Marie Osmond

Johnny Holmes

Al Lowe

Every line is then displayed in that author’s color. The story window may be moved around on-screen and has a

standard Windows File menu with functions for saving and printing. It disappears when the player exits The Bottom

Line.

The are five game states in The Bottom Line, with states 2 through 4 repeated as long as the players wish.

1\. Gathering

2\. Line submission

3\. Voting

4\. End of Round

5\. Conclusion

Voice Over Instructions

Welcome to "Say What?!", the new quiz game sensation that’s sweeping the nation! It's that special place where

you and your on-line buddies (or even strangers!) get together for fun and laughs while earning Larrybucks!

Now here's how we play the game. Think up a word that will make for funny phony definitions. When asked,

type it in. Everyone’s word is collected, then fed back one at a time. Each player creates a funny definition for each

word. (It might even be the real definition!). When all the definitions are in, they’re all displayed. Then you give

Larrybucks to the one you like best.

Here’s a few more rules. The Larrybucks you award don’t come out of your bankroll, they’re “on the house,” so

vote freely! You can’t vote for your own definition—that just wouldn’t be right. And you earn Larrybucks even

when you submit a word. So don’t be shy…throw out your best words, your funniest definitions. You just might

make people go, “Say What?!”

Game State 1: Gathering

Everything is exactly the same as 800. Say What?!, Game State 1: Gathering.

Game State 2: Line Entry

•

•

•

The story window appears and remains until the player exits the game.

The TV displays text instructing the player what to do while audio prompts in a humorous way.

Players type their line into the “My Line” editable text field, then clicks “Submit.” Entry length is limited by

the number of contestants because all the submitted lines must be displayed on-screen simultaneously.

Casino collects everyone’s entries.

•

•

The maximum time limit for this game state is 60 seconds.



<a name="br26"></a> 

Leisure Suit Larry’s Casino Design Document

Page 26

Copyright 1997 by Al Lowe

Game State 3: Voting

•

•

Casino displays all the lines, in the order received.

When the cursor is over a line, the line is given a color outline. Casino collects the votes as they are entered.

The votes are tallied and the winning player has Larrybucks added to his or her record on the server.

Players vote by clicking a line. The outline is erased, the text is highlighted, and the vote sent to Casino.

When the cursor is over a line, that line is given a colored outline.

Casino collects the votes as they are entered. If you haven’t voted when time runs out…oh, well.

The maximum time limit of this game state is a timer multiple times the number of definitions collected.

•

•

•

•

Game State 4: End of Round

•

•

The story window is updated by adding the winning entry to the story’s end.

Casino displays the number of Larrybucks the winning player won, the winner’s name, and the winning line.

The winner’s Larrybucks are recorded in the Casino server database.

•

•

The player is presented with two buttons. One is the “Write More” button and the other is the “Stop Writing”

button. When all players have clicked one of these, the state changes. (If time expires before a player clicks, the

default is “Write More.” He can always just leave.) If the player chooses “Write More” (or defaults), we loop

back to state 2. If he chooses “Stop Writing,” that player advances to state 5.

The maximum time limit of this game state is 60 seconds. This game state lasts until time runs out or all play-

ers click “Write More” or “Stop Writing.”

Game State 5: Conclusion

•

•

•

Casino displays each player’s name, Larrybucks won and number of lines chosen in order, sorted by Larry-

bucks won from high to low.

The story window still displays the entire story. names of the players who submitted them and how many Lar-

rybucks each player won is displayed below each line.

The player can stay here as long he or she wants. They can continue to chat about the game and watch ads. A

“Start New Story” button will take them immediately back to state 1. They can also right click to get the Map

and go to some other part of the Casino.

•

•

•

•

Leaving this state destroys the story window and its contents.

Chat is available for the duration of this state.

Ads are run in the TV screen.

This game state lasts until the last player leaves.

820\. Pickup Master

…is an interactive, on-line, pickup line contest. Each player submits a topic. Casino collects the topics, then

presents a topic in turn to all players. Each player writes a pick-up line related to that topic. Casino collects the

pickup lines, displays all of the lines, and players vote for what they think is the best pickup line. Players get Larry-

bucks for each vote their line gets. All lines become the property of Al Lowe, who promises to use them in the next

Larry adventure game.

There are five game states in this game:

1\. Gathering

2\. Topic submission

3\. Pickup line submission

4\. Voting

5\. End of Round

6\. Conclusion

Voice Over Instructions

Welcome to "Pickup Master," where even the loneliest loser can score…a few Larrybucks. Come here to prac-

tice with your on-line friends, or even to practice ON strangers. Have some laughs and earn some Larrybucks!

Here's how we play the game. Think up a topic that will make for great, funny, pickup lines. When asked, type

it in. Everyone’s topic is collected, then given back to you in random order. Each player makes up a pickup line re-



<a name="br27"></a> 

Leisure Suit Larry’s Casino Design Document

Page 27

Copyright 1997 by Al Lowe

lating to that topic. When all the lines are in, they’re all displayed. You award Larrybucks to the one you think is

best.

There’s only a few more rules. The Larrybucks you award don’t come out of your bankroll, they’re “on the

house,” so vote freely! You can’t vote for your own line—of course you think it’s good! And you earn Larrybucks

even for submitting a topic, so don’t hesitate. Come up with some crazy topic and see what happens. You might just

be today’s “Pickup Master!”

Game State 1: Gathering

Everything is exactly the same as 800. Say What?!, Game State 1: Gathering.

Game State 2: Topic Submission

•

•

•

Casino displays a message on the TV instructing the players to type in a topic.

The TV displays text instructing the player what to do, while audio prompts in a humorous way.

The player types his topic in the “My Topic” text field. Topics can be a word or a short phrase. Line length is

limited to the number of characters that can fit in one line on the screen. When the player is satisfied, he clicks

“Submit.”

•

•

Casino collects everyone’s topics.

This game state lasts 60 seconds.

Game State 3: Pickup Line Submission

•

A topic is selected and displayed in the order the server received them, accompanied by visuals, sound effects

and music. The TV screen tells players to enter a definition. One of a dozen random voice-over files instructs

them how to do it.

•

The player types one line into the “My Line” text field. When the player is satisfied with the entry, the player

clicks the “Submit” button. Line length is limited to the number of characters that can fit in one line on the

screen.

•

•

Casino collects everyone’s pickup lines.

This game state lasts 60 seconds.

Game State 4: Voting

•

•

Casino displays the topic plus all of the submitted pickup lines in the order received.

When the cursor is over a line, the line is given a color outline. Casino collects the votes as they are entered.

The votes are tallied and the winning player has Larrybucks added to his or her record on the server.

Players vote by clicking a line. The outline is erased, the text is highlighted, and the vote sent to Casino.

Casino collects the votes as they are entered.

•

•

•

The maximum time limit of this game state is a timer multiple times the number of definitions collected.

Game State 5: End of Round

Everything is exactly the same as 800. Say What?!, Game State 5: End of Round.

Game State 6: Conclusion

Everything is exactly the same as 800. Say What?!, Game State 6: Conclusion.

830\. Larry's Comedy Club

…is an interactive, on-line, joke-telling contest. Each player submits a joke. Casino collects the jokes. Casino

displays all of the jokes. The players vote for the funniest joke. Each player whose joke received votes gets Larry-

bucks. The one with the most votes wins. All jokes are archived for later use by Al Lowe and Sierra.

To prevent offending those sensitive Larry players, we offer three levels of bawdiness: the “Sunday School

Clean Room” for non-offensive jokes; “Club Risqué,” for off-color jokes; and, “The RaunchyDome,” where any-

thing goes. Each club’s atmosphere fits its level of raunchiness. The perceived size of the clubs also increases.



<a name="br28"></a> 

Leisure Suit Larry’s Casino Design Document

Page 28

Copyright 1997 by Al Lowe

831\. Larry's Comedy Club, “Sunday School Clean Room”

…is a tiny, closet-sized room with only one table and a postage-stamp stage. It’s where you come when you

click on Comedy Club. It has a door that’s leads to the next comedy area…

832\. Larry's Comedy Club, “Club Risqué”

…is a large, nightclub-sized room with many tables. It has a door that’s leads to the next comedy area…

833\. Larry's Comedy Club, “RaunchyDome”

…is a giant Kingdome of comedy, where anything goes.

A unique aspect of this game is the Tip Wheel, which is how you “vote” for the jokes. You can award any joke

you read from 1 to 5 Larrybucks just by clicking the corresponding area on the Tip Wheel.

The are five game states in this game.

1\. Gathering

2\. Joke Submission

3\. Voting

4\. End of Round

5\. Conclusion

Voice Over Instructions

Welcome to "Leisure Suit Larry’s Comedy Club," where you can hear the best (and worst) jokes on the Inter-

net! Bring in some friends, tell a few jokes, hear a lot more, have some laughs and leave with some Larrybucks.

For those of you new to show business, here's how the Larry’s Comedy Club works. When you’re ready to tell a

joke, just press Enter and type it in. The jokes are collected, then displayed in random order on-screen. You vote by

clicking the icon that best fits your reaction, from bored to hilarious. The better the joke, the more Larrybucks are

awarded to its author.

Remember: the Larrybucks you award don’t come out of your bankroll, they’re “on the house,” so vote freely!

You can’t vote for your own joke—of course you think it’s funny or you wouldn’t have told it! Follow the filth level

for the room you entered: no dirty jokes unless you’re in the proper environment. Oh, and we support the standard

Windows copy and paste keys (control-C and control-V) so you can prepare jokes off-line for presentation here.

Now, get rid of your stage fright and “make ‘em laugh!”

Game State 1: Gathering

Everything is exactly the same as 800. Say What?!, Game State 1: Gathering.

Game State 2: Joke Submission

•

Everyone begins with a submission dialog, accompanied by visuals, sound effects and music. The TV screen

tells players to enter a definition. One of a dozen random voice-over files instructs them how to do it.

The player types a joke into the “My Joke” text field. When satisfied, he clicks “Submit.” Joke length is limited

to the number of characters that can fit into the display area of the TV screen.

•

•

•

Casino collects everyone’s jokes.

This game state lasts 60 seconds or until the player clicks “Submit.” If the player runs out of time, whatever

part of the joke he’s completed is retained, so he can begin there next round.

Game State 3: Voting

•

•

Casino displays each of the jokes collected, in the order entered.

Each joke is displayed by itself on the TV screen. Players read the joke, then vote for it by clicking a number

on the “Tip” wheel. Tips range from 0 to 5 Larrybucks.

•

•

Casino collects the “tips” as the votes are cast. If you haven’t voted when time runs out, it counts as a zero.

The maximum time limit of this game state is a timer multiple times the length of the joke displayed (probably

60" max).



<a name="br29"></a> 

Leisure Suit Larry’s Casino Design Document

Page 29

Copyright 1997 by Al Lowe

Game State 4: End of Round

•

The tips are tallied. Casino displays the number of Larrybucks awarded the previous joke and the player’s

name. His Larrybucks are recorded in the casino server database. Below that, the total rankings for everyone in

the Comedy Club are displayed, in the same format, ranked from high to low Larrybucks.

The maximum time limit of this game state is 10" seconds or until everyone clicks “Go Ahead” or “Exit.”

“Exit” takes you immediately to state 5; “Go Ahead” loops back to state 3 for the next joke or to state 2 if there

are no jokes left.

•

•

Game State 5: Conclusion

•

Casino displays the winning joke, the name of the player who submitted it, and how many Larrybucks the

player won.

•

The player can stay here as long he wants. When the player clicks the “Start New Game” button, they immedi-

ately go back to state 1. They can also right click to get the Map and go to some other part of the Casino.

Chat is available for the duration of this state.

•

•

•

Ads are run in the TV screen.

This game state lasts until the last player leaves.



<a name="br30"></a> 

Leisure Suit Larry’s Casino Design Document

Page 30

Copyright 1997 by Al Lowe

Sound

Music

Like Larry7, a recorded live jazz combo playing real instruments. No MIDI.

Hotel rooms feature varied levels of subtlety in music, from rap to classical string quartet. The music does not

change when you go to CYBERLARRY 2000, CYBERSHOP 2000, and CYBERFACE 2000.

Sound Effects

Rip off Hoyle’s whenever possible. Create new sounds only when existing is not good enough or doesn’t exist

at all.

Pay particular attention to the four party games. Visit www.Berzerk.com and play Acrophobia. Let’s style ours

after that.

Dialog

Larry has the most dialog, but now that off-line play uses all characters they each have some lines.



<a name="br31"></a> 

Leisure Suit Larry’s Casino Design Document

Page 31

Copyright 1997 by Al Lowe

Miscellaneous

Old, Discarded Ideas

Character maker; full body and facial close-up; start not too attractive; spend Larrybucks on health club, plastic

surgeon, etc

Clothing stores; casino wear, swim suits, lingerie (women and men)

Hotel rooms with on-screen “personal chat” graphics, remote mouse cursors for interactive foreplay, massages,

verb buttons.

A jail; a place to put bad people

Self-improvement; health club to build yourself a better body; plastic surgeons

Inflatable woman in hot tub

If drink too many drinks, mouse is erratic like it’s drunk.

File Name & Location

This document is stored at C:\ALA Documents\Larry's Casino\Design.Doc

Issues Yet To Be Resolved

Ideas To Be Filed

“Liquor in the front, poker in the rear!”

Exporting dialog to game

In Access, run query “All-Lines”, save as Excel 97.

In Excel, open All-Lines.xls, select all, copy

In Word, open new document, Paste Special as unformatted text, save as text only.

Things To Do

Fix Casino floor location tooltips

