![](Aspose.Words.03ed3d5c-ae82-4e28-a9d0-d673a8df9f72.001.png)

**Design Document for:** 

**Name of Game** 

**One Liner, i.e. The Ultimate Racing Game** “Something funny here!”™ 

All work Copyright ©1999 by Your Company Name Written by Chris Taylor 

Version # 1.00 

Sunday, May 12, 2024

Copyright (C) 2000 Your Company Name – All rights reserved – Run away! 

Table of Contents 

**NAME OF GAME \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 1 DESIGN HISTORY \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 5** 

VERSION 1.10 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 5 VERSION 2.00 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 5 VERSION 2.10 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 5 

**GAME OVERVIEW \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 6** 

PHILOSOPHY\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 6 *Philosophical point #1 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 6 Philosophical point #2 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 6 Philosophical point #3 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 6* COMMON QUESTIONS\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 6 *What is the game? \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 6 Why create this game?\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 6 Where does the game take place? \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 6 What do I control? \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 6 How many characters do I control? \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 6 What is the main focus? \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 7 What’s different? \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 7* 

**FEATURE SET \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 8** GENERAL FEATURES \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 8 

MULTI-PLAYER FEATURES \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 8 EDITOR \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 8 GAME PLAY \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 8 

**THE GAME WORLD \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 9** 

OVERVIEW \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 9 WORLD FEATURE #1 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 9 WORLD FEATURE #2 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 9 THE PHYSICAL WORLD \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 9 *Overview \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 9 Key Locations \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 9 Travel\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 9 Scale \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 9 Objects \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 9 Weather \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 9 Day and Night \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 9 Time \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 10* RENDERING SYSTEM \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 10 *Overview \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 10 2D/3D Rendering\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 10* CAMERA \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 10 *Overview \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 10 Camera Detail #1 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 10 Camera Detail #2 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 10* GAME ENGINE \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 10 *Overview \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 10 Game Engine Detail #1 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 10 Water \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 10* 

Confidential  Page   5/12/20242 
Copyright (C) 2000 Your Company Name – All rights reserved – Run away! 

*Collision Detection \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 10* LIGHTING MODELS\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 11 *Overview \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 11 Lighting Model Detail #1  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 11 Lighting Model Detail #2  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 11* 

**THE WORLD LAYOUT \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 12** 

OVERVIEW \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 12 WORLD LAYOUT DETAIL #1\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 12 WORLD LAYOUT DETAIL #2\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 12 

**GAME CHARACTERS \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 13** 

OVERVIEW \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 13 CREATING A CHARACTER\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 13 ENEMIES AND MONSTERS  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 13 

**USER INTERFACE \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 14** 

OVERVIEW \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 14 USER INTERFACE DETAIL #1 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 14 USER INTERFACE DETAIL #2 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 14 

**WEAPONS \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 15** 

OVERVIEW \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 15 WEAPONS DETAILS #1 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 15 WEAPONS DETAILS #2 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 15 

**MUSICAL SCORES AND SOUND EFFECTS \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 16** 

OVERVIEW \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 16 RED BOOK AUDIO \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 16 3DSOUND \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 16 SOUND DESIGN  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 16 

**SINGLE PLAYER GAME \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 17** 

OVERVIEW \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 17 SINGLE PLAYER GAME DETAIL #1 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 17 SINGLE PLAYER GAME DETAIL #2 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 17 STORY \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 17 HOURS OF GAME-PLAY \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 17 VICTORY CONDITIONS \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 17 

**MULTI-PLAYER GAME  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 18** 

OVERVIEW \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 18 MAX PLAYERS \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 18 SERVERS  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 18 CUSTOMIZATION \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 18 INTERNET \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 18 GAMING SITES \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 18 PERSISTENCE \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 18 SAVING AND LOADING \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 18 

**CHARACTER RENDERING \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 19** 

OVERVIEW \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 19 CHARACTER RENDERING DETAIL #1 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 19 CHARACTER RENDERING DETAIL #2 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 19 

**WORLD EDITING \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 20** 

Confidential  Page   5/12/20243 
Copyright (C) 2000 Your Company Name – All rights reserved – Run away! 

OVERVIEW \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 20 WORLD EDITING DETAIL #1 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 20 WORLD EDITING DETAIL #2 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 20 

**EXTRA MISCELLANEOUS STUFF \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 21** 

OVERVIEW \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 21 JUNK I AM WORKING ON… \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 21 

**“XYZ APPENDIX” \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 22 “OBJECTS APPENDIX” \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 22 “USER INTERFACE APPENDIX”  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 22 “NETWORKING APPENDIX” \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 22 “CHARACTER RENDERING AND ANIMATION APPENDIX” \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 22 “STORY APPENDIX” \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 22** 

Confidential  Page   5/12/20244 
Copyright (C) 2000 Your Company Name – All rights reserved – Run away! 

**Design History** 

This is a brief explanation of the history of this document. 

In this paragraph describe to the reader what you are trying to achieve with the design history.  It is possible that they don’t know what this is for and you need to explain it to them. 

**Version 1.10** 

Version 1.10 includes some tuning and tweaking that I did after making my initial pass at the design.  Here is what I changed. 

1. I rewrote the section about what systems the game runs on. 
1. I incorporated feedback from the team into all parts of the design however no major changes were made. 
1. Just keep listing your changes like this. 

**Version 2.00** 

Version 2.00 is the first version of the design where a major revision has been made now that much more is known about the game.  After many hours of design, many decisions have been made.  Most of these large design decisions are now reflected in this document. 

Included in the changes are: 

1. Pairing down of the design scope. (Scope, not design) 
1. More detailed descriptions in many areas, specifically A, B and C. 
1. Story details. 
1. World layout and design. 

**Version 2.10** 

Version 2.10 has several small changes over that of version 2.00.  The key areas are in many of the appendixes. 

Included in the changes are: 

1. Minor revisions throughout entire document. 
1. Added “User Interface Appendix”. 
1. Added “Game Object Properties Appendix”. 
1. Added concept sketch for world. 

Confidential  Page   5/12/20245 
Copyright (C) 2000 Your Company Name – All rights reserved – Run away! 

**Game Overview**

**Philosophy** 

**Philosophical point #1** 

This game is trying to do this and that.  Fundamentally I am trying to achieve something that has never been achieved before.  Or.  This game will not try and change the world.  We are ripping off the competition so exactly that I can’t believe it.  The world will be shocked at how we are using an existing engine with new art. 

**Philosophical point #2** 

Our game only runs on Compaq computers.  The reason for this is such and such.  We believe the world is coming to and end anyhow so what difference does it make? 

**Philosophical point #3** 

When you create some of these overarching philosophical points about your design, say whatever you want.  Also, feel free to change it to “My game design goals” or whatever you like to call it. 

**Common Questions** 

**What is the game?** 

Describe the game is a paragraph.  This is the answer to the most common question that you will be asked.  What are you working on? 

**Why create this game?** 

Why are you creating this game?  Do you love 3D shooters?  Do you think there is a hole in the market for Jell-O tossing midgets? 

**Where does the game take place?** 

Describe the world that your game takes place in.  Simple as that.  Help frame it in the reader’s mind by spending a few sentences on it here.  You can go into lengthy detail later in a section solely dedicated to describing the world.  Remember that we want to keep this part of the design light and readable. 

**What do I control?** 

Describe what the player will control.  You will be in charge of a band of rabid mutant fiddle players.  If you want you can switch on the AI and turn it into a fish bowl simulation. 

**How many characters do I control?** 

If this applies talk a little more about the control choices.  Remember to add answers to questions that you think the reader will ask.  This is totally dependent on your design. 

Confidential  Page   5/12/20246 
Copyright (C) 2000 Your Company Name – All rights reserved – Run away! 

**What is the main focus?** 

Now that we know where the game takes place and what the player controls.  What are they supposed to achieve in this world?  Angry fiddle players take over the U.N. building.  Be careful not to add a bunch of salesmanship here.  Your design wants to stay light and informative. 

**What’s different?** 

Tell them what is different from the games that are attempting this in the market right now.  This question comes up a lot. 

Confidential  Page   5/12/20247 
Copyright (C) 2000 Your Company Name – All rights reserved – Run away! 

**Feature Set** 

**General Features** 

Huge world 

Mutant fiddle players 3D graphics 

32-bit color 

**Multiplayer Features** 

Up to 10 million players 

Easy to find a game 

Easy to find your pal in huge world Can chat over voice link 

**Editor** 

Comes with world editor Get levels from internet Editor is super easy to use 

**Gameplay** 

List stuff here that is key to the gameplay experience List a lot of stuff here 

Hey, if you got nothing here, is this game worth doing? 

Confidential  Page   5/12/20248 
Copyright (C) 2000 Your Company Name – All rights reserved – Run away! 

**The Game World** 

**Overview** 

Provide an overview to the game world. **World Feature #1** 

This section is not supposed to be called world feature #1 but is supposed to be titled with some major thing about the world.  This is where you break down what is so great about the game world into component pieces and describe each one. 

**World Feature #2** 

Same thing here.  Don’t sell too hard.  These features should be awesome and be selling the game 

on its own. 

**The Physical World** 

**Overview** 

Describe an overview of the physical world.  Then start talking about the components of the physical world below in each paragraph. 

The following describes the key components of the physical world. 

**Key Locations** 

Describe the key locations in the world here. 

**Travel** 

Describe how the player moves characters around in the world. 

**Scale** 

Describe the scale that you will use to represent the world.  Scale is important!  **Objects** 

Describe the different objects that can be found in the world. 

See the “Objects Appendix” for a list of all the objects found in the world. 

**Weather** 

Describe what sort of weather will be found in the world, if any.  Otherwise omit this section.  Add sections that apply to your game design. 

**Day and Night** 

Does your game have a day and night mode?  If so, describe it here. 

Confidential  Page   5/12/20249 
Copyright (C) 2000 Your Company Name – All rights reserved – Run away! 

**Time** 

Describe the way time will work in your game or whatever will be used. 

**Rendering System** 

**Overview** 

Give an overview of how your game will be rendered and then go into detail in the following 

paragraphs. 

**2D/3D Rendering** 

Describe what sort of 2D/3D rendering engine will be used. 

**Camera** 

**Overview** 

Describe the way the camera will work and then go into details if the camera is very complicated 

in sub sections. 

**Camera Detail #1** 

The camera will move around like this and that. 

**Camera Detail #2**

The camera will sometimes move like this in this special circumstance. 

**Game Engine** 

**Overview**

Describe the game engine in general. 

**Game Engine Detail #1** 

The game engine will keep track of everything in the world like such and such. 

**Water** 

There will be water in the world that looks awesome and our game engine will handle it 

beautifully. **Collision Detection** 

Our game engine handles collision detection really well.  It uses the such and such technique and will be quite excellent.  Can you see I am having a hard time making up stupid placeholder text here? 

Confidential  Page   5/12/202410 
Copyright (C) 2000 Your Company Name – All rights reserved – Run away! 

**Lighting Models** 

**Overview**

Describe the lighting model you are going to use and then go into the different aspects of it below. **Lighting Model Detail #1** 

We are using the xyz technique to light our world. 

**Lighting Model Detail #2**

We won’t be lighting the eggplants in the game because they are purple. 

Confidential  Page   5/12/202411 
Copyright (C) 2000 Your Company Name – All rights reserved – Run away! 

**The World Layout** 

**Overview** 

Provide an overview here. 

**World Layout Detail #1 World Layout Detail #2** 

Confidential  Page   5/12/202412 
Copyright (C) 2000 Your Company Name – All rights reserved – Run away! 

**Game Characters** 

**Overview** 

Over of what your characters are. **Creating a Character** 

How you create or personalize your character. 

**Enemies and Monsters** 

Describe enemies or monsters in the world or whomever the player is trying to defeat.  Naturally this depends heavily on your game idea but generally games are about trying to kill something. 

Confidential  Page   5/12/202413 
Copyright (C) 2000 Your Company Name – All rights reserved – Run away! 

**User Interface** 

**Overview** 

Provide some sort of an overview to your interface and same as all the previous sections, break down the components of the UI below. 

**User Interface Detail #1 User Interface Detail #2** 

Confidential  Page   5/12/202414 
Copyright (C) 2000 Your Company Name – All rights reserved – Run away! 

**Weapons** 

**Overview** 

Overview of weapons used in game. 

**Weapons Details #1 Weapons Details #2** 

Confidential  Page   5/12/202415 
Copyright (C) 2000 Your Company Name – All rights reserved – Run away! 

**Musical Scores and Sound Effects** 

**Overview** 

This should probably be broken down into two sections but I think you get the point. 

**Red Book Audio** 

If you are using Red Book then describe what your plan is here.  If not, what are you using? **3D Sound** 

Talk about what sort of sound APIs you are going to use or not use as the case may be. **Sound Design** 

Take a shot at what you are going to do for sound design at this early stage.  Hey, good to let your reader know what you are thinking. 

Confidential  Page   5/12/202416 
Copyright (C) 2000 Your Company Name – All rights reserved – Run away! 

**Single-Player Game** 

**Overview** 

Describe the single-player game experience in a few sentences. 

Here is a breakdown of the key components of the single player game. 

**Single Player Game Detail #1 Single Player Game Detail #2 Story** 

Describe your story idea here and then refer them to an appendix or separate document which provides all the details on the story if it is really big. 

**Hours of Gameplay** 

Talk about how long the single-player game experience is supposed to last or what your thoughts are at this point. 

**Victory Conditions** 

How does the player win the single-player game? 

Confidential  Page   5/12/202417 
Copyright (C) 2000 Your Company Name – All rights reserved – Run away! 

**Multiplayer Game** 

**Overview** 

Describe how the multiplayer game will work in a few sentences and then go into details below. **Max Players** 

Describe how many players can play at once or whatever. 

**Servers** 

Is your game client-server or peer-to-peer or whatever. 

**Customization** 

Describe how the players can customize the multiplayer experience. 

**Internet** 

Describe how your game will work over the internet. 

**Gaming Sites** 

Describe what gaming sites you want to support and what technology you intend to use to achieve this.  Perhaps Dplay or TCP/IP or whatever.  It is probably a good idea to break the tech stuff out into a separate area, you decide. 

**Persistence** 

Describe if your world is persistent or not. **Saving and Loading** 

Explain how you can save a multiplayer game and then reload it.  If you can or why this is not 

possible. 

Confidential  Page   5/12/202418 
Copyright (C) 2000 Your Company Name – All rights reserved – Run away! 

**Character Rendering** 

**Overview** 

Provide an overview as to how your characters will be rendered.  You may have decided to include this elsewhere or break it out to provide more detail to a specific reader. 

**Character Rendering Detail #1 Character Rendering Detail #2** 

Confidential  Page   5/12/202419 
Copyright (C) 2000 Your Company Name – All rights reserved – Run away! 

**World Editing** 

**Overview** 

Provide an overview about the world editor. 

**World Editing Detail #1 World Editing Detail #2** 

Confidential  Page   5/12/202420 
Copyright (C) 2000 Your Company Name – All rights reserved – Run away! 

**Extra Miscellaneous Stuff** 

**Overview** 

Drop anything you are working on and don’t have a good home for here. 

**Junk I am working on…** 

Crazy idea #1 Crazy idea #2 

Confidential  Page   5/12/202421 
Copyright (C) 2000 Your Company Name – All rights reserved – Run away! 

` `**“XYZ Appendix”** 

Provide a brief description of what this appendix is for and then get down to business and provide data to the reader. 

Here are a few examples of some of the appendices in my latest design… 

` `**“Objects Appendix”** 

**“User Interface Appendix”** 

` `**“Networking Appendix”                      “Character Rendering and Animation Appendix”  “Story Appendix”** 

Okay, that’s it.  I wanted to spend more time on this and really make it a great roadmap for putting a game design together.  Unfortunately it would take a ton of time and that is something that we don’t have enough of in this business.  I think you get the idea anyhow.  Also, don’t get the impression that I think a design should provide the information in any particular order, this just happened to be the way it fell out of my head when I sat down.  Change this template any way you want and if you feel you have improved on it, send it back to me and I can pass it out as an alternative to anyone that asks me in the future. 

Good luck and all that! Chris Taylor 
Confidential  Page   5/12/202422 
