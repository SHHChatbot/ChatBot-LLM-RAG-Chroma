<a name="br1"></a> 

Freddy Pharkas,

Frontier Pharmacist

GameDesignDocument

Copyright1993byAlLowe

forSierraOn-Line, Inc.



<a name="br2"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 2

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Table of Contents

Table of Contents...................................................................................2

Design Considerations ...........................................................................5

Setting...................................................................................................7

Plot Synopsis .........................................................................................9

Story Structure....................................................................................11

“The Prologue” ................................................................11

“Act I—Living the Dream”................................................11

“Act II—The Plot Sickens”................................................11

“Act III—Guns and Neuroses”..........................................11

“Act IV—Showdown at the Hallelujah Corral”...................11

“The Epilogue—Go Rest, Young Man” ..............................12

Controlling Idea..............................................................12

SubPlots.........................................................................12

Puzzle Order ........................................................................................13

Characters...........................................................................................14

Walk–Through......................................................................................19

“Act I—Living the Dream”...........................................................19

Open For Business .........................................................19

Fill Prescription #1..........................................................19

Fill Prescription #2..........................................................19

Fill Prescription #3..........................................................19

Sell “Preparation G” ........................................................20

“Act II—The Plot Sickens”...........................................................20

Flatulent Horses.............................................................20

Stopping the Stampede...................................................20

Hire a Sidekick ...............................................................20

Neutralize Contaminated Water.......................................20

The Burning of Coarsegold..............................................21

Visit Madame Ovaree ......................................................21

“Act III—Guns and Neuroses”.....................................................21

Reverting Careers ...........................................................21

Get All Dressed Up..........................................................22

“Act IV—Showdown at the Hallelujah Corral”.............................22

Stop a Card Shark..........................................................22

“Kill” Some Local Cowboys ..............................................22

Wash up The Lever Bros .................................................22

Quickdraw Showdown ....................................................23



<a name="br3"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 3

Confront the Bad “Guy” ..................................................23

Get off the ground floor...................................................23

Conquer Kenny...............................................................23

“Epilogue—Go Rest, Young Man”............................................... 23

Deaths................................................................................................. 24

miscellaneous.................................................................24

time-based problems (complete the puzzle before timer

elapses, or EndGame) .....................................................24

handgun violence ...........................................................24

schoolroom battle ...........................................................24

Inventory problems.........................................................25

Inventory............................................................................................. 26

Scene by Scene Description ................................................................. 33

Opening Sequence ..................................................................... 33

100 Logo Screen .............................................................33

110 Opening Cartoon......................................................33

150 The Prologue............................................................33

(No Opening Credits).......................................................34

Main Street Exteriors................................................................. 35

200 Robertson Cliff.........................................................36

205 Lemming Snails .......................................................38

210 Blackwater Creek bridge ..........................................39

220 West Main Street, Livery & Bank..............................40

230 West Central Main Street, Saloon & Mom’s & Hotel... 42

240 East Central Main Street, Store & Barber Shop.........45

250 East Main Street, Sheriff & Pharmacy.......................46

260 Schoolyard...............................................................48

270 Oily Swamp .............................................................51

At the Base of Collier Bluff......................................................... 52

300 West Bluff Street......................................................52

310 Central Bluff Street..................................................54

320 East Bluff Street ......................................................56

The “Other Side of the Tracks”................................................... 58

400 “Ye Olde ’Ore House” Exterior...................................58

410 Brothel Waiting Room ..............................................60

420 Madame Ovaree’s C.U. .............................................61

500 Mom’s Rear Entry ....................................................62

The Token Arcade Games........................................................... 63

540 Target Practice.........................................................63

550 Lever Brothers gunfight arcade.................................65

560 Kenny’s quickdraw arcade........................................66

Inside the Pharmacy .................................................................. 68

600 Pharmacy Interior....................................................68

610 Pharmacy Back Room ..............................................71

620 Pharmacy Lab Screen...............................................72

630 Pharmacy Bedroom..................................................79



<a name="br4"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 4

Main Street Interiors ..................................................................81

640 Barber Shop ............................................................81

650 Chester Field’s Mercantile Company .........................83

660 Mom’s Cafe..............................................................84

670 The Golden Balls Saloon...........................................86

675 The Poker Game C. U...............................................89

680 Whiskey Glass Close-up ...........................................90

690 First Bank of Bob.....................................................91

700 Safe Deposit Box C.U. ..............................................92

710 Sheriff’s office ..........................................................93

The Schoolhouse........................................................................95

720 Schoolhouse Interior ................................................95

740 Penelope C.U............................................................99

750 “Lethal Weapon” Schoolhouse...................................99

760 Explosion.................................................................99

730 Schoolhouse basement............................................100

Closing Sequence.....................................................................103

170 Closing Cartoon ......................................................103

175 Closing L.S. ............................................................103

180 Closing Credits .......................................................103

Map ...................................................................................................104

Resources ..........................................................................................106

Documentation ..................................................................................109

Lab Screen Chemicals........................................................................111



<a name="br5"></a> 

Frontier Pharmacist Design Document

As of: Tuesday, November 25, 2003

Copyright 1992 by Al Lowe

Page 5

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Design Considerations

Changes from Larry5

•

•

•

•

less HandsOff cartoon sequences

return to more challenging puzzles

don’t expect everyone to finish this game

Return of death. Forget about “No way to die!” There was no positive

critical reaction to lack of deaths in Larry5.

•

less multiple-path and multiple-puzzle solutions, except where it’s logical

and obvious to solve a puzzle in two ways or with objects you already have

•

•

•

•

no “skipping difficult puzzles for no points”

no “talk to a character until you get the solution” solutions

smaller, tighter game

less linear, more “round;” players can explore most of world immediately

Larry5 Ideas to Keep

•

•

lots of humor, silly stuff, non-sequiturs, anachronisms, goofy ideas

extra points given for logical or funny actions unnecessary to complete

FPFP

characters understand all objects and all verbs available to the player at

the time

Fast Forward icon so player can skip ahead past any HandsOff cartoon

sequences

•

•

•

•

suggested “Save Games” after key progress has been made

all “first person” scenes replace the Walk icon with the Exit icon

A few thoughts

•

•

•

•

a little sexy; some adult language

a little arcade action, adjustable by “arcade level” slider in control panel

puzzles well-paced with easy first, more difficult later

at first, Freddy outwits others without resorting to violence; when battle

is inevitable, he transforms back to gunslinger

•

characters are realistic looking, but have ability to do cartoonish

stretches, alterations, etc.

•

•

keep the score displayed continuously in the icon bar

cartoons have a flickery “stereopticon” effect for “Old West” feel and “si-

lent movie” text “slides” with large borders like an old movies

•

•

sepia-toned photographic images mark beginning of each act; image dis-

solves to full-color screen as game play begins. Each act begins with Freddy

in a different area, close to the beginning action.

text windows look like old Western newspapers: parchment color, frayed

corners, Old West-type font

•

•

control panel looks like old wood

creative cursors: non-tracking, shaky cursor during target practice; cur-

sor parks at bottom of screen before gun fight



<a name="br6"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 6

•

Freddy can’t look like Larry!



<a name="br7"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 7

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Setting

The Time

The entire game is set in Coarsegold, California in the late 1880s—30 years after the

gold ran out. Once a major Gold Rush city, serving as supplier to thousands of gold

panners and hard rock miners, when the gold ran out so did the populace. It’s a town

fallen on hard times. Current claim to fame: “home of the annual moonlight cow tipping

festival.” Current city slogan: “Gateway to Nowhere.” Abandoned buildings decay every-

where. Even the town’s railroad station is boarded up, the spur track overgrown with

weeds since it was abandoned years ago when the trestle washed out and there wasn’t

enough traffic to warrant replacement. Coarsegold is isolated, off the beaten track and

on its last legs—a shadow of its former glory. It remains merely to supply the few ranch-

ers and cowboys in the area with food, drink, hardware, supplies and (rented) female

companionship. The only similarities to the real Coarsegold are the foothill setting and

gold rush history. Essentially, we’re just using the name.

FPFP uses both daylight and nighttime exteriors, while the interiors remain con-

stant. Exteriors must be designed with VGA palette-shifting in mind for sky colors and

twinkling stars. Many puzzles have time limits that must be met before the town suc-

cumbs to disaster. The period of the 1880s allows us to have some inventions and

knowledge available that wasn’t common knowledge in rural California. Since oil plays a

motivating factor in the plot, it’s reasonable to assume someone from Pennsylvania

might know about it, but someone from Coarsegold wouldn’t, as oil wasn’t discovered in

California until the 1890s.

The Town

The main street through town is called (cleverly enough) “Main Street” and contains

what’s left of the town’s business district. Artistically, it is one, eight-screen-wide, hor-

izontal-scrolling painting, that provides access to FPFP’s business interiors. The near

side of Main Street shows various railroad features, inaccessible to the player, that

block nearly all access to the South and provide interesting shadows and shapes for

Freddy to walk behind, i.e., an old railroad trestle, some cattle loading pens, grain stor-

age bins, abandoned railroad station, assorted railroad buildings, etc.

These areas are along Main Street, from West to East. Each is not a full screen.

Area

\# of rooms Additional interior rooms

Aunt Hill

Robertson Cliff

George’s Gorge

Blackwater Creek bridge

Smithie’s Blacksmith Shop

First Bank of Bob

Balance Street

The Golden Balls Saloon

Mom’s Cafe

1

2

Close-up of exterior

Interior, safe deposit box C.U.

(North to West Bluff Street)

Interior, Poker game

Interior

2

1

abandoned Dirty Sheet Hotel

Commerce Street

Chester Field’s Mercantile Co.

abandoned Post Office

O’Hanohan’s Barber Shop

Sheriff’s Office

(North to Central Bluff Street)

Interior

1

1

1

Interior

Interior



<a name="br8"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 8

abandoned Telegraph Office

abandoned Pee Pee’s Playhouse

Freddy Pharkas’s Pharmacy

abandoned Assay Office

Education Lane

4

1

Store, back room, Lab Screen, bedroom

Only here to be burned down

(North to East Bluff Street)

schoolhouse

Interior, Penelope C.U., basement

oily swamps

South of the railroad tracks lies the “bad part” of town. This is very limited. Abandoned

buildings are implied, but on the other side of the tracks is nothing but:

Area

whorehouse

\# of rooms Additional interior rooms

Waiting room, Madam C.U.

1

North of Main Street’s shops are the three scrolling screens of Bluff Street, which lie at

the base of Collier Bluff, the large hill behind town. These include foreground silhou-

ettes of the town’s residential area, and:

Area

\# of rooms Additional interior rooms

Boot Hill

sheriff’s shooting range

church

1

Target practice M.S.

Mom’s Rear Entry

water tower

Barber shop Rear Entry

Access to saloon, hotel balcony

Access only, no picture

The Look

FPFP’s style is not real Old West, but Hollywood Western Set Decoration style: wood-

sided wood-framed buildings with wooden sidewalks beneath wooden overhangs and

wooden false fronts with gaudy period lettering; wooden water tanks, horse watering

troughs, hitching posts, outhouses, and out-buildings scattered throughout town; a

small wooden dynamite shed behind the stable; a few two-story buildings (hotel, saloon,

brothel), but only the hotel has an upstairs porch; all the stores and homes have lots of

gingerbread, etc.

Stray dogs roam through town, lie down randomly, pant a while, lick themselves,

then get up and walk off. No interaction with Freddy, just atmosphere. Class Junkyard

of Dog

The various horses standing about should all be distinctive in manes, tails, size,

color, saddlebags, saddles, ropes, rifles, etc.

Horseshoes hang above doorways, branding irons, ropes, whips, much Western

memorabilia

wagon wheels, piles of firewood everywhere

privies, outhouses are common

Wanted: Dead or Alive posters everywhere



<a name="br9"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 9

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Plot Synopsis

You are Freddy Pharkas, bachelor

pharmacist and small businessman living

a quiet life in the rapidly-decaying former

Act I

Game play begins with you standing

Gold Rush town of Coarsegold, California outside the recently closed Dirty Sheet

during the late 1880s. Only one person in Hotel. You head for your Pharmacy to

town knows the secret of your past: you find a series of customers waiting to have

were raised to be an adolescent gun- their prescriptions filled. You realize one

slinger and indeed, were once the fastest of the prescriptions is obviously danger-

draw in the West, until that fateful day ous—Ol’ Doc must have been drunk

on a dusty street in Pecos when you fi- again when he wrote this one—and pro-

nally met your match, had part of your vide the correct medicine instead. The

ear shot off, and vowed to give up your village smithie informs you he’s sold out

life of excitement and “bad guy disposal” his business and is leaving town because

for your first love: pharmacy!

the horses have developed terrible, un-

controllable flatulence. The sheriff shuts

down your pharmacy on an obviously

trumped-up charge. Act I ends on a de-

cidedly down note—you are out of busi-

ness, your life and your new career in

ruins.

Your bucolic existence is short-lived,

however, as simple Coarsegold’s peaceful

karma is soon threatened by a series of

troubles which its humble citizens are

powerless to stop. Coarsegold’s salvation

falls directly on your shoulders and it’s

up to you to save your new hometown us-

ing nothing more than your wits (and

possibly your pestle).

Act II

…begins the challenges. Your first is

to cure the horses’ severe flatulence be-

fore everyone has to leave town! Then,

“thar’s a stampede a’comin’”—a stampede

of snails! Diverting the snails, you dis-

cover a Hindu trapped on an anthill, res-

cue him and hire him as your clerk. He

soon becomes “Srini Lalkaka Bagdnish,

my loyal Indian sidekick.” He proves him-

self invaluable, not only around the store

(where he makes mistakes that prove

helpful later), but in your defense of the

town. It seems he has an uncanny ability

to perceive, and warn you of, impending

danger. Together, you halt an epidemic of

diarrhea by purifying the town’s con-

Your problems go from bad to worse.

Outlaws invade the city; gunfire begins.

The town madam persuades you it’s time

to resume “your ol’ gunslingin’ ways to

protect these simple townsfolk.” Persever-

ing through wave after wave of villains,

you finally learn who is behind these

seemingly unrelated incidents and bring

the guilty party to justice, so that

Coarsegold may once again resume its

previous boring condition, although with

a considerably healthier tax base!

The Prologue

…is a short, easily bypassable cartoon taminated water supply. Running out of

showing sepia-toned vignettes of your scatological openings, you then stop an

early life as a gunslinging toddler, your arson fire threatening to burn down the

final gunfight, your new start in your new entire city.

career in your new location, closing with

Intending to celebrate after the fire,

you head for the brothel. As you ap-

proach, you overhear the banker plotting

your demise with the sheriff! You head

inside for a little pillow talk with the

madam, who warns you of an impending

invasion by a gang of rowdy cowhands.

She convinces you your wits are no

the arrival of Coarsegold’s new school-

marm. Over the vignettes, you listen to

“The Ballad of Freddy Pharkas,” which

tells your tale, Autrey-style.



<a name="br10"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 10

longer enough; you must prepare once high noon, with your old nemesis, the evil

again to “sling hot lead!”

“Kenny the Kid!” You can’t win the duel,

but if you tie, Kenny inadvertently reveals

the source of your troubles—Penelope

Primm, the new schoolmarm!

Act III

…is your preparation for battle. You

gather your pistols, holsters, and ammo.

You patch yourself up, head for the

Your hands are shaky and your mouse schoolhouse with your six-guns cocked,

cursor’s aim weak. With Srini’s help, you ready for a “schoolmarm showdown!”

steady your aim, regain your accuracy Penelope whips something out of her bo-

and practice your quickdraw. You gather som that captures your complete atten-

your “Festus Lauren wardrobe” and pre- tion. You wake up in the basement just

pare a disguise: a silver ear which you in time to see her light a stream of oil

make from objects found ’round the that explodes just after you escape. You

house!

dramatically “buckle swashes” with her

until you must simultaneously dispatch

Kenny the Kid and disarm Penelope, then

slice the “sign of the Rx” into her shirt!

Act IV

…provides the tension you’ve been ex-

pecting. It begins with a slick riverboat

gambler who sets up shop in the saloon,

winning away the local bumpkins’ real

The Epilogue

…recapitulates “The Ballad of Freddy

estate. You catch him cheating, and Pharkas” with a few more choruses to

through some fancy shooting, freeze him wrap up our loose ends. Penelope’s reve-

in the act, then have him arrested.

lations concerning the value of oil revi-

talize Coarsegold, bring it untold wealth

as it becomes California’s first oil town!

We conclude with a long shot showing

the town covered with oil derricks and

flaunting its gaudy new paint job. The

village is abuzz with rumors about “…our

masked protector,” and, “…will he ever

return?” and, “Who the hell was the

weirdo with the silver ear?”

Immediately, dozens of cowhands in-

vade Main Street, firing their pistols

“carelessly,” killing many locals until you

stop them with a dose of laughing gas.

Next, the notorious “Lever Brothers gang”

challenges you to a shoot-out in which

you are the primary target in a wacky

shooting gallery arcade game. You “out-

shoot-out” them!

You smile unassumingly.

Our climax is a one-on-one quickdraw

standoff in the middle of Main Street, at



<a name="br11"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 11

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Story Structure

“The Prologue”

A short readily-bypassable cartoon describes your past life as gunslinger, your final ca-

reer-changing gunfight, your new occupation, new start, new location, and introduces

Coarsegold’s new schoolmarm.

“Act I—Living the Dream”

Restart Game begins here.

Fill prescription #1 using easy-to-make pills from powders clearly labeled on shelves.

Fill prescription #2 by combining proper compounds per instructions in Game Manual

to create medicine for pills.

Correct the drunken doctor’s erroneous prescription #3; prepare and issue the correct

medicine instead.

Sell Preparation G to blacksmith; learn he’s leaving town after selling out to banker.

INCITING INCIDENT

Sheriff shuts down pharmacy because “it’s a firetrap—why, this entire building is made

of wood!”

“Act II—The Plot Sickens”

Cure horses’ flatulence by Deflatulizing the town’s watering troughs while wearing a

homemade gas mask.

Divert a stampede of snails into the canyon by spreading beer across their path.

Rescue and hire your “loyal Indian sidekick;” put him to work in your pharmacy.

Neutralize the town’s contaminated water supply.

Stop “the burning of Coarsegold” by spreading baking soda on the fire.

Visit Madame Ovaree and learn of threats to your life and worsening town troubles. De-

cide to accept the challenge, return to your old life, “strap on” once again.

“Act III—Guns and Neuroses”

Prepare for battle: arm yourself, practice your target shooting and quick-draw.

Dress for success: find your wardrobe, make your ear disguise.

“Act IV—Showdown at the Hallelujah Corral”

Catch the card shark cheating at poker, firing a tricky bounce shot to hold him for ar-

rest.

Stop dozens of rowdy cowhands from tearing up the town by filling Main Street with ni-

trous oxide, causing them to roll on the ground, laughing, unable to shoot.

Stop the Lever Brothers gang through an humorous, mildly-arcade, shooting gallery.

CRISIS

Lose part of your other ear to your old nemesis Kenny the Kid in a quickdraw gunfight.



<a name="br12"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 12

CLIMAX

Confront Penelope at the schoolhouse, save yourself with your student slate.

Escape from the basement before the explosion.

Confront Penelope again via swordfight. Kill Kenny as you slice the sign of the prescrip-

tion in her shirt. Escape just as the schoolhouse explodes.

“The Epilogue—Go Rest, Young Man”

RESOLUTION

Another short cartoon wraps things up with another 3Space helicopter shot zooming

back out from Main Street showing the town cleaned up, successful, and filled with oil

derricks.

Controlling Idea

You can’t run from life’s problems. Maturity requires you to face your problems.

SubPlots

Penelope Primm’s attempt to gain oil rights from townsfolk.

Your unsuccessful attempts at romance with Penelope.

Loyal Indian sidekick Srini’s progress as an assistant; ends up medicine man on local

tribal reservation.

“Diamond Jim” Laffer hits on all the town’s women to no avail. A comic subplot, run-

ning gag, and inside joke.

The importance of sheep to the frontier man—and the women who love him!



<a name="br13"></a> 

Frontier Pharmacist Design Document

As of: Tuesday, November 25, 2003

Copyright 1992 by Al Lowe

Page 13

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_Puzzle Order

1\. Logo

2\. Opening Fly-In

3\. Titles

4\. Opening cartoon

5\. Credits

6\. Ready For Business

7\. Prescription #1

8\. Prescription #2

9\. Incorrect Prescription #3

10\. Prescription #3 Under Glass

11\. Corrected Prescription #3

12\. “Preparation G”

13\. Sheriff shutdown

14\. Start Act II

15\. Flatulent Horses

16\. need gas mask

17\. Snail stampede

18\. Lemmings

19\. hire a Sidekick

20\. Brief your sidekick

21\. Contaminated Water

22\. Burning of Coarsegold

23\. Overhear Sheriff & Banker

24\. Madame Ovaree

25\. Arm yourself

26\. Target Practice

27\. Quickdraw practice

28\. Dress Up

29\. Cat Ballou

30\. Card Shark

31\. Incoming Aces

32\. Rowdy Cowhands

33\. ROLFing Cowhands

34\. Lever Bros shooting gallery

35\. Kenny’s Quickdraw arcade

36\. bleeding in the dirt

37\. schoolhouse showdown

38\. trapped in the basement

39\. sword fight

40\. killing Kenny

41\. end game cartoon



<a name="br14"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 14

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Characters

All the characters’ Talk responses should be “curPuzzle-aware,” if that seems rea-

sonable for that character.

Freddy Pharkas

Our Hero. “Pharmacy is my life!” Six years ago, soon after

Coarsegold’s only town pharmacist moved away, our hero

showed up to set up shop. He is approximately 30 years

old; tall, bespectacled, and appears to be physically weak,

even wimpy; missing the upper part of his right ear, al-

though we’re careful never to show his right profile; intel-

ligent, literate, professional, clever, humorous; a tinkerer,

inventor, scientist; intensely private, speaks little of his

past; “loves puns, double entendrés and private moonlight

walks near the stables.” Although he is friendly and well-

liked by all, he is close to no one. Wears somber black

suits with string ties until he changes into his Palomino-

colored satin and silk gunslinger outfit.

The townsfolk wonder why he moved to Coarsegold as he

obviously doesn’t fit in very well. He never says. He is sin-

gle, never anything but polite to the few rare single women

in the area. Once a month he frequents Madame Ovaree,

the town madam—$1, straight, no funny stuff.

What the townsfolk don’t know is Freddy was once

“Freddy Boy” Pharkas, the youngest sheriff and fastest

gunslinger the West had ever known. Continually chal-

lenged by every young tough who was quick on the draw

and had something to prove, Freddy lost part of that ear

in his last gunfight against his childhood rival, Kenny the

Kid. During his recovery, he realized those bastards would

never stop until he took a bullet through the chest, so he

resigned his post at the ripe old age of 22, went back East

to college and began his new career. He became…

Freddy Pharkas, Frontier Pharmacist!

Srini Lalkaka Bagdnish Freddy's loyal Indian sidekick. Really from India, not an

Native American. Came over to build the railroads, then

found out they only hired Chinese. Helps keep the game

moving by focusing the players’ attention on the current

puzzle. When we want him, he’s there; otherwise, we don’t

know much about him. He wants to “return to my people”

and at end of FPFP, using your training, he takes a job at

the local reservation as medicine man. Turban, dark-

skinned, short, a contrast to Freddy. Throughout FPFP he

displays an uncanny ability to perceive impending danger

and warn you (conveniently for the designer!).

If curPuzzle > “Brief your sidekick” && you’ve been outside

at least once:

The first time you Talk to Srini after this, he reveals how

he “over-ordered a little, but to make up for it, I’ve entered



<a name="br15"></a> 

Frontier Pharmacist Design Document

As of: Tuesday, November 25, 2003

Copyright 1992 by Al Lowe

Page 15

us in the Western Regional Druggists’ Association’s An-

nual “Best Overpriced Vaseline-like Substance Display

Contest.” As you begin a lecture on “effective pharmaceu-

tical stocking procedures,” he interrupts with bad news:

“throughout the town, there are long lines for the out-

houses—someone has polluted the town water supply with

laxative! You must help!”

Bump curPuzzle to “Contaminated Water” and set the

badWaterTimer to 300 ?? seconds. If the timer expires be-

fore you purify the water tower, the death message shows

lines of animated men outside outhouses. EndGame.

If curPuzzle > “Arm yourself” && you haven’t encountered

Srini before, he suggests “you could use a little target

practice, Boss. Why don’t I meet you over by Boot Hill in a

few minutes.” He then leaves, walking in that direction.

Some encounter with Srini mentions “I mixed a little sugar

with some of that oily water from the swamp. It didn’t

taste very good, but when I added a little cocaine, you

don’t even notice. I think I’ll call it Cola-Caine.”

A later encounter mentions “I ordered a little extra baking

soda to mix with some of that “turned” wine Sam Andreas

had down in the basement of the saloon. I figured sodium

bicarbonate (NaHCO ) plus acetic acid (CH COOH) would

3

3

produce plenty of carbon dioxide gas (CO<sub>2</sub>).

A later encounter mentions “I removed the caffeine and

the cocaine and the oily water, leaving just the bubbles

but no flavor. I’m going to call it ‘6-Up!’”

Srini often quotes Hindu philosophy; says “Holy Cow” a

lot.

Ol’ Doc Gillespie

Penelope Primm

Alcoholic town physician. Always found playing poker in

The Golden Balls Saloon. Gray hair, slightly overweight,

sloppy dresser. Wears tiny dark glasses. Illegible hand-

writing. Writes wrong prescription which Freddy carries to

him for reinterpretation. Nickname “Dizzy.“ Never seen

walking.

The new town schoolmarm. Arrives in Coarsegold just be-

fore the start of FPFP. From the Pennsylvania oil country,

a graduate of Meadville Normal School. Seems prim and

proper. A loner. Stays away from everyone. “Devoted to my

work.”

Demure and quiet, she is the other half of Freddy's love

subplot. Not beautiful, but pretty, does little to promote

her beauty. Fascinating to Freddy, she does nothing to

discourage his interest, while never furthering it.

“What if we just keep cutting down the trees and building

wooden buildings? What happens when there’s no trees

left any more? Will this damage some layer of the atmo-

sphere we scarcely know about? Will the constant burning

of these wood fires pollute this crystalline atmosphere we

all hold so dear?”



<a name="br16"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 16

Because oil was discovered in Pennsylvania in the 1860s,

she realizes the value of the “black gold” still under the

town. She plots to gain control of the oil by running off the

town’s inhabitants, so she can cheaply acquire the min-

eral rights for the rich oil deposits she feels certain lie be-

low. In cahoots with Phineas H. Balance, the town banker.

How and specifics are explained in the schoolhouse base-

ment, at the end of the game.

Madame Sadie Ovaree

Our “hooker with a heart of gold.” Stereotypical Western

madam and Freddy's closest friend, though they are

scarcely close. Not a tart, bitch, slut, or cheat. Not good

looking, but not hideous. Portly. Is interested in Freddy as

a friend, as well as a customer. At least she has his ear

(well, part of it) one night a month (along with some of his

other organs). He refuses her girls, as Sadie is more dis-

creet. She’s the only person in town who knows of

Freddy's past. Therefore, she becomes the one who con-

vinces him to revert to his old ways and save the town.

Her scenes with Freddy are non-sexual.

Gabby “Smithie” Smith Smithie, the village smithie. begins the horse flatulence

puzzle and tells Freddy he’s sold out his business to the

banker. Large, strong, muscular, stocky, bearded, sweaty,

dirty, dim.

Checkum P.

“Chicken” Shift

The cowardly, crooked sheriff. Known as “Chicken Shift”

to most of the town. Rotund, lazy, sloppy, unkempt.

Closes down Freddy's pharmacy, thus setting up the Incit-

ing Incident. Loves coffee and apple pie. Gives Freddy

ammunition or the gun cleaning kit for either one. He’s

deviously controlled by the town banker, P. H. Balance.

Phineas H. Balance

The town banker. P. H. Balance is blatantly rich and pom-

pous, owns the big house on top of Collier Bluff, the hill

behind the town. Conservative, shifty, obviously crooked,

owns the sheriff. At first, we’ll lead the player to believe P.

H. is behind the town’s wave of problems. Actually con-

trolled by Penelope; will “do anything for a chance to dust

her erasers!” Works at the First Bank of Bob as custodian,

teller, clerk, and officer. Too cheap to hire employees. Why

didn’t he name it after himself?

Wheaton “Aces” Hall

dozens of cowboys

Slick riverboat gambler. Brought to Coarsegold from Back

East to take money, land, buildings, businesses from hon-

est townsfolk via his poker-playing skills. Cheats using a

third, fake hand. Freddy catches him cheating, then drops

a chandelier on him, holding him in place until the sheriff

comes.

From the cattle drive that’s “jest’a passin’ thru outside’a

town!” Interchangeable parts. Many look alike (since

they’re the same view used over and over). These boys are

hired to come in and shoot things up, scare the locals,

and hopefully, drive ’em out of town. They have no inter-

action with Freddy other than to kill him whenever he

steps out into the street! Freddy gasses ’em with laughing

gas.



<a name="br17"></a> 

Frontier Pharmacist Design Document

As of: Tuesday, November 25, 2003

Copyright 1992 by Al Lowe

Page 17

The Lever Brothers

Names: Lorne, Hoss, Adam, Little Joe. A quartet of ma-

rauding bandits, horse thieves, and cattle rustlers, obvi-

ously tough, up to no good, each with a sizable price on

his head. They ambush Freddy as he leaves the brothel

exterior after firing at the cannister of laughing gas. When

the shooting starts, they become shooting gallery card-

board cutouts with red lights on chest and points painted

on belly. When you shoot them, they fall over as if 2-D,

then rise back up. Make ’em look mean.

Kenny the Kid

Big time, mean-assed gun-slinger from out of town. Ulti-

mate bad guy. Has own rattlesnake soundFX he plays

himself whenever he’s around. Freddy can not out-draw

him. Kenny either shoots Freddy dead, or preferably,

shoots off his ear. Looks remarkably like Ken Williams,

but surprisingly, no relation.

Salvatore O’Hanohan

Helen Back

Town barber and local “dentist.” Irish-Italian, dark,

swarthy, redhead. Loves Irish whiskey and opera. First

barber in history to provide “reading material” for his cus-

tomers. Trades Freddy a tank of nitrous oxide for some

French postcards.

Proprietor of of “Mom’s Eats” cafe (“You know it’s good—all

the stagecoaches stop there!”). “I want sumptin’ to eat!”

“Go to Helen Back.” Freddy tries to convince her to put es-

cargót on her menu to clean up the town. Fails. Hates

flies, always swatting.

Sam Andreas

Friendly bartender. Runs The Golden Balls Saloon, a (rela-

tively) clean joint with no foul language while ladies are

present, honest poker games, and drinks that are too wa-

tered down to get drunk on. Favorite sayings are “it’s my

fault” and “I’m honest to a fault.” Sells beer to Freddy.

Chester Field

Proprietor of the General Store. Never seen, only yells out

from back room “Help yourself, I’ll be right out,” but never

shows.

Whittlin’ Willie

Sits by the pot-bellied stove in the General Store whittling

all day. If you Talk to him, he just makes small talk. But if

you give him the silver medallion, he gives you clues about

the lost wax casting process before handing the medallion

back.

Judge Jim Beam

The crooked county judge. Only found in The Golden Balls

Saloon, Jim is a whiskey drinker, poker player and tip-

pling buddy of P. H. Balance. Only finds Freddy guilty

whenever he’s given the chance through a death sequence;

otherwise, no interaction.

“Zircon Jim” Laffer

Great-great-grandfather of Larry Laffer. Self-imposed lady-

killer, a guy “stuck in the 70’s (1870’s that is).” Looks just

like Larry, only in 1880s wardrobe. Mark Twain white suit

and hat. Local lumberyard owner. Harmless, humorous,

non-essential character, his principal job is hitting on the

new schoolmarm. No interaction with Freddy. At end of

game, he wonders if you could make clothes out of the

newly-discovered oil.



<a name="br18"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 18

assorted “drugstore

Indians”

Various Indians stand without moving outside the phar-

macy holding cigars for no apparent reason. Running Gag.

(No, that’s not a description, he’s one of the braves!)

assorted townsfolk

a sordid hookers

as needed.

Named after virtues: Purity, Chastity, Charity, Patience,

Hope, Modesty, Virginal. No real roles, just hang around

the brothel, looking for work.



<a name="br19"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 19

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Walk–Through

“Act I—Living the Dream”

Open For Business

A door key is provided in Inventory when FPFP begins; Use it on the front door of

your Pharmacy to open up for business.

Fill Prescription #1

Penelope Primm follows you inside as you open your Pharmacy. She hands you Pre-

scription #1 as soon as you are inside. Find the back room, discover how to access the

Lab Screen. On the Lab Screen, Take an empty medicine bottle and a cork from the

shelf and put them on the Lab table. Take the bulk liquid medicine jar from the shelf

and click it on the graduated cylinder. Click the cylinder on the empty bottle. Click the

cork on the filled bottle to create Medication #1. Take it, leave the Lab Screen, return

to the store, and Use it on Penelope Primm.

Fill Prescription #2

Helen Back hands you Prescription #2 as soon as you give Medication #1 to Pene-

lope. Return to the Lab Screen. Find the pill-making machine, a graduated cylinder, a

spatula, and place them all on the Lab table. Find a pill bottle and click it on the pill-

making machine to place it under the machine’s spout. Take the correct bottle of liquid

from the shelf, click it on the graduated cylinder until it is filled to the correct mark, put

the bottle back on the shelf. Move the balance’s weight to the correct number, find the

correct powder, place it on the table. Click the spatula on the jar to get some powder,

click the spatula on the balance to place it there. Do this until the balance is balanced.

Put the jar of powder back on the shelf. Take the powder from the balance. Click it on

the pill-making machine to pour it inside. Click the graduated cylinder on the pill-

making machine to pour its contents inside. Click the Hand on the machine to form the

mixture into three pills. Repeat six times to make a total of 21 pills (“take three daily for

a week”). Stick a cork in it. Take Medication #2, leave the Lab Screen, Use it on Helen

Back.

Fill Prescription #3

Madame Ovaree hands you Prescription #3 as soon as you give Medication #2 to

Helen Back. Leave her in the Pharmacy, go to the saloon, Take the whiskey glass, click

it on prescription #3 in Inventory to read it. Realize it is wrong, go to the saloon, find

Doc playing poker, click Prescription #3 Under Glass on him. He realizes his error and

corrects it. Return to the Lab Screen. Move the wooden box of crystals, three spat-

ula/scoops, an empty bottle, the mortar and pestle, the medicinal papers, and medical

powder #2 to the table. Measure three ccs of crystal granules into the mortar, measure

two ccs of medical powder into the mortar, grind with the pestle, measure one cc of the

mixture onto each sheet of paper, repeat until three papers are prepared. Click the pa-

pers on the wooden box to insert them inside. This creates Corrected Medication #3,

Take it, leave the Lab Screen, return to the Pharmacy, and Use it on Madame Ovaree.



<a name="br20"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 20

Sell “Preparation G”

…to Smithie, who walks in as soon as you give Corrected Medication #3 to Ma-

dame Ovaree. After he requests “Preparation G,” you find it on the main shop screen

(not on the Lab Screen as it’s an OTC drug). Take it, then Use it on Smithie. Smithie

then sets up the banker subplot, and introduces you to the…

“Act II—The Plot Sickens”

Flatulent Horses

Smithie’s clue about the horses’ problem starts this puzzle’s timer. Whenever the

timer is running, but before you’ve created the Deflatulizer™, whenever you walk out-

side the Pharmacy you get a warning about the aroma. Take the tin can sitting on the

foreground shelf at Mom’s; Take some charcoal from Smithie’s hearth; Take the ice

pick stuck in the wall behind the saloon; Take a bridle from one of the horses on Main

Street. In the Inventory window, click the ice pick on the tin can to perforate it, click

the charcoal on the tin can to place the charcoal inside, click the bridle on the tin can

to create the gas mask. (Any other logical order of creation is also acceptable.) After a

timer expires, you must wear the gas mask by clicking it on yourself before venturing

outside. Get an empty paper bag from the General Store. Fill it with horse flatulence by

Using it on the rear end of any horse with its tail up in the air to get the horse flatu-

lence sample. Go to the Lab. Study the Game Manual to learn how to create the solu-

tion. The ingredients you need are on the Lab Screen. Use the Deflatulizer™ on any

horse trough and we fade to black, cover its application to all the town’s horse troughs

through text, then fade up on you with your gas mask gone, standing outside your

closed Pharmacy.

Stopping the Stampede

Immediately, Paulette Revere rides through town yelling, “thar’s a stampeeede

a’comin’!” to start this puzzle’s timer. Snails appear at Robertson Cliff. You could take

the snails and give them to Helen Back for some points. You should Take some money

from the pharmacy’s cash box, enter The Golden Balls Saloon, Use the money on the

bartender to buy a case of beer. Take the church key sticking out of the lock inside the

door of the church, go across the bridge, and Use the church key on the beer in the

Inventory window. Use the now-open beer bottle on the snails. We see you pour a trail

of beer leading the snails away from the bridge to the railroad track trestle, down the

tracks to fall off rails’ “split ends” to their death in Blackwater Creek.

Hire a Sidekick

Upon returning to Robertson Cliff after solving the snail puzzle, Srini will always be

seated on an anthill surrounded by swarms of ants. Take the ladder from the school-

yard slide, click it on the anthill to allow his escape. Hire him. We cut to the Pharmacy’s

back room to see you give him his first assignment.

Neutralize Contaminated Water

This puzzle’s timer begins when you first see waiting lines at the town’s outhouses.

Go to the Lab, create the water purification solution, and go to Smithie’s blacksmith

shop. Take the rope from the wall, make a lasso by clicking the Hand on the rope in

the Inventory window. Take the schoolyard ladder from Robertson Cliff, return to the

water tower, lean the ladder against the water tower leg, climb the ladder to the tower’s

platform. Take the ladder from below you, then lean it against the tank by Using it on

the tank. Climb to the top of it again. From the top, throw the lasso by clicking it on the



<a name="br21"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 21

ornament on the top of the water tank. Your first two throws miss, but your third throw

lassos the ornament on top. You climb the rope to the tank’s roof. Click the Hand on the

hatch to kneel down and open it. Use the water purification solution on the now-open

tank. Fade to black; we skip the animation of your descent, then fade in on your bed-

room with you in bed, asleep. Your ladder, rope and any other no longer needed Inven-

tory objects are missing from Inventory.

The Burning of Coarsegold

Your respite is brief. Srini awakens you with big news: “Fire!” You run downstairs

and outside to see the assay office next door on fire. Take the baking soda from the

sidewalk in front of your store. Go to the schoolyard, Use the baking soda on the east

end of the teeter-totter, click the Hand on the swing to climb aboard, swing faster and

higher by clicking the Hand on yourself as you swing forward, until you are swinging

high enough to leap from the swing to the roof of the school. Click the Hand or Walk

icon on the school roof to jump. Walk to the other end of the school roof, jump off onto

the opposite end of the teeter-totter from the baking soda. You land on the teeter-totter,

flinging the sacks of baking soda high into the air, across the street and onto the fire.

Visit Madame Ovaree

Since it’s night and nothing else is open, you head for the brothel. Entering the

scene, you overhear the banker and the sheriff standing on brothel porch, discussing

your demise. Take the French postcards from a table in the brothel’s waiting room. En-

ter Madame’s “office.” Talk to Madame, learn of the bad times coming, decide to save the

town with your guns. Madame helps you “shoot off a couple of rounds” before you go.

“Act III—Guns and Neuroses”

Reverting Careers

Again we fade in on your bedroom with you in bed as you awaken. Take the desk

key from your nightstand drawer. Walk downstairs to the back room, Use the desk key

to unlock the pharmacy desk, open it, Use the same desk key again to unlock the cub-

byhole drawer, open it, Look inside the drawer and automatically Get a letter. Look at

the letter in Inventory to learn the name of the man you made swear to never give you

your pistols again. Walk to Boot Hill, Take the shovel. Find Phillip Graves’s tombstone.

Use the shovel on the grave to dig it up. Click the hand on the now-open grave to jump

in, open the casket, search Phil’s clothing and Get your safe deposit box key and

automatically refill the grave. Go to the bank, the banker threatens you and urges you

to sell out to him and leave town for greener pastures. You reply you are “packing right

now” as you Use the safe deposit box key on him. He enters the vault, retrieves your

safe deposit box, places it on the counter, and leaves. A C.U. shows the safe deposit

box. Click the Hand on it to open it, revealing your lucky neckerchief covering your

brace of gun-fighting pistols. Take them both. Go to Mom’s. Take a cup of coffee. Use it

on the sheriff and he’ll give you some ammunition. Take a pile of steaming horse plop

from the street in front of Mom’s Cafe; drop it on Mom’s floor by Use-ing it anywhere

inside the cafe. While Hop Singh cleans it up, go around to “Mom’s Rear Entry.” Take

the apple pie from her window sill. Use it on the sheriff to get a gun cleaning kit. Click

the gun cleaning kit on the pistols to clean them. Go to Boot Hill. Click the bullets on

the pistols to load up, click the empty beer bottles on Srini to begin target practice.

Choose your pistols from the Inventory window. Practice. Lots. Get accurate. After a

while, Srini suggests you practice your quick-draw. When you’re good enough, Srini

suggests you need an outfit and disguise to hide from the sheriff who’s still interested in

killing you—he recommends a silver ear.



<a name="br22"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 22

Get All Dressed Up

Take your old gunslinger clothes from under your bed. Take the boot black claim

check from your nightstand drawer. Use it on the barber to retrieve your passenger pi-

geon-skin boots. Return to the pharmacy, Take the silver medallion now hanging on

the pharmacy wall. Use it on Whittlin’ Willie in the General Store for a free clue con-

cerning lost wax casting. Take some wax from the votive candles inside the church. Re-

turn to the General Store; Take the knife from the pot-bellied stove. Use it on the wax

in the Inventory window to carve the wax into a wax ear. Take some clay from the

freshly-dug grave in Boot Hill. Use the clay on the wax ear to form an clay ear mold.

Return to the pharmacy’s lab screen, Use the clay ear mold on the Bunsen burner to

melt the wax and dump it out, creating an empty clay ear mold. Then Use the silver

medallion on the crucible, Use the crucible on the Bunsen burner, heat it, then Use the

crucible on the now-empty ear mold to fill it with molten silver. Click the Hand on the

silver-filled mold in the Inventory window to break away the clay and remove your sil-

ver ear. Get dressed by clicking either the ear, neckerchief, clothes, or boots on ego. If

your Inventory contains everything else you need to get dressed, we dissolve to your

bedroom for a send-up of the Cat Ballou “dressing room scene” with you as Lee Marvin

and Srini as your faithful manservant, then fade in outside the saloon.

“Act IV—Showdown at the Hallelujah Corral”

Stop a Card Shark

Enter the saloon, walk to the poker table, click the Hand on the table. Cut to a M.S.

first-person view of the poker game. (You are not in the game.) Whenever you watch

him, “Aces” Hall wins. Click the Hand on his third hand while it is showing and you

proudly announce, “You’re cheating!” Then it’s his turn to proudly announces “You’re

dead!” There’s a pistol in his lap aimed at your heart! He orders you to turn around. We

cut back to the L.S. of the room as you do, only to see you dive for cover behind the next

table as Aces fires and misses. Fire your pistol away from him, at a small spot on the

bar’s foot rail. The bullet ricochets around the room, clips the chain holding the chande-

lier, which drops around Aces, clearly revealing his extra arm and hand. Sheriff

“Chicken Shift” has no choice but to arrest “Aces” for cheating, so he does.

“Kill” Some Local Cowboys

Leaving the saloon by the back way, you hear gunfire. Main Street is filled with local

cowboys shooting up the town. If you enter West Central Main Street, East Central Main

Street, or East Main Street, you always get shot—there’s just too many cowboys for your

twelve bullets. Enter the barber shop via the back door, Use the French postcards you

took from Madame Ovaree’s table on the barber. He accepts them gladly and gives you a

bottle of nitrous oxide in return. Leave by the back door, go to Mom’s Rear Entry, climb

the back stairs of the hotel to the outside front balcony. Use the nitrous oxide bottle

anywhere on the balcony, climb down the stairs, walk north, then west, then south,

then south again to the brothel exterior. Enter the gazebo. From there, you can just see

the hotel balcony. Carefully Use your pistol on the hotel balcony, squeeze off a shot, hit

the nitrous oxide cannister’s valve. We cut back to West Central Main Street, see the

bottle break open and spray nitrous oxide over the crowd, silencing their guns as they

all ROFL in the streets.

Wash up The Lever Bros

As you leave the brothel exterior following your super-shot, you find the Lever

Brothers waiting for you as you enter Main Street. They confront you, surround you and

begin shooting. There is no escape. We cut to a arcade shooting gallery parody screen.



<a name="br23"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 23

The boys turn into 2D, with flashing lights and points numbers on their chests. When

you shoot them with your pistol, they fall over, then stand up again like cardboard cut-

outs. If you miss and “hit” wood or glass, it explodes with realistic soundFX, but does no

visible damage. The length and difficulty of this arcade game depends on your arcade

setting in the control panel. There are no puzzles per se here. When the game ends, you

return to Main Street once again.

Quickdraw Showdown

Immediately, you hear and recognize “Kenny the Kid’s” theme music. He ap-

proaches, pauses, draws. You can’t draw your pistol before he makes his move. You die

if you draw too slowly, but the best you can do is wing him, altering his aim so his bul-

let only removes a piece of your other ear. After Kenny leaves you dying in the dust, you

Use your lucky neckerchief on your ear as a bandage, drag yourself to your feet, and

we cut to the schoolhouse exterior.

Confront the Bad “Guy”

You enter the schoolhouse under program control to find Penelope all alone. Her

romantic advances, unbuttoned bodice, and rapidly revealed Derringer convince you to

drop your gun belt. You have only a second or two to Take a student slate from a desk

to protect yourself from her single shot. She shoots the slate, but as you then bend over

to retrieve your gun belt, she beans you with her empty weapon, knocking you uncon-

scious.

Get off the ground floor

You regain consciousness in the basement, tied to a chair, your inventory stolen,

wrapped in heavy rope like a mummy. She is curious about your identity, rips off your

silver ear, drops it on the ground in her shock, fills in the back story for us, then lights

a trail of oil that will soon explode. You drop to the ground, Take your silver ear, and

sharpen it on the rock pillar. Use the sharpened silver ear to cut your ropes, then run

upstairs.

Conquer Kenny

Penelope grabs a sword from the schoolroom wall’s Civil War bulletin board. You

Take the other sword, and you fight until you “push” her backwards far enough for her

to trip on the schoolhouse stage. As she’s begging forgiveness, Kenny enters, late as

usual. Since you’re not wearing the silver ear, he recognizes you. His surprised at seeing

you again after all these years gives you just enough time to Use your sharpened silver

ear on him. We see you fling it across the room, into his throat, killing him just as the

smoking basement door bursts into flames reminding you that you need to exit quickly.

You automatically slash the sign of the “Rx” into her bodice and leap from the school-

house door just as the entire building explodes! Kenny’s body is found within, but

strangely enough, Penelope’s body is never found, thus giving us leeway for another se-

quel!

“Epilogue—Go Rest, Young Man”

Run the “End of Game” cartoon.



<a name="br24"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 24

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Deaths

Each of these deaths has a specific icon cel, message text, and message window title

text. Some icons will be full loops of animation. Some of those loops will cycle; others

will EndLoop.

miscellaneous

walk off cliff

sink into the oily swamp

fall off water tower

fail to correct prescription #3 in time

jump off swing and hit schoolhouse wall

jump off swing and fly off-screen into swamp

jump off schoolhouse roof and miss teeter-totter

jump onto wrong end of teeter-totter so baking soda smashes you

time-based problems (complete the puzzle before timer elapses, or EndGame)

sell out to town banker when he asks you to

fail to control horse flatulence

allow snails to slime town

fail to counteract laxative in water tower

allow city to burn down

allow Aces Hall to win all the town through poker

allow cowboys to shoot up town

fail to escape from schoolhouse basement before explosion

handgun violence

cowboys shoot you for walking onto Main Street

cowboys hear you on balcony laughing from nitrous oxide

you try to shoot the cowboys from the balcony

sheriff arrests you for murder when you shoot Wheaton “Aces” Hall

Wheaton “Aces” Hall shoots you when you don’t stay behind your table

The Lever Bros out-shoot you in shooting gallery arcade

Kenny the Kid outdraws you

you fail to bandage your ear wound in time

schoolroom battle

you attempt to fire your gun when ordered to drop it

you don’t drop your gun belt quickly enough when ordered

you don’t grab the student slate lying on the desk

you don’t grab the other saber

you don’t press forward during sword fight

you don’t hurl your ear at Kenny



<a name="br25"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 25

Inventory problems

eat chemicals, pills, or medications

consume horse flatulence sample

consume horse flatulence medicine

breath severe horse flatulence without gas mask

breath horse flatulence with poorly constructed gas mask (several messages)

eat snails

drink beer

drink contaminated water tower water from spigot

drink contaminated water tower water sample

take anti-laxative before adding to water tower

eat 20 50-lb sacks of baking soda

shoot yourself with your gun

eat the steaming pile of horse crap

breath nitrous oxide



<a name="br26"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 26

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Inventory

Note: In addition to the following objects which are classic Sierra adventure game

Inventory objects (i.e., carry them anywhere, access them through the Inventory window

at any time), FPFP’s “Lab Screen” does its own Inventory manipulation. Many objects on

the Lab Screen are only accessible and usable while in the Lab Screen; they are not

added to Inventory. See the Lab Screen description for more information.

If you Use any of the wardrobe objects (passenger pigeon-skin boots, gunslinger

clothes, or silver ear) on ego:

If the wardrobe is incomplete, Print “If your gunslinger look were only a little more

refined, you’d be glad to change clothes. You vow not to change clothes until you have

everything a gunslinger could possible want!”

Else, bump curPuzzle to “Cat Ballou,” fade the current scene to black and go to your

bedroom.

door key

Provided in Inventory as game begins. Use it to open

Pharmacy for business.

prescription #1

Automatically given to you by Penelope Primm as you

enter the Pharmacy for the first time. If you Look at it in

the Inventory window you see, “Penelope Primm, 2 mls

Tyloxapolynide orally 3x/7 days.” folowed by, “Why, the

poor dear! She must be suffering from the vapors, those

injurious exhalations produced within the body creating

feelings of hypochondria and depression.” Using the pre-

scription does nothing.

medication #1

Prepared on Lab Screen. Game Doco suggests Pepticly-

macine Tetrazole is an alternative to the Tyloxapolynide

prescribed in Prescription #1. See “Lab Screen” for de-

tails. Use it on Penelope in Pharmacy. If you Look at it in

the Inventory window you see: “Penelope Primm—for

internal use only. 1 teaspoon orally 3 times daily with

meals for 7 days.”

If you Use it on yourself, you die. Show the collapsing

EndLoop and print “Don’t you remember the first lesson

of pharmacy school? Never drink your own mistakes!”

prescription #2

medication #2

Automatically given to you by Helen Back after you give

Medication #1 to Penelope. A Look while in Inventory

window reveals drips and spots, as if whiskey had

splashed on it, “Helen Back, Quinotrazate, 500 mgs,

3x/7 days.” Game Doco includes instructions for prepar-

ing Quinotrazate. Using the prescription does nothing.

Prepared on Lab Screen, following instructions in Game

Doco, using ingredients found on Lab Screen. See “Lab

Screen” for details. Give to Helen Back in Pharmacy. If

you Look at it in the Inventory window you see: “Helen

Back, 1 tablet 3 times daily until all are consumed.”

If you Use it on yourself, you die. Show the collapsing

EndLoop and print “Don’t you remember the first lesson



<a name="br27"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 27

of pharmacy school? Never eat your own mistakes!”

incorrect prescription #3

Automatically given to you by Madame Ovaree as you

give Medication #2 to Helen Back. A Look while in the

Inventory window prints, “This prescription is extremely

difficult to read. You think it says, ‘Testosterate, 25

mg/day.’” then brings up an enlarged inset of the pre-

scription, clearly showing a large round stain, exactly as

if a wet whiskey glass had been set on top of it. (It was.)

Madame’s name and Doc’s scrawly signature are read-

able, but many of the words are smeared by the water,

and some of it looks like “Testosterate, 25 mg/day”.

Use it on Doc to show it to him. Use it on the whiskey

glass (or vice versa) in the Inventory window to create

“prescription #3 under glass” below. Using the prescrip-

tion on anything else does nothing.

incorrect

medication #3

Prepared on Lab Screen following instructions in Game

Doco, using ingredients found on Lab Screen. See “Lab

Screen” for details. A Look at it in Inventory says, “Tes-

tosterate ” Use it on Madame Ovaree in the Pharmacy to

give it to her. Wrong answer. She comes back later and

complains how all her girls have become masculine and

hairy. You die of embarrassment.

If you Use it on yourself, you die. Show the collapsing

EndLoop and print “Don’t you remember the first lesson

of pharmacy school? Never drink your own mistakes!”

whiskey glass

Find in bar. Take. If you Use it on yourself, print “Are

you crazy? You’ve seen how Sam makes that stuff!” Use

in Inventory window by clicking it on prescription #3 to

create…

prescription #3

under glass

Created in Inventory window by combining Prescription

#3 and the whiskey glass. Clarifies Prescription #3 so

Doc can read it through the glass. Reveals wrong medi-

cation. Show it to Doc to create…

correct

prescription #3

Given back to you automatically after you give Prescrip-

tion #3 Under Glass to Doc.

A Look while in Inventory window brings up a similar in-

set as before, but now the word “Testosterate” has been

crossed out, the word “Estrosterane” and a big “OK, Doc”

are scribbled in. The “25 mg/day,” “Madame’s name,”

and Doc’s scrawly signature remain readable.

If you Use it on yourself, print “You rub the paper all

over your hands, but it still is legible!”

correct

medication #3

Prepared on Lab Screen, following instructions in Game

Doco. See “Lab Screen” for details. Give to Madame

Ovaree in Pharmacy. Right answer.

If you Look at it in the Inventory window you see: “Ma-

dame Ovaree, Estrosterane, 1 paper each morning after.”

If you Use it on yourself, you die. Show the collapsing



<a name="br28"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 28

EndLoop and print “Don’t you remember the first lesson

of pharmacy school? Never drink your own mistakes!”

Preparation G™

empty paper bag

Find in main part of your Pharmacy. Give to Smithie

when he comes in preparing for his long ride. If you Use

it on yourself, print “You heave… a sigh of relief.”

Find in General Store. Use it on the rear end of any Main

Street horse with its tail in the air to obtain a horse

flatulence sample.

If you Use it on yourself, print “You are not going to hy-

per-ventilate in this game!”

horse flatulence sample

Get by clicking the empty paper bag on any ol’ horse’s

ass in town! Use it on the Lab Screen to test for cause of

flatulence.

If you Use it on yourself, you die. Show the collapsing

green ego EndLoop and print “You are a sick, sick little

pharmacist!”

gaseous spectroscope

tin can

Find in back room inside large cupboard. Use on the lab

screen to perform spectral analysis of the horse flatu-

lence sample.

Find on the counter inside Mom’s. Use in Inventory win-

dow to make gas mask. Can be “pricked” or plain. May

also be used for target practice.

ice pick

Find behind the saloon. Use in Inventory window on tin

can to make holes for its use as a gas mask. If you Use it

on yourself, you die. Death cel shows Swiss Cheese

Freddy. “Congratulations. Nice form, Mr. Ripper!”

charcoal

bridle

Find in blacksmith shop. Use in Inventory window to

make gas mask by clicking it on the tin can.

Find hanging on wall at Smithie’s blacksmith shop. Use

in Inventory window to make gas mask by clicking it on

the tin can.

If you Use it on yourself, print “You glance around to

make sure no one is watching, then flagellate yourself

just a little bit.”

gas mask

Create by combining “pricked” tin can, charcoal, and bri-

dle in the Inventory window. If you Use it on yourself, we

say you wear it, without any visible change in ego’s view.

Must wear before going outside during the horse flatu-

lence period.

Deflatulizer™

Develop on Lab Screen. Place in any horse trough while

wearing gas mask. After showing Freddy mix it in one

horse trough, text covers its automatic distribution to

the rest.

If you Use it on yourself, you die. Death EndLoop shows

Freddy dehydrating and shriveling up to a withered

prune. “No one will ever point the finger at you, Freddy!”

a few snails

Find at Robertson Cliff. Can eat for minus points, or give



<a name="br29"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 29

to Helen Back for plus points. If you Use it on yourself,

you eat the snails. You die—“from a lack of garlic but-

ter!”

money

beer

Get from pharmacy cash box. Use in saloon to buy beer

to combat snails.

Get at saloon by spending money. If you Use it on your-

self, you “rub the bottle cap across your lips. How fun!”

Click it on the church key (or vice versa) to change it

to…

open beer

Get by clicking church key on beer. Pour on ground at

Robertson Cliff to divert snails. If you Use it on yourself,

you “drink it all!” Then… “Burp!” Changes to…

empty beer bottles

Get by pouring beer on ground to divert snails. Used in

target practice. If you Use it on yourself, “you coyly avoid

a trip to the outhouse… but you refuse to carry those

bottles around any more!” Remove from Inventory.

church key

If it is shaped like this, it could conceivably open a

bottle cap. Find it in the lock on the inside of the church

door. Use it to open beer bottles at Robertson Cliff. Use it

on the church door, but to no avail.

If you Use it on yourself, “you are amazed to find its

shape precisely fits your navel, making a perfect belly-

button lint remover.”

ladder

Take from schoolyard slide. Use at Robertson Cliff to get

Srini off the anthill. Also Use at Central Bluff Street to

reach water tower platform.

coil of rope

lasso

Take from blacksmith’s shop wall. Use the Inventory

window’s Hand to tie it into a knot to create a…

Create from coil of rope. Use at water tower to climb to

top of water tank. If you Use it on yourself, “you strongly

consider lynching yourself, but you decide you’re hung

well enough already!”

water purification

solution

Develop on Lab Screen. Use it while on top of the water

tower. A Look while in Inventory says “Bisalicylate Anti-

toxidene, Handle with Caution!”

If you Use it on yourself, you die. EndLoop shows col-

lapsing ego. Print “You are now clean clear through!”

nitrous oxide

baking soda

Get tank of nitrous oxide from barber/dentist. Use on

Main Street to stop cowboys. [Real true fact: Nitrous ox-

ide was first used by a dentist in 1844.]

If you Use it on yourself, “What a comedian! You really

kill yourself. In fact, you die laughing.” Show laughing

ego loop.

Find large pile of it on sidewalk in front of pharmacy

shortly after hiring Srini. Use to put out fire at assay of-

fice. Chemical formula: NaHCO<sub>3</sub> If you Use it on your-

self, you die. Use collapsing ego EndLoop.



<a name="br30"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 30

French postcards

Get from the table in the brothel waiting room. Use in

barber shop to trade for nitrous oxide. “Oooh, la la!” If

you Use it on yourself, print “You smile surreptitiously!

There could be a big future in photos like this!” A Look in

Inventory shows some “titillating” cels, and a message in

funny fractured French.

candle wax

Get from the votive candles inside the front door of the

church. Use by clicking the whittlin’ knife on it in Inven-

tory window to create wax ear.

whittlin’ knife

Find in Chester Field’s General Store where it was left

beside the pot-bellied stove where some whittler. Use in

Inventory window to carve candle wax. If you Use it on

yourself, print “Good idea! Those fingernails were getting

a little dirty!” A Look says, “Those Confederate Army pen

knife replicas are becoming quite popular among the

more sophisticated whittlers.”

desk key

Find in the nightstand drawer in your room. Use in

pharmacy to unlock cubbyhole in your rolltop desk. In-

side your desk’s cubbyhole you find…

Phillip Graves’s letter

Find in locked cubbyhole in the rolltop desk in the back

room of the pharmacy. Look at in Inventory window to

read it and discover you gave your safe deposit box key

to a man for safekeeping and he vowed he would follow

your wishes and never give it back. Search through Boot

Hill until you find Phillip Graves’s tombstone.

shovel

Find stuck in freshly-dug grave in Boot Hill. Use on Phil-

lip Graves’s grave in Boot Hill to dig it up.

safe deposit box key

After finding Phillip Graves’s tombstone and digging up

his grave with the shovel, a Look at the open grave gives

you the key. Use it in the bank to open your locked safe

deposit revealing your…

brace of pistols

Get from safe deposit box in bank. Dirty, no bullets. Be-

fore using, must clean with gun cleaning kit. Must wear

to The Golden Balls Saloon for poker game puzzle and

always thereafter. Use throughout game to kill people

and blow up stuff. Click the loaded pistols on any Inven-

tory object at any time to make it explode. EndGame.

If you Use the loaded pistols on yourself, play the gun-

shot soundFX, then do an immediate exit to DOS.

cup of coffee

Take from Mom’s Cafe. Use in Sheriff’s office to swap for

bullets (if you haven’t given him the pie) or for a gun

cleaning kit (if you have).

If you Use it on yourself, print “Ummmm. Good to the

very last drop.” Remove from Inventory. They can always

go get more.

steaming horse plop

Take from street in front of Mom’s Cafe. Use in Mom’s

Cafe by dropping on floor to distract Hop Singh from

cooling apple pie. This is only good until the horsePlop-

Timer expires. Then you have to do it all over again.



<a name="br31"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 31

If you Use it on yourself, you die. Show collapsing End-

Loop. Print “How disgusting!”

apple pie

Take from behind Mom’s Cafe after distracting Hop

Singh by dropping the horse shit inside the cafe. Use in

Sheriff’s office to swap for bullets (if you haven’t given

him the cup of coffee) or a gun cleaning kit (if you have).

If you Use it on yourself, print “You just can’t resist nib-

bling off a little corner of the crust. No one will ever no-

tice that!”

bullets

Get from Sheriff in swap for the apple pie or cup of cof-

fee. Use in gun by clicking bullets on gun in Inventory

window.

If you Use it on yourself, print “Just where did you in-

tend to stick those bullets, Freddy?”

gun cleaning kit

nitrous oxide

Get from Sheriff in swap for the apple pie or cup of cof-

fee. Use by clicking on pistols in Inventory window to

clean them. Contains rags, gun oil, rod, etc.

Get from barber by giving him the French postcards in

trade. Use on cowboys on Main Street by shooting valve

open from across town.

Click the Hand on the bottle or Use it on yourself, either

way, show the Death laughing loop, and print “you open

the valve on the tank of nitrous oxide and you soon die

laughing!”

lump of clay

wax ear

Find in freshly dug grave in Boot Hill. Use in Inventory

window (see wax ear below).

Create in Inventory window by clicking the whittlin’ knife

on the candle wax. (“Are you playing with ear wax

again?”) Use it in Inventory window by clicking it on the

clay (or vice versa) to create…

medicine show elixir

Get from back of medicine show wagon outside Mom’s

rear. Use on Lab Screen to fill alcohol lamp.

wax-filled clay

ear mold

Create in Inventory window, let harden. Heat with alco-

hol lamp on Lab Screen to melt the wax inside, then

pour the wax out to create…

empty clay

ear mold

Create on Lab Screen by melting the wax with the alco-

hol lamp and pouring it out. Wait until cool. Use on Lab

Screen by filling it with the molten silver from the…

silver medallion

Find mounted on Pharmacy wall after Srini wins display

award (after successfully completing target practice ar-

cade game). Use on Lab Screen (see silver ear below).

If you Use it on yourself, print “You hang the medallion

around your neck, softly whistle the National Anthem

and picture yourself standing on the next to highest

platform while sweating profusely. You can’t wait for

1896 to arrive! You remove the medallion.”

silver-filled clay

Create on Lab Screen by clicking molten silver on empty



<a name="br32"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 32

ear mold

silver ear

clay ear mold. Wait until cool. Click Hand on it in Inven-

tory window to break clay mold thus creating…

Make in back room by melting breaking silver-filled clay

mold.

If you Use it on yourself and have a complete gun-

slinger’s outfit, we cut to the dressing room cartoon. If

you don’t have everything, print “You will want to wear it

later, but only after you have completed your outfit.”

gunslinger clothes

Find in trunk at the foot of your bed in your bedroom.

Your “Good Guy Model” hat is included.

If you Use it on yourself and have a complete gun-

slinger’s outfit, we cut to the dressing room cartoon. If

you don’t have everything, print “You will want to wear it

later, but only after you have completed your outfit.”

Once you’ve changed, “you can never go back.” “Mr.

Pharkas’s Wardrobe by Festus Lauren.”

boot black claim check

Find in your room. Use in barber shop to retrieve…

passenger pigeon-skin boots Get at barber shop by giving the barber your claim

check. They’ve been there getting a shine.

If you Use it on yourself and have a complete gun-

slinger’s outfit, we cut to the dressing room cartoon. If

you don’t have everything, print “You will want to wear it

later, but only after you have completed your outfit.”

lucky neckerchief

Find in your safe deposit box beside your pistols. If you

Use it on yourself and have a complete gunslinger’s out-

fit, we cut to the dressing room cartoon. If you don’t

have everything, print “You will want to wear it later, but

only after you have completed your outfit.”

“Wasn’t this the neckerchief you were wearing when

Kenny shot you?” As you lie dying in the street, after

Kenny steps over you, you can Take the neckerchief off

your neck and Use it on your newly-shot ear to keep

from bleeding to death.

student slate

Take from schoolroom desk. You automatically Use it

immediately to block Penelope’s bullet.

sharpened silver ear

Make in schoolhouse basement by rubbing silver ear on

pillar. Use by clicking on self to cut ropes. Use again up-

stairs to by clicking on Kenny to kill him.

If you Use it on yourself, print “It’s too sharp to wear

now!”

Civil War sword

Take from schoolroom wall. You automatically Use it

immediately to block Penelope’s attempt to kill you. If

you Use it on yourself, print “It’s bad enough Penelope’s

trying to kill you! Now you want to fall on your sword?!”



<a name="br33"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 33

\_\_\_\_\_\_\_\_\_\_\_ Scene by Scene Description

Opening Sequence

100 Logo Screen

FPFP begins with the standard Sierra logo and opening fanfare, which then shrinks to a

smaller size as the Title Screen pops on and the titles zoom out. When the music is fin-

ished (or any time earlier, if anyEvent), an animated dialog showing a smiling Freddy

mortaring his pestle appears with five choices: “Restore,” “Prologue,” “Learn,” “Play,”

and “Quit” (with “Restore” the default). Selecting “Prologue” skips to “The Prologue” be-

low. Selecting “Learn” takes you to the pharmacy exterior in “learn mode” and begins

the walk-thru. Quit exits. The others Restart and Restore.

110 Opening Cartoon

Erase the Title Screen and dialogue. Leave the Sierra Half Dome “Logo Screen”

where it is, while we load the following animation. Half Dome dissolves into a matching

VistaPro Half Dome. We fly around it, then away from it, and take a jet ride over the

mountains to Coarsegold, 1888. We fly over the town to reveal its state of decay, fly

down over Main Street at the Hotel, then slide right along Main to the Pharmacy, then

fly in and down for a C.U. of the Pharmacy front window. As we approach the town, the

music becomes more Western; when we stop at the window, we shift to a bit map of the

Pharmacy window which serves as background, while the title pops on as dramatic

Western music begins. Meanwhile, we load up SCI. As the musical introduction contin-

ues, it changes to less “Copeland” and more “Gene Autrey” for “The Ballad of Freddy

Pharkas.” As the words describe Freddy’s life, we dissolve to…

150 The Prologue

…a sepia-toned screen with Freddy’s face in the center, as we show small, old-timey

photos surrounding it. Above, “Prologue: Freddy Pharkas, The Early Years” is overlaid.

“The Ballad of Freddy Pharkas” plays in the background, with synchronized lyrics po-

sitioned so the photos aren’t covered. The song tells the back story while a series of less-

than-full-screen vignettes dissolve in and out of the screen corners. We see your up-

bringing back in St. Louis: Dad teaching you to quickdraw your tiny toy pistols; friendly

gunfights with the neighborhood kids; and your rise to those not-so-friendly gun battles

as “Freddy Boy” Pharkas, fastest gun in the West. Continually challenged by every

tough who thought he was quick on the draw and had something to prove, you beat ’em

all until that fateful day on a dusty street in Pecos when you finally met your match—

none other than your old childhood buddy, the one kid from the neighborhood you

could never beat: Kenny the Kid! We watch Kenny outdraw you and shoot off part of

your ear. We hear you vow to “give up this lousy business for my true love!” We learn by

that you meant pharmacy. We see short vignettes of your college years (in which you

say, “eh?” a lot); your arrival in Coarsegold; your quiet life as a bachelor pharmacist and

not too successful small businessman; and conclude with a morning a few months ago,

when Fargo Wells’s stagecoach arrived in Coarsegold and delivered the new school-

marm. After you are introduced to her, the stagecoach drives away, and our cartoon

loops back to the title screen again.



<a name="br34"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 34

After the sepia-toned version of the title screen with overlaid caption, come the following

partial-screen vignettes:

Dad teaches you to quickdraw your tiny toy pistols

a friendly gunfight with the neighborhood kids

a not-so-friendly gun battle as “Freddy Boy” Pharkas

Kenny the Kid outdraws you and shoots off part of your ear

a bloody close-up where you vow to “give up this lousy business”

your college years (with you saying “eh?” a lot)

your arrival in Coarsegold

your quiet life as a bachelor pharmacist

Fargo Wells’s stagecoach delivers the new schoolmarm

your introduction to her

he stagecoach drives away

(No Opening Credits)

Credits do not appear in the “Sierra standard” position after the title screen, before

the cartoon, but rather, dissolve in and out during game play (like Larry3), floating in

front of the Main Street exteriors during normal game play. Keep a creditsCounter, and

load any credit in any Main Street exterior in this manner: after a room change, wait

about 8 seconds, fade the credit in, advance the counter, wait about 3 seconds, fade it

out. Do nothing further until after the next scene change. After showing last credit, do

nothing more until end of game, when we re-use the same images for the “Closing Cred-

its” below. Can we use the same colors as the stars that twinkle at night, so we’d only

need one cel of the text, then we’d tweak that palette color?



<a name="br35"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 35

Main Street Exteriors

Main Street is one giant scrolling screen connecting the shops’ interior locations.

The exteriors are listed here in order from West to East. There are some common condi-

tions to this region, that also apply to the three Collier Bluff scenes.

Various Coarsegold inhabitants walk around through the town, minding their own

business. If you Talk to them, they have intelligent responses. They each keep their own

conversation counter. Their movements are realistic (i.e., not walk outside, change

screens, find them inside somewhere it was impossible to get to in the elapsed time).

Throughout the game, characters notice the background music and comment on it.

Horses stand before hitching rails, ostensibly tied up. They randomly flick their

tails, raise their heads, shake their heads, snort.

Dogs roam in and out, lie down, pant a lot, lick themselves occasionally, stand up,

and walk out.

Chickens roam throughout the streets, pausing to peck every so often.

Tumbleweed rolls through town, but not very often; perhaps 1/10 chance ??

If curPuzzle == “Snail stampede” && the snailTimer has expired:

The next time you enter Main Street, print “Look! A cloud of dust at Robert-

son Cliff!” You die, with the death message showing a long shot of the town

shiny with slime. EndGame.

If they Use any of the empty containers on a horse trough, print, “The problem is

not with the horses’ water.”

If curPuzzle == “Flatulent Horses:”

As you walk around town you occasionally hear soft samples of delicate

“horse reports” in the background.

If you Use the empty paper bag on a horse’s ass:

Walk to rear of horse, do the animation that raises the horse’s tail,

show the bag inflating, and add the horse flatulence sample to Inventory.

If you Use the Deflatulizer™ on any horse trough:

Walk ego to the trough and show him pour some liquid in. Fade to

black, cover its application to all troughs in town through text, then fade

up on you with your gas mask gone, standing outside your Pharmacy.

If the fartTimer expires before the puzzle is completed, the next time ego

walks from an interior to an exterior room, he dies. Death loop shows the whole

town under a brown cloud. EndGame.When curPuzzle == “Contaminated Water:”

As you walk around town you see townsfolk lined up outside the outhouses.

When curPuzzle >= “Burning of Coarsegold” && curPuzzle <= “Madame Ovaree:”

The exteriors are in Night Mode, with twinkling stars, a moon, etc.; an occa-

sional shooting star flashes by (very occasionally: no more than one per scene,

delayed by Random(15, 60) seconds).



<a name="br36"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 36

200 Robertson Cliff

Physical Description:

No exit north or south. East leads to Blackwater Creek bridge. To the South we can

see the railroad tracks. Although the main road clearly leads off-screen, you can’t go

that way. There is a large (big enough to hold Srini), although subtle, anthill here, ex-

actly one schoolyard slide’s ladder length from a rock formation that Srini can walk over

to and climb down without stepping on any ants. If you walk to the anthill, you can’t

walk on it because it’s too steep.

“The road leads off around the hills to Oakhurst and the floppy disk mines.” You

can’t go that way. “Why would you want to?”

Features

anthill, rock, cacti, road, bridge, tracks, cliff

Props

scurrying ants, vultures over dead Cedrick, snails in distance raising dust

Actors

Srini, lots of snails

Objects Found Here

snails, ladder (if placed here by ego)

Objects Used Here

beer, ladder

Description of Events

Always animate ants scurrying around anthill.

If curPuzzle > “hire a Sidekick,” init buzzards circling Cedrick. After three times, on

fourth time in room, init buzzards eating Cedrick instead.

If the curPuzzle == “Snail stampede:”

Animate the “snails in distance raising dust” prop.

Place “the escargót advance party,” a row of snails stretching from screen left

to right, whose distance across the screen is a function of time remaining on the

snailTimer. A Look at the escargót gives you hints about the solution as well as

the state of the puzzle’s timer. “These snails are the leading edge of a stampede

of imported French escargót, escaped from a haughty San Francisco restaurant,

being chased by a posse of haughty San Francisco chefs.” You can Take some

snails from the row, but it makes no visible difference.

If you click the closed beer bottles on the ground ahead of the snails or on

the snails, print “You could try to kill every snail by smashing it with a beer bot-

tle, but there’s a better way.”

If you click the open beer bottles on the ground ahead of the snails or on the

snails, (“It’s Miller time!”) start an animated sequence in which we see you open

and pour bottle after bottle of beer to paint a trail of beer leading from the cur-

rent leading edge of the snail row, to the broken-down railroad trestle and down

the tracks. We see you cover the rails with beer, then step aside as the snails

form their “line o’ death.” As they reach the tracks, bump curPuzzle to “Lem-

mings”and cut to “205 Lemming Snails” scene below.

If curPuzzle == “hire a Sidekick:”

No more snails.



<a name="br37"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 37

A sitar solo wails in the background.

Init Srini Lalkaka Bagdnish on the anthill. He randomly turns his head. He

shrugs his shoulders after talking to you.

Srini is sitting cross-legged on top of the anthill, surrounded by swarms of

ants. He remains there until you hire him. He’s not staked to the anthill, just

sitting on it. He won’t initiate a conversation with you, but you may Talk to him.

You must hire him to advance to the next problem.

Talking to him reveals how he got placed there by some evil travelers (“I don’t

know who they were—but they looked like tourists heading for Yosemite!”) and

his desire to escape. Since he refuses to chance stepping on an ant, he can’t

move. You mention you’ve been looking for “a loyal Indian side-ki–, er, an as-

sistant clerk.” He says he’s “been considering a new position.” But, you must get

him off the anthill first.

If you Use the ladder on the anthill:

Do the “hiring Srini” cartoon. We watch you place the ladder so it

stretches from Srini’s anthill to a nearby antless rock formation. Animate

Srini crossing the ladder to the rocks, then down beside you. Show him

giving the big guy a big hug. You offer him a job, he accepts, bump cur-

Puzzle to “Brief your sidekick” and cut to “610 Pharmacy Back Room” for

the “hiring Srini” cartoon.

If you click on the Fast Forward icon at any time during this cartoon,

we jump to “610 Pharmacy Back Room” at the conclusion of “hiring

Srini” speech.



<a name="br38"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 38

205 Lemming Snails

Physical Description

A short cartoon-only parody of Lemmings, featuring cute snails marching to their

death. Show rails above, twisting to vertical, with boiling, churning rapids below. Just a

reward gag for solving the beer puzzle. You only get to this screen during the snail puz-

zle solution.

Features

rails, rapids

Props

boiling, churning rapids

Actors

identical snails (but lots of ’em)

Objects Found Here

Objects Used Here

Description of Events

curPuzzle = “Lemmings”

We see thousands of identical snails (okay, dozens, lots, some, a few…) form a line

on the rails, turn into “Lemmings-like” animation, stand up and march like little weenie

soldiers for a ways, then in unison, all bend down and lick up some beer, then forward

march again. They follow the tracks to their death in Blackwater Creek, eventually fal-

ling off the ends into the rapids with great aplomb. (Let’s see animation that shows

that!)

Be sure to consider machineSpeed and detailLevel when initing the masses of snails.

After a few repetitions of this, bump curPuzzle to “hire a Sidekick” and return to the

previous screen, never to see this screen, or a snail, again.

If you click on the Fast Forward icon at any time during this cartoon, we jump to

“200 Robertson Cliff” with curPuzzle == “hire a Sidekick.”



<a name="br39"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 39

210 Blackwater Creek bridge

Physical Description

“You wonder why the water is black.” “And gooey.” old railroad trestle abandoned,

broken in middle; tracks curling down toward the creek since the trestle has washed

out. Rapids below.

Features

rapids, bridge, cliff, rail ends

Props

Rapids below

Actors

falling board (old Indian name?)

Objects Found Here

Objects Used Here

Description of Events

Each time ego walks across, at a suitable, random X-coordinate, a board tumbles

from out of sight below the bridge to the creek below (scaling down as it falls). As it hits

the creek and disappears, print “Whew! That was a close one! Considering the condition

of this old bridge, you may only have about four crossings left.” (I would prefer a ran-

dom number in the message between 2 and 5, if that’s not impossible with our sophisti-

cated new language.)



<a name="br40"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 40

220 West Main Street, Livery & Bank

Physical Description

The Bank is accessible from this screen. Balance Street heads North beside the

bank (at the right edge of this pic). A coil of rope hangs on the wall. A pile of charcoal is

beside the forge. If Act I, a blacksmith works his forge; the forge is burning; a horse is

up on blocks with no legs.

Features

leather strap, charcoal, coil of rope, bank, blacksmith shop, blacksmith shop doors,

corral, saddle, water trough, hitching post, foreground clutter, Balance Street, Main

Street

Props

burning forge, bank door, horse on blocks

Actors

Smithie (if Act I), animals in corral, 4 (count ’em, 4) Lever Bros, Kenny the Kid

Objects Found Here

leather strap, charcoal, coil of rope

Objects Used Here

Description of Events

If it’s daylight: animate the animals in the corral. (Cond:

If curPuzzle < “Quickdraw practice,” show horses. If you Look at the corral,

print “For one brief shining moment, there truly was a place called ‘Cattle Lot!’”

If curPuzzle < “Rowdy Cowhands,” show sheep.

If curPuzzle < “Kenny arcade,” show heeps.

If curPuzzle < “Card Shark” && it’s daylight:

the bank is open, click hand on door to enter.

If curPuzzle < “Preparation G:”

Smithie is here working, you can talk to him.

The blacksmith shop doors are open, thus the coil of rope is not visible nor

“Take-able.”

The horse-on-blocks is here, cycling randomly.

If curPuzzle >=“Preparation G:”

The blacksmith shop doors are closed, thus the coil of rope is visible, if they

haven’t been taken.

If curPuzzle == “Lever Bros shooting gallery”

You just left the brothel exterior after successfully shooting the nitrous oxide

container. Enter this screen, then freeze ego while the frightening Lever Bros

theme plays and the boys walk on to their four respective locations. Freddy

hears the background music and realizes these guys mean trouble. The boys are

color-coded, each has his own primary color. Print “What’s that smell? Oh, no!

You recognize that stench from your old days as a lawman. More dangerous

than Jesse James, meaner than Johnny Ringo, deadlier than the Reno brothers,

(dumber than Doc Holliday), it’s the legendary…” “…Lever Brothers, here to

clean house!” “Reach for the sky, Chrome-Ear! We’re ah gonna kill you now.”



<a name="br41"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 41

“You hope your target practice with Srini was sufficient to prepare you for odds

like this…” Give a typical Western description of these villainous outlaws, fol-

lowed by intense psychoanalytical diagnosis. Then cut to “550 Lever Brothers

gunfight arcade” below.

If curPuzzle == “Kenny’s Quickdraw arcade”

You just finished off the Lever Bros. Upon your return to this screen you get

a few congratulatory messages. But your victory celebration is short-lived, be-

cause you immediately hear (and recognize) the theme music of the evil “Kenny

the Kid,” your old nemesis, the one kid in your old neighborhood that you could

never outdraw! We cut to “560 Kenny’s quickdraw arcade” below, never to return

here.



<a name="br42"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 42

230 West Central Main Street, Saloon & Mom’s & Hotel

Physical Description

On the South side of Main Street is the old railroad station, now abandoned and

overgrown, plus lots of foreground clutter. There are no streets heading North from this

pic. The saloon and Mom’s Cafe are accessible from here, although the abandoned Dirty

Sheet Hotel’s front door is boarded up.

The hotel has a balcony across the front, with a hint of exterior stairway leading

down to the left visible from this pic. Those stairs lead to “500 Mom’s Rear Entry,” and

there is no means of access to the balcony from this screen. From the hotel balcony

hangs a banner you can’t read without an Eye click, plus some bunting that forms a

subliminal “bunting bulls-eye.” A Look at the banner says, “It reads, ’Coming soon—

Mom’s Comedy Club! Try our ‘Open Megaphone Night.’ Take your best shot at making

grown men laugh!’”

Features

saloon window, saloon sign, saloon porch, Mom’s sign, Mom’s porch, Mom’s window,

hotel balcony, hotel sign, comedy sign, hotel bunting, hotel porch, hotel windows up-

stairs, hotel windows downstairs, hotel door, watering trough, barrel, hitching post,

foreground clutter

Props

randomly swinging weather vane, saloon swingin’ doors, Mom’s door, broken saloon

glass

Actors

sign painter, window glass repairperson, stuntman

Objects Found Here

horse flatulence sample

Objects Used Here

nitrous oxide, Deflatulizer™

Description of Events

After a Restart Game (OR if a key is pressed during the opening cartoon):

We dissolve to black, then dissolve into this exterior with a sepia-toned pal-

ette and “Act I, Living The Dream” overlaid. The title banner disappears, the

sepia pic slowly dissolves into the actual, full-color, game picture of Central

Main Street, animation begins, and FPFP begins with you standing outside the

hotel with nothing but a door key in your Inventory.

If it’s your first time here:

A man is boarding up the Hotel’s front door with a “Closed” sign. If you Talk

to him, he tells you, “it was taken over by somebody, but no one knows who.”

If you click the Hand on Mom’s door:

If you haven’t taken the apple pie, enter Mom’s interior. (Hmmm?)

Else, print “It appears Mom’s has been closed by order of the sheriff. Some-

thing to do with Health Code violations!”



<a name="br43"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 43

Anytime:

The saloon is open, click hand on door to enter or click walker in doorway to

walk right through (since these are swinging doors).

If prevRoom == 240 && Random 1/3 && no other, more important conditions apply

&& ego is otherwise unoccupied:

a few seconds after the room change, the stuntman comes flying through the

saloon window, to lie lifeless in the street until ego leaves the scene. Set a flag to

force the glass man to appear later on.

If the glass man flag is set and no other, more important conditions apply:

Show the glass man replacing the saloon window. He works a while, then

walks off-screen to the left. If ego follows him into 220, he should be there, walk-

ing off-screen to the north, but veers right before he’s out of the picture, as if he

entered another area that ego can’t get to.

If prevRoom == “dressing like Cat Ballou” cartoon && curPuzzle == “Card Shark:”

You resume play here, standing just outside the saloon, under playerControl,

in your new outfit, never to change clothes again.

If curPuzzle == “Card Shark:”

Chester Field is standing near the saloon door wearing a sandwich board

reading “will clean stables for stagecoach fare.” He tells his woeful tale: he lost

his business in the game inside! “That sucker jes’ gotta be cheatin’!” Aces theme

song plays softly in the background. Freddy hears the background music and re-

alizes this guy means trouble.

If curPuzzle == “Local Cowhands:”

You encounter “dozens of those silly ol’ rowdy cowhands from that cattle

drive outside of town” who are “carelessly firing their guns everywhere,” and

frightening (not to mention killing) the locals. “Let’s stampede the women and

rape the cattle!” As you walk into the scene, play the cowboys’ background mu-

sic. Freddy hears the background music and realizes this means trouble.

Animate as many cowboys as the user’s computer’s speed and detailLevel

will allow. Show them all, but randomly cycle through them firing their guns in

the air. The soundFX need not match the gunfire. Let it imply there are more

men off-screen also shooting their guns.

If prevRoom == “Mom’s Rear Entry:”

However, if you climb the hotel balcony stairs from the back alley, the

cowboys don’t notice you and you can walk about on the balcony and

stairs with impunity. Provide different messages for the room’s features,

based on balcony/ground level locations.

If you try to shoot the cowboys from the balcony, you die just as you

did from down below. EndGame.

Instead, click the tank of nitrous oxide anywhere on the balcony to

leave it, and we walk you automatically to the center of the “bunting

bulls-eye”, see you bend down and the tank appear.

Else:

Give ego a little time in this scene before killing him, so the player

can see the cowboys, get a message about them, and then kill him!



<a name="br44"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 44

You can shoot at them if you have time to get a shot in, but you al-

ways fail. They easily shoot you every time—“remember: there are twenty

of them and you only have 12 bullets!” EndGame.

If curPuzzle == “ROLFing Cowhands:”

This is just a short reward cartoon that shows the bottle break open (Clang!

soundFX) and spray nitrous oxide (which is invisible, isn’t it?) (hiss soundFX).

The street is filled with rowdy, identical cowboys, randomly whooping things up.

They begin dropping in direct relationship to their distance from the bottle. As

they fall, they begin ROFLing in the street.

Consider machineSpeed and detailLevel when initing the number of cowboys.

They more the merrier, but don’t run slow.

After 10 ?? seconds, whether all the boys or down or not, print “Nice shot,

Freddy!” and return to “400 Brothel Exterior.”

If you click on the Fast Forward icon at any time during this cartoon, we re-

turn to “400 Brothel Exterior.”



<a name="br45"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 45

240 East Central Main Street, Store & Barber Shop

Physical Description

Mercantile Street heads North along the left edge of this pic. Across it are the gen-

eral store, the abandoned post office, and the barber shop.

A steaming pile of horse plop, complete with circling horde of flies, may appear at a

random location somewhere in the street. You can Take it at any time.

Features

Mercantile Street, wagon on Mercantile street, store, store window, store porch,

store sign, post office, post office door, post office sign, post office window, barber shop,

barber shop sign, barber shop window, hitching post, watering trough, buildings in dis-

tance, foreground clutter

Props

store door, barber door, barber pole, steaming horse plop

Actors

Objects Found Here

steaming horse plop, horse flatulence sample

Objects Used Here

Deflatulizer™

Description of Events

Anytime:

If General Store is open, click hand on the General Store’s door to enter.

If the barber shop is open:

Animate the barber pole.

Click hand on door to enter barber shop.

If curPuzzle > “Madame Ovaree” && you haven’t already taken the horse plop:

Animate a steaming pile of horse plop at a random location somewhere in the

street. You can Take it at any time.

If the horsePlopTimer runs out and you haven’t grabbed the apple pie yet, re-

set the takenHorsePlop flag so another pile appears. Otherwise, there’s no way to

continue the game.

If prevRoom == Pharmacy Bedroom dressing cartoon:

We dissolve to this exterior with a sepia-toned palette and “Act IV, Show-

down at the Hallelujah Corral” overlaid. The sepia pic slowly dissolves into the

actual, full-color, game picture of East Central Main Street.

If curPuzzle == “Local Cowhands:”

See 230 for description, and handle identically here.



<a name="br46"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 46

250 East Main Street, Sheriff & Pharmacy

Physical Description

The Sheriff’s Office, the abandoned Tall & Thin shop, the abandoned PP’s Playhouse,

and your pharmacy open onto this pic.

Your pharmacy door is locked at the very beginning of FPFP until you unlock it to

open your shop for business. You don’t need to Use your key to unlock or lock or open

the door during the prescription-filling puzzles in Act I. But once the sheriff has closed

you down, the pharmacy door automatically locks whenever you leave the building and

it remains locked throughout the rest of the game. You have no more customers.

A series of Indians with funny names stand woodenly outside your pharmacy hold-

ing cigars. Not wooden Indians, real ones! Running Gag.

Features

sheriff’s office, window, sign, and sidewalk; Thin & Tall Shop, sidewalk and door;

PP’s Playhouse door, window, sidewalk, and sign; pharmacy, sign, windows, and up-

stairs windows; hitching post, watering trough, foreground clutter

Props

sheriff door, pharmacy door, sacks of baking soda

Actors

drugstore Indians 1, 2 & 3 (Running Gag, Standing Water, Humping Buffalo),

Paulette Revere, horse flatulence sample

Objects Found Here

baking soda

Objects Used Here

key

Description of Events

Anytime:

If sheriff is in, click hand on his door to enter. If you’ve seen him recently

elsewhere and there was no logical way for him to beat you back to his office,

he’s not in, the office door is locked and you get an appropriate message to that

effect when you try to enter.

If pharmacy door is locked, click key on door to unlock.

If pharmacy door is unlocked, click key on door to lock.

If pharmacy door is unlocked, click hand on door to open.

If the pharmacy is open for business and prevRoom == pharmacy interior:

If indianCount == 1:

AddToPic Indian #1 beside door. Handle different messages than fol-

lowing Indians.

If indianCount == 2:

AddToPic Indian #2 beside door. Handle different messages.

If indianCount == 3:

AddToPic Indian #2 beside door.



<a name="br47"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 47

As ego walks away from door, Indian #3 walks in from East, ap-

proaches Indian #2, taps on shoulder, makes a comment, Indian #2

wakes up, walks off-screen to East, Indian #3 takes his place. No more

Indians.

If indianCount < 4 && prevRoom != pharmacy interior:

When ego reenters pharmacy, ++indianCount.

If curPuzzle < “Sheriff shutdown” && Random( 1, 11) == 1 && prevRoom != 240 East

Central Main Street:

Animate the Thin Man walking from in front of his shop and into the crack

beside the shop. Set a flag so this never happens again.

If curPuzzle >= “Sheriff shutdown:”

addToPic the Closed Sign on the Pharmacy.

If curPuzzle == “need gas mask” && prevRoom == pharmacy && you’re not wearing

the gas mask:

Give him a few seconds to walk about in this scene (but don’t let him change

rooms). Do dying animation. “You die from the noxious fumes.” EndGame.

If you just finished spreading the Deflatulizer™:

we dissolve back to this screen. Immediately a horseman (Paulette Revere)

rides in from West to East yelling, “Board up yer winders ’n’ doors, thar’s a

stampeeede a’headin’ fer town!” (Oh, no! Another western cliché!) “Hurry up,

Freddy! Ya only got a week and a half a’fore they git here!” Start the snailTimer.

Give ’em 20\*60 seconds. See “Main Street” regional stuff above for expiration de-

tails.

If curPuzzle == “Start Act II” (the sheriff just closed your shop):

fade in on a sepia-toned version of this exterior, this time with a “Closed”

sign visible in your pharmacy window, and “Act II, The Plot Sickens” overlaid.

This dissolves into the normal pic, with you standing in front of your pharmacy.

Bump curPuzzle to “Flatulent Horses.” Start the fartTimer at 600 ?? seconds.

If curPuzzle > “Brief your sidekick” && you’ve been in this scene at least once since

the briefing && you haven’t taken the baking soda:

a gigantic pile of 50-pound sacks of baking soda fills the sidewalk in front of

your store, nearly blocking the entrance. The baking soda is the “LeGand Ham-

mer” brand, named for the famous international industrialist. His slogan: “one

sack in the smokehouse and another in the stable.” You may Take the baking

soda at any time; the huge pile disappears into your Inventory.

If curPuzzle == “Local Cowhands:”

See 230 for description, and handle identically here.



<a name="br48"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 48

260 Schoolyard

Physical Description

Edukashun Lane heads North (between the abandoned assay office and the school-

yard) at the left edge of this pic and leads you to East Bluff Street. Old one-room school-

house. Covered porch. Steps lead up to door. You can not enter the school. Playground

in front. A ladder is insecurely attached to the playground’s slide. You can Take the lad-

der. There is a teeter-totter. A swing hangs from a tall hickory tree at such an angle that

Freddy could leap from it to the roof of the school. Read on for the dramatic interrela-

tionships between the various pieces of playground equipment, the roof and Freddy.

Features

Edukashun Lane, slide, teeter-totter, swing, tree, school, school windows, school

roof, assay office, buildings in distance, foreground clutter

Props

teeter-totter, swing, school door, slide ladder, 3 “loopsOfire” for the assay office fire,

kid on swing, kid on slide, kids skipping rope

Actors

kid on teeter-totter

Objects Found Here

ladder

Objects Used Here

baking soda, swing, teeter-totter

Description of Events

If prevRoom == “Kenny gunfight:”

Fade in on this scene with Freddy standing on the schoolhouse steps. He

opens the door, and enters the schoolhouse for the first time (under program-

Control). Cut to “720 Schoolhouse Interior” below.

If curPuzzle < “Burning of Coarsegold:”

Kids play on the playground equipment: two kids on the teeter-totter, a kid

on the swing, a kid on the slide (if it has a ladder), three girls jumping rope,

some kids playing craps, etc.

Penelope “Wanders” around the schoolyard, watching the children, pausing

more than she walks. Ego can talk to Penelope. If you talk to her, she stops her

Wander, and faces you until you walk away.

If you click on the teeter-totter or swing while kids are playing, you get a

message saying you can’t play now.

If the ladder is here && you click the hand on it:

If the kid is climbing the ladder, you can’t take it. Print “You refuse to

grab a young boy on a school playground!”

If he’s sliding down, or coming back around, you can take it. The kid

reaches the end of his loop, but instead of beginning again by climbing

the ladder, he stops and goes into a crying loop. Print “Good idea, Freddy!

Wreck the little kids’ playground equipment!”

If curPuzzle > “Burning of Coarsegold:”



<a name="br49"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 49

AddToPic the burned-out shell of the Assay Office. Change the feature mes-

sage.

If you click the Hand on the swing, print “You’ve swung enough.”

If you click the Hand on the teeter-totter, print “You’ve teetered enough.”

If curPuzzle == “Burning of Coarsegold:”

It is nighttime when you enter this scene. “The closed assay office ablaze,

threatening to burn down not only itself and your Pharmacy, but the whole

town!“ Animate the fire loops on the office.

There are no kids or Penelope here. The playground equipment is unused.

If you click the Hand on the teeter-totter, print “Of course you want to play

on the children’s equipment, don’t you? But shouldn’t you put out that fire

first?”

If you Use the baking soda on the flames:

Animate Freddy going near the assay office, throwing a bag, making a

splat and retreating. AddToPic the splat. (Repeat attempts randomly

move the throw and splat points.) Print “You try to get close enough to

throw it, but are forced back by the extreme heat and accomplish nothing

but a large white splat on the ground.” The baking soda remains in In-

ventory.

If you Use the baking soda on the teeter-totter:

Show the huge pile of sacks on the end of the teeter-totter nearest the

click, with the opposite end up in the air. You can place the bags of bak-

ing soda on either end of the teeter-totter. Everything is the same until

you jump off the roof. See below for that difference.

Here’s how the Swing works: you can’t use it before the town is burning be-

cause kids are in it. During the fire, click the Hand on the swing to sit on it,

swing faster and higher until you can leap from the swing to the roof of the

school. You then Click the Hand on the school (or “Exit”) to jump. The idea here

is to make swinging higher a timing puzzle.

If you click the Hand on the swing:

If it’s unoccupied, place ego in the swing, but not moving. (To exit the

swing, click the “Exit” icon.)

If it’s occupied by ego, make him go faster or slower:

If the cel < 1/2-way, swing slightly more, unless he’s already

“going all the way.”

If the cel >= 1/2-way, swing slightly less, unless he’s stopped.

If you are in the swing and click the Hand on the school (or click “Exit”) to

jump:

If the cel is within 1 cel of the top of his swing:

cut to the animation of Freddy flying from the swing to the

roof and landing safely. Use his “stand-up” animation to put him

back on his feet. Switch back to playerControl.

If the cel is in the “forward half” of his swing:

cut to the animation of Freddy flying splat into the wall. “Bad

timing,” you think, as you slide down the wall, filling every inch of



<a name="br50"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 50

your body with major splinters. You immediately bleed through

thousands of tiny openings. EndGame.

If the cel is in the “backward half” of his swing:

cut to animation showing him flying completely off-screen to

the right. “Bad timing,” you think, as you plummet to your death.

EndGame.

If ego is on the schoolhouse roof:

After you land on the roof, you can walk around. The idea is to walk

to the other end of the roof and jump off onto the empty end of the loaded

teeter-totter.

If he walks off the edge:

he walks to that edge and falls to the ground, splat! “Too bad

you don’t have some way to cushion your fall.” EndGame.

If he Uses the ladder, print “The ladder can not reach the ground

from here… and you have no desire to go any higher.”

If he clicks the Hand on the teeter-totter:

If the teeter-totter has NO sacks of baking soda:

he walks to that edge and falls to the ground, splat!

“Too bad you don’t have some way to cushion your fall.”

EndGame.

If the teeter-totter has sacks on wrong end:

Show Freddy jumping off, landing on empty end of tee-

ter-totter, causing the sacks on the other end of the teeter-

totter to fly high in the air, out of the frame. Show Fred

look up, look out at player, as sacks land directly on top of

him, Roadrunner style. EndGame.

If the teeter-totter has sacks on right end:

Show Freddy jumping off, landing on empty end of tee-

ter-totter, causing the sacks on the other end of the teeter-

totter to fly high in the air, over Fred’s head, across the

street, and onto the fire.



<a name="br51"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 51

270 Oily Swamp

Physical Description

Past the school lies some oily swampland, no good to anyone, with “black goo oozing

from the ground creating nothing but a messy problem for the townsfolk.” Past the

school is nothing but mountains.

Features

water tank, caboose, tracks, swamp, mine, background buildings, foreground clutter

Props

bubbly gooey swampy stuff

Actors

Objects Found Here

Objects Used Here

Description of Events

Always animate the bubbles randomly throughout the swamp.

If ego walks onto goo, take programControl, walk him towards the center of the

swamp a step or two, switch to the “sinking into swamp” animation, and watch him dis-

appear. EndGame. “Now you’re really in over your head, Fred!”



<a name="br52"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 52

At the Base of Collier Bluff

300 West Bluff Street

Physical Description

Boot Hill is located here, although the gate is in 310. A fake outhouse is here. Open

the door and you can see right through it, including the prop that holds it up. You can

read many humorous messages on the headstones, see two adjoining half-width graves

and headstones (for a woman who was cut in half when her hero didn’t make it to the

sawmill in time); boots sitting on gravestones; a Swiss cheese tombstone (for a gunfight

victim), and IPO prospectuses of some mythical computer game companies.

Features

angel fence post, gallows, noose, sign by noose, many headstones, open grave,

newly-dug grave, flock, rabbi sheep, fence around Boot Hill, broken fence, large rock

behind fence, background mountains, foreground clutter

Props

swinging sign, swinging noose, prop outhouse door, open grave, newly-dug grave

Actors

buzzards circling in distance, sheep rabbi, his “flock” around grave

Objects Found Here

clay, shovel, safe deposit box key

Objects Used Here

empty beer bottles

Description of Events

Always animate the swinging noose and sign. Keep them random like “variable

breezes from the northwest at 5-9 miles per hour.”

If you click the Hand on the fake outhouse:

You enter under programControl, walk right through, out the back, around

front and re-close the door.

If curPuzzle > “Snail stampede” && curPuzzle < “Contaminated Water:”

Show grave digger at work in Boot Hill.

If curPuzzle >= “Contaminated Water:”

Show the fresh grave. If the clay is still here, you can Take some. If the

shovel is still here, you can Take it too.

If you Use the shovel on a grave:

If it’s Phillip Graves’s, print “Your ol’ buddy Phil! You haven’t seen him for

quite a while; not since right after you moved to Coarsegold.” Show animation of

Freddy digging, show pile of dirt increase, show him stick shovel in dirt pile.

If Phil’s grave is open:

If you click the Hand on the shovel, fill the grave back in, but the grave al-

ways looks like a fresh grave. Keep the shovel in Inventory.

If you click the Hand on the grave, show ego jump down into the grave, and

bend over. Play casketOpeningCreaking soundFX. Print “Whew! Phil never

smelled good when he was alive, but now…” “You carefully search through the



<a name="br53"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 53

many pockets of Graves’s three-dollar suit, until you discover…” “…your safe de-

posit box key!” Add the safe deposit box key to Inventory. Bend over, play creak-

ing soundFX, jump out of grave, grab shovel, shovel dirt until dirt pile is gone,

but the grave always looks like a fresh grave. Keep the shovel in Inventory.

If curPuzzle > “Arm yourself” && curPuzzle < “Dress Up:”

Srini is here waiting for you.

If you arrive without the necessary equipment, he’ll give you clues, offering

suggestions as to the feasibility of shooting without bullets, without targets, with

a dirty weapon, etc.

If you have all the equipment you need and you click the empty bottles on

the fence posts to set up the targets, we see you place the bottles in position,

and see Srini walk behind the large rocks. We then change automatically to “540

Target Practice” below…

If prevRoom == “540 Target Practice:”

Return from target practice with Freddy positioned near the fence posts.



<a name="br54"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 54

310 Central Bluff Street

Physical Description

North of Main Street’s shops are lots of homes which aren’t accessible, the village

church, and an eroded clay bluff. You can open the gate and enter Boot Hill. If you do,

you walk to the edge of the screen and we scroll to room 300.

Features

graveyard fence, hearse, coffin, church, church windows, belfry, bushes beside

church, windmill, windmill tower, foreground clutter

Props

graveyard gate, coffin lid, church doors, burning candles, windmill, weather vane

Actors

Objects Found Here

candle wax, church key

Objects Used Here

key (may be used to lock/unlock church doors)

Description of Events

If you click the Hand on the coffin lid, it opens & closes. Handle several verbs in

both conditions.

Always:

Upon entering the room, randomly set the cel of the weather vane to indicate

the direction of the wind has changed. (Subtle, eh?) (So why doesn’t the windmill

change too?)

Animate the windmill blades slowly turning.

If it’s daylight, randomly 1/5 put the sleeping owl in the treetop.

If it’s night, the awake owl is always here looking at you with big bright eyes.

If curPuzzle > “Snail stampede” && curPuzzle < “Contaminated Water:”

Don’t let ego enter Boot Hill. If you click the Hand on the gate, print “You

don’t want to go anywhere near that grave digger.”

If curPuzzle == “Contaminated Water:”

Don’t let ego enter Boot Hill. If you click the Hand on the gate, print “Ewe

wouldn’t want to interrupt that funeral!”

If you Look at the closed church door (a Cond):

If the church key is still here, “You bend over and attempt to look through

the keyhole, but you can’t because it’s blocked.”

If the door is locked, print “You locked it, remember?”

Else, print “This looks just like the door where you stole that church key.”

If you click the Hand on the closed church door, you open it.

If you Look at the inside of the left open church door, print “The door clearly shows

the beauty of natural wood-grain finish. (In other words, it needs a coat of paint!)”



<a name="br55"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 55

If you Look at the inside of the right open church door, you get a overlay showing a

close-up of the inside of the door. If the key is still here, show a skeleton key sticking in

the door’s keyhole. When the overlay is up, you can Take the church key.

If you Look at the inside of the church while the doors are open, print “You see some

votive candles burning just inside the left front door.”

If you click the Hand on the inside of the church to Take a candle, print “You would

never dream of stealing a candle from a church. But… they wouldn’t miss a puddle of

this candle wax.”



<a name="br56"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 56

320 East Bluff Street

Physical Description

The “Fargo Wells Company’s” water tower is situated on the hillside here. The round

water tank rests on a square platform mounted on a tower about 10 feet tall.

Features

windmill tower, outhouse, covered wagon, water tank, tank peak ornament, tank

tower, foreground clutter

Props

windmill blades, outhouse door, water tower hatch door, spigot, Zircon Jim Laffer on

the can

Actors

animals to roam in the background scene??

Objects Found Here

water sample

Objects Used Here

Deflatulizer™, ladder, lasso

Description of Events

Always:

Animate the windmill blades, slow, stop a while, speed up again.

Animate animals in the background scene.

If curPuzzle == “Contaminated Water:”

addToPic people standing in line for the outhouse.

If you click the Hand on the outhouse:

If there’s a line:

Print “You must wait your turn.” (Of course, the line will never move,

but… oh, well.)

OR, “It may be a while. He’s suffering from the Hershey squirts!”

Else, If Random 1/3 odds, set in room init:

Open the door to reveal Zircon Jim Laffer sitting there reading. He

makes a smart remark. You close the door and vomit.

Else:

Open the door, walk Freddy in, close the door, wait a few seconds,

play the buzzer soundFX, print “Those damn kids! Hiding their joy buzzer

under the outhouse seat!”, wait a few seconds, open the door, walk him

out, close the door, make a rude remark about bladder control.

If you click the Hand on the spigot, turn the water on/off. AddToPic the water pud-

dle below it. The puddle magically disappears whenever ego leaves the room. (“It’s that

dry desert soil, you suppose…”)

If you click a container on the spigot, “If you’re thirsty, take a drink.”

If you Use the rope on the water tower or tank, show Freddy go through the anima-

tion of throwing a rope and print “Funny how it doesn’t catch on!”



<a name="br57"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 57

If you Use the lasso on the water tank, whether from the ground, on the low ladder,

on the platform:

swing the rope over your head a few times and throw, but your lariat is

much too short. (The lasso animation must be usable in all three locations.)

If you Use the ladder on the tank tower:

If ego on ground, walk over to the rear of the tank, show him put the ladder

in place. Remove the ladder from Inventory.

If ego on the platform, walk over to the front of the tank platform, show him

lean the ladder against the tank. Remove the ladder from Inventory.

If you click the Hand on the ladder:

If you are on the ladder, print “You can’t seem to pick it up. It seems much

heavier now!”

Else, Take the ladder, and add it to Inventory.

If you click the Walker on the ladder, you climb the ladder to its other end.

If the ladder is on the ground:

If you are on the ground, you climb up the ladder until you are stand-

ing on the water tower platform.

If you are on the platform, you climb down until you are standing on

the ground.

If the ladder is on the platform:

If you are at the top of the ladder, climb down to the platform.

If you are on the platform, climb up to the top of the ladder and stop.

If you Use the lasso on the ornament on the top of the water tank while standing on

the top of ladder while the ladder is resting on the tower platform (whew!):

Go through two tries that miss the ornament. Each time print, “Almost.” The

third try brings success! The loop catches on the ornament, switch to ego anima-

tion to show him climb the rope and swing up on top of the tank. Return to play-

erControl, with ego able to crawl around on the top of the tank.

If ego is on top of the water tank:

Under playerControl, let him walk around. If he falls off, he dies. EndGame.

Use splat Freddy cel and print “It’s a long way down from there!”

If you click the Hand on the hatch, we see you move to it, open it, and re-

main kneeling.

If you Use the water purification solution on the hatch: show Freddy pouring

it in, then fade to black, explain through text that you finish here, save the city,

and go home to a quiet dinner alone. Soon, “Night Falls” and with it, you. Cut to

your bedroom.

If he clicks the hand on the rope, he climbs down the rope to the ladder.

He can not remove the rope once it is around the tank ornament.



<a name="br58"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 58

The “Other Side of the Tracks”

400 “Ye Olde ’Ore House” Exterior

Physical Description

South of the RR tracks, South of cattle pens, lies the “bad part” of town. You can

just see the hotel balcony in the upper right corner of the screen. A Look to the North-

east says, “It’s a clear shot to the Hotel from here.” A banner flaps on the Hotel that

reads, “Coming soon—Mom’s Comedy Club! Monday’s are ‘Open Megaphone Night’ Take

your best shot at making grown men laugh!”

If you just extinguished the assay office fire, there’s “another kind of fire you need to

extinguish!” “What is there to do, in this town, at night, when you’re wide awake and all

alone, with all townspeople asleep and all the buildings locked? Of course!”

Features

brothel, upstairs windows, porch, sign, RR buildings, RR clutter, RR crossing sign,

Hotel, bunting, other Main St buildings, gazebo, fence, foreground clutter

Props

door, sheriff, banker, leaves on tree

Actors

(sheriff & banker are props, since they never move)

Objects Found Here

Objects Used Here

gun

Description of Events

Always animate the leaves on the tree limb gently swaying.

Brothel business hours:

If curPuzzle < “Burning of Coarsegold,” the brothel is closed. Trying its door

gives, “Wait until dark, Freddy!”

If curPuzzle == “Burning of Coarsegold,” it is night, the brothel looks open,

but trying the door gives, “Freddy! Your store is ready to burn. You must save

your town from sure destruction!”

If curPuzzle > “Burning of Coarsegold,” && < “Arm yourself,” the brothel is

open, “fully stocked” and ready for business until you “see Madame.”

If curPuzzle >= “Arm yourself,” the brothel is unlocked (but the parlor is wo-

manless) if the postcards are still inside. After you Take them and exit the “par-

lor” to this room, you can still walk back inside. But when you exit this room

North to Main Street, the joint is then closed for the rest of the game.

If curPuzzle == “Overhear Sheriff & Banker:”

When you enter this scene from the North, animate the sheriff and the

banker on the porch, randomly smoking cigars. As ego approaches a point in

line with the porch (where he might be able to overhear a conversation without

being seen) stop him and print their “plot Freddy’s demise” conversation. “That

oughta lower property values!” “Ha, ha, ha!” “You seem frustrated by your low

sexual intensity.” “Murder, intrigue, extortion, arson, swindling, high stakes po-

litical power plays… damn this is a fun time to be alive!”



<a name="br59"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 59

During the conversation, you are free to walk. If you go forward, they notice

you, and their conversation stops. You can exit North to Main Street. If you re-

turn, their conversation picks up where it left off when you interrupted it.

When they finish their conversation OR if ego walks past them into the

brothel, bump curPuzzle to “Madame Ovaree.”

If you Look at them, print “While it’s difficult to see in this light, you are cer-

tain you can smell coal oil on both of them.”

When Freddy steps on the brothel steps, he has a short “greetings” conversa-

tion with them.

If curPuzzle == “Local Cowhands” && the nitrous oxide is on the Hotel balcony:

Occasionally (seldom) show a “glint” from the cannister.

Show the cannister on the balcony. (All 2 pixels of it?)

If you Use the gun anywhere near the cannister while not in the gazebo,

print “Good idea, but you just don’t have a straight shot from here.”

If you are in the gazebo and Use the gun near (but miss) the tiny cannister:

Show Freddy turn to face the hotel. Do animation of Freddy aiming

the gun, print “You take careful aim with your pistol, slowly squeeze off a

shot…” Show him shoot. BANG soundFX. Print “Good idea, but you

missed!”

If you are in the gazebo and Use the gun on the tiny cannister:

Repeat above, except Print. Small sparks on balcony. “You did it! You

shot off the cannister’s valve.” Bump curPuzzle to “ROLFing Cowhands”

and cut to West Central Main Street, to watch the bottle break open and

spray nitrous oxide (which is invisible, isn’t it?), silencing their guns as

they all ROFL in the streets. “Nice shot, Freddy!”

If curPuzzle == “ROLFing Cowhands:”

We cut back to this scene from West Central Main just in time to watch

Freddy blow the smoke from his pistol, holster it, bump curPuzzle to “Lever Bros

shooting gallery” and resume playerControl. Be sure he’s positioned where he

was standing when we left.



<a name="br60"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 60

410 Brothel Waiting Room

Physical Description

A nice place if you enjoy reds and violets. The brothel has a barrelhouse piano

player off-screen pounding up a storm. Several hookers sit around the front room,

draped over chair arms and sofas. They are all named after virtues: Purity, Chastity,

and Modesty. No real roles, just hang around, looking for work.

Features

chandelier, beaded curtain to Madame’s room, coffee table, coffee service, clock, Cu-

pids, bar, spittoon, stairs, chairs

Props

hanging beaded curtain, clock pendulum, Purity, Chastity, Modesty

Actors

Madame

Objects Found Here

French postcards

Objects Used Here

Description of Events

There are some racy French postcards on table here which you can Take. Look says,

“Evidently Madame has just received some correspondence from a friend in France.” A

Look in Inventory shows some “titillating” cels, and a message in funny fractured

French.

You can’t go upstairs, “because there’s nothing up there you need.” You can’t enter

Madame’s beaded curtains (“without an invitation.”)

If curPuzzle > “Madame Ovaree” && postcards are still here:

The downstairs is deserted, although the postcards are readily accessible. You can’t

enter Madame’s beaded curtains (“You wouldn’t want to interrupt her “hard-earned”

sleep.”)

If curPuzzle == “Madame Ovaree:”

Animate the three girls filling the three chairs so there’s no place for ego to sit down.

He can Talk to all of them, but nothing more.

Handle Use-ing the girls, spittoon, coffee pot and bar.

After you’ve waited 30 ?? seconds in the waiting room, Madame Ovaree makes her

grand entrance through the beaded curtain. She greets you comfortably and graciously,

as if you spent a lot of time there (which, of course, you do!). You are not interested in

the girls in the waiting room, just Madame. “Remember girls, you’re not whores—you’re

prairie hostesses!”

When you Talk to her enough, she intimates she has information for you. “Follow

me, Freddy.” “But I have no money, Sadie.” “I’ll just put it on your account.” When you

walk over to her, we take programControl and walk the two of you through the curtain,

into her room, then cut to…



<a name="br61"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 61

420 Madame Ovaree’s C.U.

Physical Description

This is not a sexy pic, just two faces, close together, talking. From the looks of the

background, they could be in a bed with a fancy headboard, or sitting on a Victorian

sofa. It doesn’t matter, except we shouldn’t see enough to be certain they’re in bed.

Their faces should be large enough that we can animate the picture directly, as this is a

critical conversation.

Features

her, you

Props

her eyes, nostrils, mouth; his eyes, nostrils, mouth

Actors

Objects Found Here

Objects Used Here

Description of Events

Madame and you chat for a while (first?). She warns you about rumors she’s heard;

there’s big trouble brewing for Coarsegold. Someone wants the entire population gone.

The perpetrator will stop at nothing until it’s a ghost town. The problems you’ve solved

so far are nothing compared to what she has heard is coming! (Of course, she is unable

to reveal her sources because of “hooker/client privilege.”) But she is confident the big

troubles will begin soon, and will involve gun play. From the way she talks, it is obvious

she knows all about your past. She feels you’re the only man in town able to stop the

threat. You realize your wits will no longer be enough; you must prepare once again to

“sling hot lead!” We fade to black, with a little pun concerning how “she helps you shoot

off a couple of rounds.” We fade up with you in bed in your own bedroom for another

sepia-toned screen.



<a name="br62"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 62

500 Mom’s Rear Entry

Physical Description

This is a reverse angle shot showing the stairs leading to the hotel balcony, the rear

of Mom’s Cafe and the back door of the saloon. A rear window into Mom’s kitchen shows

Hop Singh hard at work.

Features

stairs, Mom’s, Mom’s window, saloon, saloon door, rubbish, foreground clutter

Props

sheep weathervane, steaming pie, saloon door

Actors

Hop Singh

Objects Found Here

ice pick, pie

Objects Used Here

Description of Events

In room init, randomly set the cel of the weather vane to indicate the direction of the

wind has changed.

If you Walk to the top of the stairs, change to “230 West Central Main Street.”

You can Take the ice pick that’s stuck in the wall of the saloon here.

If the horsePlopTimer is not running and Mom’s is still open (IOW, if Hop Singh’s not

busy cleaning up your horse shit in the cafe and you haven’t taken the apple pie yet):

Animate Hop Singh inside the kitchen, randomly wandering back and forth,

pausing in various places, looking busy, mostly out of sight, or nearly so.

If curPuzzle > “Madame Ovaree” && the pie hasn’t been taken:

Animate the apple pie cooling on Mom’s window sill.

If you Look at the pie, print “How tempting! Fresh apple pie, still warm from

Mom’s oven. What could be more American?”

If you click the Hand on the pie to Take it:

If Hop Singh is here:

Show Freddy walk over to window, reach for pie, take pie,

print “You slyly attempt to swipe the apple pie from under the

cook’s nose!” Show Freddy walk around the corner towards the

saloon door. As he reaches the corner, a huge meat cleaver flies

through the open window. Bang! You’re dead. Freddy drops, and

the pie explodes dramatically. Use collapsed death cel, and “He’s

serious about his cooking!”

else,

Show Freddy walk over to window, reach for pie, take pie,

print “Cool move, Freddy! Dropping one steaming hot pie to get

another!”



<a name="br63"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 63

The Token Arcade Games

540 Target Practice

Physical Description

This is a M.S. showing your gun visible at the bottom of the screen, with the bottles

visible above. (This must look similar to the gunfighting screen used later on in the

Lever Brothers arcade game.) You may leave this target practice screen and return later

to the same achievement level you left.

Features

targets, hand, gun, shadow

Props

Srini, Srini throwing bottle, bottles on posts, cardboard hands w/guns

Actors

gun in hand, shadow, bottles in air, exploding bottles

Objects Found Here

Objects Used Here

gun, bullets

Description of Events

If you Use your gun and it’s not loaded, print “Click.”

Don’t display the gun until you make the gun the active inventory object and select

it.

This arcade game is built around achievement levels, from 1–3.

In Level 1 of this game, you blast away at the bottles with total disregard to the

number of shells available (i.e., there’s no twelve-bullet limit). As bottles get hit, the

fence posts and bottles scroll left and more bottles scroll in from the right. In the begin-

ning, your hand wavers, your aim is unreliable, and your confidence low. This is repre-

sented on-screen by a wildly erratic pistol cursor. Srini provides confidence building (or

deflating) messages based on your performance. As you practice, your cursor calms

down, you score more often, and Srini becomes more complimentary. After ?? seconds

or ?? shots (depending on arcade level setting), your aim is true and you advance to the

next level.

Srini introduces Level 2 by rising up from his hiding place to suggest it’s time now

for you to practice your quickdraw. “Keep your gun down until I say, ‘Draw!’” he says.

Your gun automatically lowers to the bottom of the screen and remains there while Srini

sets up only one bottle. It will not move until you hear Srini shout, “Draw!” (sampled

soundFX). Then you gain control of the cursor, quickly move it to the only bottle and

fire. After ?? seconds or ?? shots (depending on arcade level setting), you advance to the

next level.

Level 3 is introduced with Srini’s instructions to you. “Wait until you see the gun be-

fore you draw.” You have full cursor control. Srini hides behind a rock, but waits until

you move your cursor to the bottom of the screen. Then, after a random number of cy-

cles with the cursor below 160Y ??, he pops up a cardboard hand with a crude pistol

drawn on it. You draw, shoot and hit the target before he hides it again. You miss a lot

at first, but eventually improve.

After ?? seconds or ?? shots (depending on arcade level setting), you receive a short

cartoon: under programControl, Srini tosses six bottles into the air simultaneously. You



<a name="br64"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 64

fire six nearly-instantaneous shots and automatically break every one. Srini is im-

pressed, proud, and pleased. “For battle you are ready, Freddy.”

Then, if you don’t have all your clothes in Inventory, he’ll suggest you need an outfit.

If you don’t have your silver ear in Inventory, he’ll suggest you need a disguise. “I’ll tell

everyone you left town; otherwise the sheriff will hunt you down and kill you. But you

must have a disguise. What about a silver ear? No one will recognize you if you’re wear-

ing a silver ear!” “A silver ear?” you muse. “Hey, that just might work!” We fade to black,

praise your readiness, and return to 300 West Bluff Street above.



<a name="br65"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 65

550 Lever Brothers gunfight arcade

Physical Description

First person view, but totally unrealistic. This looks like a surrealist’s shooting gal-

lery arcade game—suddenly the bad guys have flashing lights and points numbers on

their chests and fall over, then rise back up, as if they were 2-D cardboard cutouts. As

they stand up, you shoot them or they shoot you (depending on the arcade level setting).

EndGame. The wackier, the better.

Guys hide behind wagons, water barrels, horse watering troughs, false fronts of

buildings, hotel balcony, the top of the water tower, all of which drift across the screen

randomly and irrationally. Whenever possible, as you hit targets in high places, the bod-

ies tumble out of windows and over railings to fall to the ground in dramatic “authentic

stuntman” fashion; when your bullets “hit” wood, pieces of wood explode; a shed labeled

“Dynamite” explodes when you shoot it.

Features

add later (depending on art)

Props

dynamite shack, explosions, ego’s gun and gunfire

Actors

lots!

Objects Found Here

Objects Used Here

gun

Description of Events

Objects float across the screen. People, animals walk; birds fly; sheep float. Some-

times things appear from behind windows in high-rise buildings in the background.

Some targets (like widows and orphans) are “good”—shooting them lowers your score.

Some (like the Lever Bros) are “bad”—shooting them gives you points. Some are just

“fun”—sheep, ducks, flying toasters, kittens. Some are “in disguise”—what appears to

be a child, widow, policeman or sheep, spins around to reveal themselves as a Lever

Brother, and begins firing at you. Each target should have a “Points” property, either

positive or negative. A “hit” adds the “Points” to your score.

When hit, “Fun” targets, puff a little explosion (1 or 2 cells is enough), and its points

value appears in its old position. Hitting a Lever Brother provides more elaborate ani-

mation. Shooting “Good” targets gives a “wrong” soundFX.

The fraying rope “Health-O-Meter” is visible and active on-screen at all times. Shots

fired at you affect your “Health-O-Meter” setting. If it hits bottom, you die. EndGame.

“Think you lived through that one, Freddy?” “Frayed knot!”

The “Arcade” setting in the Control Panel directly affects the “hit radius” of your

shots and the speed with which you regain strength. It also determines the “points”

property of the objects.

After killing each of the Lever Brothers a few times (depending on the arcade level

setting), they stay down. Eventually, the number of opponents dwindles. After shooting

the final villain, bump curPuzzle to “Kenny’s Quickdraw arcade” and return to West

Main Street.

Have fun with this.



<a name="br66"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 66

560 Kenny’s quickdraw arcade

Physical Description

Gunsmoke’s classic opening shot, showing Kenny walking towards you from a dis-

tance, visible between your legs, while your gun hangs at your side. Here he comes,

slowly walking towards you! A better shot, a faster draw, you’ve never been able to beat

him before; but now you must stare him down, never flinching, in the middle of Main

Street, at high noon, eyeball-to-eyeball, cheek-to-jowl, man-to-man… well, you get the

picture.

Features

distant landscape, bullets, gun, quickdraw holster, your ass, boots

Props

ego’s gun, 2 gunfires w/smoke, neckerchief, blood

Actors

Kenny, Freddy

Objects Found Here

Objects Used Here

gun

Description of Events

Before Kenny is in position and ready to fire:

We see Kenny from between your legs. He walks forward towards us, stops at

a medium distance and assumes his ready position. You warn him, “Kid, I want

you out of town by sundown!” He laughs in your face, “Take your best shot,

Stranger!” He pauses for 5?? seconds. “Say, nice outfit!” he snarls. At that mo-

ment, you lose control of the cursor. It remains at the bottom of the screen until

Kenny makes his move.

If you shoot before he reaches his starting position (while he is still walking),

you automatically miss, he ridicules you for your poor shot and lack of etiquette

as he walks backwards to the starting position to begin again.

After he’s in position:

if you try to cheat by moving or clicking early, “your respect for frontier eti-

quette won’t let you draw first.”

If your cursor is not a gun when he’s getting ready to draw, he warns you to

“get ready!”

They have a little dialogue featuring lines such as, “I remember you from the

OK Corral down in Tombstone.” “No, never been to Arizona Territory.” He men-

tions your clothes. “I dress this way because it makes me look good; damned

good!” He laughs. “Kiss my pestle!”

When he’s in his firing sequence:

If you click your gun cursor on Kenny after his 3rd ?? cel, we see him fire, we

hear one shot only, your cursor disappears and we slowly manipulate the VGA

palette directly to all reds (indicating your eyes filling with blood). “You be one

dead Fred.” EndGame.

If you do shoot within the first 3 cels (i.e., you do draw quickly enough), we

see him fire, we hear two shots, and we cut to…

“565 Two Oval Vignettes of West Main Street:”



<a name="br67"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 67

A dark screen version of “220 West Main Street”with just two normally-lit

oval vignettes, one for each of you, and a fancy label below reading “Exclusive

Sierra Slow Motion Instant Replay.” We watch a “Slow Motion Instant Replay” of

your successful (only) quickdraw action.

We see Kenny draw first, but you draw faster. We see your gun fire one

frame before his, see the flash from both barrels, see his gun deflect slightly as

he fires, and see you get hit in the left ear (the side towards the camera) by his

bullet. We see you fall to the ground, bleeding profusely. We see Kenny coolly

blow the smoke from his gun, shake his hand, holster his gun, then walk over to

you by walking behind the black portion of the pic, i.e., out of one vignette and

into the other. Cheat the slow-mo speed on the walk-over so it doesn’t take too

long. He stops beside you. Bump curPuzzle to “bleeding in the dirt” and cut back

to…

“570 Freddy Down & Dirty C.U.:”

This is nearly the same picture as 560.p56. We are again looking down Main

Street, but now instead of standing with your butt filling the frame, you’re lying

in the dust, your head filling the frame, your eyes closed, your injured ear oozing

blood and your “lucky” neckerchief clearly visible. You show no signs of life.

Kenny towers above you.

He assumes you’re dead, kicks a little sand in your face, ridicules your lack

of skill, and then we see one cell of the bottom of his boot (which completely

hides him) as he steps over you. He’s now off-screen, but we remain looking at

your face.

You hear his voice as he walks away unseen, “Time for me to give Penelope a

little more than a full report!” You realize he’s heading for the schoolhouse, that

Penelope is behind the conspiracy, and that you’re going to bleed to death in the

middle of Main Street.

Waiting to die sequence:

“As you lie in the dirt, filled with despair…” if you don’t click the neckerchief

on your ear within 20 ?? seconds, you bleed to death. EndGame.

But if you do, “you use your lucky neckerchief as a bandage to apply direct

pressure to your wound. The bleeding stops. Say… weren’t you wearing your

lucky neckerchief when he shot your other ear?” We cut back to 565.p56, see

Kenny’s vignette empty, watch as you rise shakily to your feet and stumble off-

screen after Kenny. We then fade to black, then fade in on the “Schoolhouse Ex-

terior,” with you standing on the schoolhouse steps.



<a name="br68"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 68

Inside the Pharmacy

600 Pharmacy Interior

Physical Description

Ego’s place of business. Invisible cowbell on front door rings any time anyone passes

through. A sign on the wall reads, “Just say ’No’ to Ether”.

ART NOTE: be sure to allow for Srini’s “award-winning product display” and a place

for the silver medallion to hang. Hide the face of all clocks in the game behind reflec-

tions, but allow the pendulum to show.

Features

lots of

Props

clock pendulum, product display, silver medallion, cash box ??

Actors

Penelope, Helen Back, Madame Ovaree, Smithie, Sheriff Shift, Srini

Objects Found Here

Prescription #1, Prescription #2, Prescription #3, Preparation G, money

Objects Used Here

Medication #1, Medication #2, Medication #3, Preparation G

Description of Events

You may leave the Pharmacy at any time while a customer is present. When you re-

turn, that same customer will still be there, “patiently” waiting. They wait until you fill

her/his prescription before leaving. If two customers were there, save both their posi-

tions and place them there when ego reenters this scene.

If prevRoom == “250 East Main Street, Sheriff & Pharmacy” OR a character walks in

from Main Street, play the cowbell soundFX.

If ego exits to Main Street OR a character exits to Main Street, play the cowbell

soundFX.

If curPuzzle > “Brief your sidekick” && you’ve been outside at least once:

addToPic the “huge, attractive display of “Wolverine Brand Salve” Srini has

worked so hard to create.”

If curPuzzle > “Quickdraw practice” && you haven’t taken the silver medallion al-

ready:

Hang the silver medallion somewhere in the shop.

If you Look at the medallion, print “It seems Srini’s entry in the ‘Wolverine

Brand Salve’ contest won second place!”

If you click the Hand on the medallion, you Take it.

If curPuzzle == “Ready For Business” (it’s your first time in here), bump curPuzzle to

“Prescription #1” and make Penelope follow ego in. When she catches ego, show her

hand him Prescription #1. She’s suffering from the “Vapors.” Show him accept it. Pro-

vide a little chit-chat. Set the local whinerTimer to Random 20 40 ?? seconds. Reuse

this “walk-in, talk & whine” code for Helen and Madame and Smithie.



<a name="br69"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 69

If the whinerTimer expires && ego doesn’t have (either the correct or an incorrect)

medication in Inventory && ego hasn’t already given Medication to customer:

Reset the whinerTimer. Make the customer bug ego about the delay. “Well?

Are you going to fix my prescription or not?” The customers handle this differ-

ently; earlier customers provide clues, later customers are belligerent.

If prevRoom == “Back Room” && an improperly made Medication is in Inventory, the

next customer doesn’t enter. (IOW, if you come from the Lab with bad medicine, don’t

bring on the next prescription.)

If you give a “wrong” medication to a customer:

Set a “badMedicine” flag. Handle her just as you would a “correct” medica-

tion, except the next customer doesn’t enter. She leaves. No new customer ever

appears. You are then free to wander around town at will. But when you re-enter

this scene:

If prevRoom == “Main Street” && the “badMedicine” flag is set:

As you enter the pharmacy, the same customer follows you in, telling

you “Lucky for me, I tried some of that medicine you gave me on my %s!

And you killed it!” (dog, cat, goldfish, bird, horse, cow, son’s sheep, etc.)

Walk through the array; if you finish, add “new” before each pet’s name.

If prevRoom == “Back Room” and Medication #1 is in Inventory, Helen Back enters

(before Penelope leaves). She waits near the entrance, until Helen Back starts out, then

she heads for ego. When she catches ego, show her hand him Prescription #2. She’s suf-

fering from “Melancholia.” Show him accept it. Set the local whinerTimer to Random 20

40 ?? seconds.

If prevRoom == “Back Room” and Medication #2 is in Inventory, Madame Ovaree en-

ters (before Helen Back leaves). She waits near the entrance, until Helen Back starts

out, then she heads for ego. When she catches ego, show her hand him Prescription #3.

“It’s not for me, you know. Some of my girls are suffering from… that problem.” Show

him accept it. Set the local whinerTimer.

If prevRoom == “Back Room” and Medication #3 is in Inventory, Smithie enters to

the tune of “Blood in the Saddle” (before Madame leaves). He waits near the entrance,

until Madame starts out, then she heads for ego. When he catches ego, they chat a lit-

tle. He requests a large tube of Preparation G. Set the local whinerTimer.

If you Look at the counters and shelves, eventually you’ll discover the Preparation G.

It is on this screen (not in the back room or the Lab Screen),

If you click the Hand on the Preparation G, you Take it. Add it to Inventory.

If you Use the Preparation G on Smithie, you give it to Smithie. Remove it from In-

ventory. Bump curPuzzle to “Sheriff shutdown.” Print “Why not your usual six-pack of

liniment, Smithie?” “Wall, Mr. Pharkas, I’ma fixin’ to take a long ride. I’ma gonna leave

town. I sold offen that lousy stable to ma friend, Mr. P. H. Balance down at the bank.

Besides, you ought’a jes’ smell them horses a’fartin’!” As you walk Smithie out, walk in

Sheriff “Chicken” Shift, who walks to ego, then proudly announces, “Fire inspection! I’m

here to check out chur fire safety, per the new town regulations.” He looks around.

“Whoa! Good thing I came, too! Pharkas, I’ma gonna havta shut this place up tighter

than a pissant’s scrotum.” “But, Sheriff! How could you? What the charge? I haven’t

done anything wrong!” “Fire hazard! Why, this buildin’’s a terrible fire hazard, Pharkas!

I do believe this whole buildin’’s made outta wood!” “But, Sheriff!” you protest, “every

building in this town is constructed of wood!” “I dunno nuttin’ ’bout that, son. Oh, well.

Tough luck, Pharkas. I’ll have that young Sam Walton boy come right away to put up a

big “Closed” sign over your front window. From now on, keep that front door locked.”



<a name="br70"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 70

“But what am I supposed to do, Sheriff? This is my only livelihood.” He heads for the

exit. Halfway there, he says, “I’d talk to the bank, if’n I was you. Ga’day!” Bump curPuz-

zle to “Start Act II.” Fade to black. Print a few sad messages in which you realize some-

one is out to get you, just like they did Smithie! Cut to “East Main.”

If you click the Hand on the cash box:

If you have collected money from any customers:

Print “You Take your money from the cash box but leave the box on

the counter.” Add money to Inventory.

Else:

Print, “Your strong box is empty.”



<a name="br71"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 71

610 Pharmacy Back Room

Physical Description

Includes your rolltop desk, the lab area, and the stairs to your room. You may al-

ways walk up the stairs. If you walk near the lab table, cut to the “Lab Screen” below. If

you walk off-screen to the South, cut to the “Pharmacy Interior.”

Features

Props

desk’s rolltop, clock pendulum

Actors

Srini

Objects Found Here

letter, gaseous spectroscope

Objects Used Here

desk key

Description of Events

You Use the desk key to unlock the rolltop desk, then click the Hand on it to open

the lid. A Look at the open desk reveals a locked cubbyhole drawer. Use the same desk

key again on the desk to unlock the drawer, then click the Hand on the drawer to open

it. A Look reveals the letter inside and Gives it to you.

If curPuzzle == “Brief your sidekick:”

You can only be here if prevRoom == “Robertson Cliff.” We watch a short car-

toon in which you give Srini his “welcome aboard” speech, order him to “refresh

the stock and to create some attractive displays in preparation for our big ‘Grand

Re-Opening Sale.’” Prepare for some long-winded silly work-ethic human re-

sources speech.

If you click on the Fast Forward icon at any time during this cartoon, bump

curPuzzle to “Contaminated Water,” jump to the end of the speeches and return

playerControl.

If the baking soda is outside and you haven’t yet Talked to Srini, you always find

him here. When you Talk to him, he tells you he messed up his first order, ordering

“baking soda, 1 gross” expecting 144 boxes, but got 144 sacks instead! That is gross!



<a name="br72"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 72

620 Pharmacy Lab Screen

Physical Description

This room is the meat of FPFP. A old-fashioned laboratory table with apparatus on a

counter below, and bottles of chemicals, jars, beakers, tools, and assorted laboratory

paraphernalia above. An area of the screen is reserved for constantly-changing text,

hereinafter referred to as the “text display area” or TDA. The TDA shows the name of the

object the mouse is over, so as the mouse moves across the screen, that line is conti-

nously updating, regardless of the current cursor. This scene handles mixing medicines,

forming pills, smelting silver, mortaring-and-pestling, etc.

It requires the following objects; add others to fill up the holes: empty medicine bot-

tles, corks, bulk liquid medicine jar #1, pill-making machine, graduated cylinder, spat-

ula, balance, balance weights, empty pill bottles, jar of medicinal powder #2, mortar,

pestle, jar of medicinal crystals #1, jar of medicinal crystals #2, wooden box of medicinal

powder #3, etc.

All of the chemicals are “usable,” but using them will create “bad” medicine. It only

takes one wrong ingredient to create “bad medicine.” Some bad mixtures immediately

return to the “Back Room” scene, with a soon-to-be-dead ego standing there in some

humorous pose.

The Lab Screen handles Inventory in a unique manner. Almost everything on-screen

is a “local object” that remains here and doesn’t enter Inventory. If you Take them by

clicking on them with the Hand icon, they become the active cursor so they are easy to

use without a trip to the Inventory window. They remain visible on-screen. They do not

appear in the icon bar as the currently active object. This prevents the player from tak-

ing and carrying around vast quantities of chemicals, etc., but allows them to be used

as needed here. The only real Inventory objects are the completed medications (right or

wrong), Deflatulizer™, water purification solution, empty clay ear mold, and the silver-

filled clay ear mold.

Features

dozens

Props

empty medicine bottles, corks, pill-making machine, balance, jar of medicinal crys-

tals #1, jar of medicinal crystals #2, wooden box of medicinal powder #3, and much

much more

Actors

bulk liquid medicine jar #1, mortar, pestle, graduated cylinder, spatula, balance

weights, empty pill bottles, jar of medicinal powder #2, mortar, pestle, jar of medicinal

crystals #1, jar of medicinal crystals #2, wooden box of medicinal powder #3, etc.

Objects Found Here

medication #1, medication #2, medication #3, corrected medication #3, de-

flatulizer™, water purification solution, empty clay ear mold, silver-filled clay ear mold

apothecary jar, beaker, Bunsen burner, burette (glass measuring tube), crucible, fil-

ter paper, funnel , lab flask, litmus paper, medicine dropper, mortar and pestle, petri

dish, pipette, retort (glass container), test tube, test-tube holder, vial

Objects Used Here

horse flatulence sample, water tower water sample, wax-filled clay ear mold, silver

medallion, empty clay ear mold



<a name="br73"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 73

Description of Events

Continously update the TDA (Text Display Area) with the name of the object the cur-

sor is currently over, regardless of the current cursor.

There are four classes of local objects: chemicals, measuring devices, mixing devices,

and containers.

If a local object is clicked on the table top:

set observeActors on the object so it will “find” its own location free of the

other things sitting there. IOW, the table should look like the objects have rea-

sonable depth and substance to them.

if nothing else is there, assume the player wants to “drop” the object there.

Place it where he dropped it. He can pick it up again later. If he leaves the room

and returns to here without putting things away, we’ll automatically put them

away for him upon his return (i.e., don’t bother storing coordinates).

All four classes exhibit the same behavior under the following circumstances:

If you click the Hand on them, the cursor changes into that object, and the

object becomes the curLocalObj.

If you click the curLocalObj on its original, now-empty, starting location, the

cursor changes to the Hand as the old object automatically floats back to its

original starting location.

If you click the curLocalObj on another member of the same class, the ob-

jects are exchanged, the cursor changes to the new object which becomes the

new curLocalObj as the old object automatically floating back to its original

starting location.

Chemicals

Chemicals include all supplies, whether solid or liquid. The chemical jars never run

out of contents, no matter how much you use.

If the curLocalObj is a chemical:

If it is clicked on a measuring device consider it the same as clicking the

measuring device on the chemical. Thusly: (Cond)

If the measuring device is not suitable for measuring that chemical,

play an “Oops” soundFX to indicate nothing happened and print “The %s

is not suitable for measuring that substance.”

If the measuring device is full, play an “Oops” soundFX and print

“The %s is full.”

If the measuring device already contains something else, play the

“Oops” soundFX and print “You must empty the %s before using it to

measure something else.”

Else, increase the level in the device by 1.

If the chemical is clicked on a mixing device, print “It is advisable to measure

your ingredients instead of just dumping them together.”

If it is clicked on a container:

If the container is not empty, print “This container is for your finished

product, not for mixing. Do your mixing in the proper device.”

Else, increase the level in the container by 1.

Else, play the “Oops” soundFX.



<a name="br74"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 74

Measuring devices

Measuring devices include the graduated cylinder, spatula and balance.

If the curLocalObj is a measuring device:

If it is clicked on a chemical consider it the same as clicking the chemical on

the measuring device. Thusly: (Cond)

If the measuring device is not suitable for measuring that chemical,

play an “Oops” soundFX to indicate nothing happened and print “The %s

is not suitable for measuring that substance.”

If the measuring device is full, play an “Oops” soundFX and print

“The %s is full.”

If the measuring device already contains something else, play the

“Oops” soundFX and print “You must empty the %s before using it to

measure something else.”

Else, increase the level in the device by 1.

If the measuring device is clicked on a mixing device, transfer the entire

amount to the mixing device.

If the measuring device is clicked on a container:

If the measuring device is empty, print “That made a nice sound, but

accomplished little.”

Else, the entire amount is transferred to that container.

If the measuring device is clicked on the dumper, empty it completely and

print, “The %s is empty.”

Else, play the “Oops” soundFX.

Mixing devices

Mixing devices include the mortar and pestle, beaker,

If the curLocalObj is a mixing device:

If the mixing device is clicked on a chemical, print “Click the chemical on the

mixing device, not vice versa.”

If the mixing device is clicked on a measuring device, print “There’s no need

to measure it now, it’s already mixed.”

If the mixing device is clicked on a container, transfer the entire amount to

that container.

Else, play the “Oops” soundFX.

Containers

Containers include empty medicine bottles, empty pill bottles.

If the curLocalObj is a container:

If the container is clicked on a chemical, play the “Oops” soundFX and print,

“Place the chemical into the container, not vice versa.”

If the container is clicked on a measuring device, play the “Oops” soundFX

and print, “Click the measuring device on the container, not vice versa.”

If the container is clicked on a mixing device, play the “Oops” soundFX and

print, “Click the mixture on the container, not vice versa.”

Else, play the “Oops” soundFX.



<a name="br75"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 75

Other

The dumper is where you can “empty” any container, measurer, or mixing device.

The dumper never becomes full.

If you click anything containing something on the dumper, that thing be-

comes empty.

If you click whole bottles of chemicals, empty devices or empty containers on

the dumper, print “Don’t throw that away!”

The pill-making machine is a container that accepts any mixture. When its handle is

pulled, it animates for awhile, then:

If there is an empty pill bottle under its output spout, show the handle come

down and some pills roll into the bottle.

Else, print “You would place the pills into a bottle, but there isn’t an empty

bottle under the machine’s output spout.”

The alcohol lamp begins the game empty and must be filled before it works. It is ei-

ther hot or cool. It is used to heat containers:

If you click the Hand on it:

If it’s burning, print “You quickly lick your fingers and pinch out the

alcohol lamp’s flame.” Hide the animated flame.

Else, print “The alcohol lamp feels cool to the touch.”

If you click the elixir on it:

Fill the lamp with alcohol. Remove the elixir from Inventory.

If you click the matches on it:

Animate the flame. Set it to On. Float the matches back to their

proper location. Change the cursor back to the Hand.

If you click the medallion on it:

If it’s off, print “The medallion looks nice beside the cold alcohol

lamp.”

Else, show the empty “skillet” parked above the flame. Wait a few

seconds, then print “The silver medallion is now completely melted. Now

what?”

If you click a chemical on it:

Print, “Measure some chemical into a mixing bowl first, then heat it

here.”

If the player adds any incorrect ingredient to a mixture, set the “bad medicine” flag.

Check a look-up table to see if adding it creates a “deadly combination.” Most combina-

tions produce only slightly wrong medicine.

If it is not a “deadly combination,” do nothing. Set the flag and handle it later

when the customer returns after giving the mixture to them.

Else, pause a few seconds to allow time for stirring, then immediately go to

the “Back Room,” with a dying ego standing there in a corresponding humorous

pose, i.e., mushroom cloud, stink bomb, blackened and burned, etc.

If curPuzzle == “Prescription #1”:



<a name="br76"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 76

if it’s the first time in this room, print “You study Penelope’s prescription and

prepare to carefully fill it. You wouldn’t want to make a mistake with her medi-

cine.”

if the player does all the following (not necessarily in this order) without any

omissions, change the bottle to “Pepticlymacine Tetrazole”:

Measure 42 ccs of “Pepticlymacine Tetrazole” from the bottle into the

graduated cylinder.

Place an empty medicine bottle on the Lab table.

Click the graduated cylinder on the empty bottle.

Return the graduated cylinder to the shelf.

Take a cork from the shelf and click it on the bottle.

This creates a bottle of Pepticlymacine Tetrazole, the correct Medica-

tion #1, which is then a regular “Take-able” Inventory object.

When he Takes Medication #1, print “You carefully label the bottle ‘Miss

Penelope Primm—for internal use only.’ You wonder if she’ll ever realize your

strong feelings for her?” You then automatically leave the Lab Screen and return

to the Back Room.

If curPuzzle == “Prescription #2”:

if it’s the first time in this room, print “You study Helen Back’s prescription

and prepare to carefully fill it.”

if the player does all the following (not necessarily in this order) without any

omissions, change the bottle to “Quinotrazate”:

Move the graduated cylinder to the table top.

Move the beaker to the table top.

Click the bottle of Bismuth Enterosalicyline on the graduated cylinder

until the cylinder contains 12 ccs.

Move the balance’s slider to the 30 grams.

Click the bottle of Phenodol Oxytriglychlorate on the balance’s pan

until the balance is balanced.

Click the balance pan on the beaker to pour the Phenodol Oxytrigly-

chlorate into the beaker.

Click the filled graduated cylinder on a beaker to pour the Bismuth

Enterosalicyline into the beaker.

Click the glass rod on the beaker to stir the mixture. Under program-

Control, show the rod stirring for a few seconds.

Click the beaker on the pill-making machine to transfer the mixture

to the machine.

Click an empty pill bottle under the pill-making machine’s spout.

Click the Hand on the machine’s handle to form the mixture into 3

pills. Play 3 soundFX of pills hitting the bottle. Click it six more times to

make a total of 21 pills.

Take a cork from the shelf and click it on the pill bottle.



<a name="br77"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 77

This produces a bottle of Quinotrazate pills, the correct Medication

#2. The pill bottle then becomes a normal “Take-able” Inventory object.

When he Takes Medication #2, print “You carefully label the bottle ‘Mrs.

Helen Back—take three times daily, just before meals.’” Add it to Inventory. You

automatically leave the Lab Screen and return to the Back Room.

If curPuzzle == “Incorrect Prescription #3”:

if it’s the first time in this room, print “As you study Madame Ovaree’s pre-

scription, you realize you cannot read it. The writing looks so blurry.”

If curPuzzle == “Prescription #3 Under Glass”:

if it’s the first time in this room, print “As you study Madame Ovaree’s pre-

scription, you realize it can not possibly be meant for her.”

If curPuzzle == “Corrected Prescription #3”:

if it’s the first time in this room, print “You study Madame Ovaree’s pre-

scription and prepare to carefully fill it.”

if the player does all the following (not necessarily in this order) without any

omissions, change the bottle to “Estrosterane”:

Measure 100 mgs of Bimethylquinoline crystals on the balance.

Pour the crystals from the balance into the mortar.

Measure 50 mgs of Metyraphosphate powder on the balance.

Pour the powder from the balance into the mortar.

Click the pestle on the mortar to grind the mixture with the pestle

automatically for 7 seconds.

Move the medicinal papers to the lab table.

Move a small prescription box to the lab table.

Use the 1 cc measuring spoon to move 1 dose of the mixture from the

pestle to the medicinal papers.

Use the Hand to automatically folds the paper.

Use the Hand to move the paper to the the prescription box.

Repeat until all 6 papers are in the box. This produces a correct

Medication #3. The bottle then becomes a normal “Take-able” Inventory

object.

When he Takes Medication #3, print “You carefully label the bottle ‘Madame

Ovaree.’” Add it to Inventory. You automatically leave the Lab Screen and return

to the Back Room.

If curPuzzle == “Flatulent Horses”:

if he Uses the loaded paper bag on the unlit lamp, print, “Whew! What an

aroma! You’d better do something about it before everyone leaves town.”

if he Uses the loaded paper bag on the lit burner, make a small puff of flame,

and print, “Allowing only a slight portion of your sample to escape near the al-

cohol lamp, you notice it turns the flame an unusual color.”

if he Uses the gaseous spectroscope on the burner, place it on the table and

leave it there, hiding the burner. It may be Taken again later, though for no good

purpose.



<a name="br78"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 78

if he Uses the loaded paper bag on the lit burner while the gaseous spectro-

scope is in place, animate the same small puff of flame, display the print,

“Good idea, Freddy. The spectrum lines on that etched glass viewer reveal vol-

umes to those who know how to read.” The Doco reveals someone has mixed

dried lentils in with the horses’ oats.

If curPuzzle == “need gas mask”:

if the player does all the following (not necessarily in this order) without any

omissions, change the bottle to “Aminophyllic Citrate”:

Measure 40 grams of Sodium Bicarbonate on the balance.

Pour the Sodium Bicarbonate from the balance into a 100 ml jar.

Measure 16 ml of Furachlordone with a graduated cylinder.

Pour the Furachlordone into the jar.

Fill the jar with water (to make 100 ml).

Measure 2 grams of Magnesium Sulfate on the balance.

Pour the Magnesium Sulfate into the jar.

Put a cork in the jar.

Shake the jar. This produces a correct Deflatulizer™. The jar then be-

comes a normal “Take-able” Inventory object.

When he Takes the jar of Deflatulizer™, print “You carefully label the brown

jar, ‘Aminophyllic Citrate.’ Congratulations. You’ve just created your first batch

of “Pharkas’ Deflatulizer™.”

If curPuzzle == “Contaminated Water”:

if the player does all the following (not necessarily in this order) without any

omissions, change the bottle to “Bisalicylate Antitoxidene concentrate”:

Measure 3 ml of Bismuth Subsalicylate in the graduated cylinder.

Pour into a test tube.

Measure 4 ml of Orphenamethihydride in the graduated cylinder.

Pour into the same test tube.

Light burner.

Click tube on burner. Hold in place until mixture begins to boil.

Remove from flame.

Pour into bottle.

Put stopper in bottle.

This produces “Bisalicylate Antitoxidene.” The bottle then becomes a

normal “Take-able” Inventory object.

When he Takes the jar of Bisalicylate Antitoxidene, print “You carefully label

the brown bottle, ‘Bisalicylate Antitoxidene.’ Congratulations. Be careful; this

stuff is mightly concentrated.”



<a name="br79"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 79

630 Pharmacy Bedroom

Physical Description

Features

mooseskin rug, moose head, antlers, bed, wardrobe, nightstand, dresser top, dresser

drawers, dresser mirror, armoire drawer, armoire doors, trunk, trunk lid, lamp, book-

case, chair, stairs, railing

Props

moose eyes, antlers, wardrobe doors, nightstand drawer, dresser drawer, trunk

Actors

Srini

Objects Found Here

pharmacy rolltop desk key, gunslinger clothes

Objects Used Here

Description of Events

You can never go to bed on your own.

Every time you walk near the antlers, you do the “trip shtick” (Isn’t that also a AAA

map service?) where Freddy does a hitch step, pauses, looks at the antler, looks at the

audience, then continues to his original destination. (If this creates programming prob-

lems, it’s okay with me to require another click to get him going again.)

If you click the Hand on the armoire, its doors open/close. Handle verbs both ways.

If you click the Hand on the bookcase, its doors open/close. Handle verbs both

ways.

If you click the Hand on the nightstand drawer, it opens/closes. Handle verbs both

ways.

If you Look at the nightstand drawer while it is open:

If the desk key is here, print “you find your desk key.” Add it to Inventory au-

tomatically.

Else, print “There’s nothing left in the drawer you can use.”

If you click the Hand on the dresser drawer, the top drawer opens/closes. Handle

verbs both ways.

If you Look at the dresser drawer while it is open:

If the claim check is here, print “you find a claim check for a pair of boots.

You wondered what happened to those.” Add it to Inventory automatically.

Else, print “You consider whether it’s time to wash some of those socks!”

If you click the Hand on the trunk, the lid opens/closes. Handle verbs both ways.

If you Look at the trunk while it is open:

If the clothes are still here, print “You find your old gunslinger clothes and

your “Good Guy Model” Stetson hat.”

Else, print “There is nothing more of importance in your trunk.”

If you Look at the area under your bed, walk him over, bend him down and print,

“You find some dust bunnies which you do NOT take.”



<a name="br80"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 80

If prevRoom == 320 East Bluff Street:

A short cartoon. Fade up with you lying in your bed after saving town’s water

supply. It is dark outside your window. We see Srini run in, shouting. “Fire!

Fire!” he cries, starting the puzzle’s fireTimer. (“Is it morally wrong to shout fire

on a on this crowded hard disk?” you wonder.) He races back down the stairs.

You leap from bed fully clothed, make the bed in about 3 cels, then regain play-

erControl with curPuzzle == “Burning of Coarsegold.”

If you click on the Fast Forward icon at any time during this cartoon, we

jump to you standing beside the bed with the bed made and curPuzzle set.

If prevRoom == “Madame’s C.U.:”

Fade in on this screen with sepia-tone palette, with “Act III, Guns and Neu-

roses” overlaid. It dissolves to your real room colors. Bump curPuzzle to “Arm

yourself.” It is once again daylight, never to become dark again.

If curPuzzle == “Cat Ballou:”

Fade in on Srini the faithful man-servant and you as Lee Marvin in a brief

cartoon that’s a clear send-up of the Cat Ballou dressing-room-scene.

If you click on the Fast Forward icon at any time during this cartoon, we

jump to “230 West Central Main Street.”

You can get here from anywhere. Enter this scene with screen black, print

“Your outfit complete, you return to your bedroom so Srini can preen you for

battle.” Remove clothes from inventory. Fade in on this scene with you mostly

dressed in your new wardrobe (pants, boots, pistols already on). We watch as

Srini helps you into your fringed shirt, walks off-screen, returns with the silver

ear on a black velvet cushion. You carefully lift the ear from the cushion and

place it on your head. Srini fetches your new hat, jumps on the bed, to carefully

lower it onto your head. There’s a glint of silver as you turn to face him, resplen-

dent in your new-found glory.

Srini wishes you success; you offer him the pharmacy if you don’t succeed

and order him not to reveal your identity by approaching or helping you. Once

you change into that Palomino-colored outfit, there’s no going back to those

somber dark suits. (“Once you go Palomino, you’ll never go back to black!”) This

scene fades back to black, bump curPuzzle to “Card Shark,” then fade up on

you, in your sparkly new outfit, standing outside the saloon.



<a name="br81"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 81

Main Street Interiors

640 Barber Shop

Physical Description

Home base of Salvatore O’Hanohan, the town barber, who never roams far from his

barber chair. He always has an anonymous customer in the chair, so there’s no oppor-

tunity for Freddy to sit down. A back door here leads to “Central Bluff Street” but it’s

hidden behind a wall so it’s not obvious. You can, however, see it reflected in the mirror.

Mirror art: entire back wall must be priority 4, except for actual mirror area, which

is not prioritized. “Glass mark” (those diagonal lines that indicate glass) should also be

priority 4. Then, mirror image characters can be priority 3 and door in mirror can be

priority 2. Programmer and artist must work closely on this scene.

Features

mirror, chair, desk, small mirror, bench, stove, buffalo head, back door (in mirror),

foreground clutter

Props

customer #1, customer #2, customer #3, stove flame, back door (only in mirror),

chair

Actors

Salvatore O’Hanohan, alter Salvatore O’Hanohan, alter ego

Objects Found Here

boots, nitrous oxide

Objects Used Here

claim check, French post cards

Description of Events

Always animate Freddy’s alter ego behind the mirror.

Always animate Salvatore’s alter ego behind the mirror. (No mirror image needed for

the person in the chair as he always stays down.)

If prevRoom == “240 East Central Main Street” Freddy enters from off the lower right

corner of the screen. If prevRoom == “320 East Bluff” he walks in from off the upper

right corner of the stove, and we see alter ego close the door in the mirror.

Upon entrance, the barber always does some business with his customer, in this or-

der: cutting hair, sharpening his razor, shaving the customer, or pulling teeth.

If you click in lower right corner, walk ego off-screen diagonally down and right and

return to street.

If you click the Hand on the door in the mirror, walk Freddy off-screen to the upper

right to show the alter ego in the mirror approaching the mirror door. Open the door,

and walk both out.

If you Talk to the barber:

“I’ve been tryin’ to think up a new way to attract business.” “Oh? What?”

“Dirty readin’ material for ma customers ta read whilst they wait.” “But they’re

illiterate!” you protest. “Yup,” he replies, “and they cain’t read good neither!”



<a name="br82"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 82

If you do anything to the customer, he only mutters something unintelligible.

If you Use the postcards on the barber:

“Your customers may not be able to read, but I bet they would look at pic-

tures!” you say as you hand him your racy French postcards. “Whoa! Tres cool!

But your exceptional generosity must be reciprocated: perhaps I could interest

you in a free shave?” “No, thank you.” “Then, how about a free wisdom tooth ex-

traction?” “Mine are already out.” “Then why doncha take this bottle o’ summa

this new-fangled laughin’ gas?” “Why, thank you, Salvatore. I try to always keep

nitrous oxide around the house!” Barber walks into left foreground, returns, ges-

tures to Freddy, Freddy reaches to accept, add nitrous oxide to inventory, barber

returns to customer.

If you Use the claim check on the barber:

“Do you still have those boots I dropped off for a shine six years ago?” “Yup,”

he replies, “they’ll be ready Tuesday!” Pause. “Never mind, I’ll just take them as

is.” Barber walks into left foreground, returns, gestures to Freddy, Freddy

reaches to accept, add boots to inventory, barber returns to customer.



<a name="br83"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 83

650 Chester Field’s Mercantile Company

Physical Description

Whittlin’ Willie sits by the pot-bellied stove whittling. Chester Field is proprietor of

the General Store, but he’s always working in the back room. He yells things out from

the back room like, “Help yourself, I’ll be right out,” but he never shows. This cuts down

on graphics requirements considerably.

Features

post, horseshoe, shelves, sacks, coffee mill, foreground clutter

Props

fire in stove, door

Actors

Willie

Objects Found Here

whittling knife, empty paper bag

Objects Used Here

clay, wax, medallion (all shown to Willie, but not removed from Inventory)

Description of Events

If you enter here and have both the clay and the wax in Inventory OR you’ve heard

Willie’s lost wax spiel:

There is no Willie here.

His whittling knife is lying on the stove. You can Take the knife.

If you Talk to Whittlin’ Willie, he just makes small talk.

If you Use the silver medallion on Whittlin’ Willie:

do the “ego giving things” loop, show Willie’s “reach out and take things”

loop. Willie then gives clues about the lost wax casting process. Then show his

“reach out and take things” loop again, then “ego giving things” loop. You can’t

leave this room while Willie has your stuff, so don’t change Inventory.



<a name="br84"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 84

660 Mom’s Cafe

Physical Description

If you and the artists can work out the “through the wrinkled glass bottle” effect, do

it.

There is a large tin can of beans on the foreground shelf here that you can take.

ART NOTE: change the far table to a self-service coffee area so ego has a place to

“get coffee.” Add some loops of Mom swatting flies.

Features

tables and chairs, flowers in foreground, tin cans, bottles, counter, glass-front cabi-

net, shelf on far wall, lamp on post, kitchen

Props

steaming horse plop, swinging doors to kitchen, steaming apple pie on back window,

steam and assorted cooking effects in kitchen, flyswatter on rear counter

Actors

Hop Singh, Helen Back, Penelope, various other townsfolk (that aren’t in the saloon),

numerous flies buzzing around for Mom to swat

Objects Found Here

tin can, cup of coffee

Objects Used Here

snails, steaming horse plop

Description of Events

You always enter and exit this scene from the left.

You can’t walk through the swinging doors to the kitchen.

If you click the Hand on the tin can sitting on the foreground shelf, you can Take

the can.

There’s a 1/3 chance you’ll see Penelope sitting in here. If so, use her logics to keep

the conversation flowing.

Helen wanders around, wiping the counter and swatting flies when one flies into her

range and she’s not busy with Freddy or something else.

Keep several flies on Wanders, roaming around the room.

If a fly Wanders into the vicinity of the counter:

Fly it to a random location on the counter, where it stops to rest. Set the fly’s

waitTimer to Random (10, 90) cycles. If the waitTimer expires, the fly takes off

and flies directly out of the counter vicinity, then gets a new Wander.

If a fly lands on the counter and Helen isn’t busy doing something else:

She slowly reaches for the flyswatter, slowly picks it up, slowly raises it into

the air over the fly and instantly drops it on the fly. “Damned flies,” she says.

“This place is like a stable!”

If the flyTimer expires at any time during her sequence, she stops where she

is and returns the swatter to its location.

If you Talk to Helen Back while you have the snails, you promote their sale and

tastefulness to Helen Back, trying to convince her to make escargót a menu staple.



<a name="br85"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 85

If you Use the snails on Helen Back, you give them to her. If you haven’t Talked to

her and given your promotion speech, give it now. (But don’t give it a second time.) She

gratefully accepts and walks to the kitchen “to put them in a bag of cornstarch.” You get

a few points for creativity.

If you click the Hand on the coffee pot against the far wall:

you Take a cup of coffee without paying. “Mom offers free coffee to her regu-

lar customers. You’re as regular as anyone—10 a.m. every morning, you head

straight for the outhouse!”

If curPuzzle > “Madame Ovaree” && the pie hasn’t been taken:

Animate the steaming apple pie cooling on the kitchen window sill.

If you Look at the pie, print “How tempting! Fresh apple pie, still warm from

Mom’s oven. What could be more American?”

If you click the Hand on the pie to Take it, print “There’s no way you can get

into the kitchen to steal anything. Momma don’t allow no pharmacists playing in

there!”

If you Use the steaming horse plop anywhere in Mom’s:

Walk ego to a position where his feet are behind the right table. Animate

through the loop of Freddy slam-dunking the horse plop onto the floor. Set the

horsePlopTimer to 300 ?? seconds. Helen and Hop Singh both get very excited

and angry, speaking lots of clever lines about your relationship to a stable. Hop

Singh rushes from the kitchen with his bucket and brush to clean up the mess.

Before the horsePlopTimer expires, you can go to “500 Mom’s Rear Entry”

and grab the apple pie cooling in the window without getting shot because Hop

Singh is busy cleaning up your mess.

If the horsePlopTimer is running:

Animate Hop Singh out front, scrubbing with his brush and bucket, trying to

clean up the mess you made on the floor when you dropped the horse plop.

Else:

Animate Hop Singh in the kitchen, acting busy via various, randomly se-

lected loops in various, randomly selected locations, for randomly selected num-

bers of seconds.



<a name="br86"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 86

670 The Golden Balls Saloon

Physical Description

Sam Andreas works the bar, various drunks sit around mumbling incoherently, a

tack-piano is in the corner. A tacky piano player always plays a trite collection of fron-

tier music. Bad lighting. A rear door, barely visible through the smoke and haze, leads

to the back alley (“500 Mom’s Rear Entry”). There’s always a poker game playing around

a full table, so there’s no chance of you ever sitting in. The bar is behind the poker game

and has a brass rail. A chandelier hangs over the far edge of the table, perfectly aligned

for later dropping on “Aces’s” head. Ol’ Doc’s whiskey glass sits beside him on the poker

table when he’s in the game. Sign near stage reads, “Round the clock live entertain-

ment! So Baaaah-d, it’s good!”

Features

moose head, piano, each table, poker game, bar, bar’s brass foot rail, stage, picture

window to Main Street, swinging doors, picture over bar

Props

piano player, swinging doors, ricochets for bullets’ points of contact, table (without

poker game), other poker players, Doc

Actors

Sam Andreas, the dancing Sheepettes, chandelier, bullet, Aces, sheriff, Penelope,

others if machineSpeed allows

Objects Found Here

whiskey glass, beer

Objects Used Here

pistols, money, “Prescription under Glass”

Description of Events

If you Look at the sheep while dancing, print “They’re the best you’ve ever herd!”

If curPuzzle < “Corrected Prescription #3:”

Animate Ol’ Doc in the poker game.

If his whiskey glass is still here, place it beside him on the poker table. If you

click the Hand on the whiskey glass, you Take it.

If curPuzzle > “Incoming Aces,” there is no card game here, the tables are in place,

but the chairs are removed. There are no people around either. (They’re all frightened of

the gunslingers outside.)

If you Look at the picture window (Cond):

If it’s broken, print “That window looked better before.”

If curPuzzle == “Rowdy Cowhands,” print “You dare not enter that street.

There’s so many of them and only one (well, okay, 13 counting your bullets) of

you.

Print “You see Main Street through the glass darkly.”

If you Use any of the prescriptions on Doc (Cond):

If he’s asleep, print “Don’t bother him.”

If “Prescription #1” OR “Prescription #2,” print “Yep, I wrote these. Waddaya

think, there’s sumptin wrong wit’ ’em? They look okay to me!”



<a name="br87"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 87

If “Prescription #3,” print “I cain’t read this so good. Mus’ be sumptin wrong

with ma eyes.”

If “Prescription #3 under glass,” print “Wall, lookee here! Why, I musta been

thinkin’ ’bout sumptin else when I wrote this.” (Yeah, and you know what it was,

eh, Freddy!) “Here, jes’ lemme scribble ya out a new’n, and you run right back to

your little pharm'cy and have fun!” Take “Prescription #3 under glass” from In-

ventory and replace with “Corrected Prescription #3.”

If you Use the money on Sam:

Print, “Hey, Sam! Gimme a case of the beer you just got in from St. Louie!”

Walk ego to bar, walk Sam to ego, show ego’s “giving” loop, show Sam’s “taking”

loop, walk Sam off-screen to the left, pause 3 seconds, walk him back to ego, do

his “giving” loop, do ego’s “taking” loop. Add beer to Inventory.

If you Talk to Sam:

you order a drink. Print “Gimme a glass of warm milk.” Gasp soundFX from

the crowd. Print “Well, never mind that. Gimme a sasparilla.” Moan soundFX

from the crowd. Print “Okay, forget that! Gimme a glass of warm beer…” Ahhh

soundFX “…and coat the rim with nose hair!” Big applause soundFX from the

crowd. “Here ya go, pardner!” says Sam. “It’s on the house!”

If you click the Hand on the poker game:

If curPuzzle < “Incoming Aces,” print “There’s no room available in this

game.”

If curPuzzle == “Incoming Aces,” print “There’s no way you can engage Aces

in fisticuffs.”

If curPuzzle > “Incoming Aces,” print “There won’t be a poker game here for

quite a while.”

If curPuzzle == “Card Shark:”

Animate Wheaton “Aces” Hall sitting at the far side of the table in Doc’s old

chair.

Animate Doc in a chair in the corner, trying to sleep it off.

If you Look at Aces or the poker table, cut to “The Poker Game” below. You

can return from there either by choice or under duress (see below).

Animate Penelope standing somewhere near the poker game so she can run

up to ego and congratulate him after he has Aces arrested.

Animate as many of FPFP’s main characters as machineSpeed will allow scat-

tered around the room, just watching the action. Everything else in town is

closed.

If prevRoom == “The Poker Game C. U.” && you Used your gun on Aces:

we see you standing with your gun drawn, aimed at Aces, but you are

frozen in place. The Sheriff stands beside you. He arrests for attempted

murder. “You had no cause to draw on a poor, defenseless, unarmed man

like Mr. Hall!” EndGame.

If curPuzzle is “Incoming Aces” and prevRoom == “The Poker Game C. U.:”

You are under extreme duress! We see you dive beneath the left table as Aces

fires at you and misses. You tilt up the table as you fall to protect you from

Aces’s guns. All the other men in Aces’ poker game also exit quickly, each in a

unique, humorous way. Piano player changes music. “Yah hoo, boys! Kin we



<a name="br88"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 88

have another Old West saloon brawl, Sam?” “Hail, no! I ain’t finished makin’ the

payments on the last one yet!”

Now, Aces has his gun aimed directly at you but you’re protected by the

heavy wooden table. He also blocks your way to both doors. Why doesn’t he get

up and walk around to kill you. (He’s just lazy.)

If you fire your gun anywhere East of your table:

We watch you rise above the table to shoot, but before you can, Aces

shoots you every time. EndGame.

If you fire your pistol West of the table:

If you miss the “magic” spot:

You do not rise up, but rather, shoot sitting down. We watch

as you fire, see the bullet hit the spot you aimed at, then ricochet

around the room, with sampled soundFXs, bouncing off things

until it finally strikes an innocent bystander. Each shot kills a dif-

ferent, wrong person who dies a funny, creative death. After each

wrong shot, you get an “Oops” dialog about your mistake, with a

“Rewind” button. You must click “Rewind” (you have no other

choice). We then see the animation in reverse, the bullet’s ricochet

path traced right back to your gun barrel, while sampled

soundFXs play in reverse. Thus, players can keep trying shots

until they find the “magic” spot.

Else:

When they do find the correct small spot on the bar’s foot rail,

the bullet ricochets many, many times following an exaggerated,

convoluted route, but eventually it clips the chain holding up the

chandelier, which drops directly onto Aces (shakeScreen), the pe-

rimeter of the circle wrapping completely around him immobi-

lizing him, trapping him with his third hand clearly revealed.

Print a few messages about how you summon the sheriff, who en-

ters immediately. You expose the fake third hand to Sheriff

“Chicken Shift” who has no choice but to arrest “Aces” for cheat-

ing, so he does. Print a few messages mentioning how you “dis-

armed” him. Walk Sheriff and Aces out together, headed for jail.

Walk Penelope over to you to congratulate you. (The bitch!) No

kissing, hugging, or PDA, though it enters your mind. Walk Pene-

lope out the front door. Change piano player music to calm.

Bump curPuzzle to “Rowdy Cowhands.” Start “Rowdy Cowhands”

soundFX softly in background. Mention they are outside. Return

playerControl.



<a name="br89"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 89

675 The Poker Game C. U.

Physical Description

We only get to this screen when this puzzle’s pokerTimer is running. This is a first-

person view of the poker game. You are not in the game. You can leave this screen by

clicking the “Exit” icon (where the Walker icon usually is). “Aces” Hall sits in the far

chair, where Doc sat, winning consistently.

Occasionally, a third hand flashes subtly on screen for just one cycle.

Features

stacks of money, Aces’ body, hat, card in hatband

Props

Aces’ hands (3), cards, smoke from cigar in ashtray on table, eyes, moustache,

mouth, coins, pot, other players’ hands (occasionally)

Actors

cards, coins

Objects Found Here

Objects Used Here

guns (to no avail)

Description of Events

If you Look at Aces, print “Wheaton “Aces” Hall, slick big-time, back-East, riverboat

gambler, has turned the saloon’s friendly poker game into vicious high-stakes gambling,

winning money, land, buildings, and businesses from the local bumpkins.”

If you Use the gun on Aces, we cut back to the “Saloon Interior” above, see you with

your gun drawn frozen in place, the Sheriff standing beside you. He arrests for at-

tempted murder. EndGame.

If you click the Hand on Aces’ extra hand while it’s on-screen:

Erase the hand. Print “He’s cheating! That’s a fake left hand! His real hand is

hidden under the table!” His response is, “Why, yes, silver-eared stranger! You’re

correct! But I have no cards in my left hand. I only have this…” He slowly raises

his left hand from his lap, revealing his pistol aimed directly at you! “Turn

around, Slick!” he growls. “I think I’d rather shoo' cha in the back so I don’t

havta see that ugly face of yours!” We then return to the normal “Saloon Inte-

rior” above to watch you turn around and dive beneath the nearest table.



<a name="br90"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 90

680 Whiskey Glass Close-up

Physical Description

You can come here from nearly anywhere, when you click the whiskey glass on Pre-

scription #3 in the Inventory window. You move the glass around above the pre-

scription, until the correct prescription is clearly legible.

Features

prescription

Props

Actors

moving glass

Objects Found Here

“Prescription #3 Under Glass”

Objects Used Here

whiskey glass, Prescription #3

Description of Events

You move the glass around above the prescription, until the correct prescription is

clearly legible. When it is, remove the whiskey glass and Prescription #3 from Inventory

and replace with “Prescription #3 Under Glass.” Return to previous location and condi-

tions.



<a name="br91"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 91

690 First Bank of Bob

Physical Description

It looks like Bob’s drawing! P. H. Balance is the only person working in the bank,

ever. Penelope comes in occasionally.

Features

table, plant, vault door, cages, lamps, clock, settee

Props

vault door, lamp flames, clock pendulum

Actors

PH Balance, Penelope (random 1/3)

Objects Found Here

none (guns & neckerchief found inside safe deposit box)

Objects Used Here

safe deposit box key

Description of Events

There is a random 1/3 chance of meeting Penelope in the bank. If she’s there, use

her logics to keep track of whatever conversations you two have had.

If curPuzzle < “Sheriff shutdown:”

PH just makes “small talk” about their new Columbus Day (Halloween, Palm

Sunday, etc. always different), non-interest-bearing passbook savings accounts.

If curPuzzle >“Sheriff shutdown:”

PH gives you a “come on; sell out to me” pitch which escalates through mul-

tiple “sell out” lines.

If you click the money on PH:

He takes it from your Inventory and “keeps it safe in your Christmas Club

account.”

If you click your safe deposit box key on PH:

If he hasn’t given you the first “come on; sell out to me” pitch, he does.

Fred stands in place. PH walks to the vault, works the combination, opens

the giant vault door, walks inside, returns with your safe deposit box, places it

on the table and returns to his desk.

If the safe deposit box is on the table and you click the Hand on it to open it:

Cut to “700 Safe Deposit Box C.U.” below…

If prevRoom == “700 Safe Deposit Box C.U.:”

Under programControl, you summons PH, announce “I’m all done now.”, he

takes the box from you, returns it to the vault, closes the vault door, spins the

lock with a flourish, walks back over to you, hands you the key, and “Thank you

for using The Bank of Bob.”

Small talk with PH must mention Bob.



<a name="br92"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 92

700 Safe Deposit Box C.U.

Physical Description

A C.U. of the closed safe deposit box. You can open the box to reveal your “lucky

neckerchief” wrapping something. You can open the neckerchief to reveal your brace of

“gunslinger pistols.” You reminisce about your memories of them.

Features

guns & holster, neckerchief

Props

guns & holster, neckerchief

Actors

Objects Found Here

guns, neckerchief

Objects Used Here

Description of Events

If you click the Hand on the lid:

If it’s closed, it opens.

If it’s open, it closes, and we return to the Bank Interior, above.

If you click the Hand on the neckerchief:

If it’s closed, it unfolds to reveal your pistols.

If it’s open:

If the guns are there, the neckerchief folds back over the guns.

If the guns are gone, you Take the neckerchief.

If you click the Hand on the pistols, you Take them.

You can leave by closing the box lid with the Hand or by choosing “Exit.” You don’t

have to take the pistols or the neckerchief, but you’ll need ’em both eventually. You can

come back and get them later.

Also handle returning the pistols and neckerchief to the box.



<a name="br93"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 93

710 Sheriff’s office

Physical Description

We’re peering in the front window, looking through the bars at the tiny office and jail

with its one cell. There is nothing inside here you can take. You can never enter unless

the sheriff is here. Face of clock has reflections blocking view of hands (since they never

move).

Features

bars, cell, hat & coat on coat rack, desk, gun rack

Props

sheriff, clock pendulum

Actors

Objects Found Here

ammunition, gun cleaning kit

Objects Used Here

coffee, apple pie

Description of Events

Whenever this scene is accessible, we see the sheriff sitting at his desk, in his desk

chair. He has some “fidget” code to keep him from looking like a statue.

If you Look at the sheriff, print “Shh! He’s trying to invent “coffee and donuts.””

If you try to Take anything in this room, the sheriff corrects you, “Git chur hands of-

fen that, boy! You got no bizness fingerin’ stuff in here!”

If you Use the coffee on the sheriff:

Remove the coffee from Inventory.

If you have NOT given him the apple pie previously:

Add the ammo to Inventory. Print “Thanks, pardner! But, cha know

what? Sumptin sweet would shore taste good right now!” “Why, I bet

that’s true. I’ll be glad to try and find you something to munch on. But,

in the meantime, I’ve been thinking about moving to another city. But,

I’ve got no bullets. I was wondering if you have any bullets that would fit

an old.45?” “Whey, shore, son. Here. Have a box o’ these Remingtons! No

charge; they’re on the County!”

Else:

Add the gun cleaning kit to Inventory. Print “Thanks, pardner! This’ll

shore go good wit’ dat apple pie ya gave me!” “You are most welcome,

Sheriff. Say, you wouldn’t happen to have a spare gun cleaning kit,

would you? These old pistols of mine are dirty as sin!” “Okay, son. But

this gun cleanin’ kit’ll be the last thing I give ya. Now git chur pistols

cleaned, git chur stuff packed up and git chur ass outta town!”

If you Use the apple pie on the sheriff:

Remove the pie from Inventory.

If you have NOT given him the coffee previously:

Add the ammo to Inventory. Print, “Whey, thank cue! I bin so hongrey

I coulda et a bear! But, do ya think I could git a cuppa coffee to go with



<a name="br94"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 94

this?” “Why, sure, Sheriff. But, in the meantime, I’ve been thinking about

moving to another city. But, I’ve got no bullets. I was wondering if you

have any bullets that would fit an old.45?” “Whey, shore, son. Here. Have

a box o’ these Remingtons! No charge; they’re on the County!”

Else:

Add the gun cleaning kit to Inventory. Print, “Whey, thank cue! I bin

so hongrey I coulda et a bear! This’ll shore go good with that cuppa coffee

ya brung me earlier!” “Uh, Sheriff? Do you have anything I could use to

clean these old guns of mine before I leave town? They’re mighty dirty

and I want to be prepared for my long journey!” Print “Okay, son. But

this gun cleanin’ kit’ll be the last thing I give ya. Now git chur guns

cleaned, git chur stuff packed, and git chur ass outta ma town!”



<a name="br95"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 95

The Schoolhouse

720 Schoolhouse Interior

Physical Description

You can only be in this scene at the end of FPFP, after Kenny the Kid shoots you in

the street. You enter from outside under programControl to find Penelope standing near

the stove blocking your way to the stage. You can not leave. Entrance not visible on-

screen.

Stage in front of classroom with desk to left and door to basement on right. Civil

War bulletin board display. Swords above chalkboard. All desks are identical, except the

desk nearest Freddy when he enters; it has a student slate lying on it.

Features

blackboard, desk, flag, desks, slate, stove, swords, windows, lamps, foreground clut-

ter

Props

basement door, his & her swords, student slate, misc. gunfire

Actors

Penelope, flying Derringer, flying ear, Kenny

Objects Found Here

slate, sword

Objects Used Here

slate, sword, sharpened silver ear

Description of Events

If curPuzzle == “schoolhouse showdown:”

If you click the Hand on the door to the basement, print “There’s no use try-

ing to escape to the basement!”

If localPuzzle < “Derringer:”

We begin with a little cartoon. You walk in, stopping halfway to the

stove. She turns to you and says, “Ooooh, stranger! I’ve been hoping

you’d pay me a visit ever since I watched you beat Aces back at the sa-

loon. How did you know leather chaps with silver accessories excite me

so?” As she breathes faster and heavier, she begins to unbutton her bod-

ice while you stand amazed, confused, but not disinterested. Perhaps

clothes do make the man, eh Freddy?

Wrong. It’s merely a ploy! From her bodice, she whips out… a Derrin-

ger and aims it directly at you! “Drop ’em,” she orders, with a meaning

completely different from what you had expected a moment ago! At this

point we start a 20” ultimatumTimer, bump localPuzzle to “Derringer,”

and return to playerControl.

If localPuzzle == “Derringer:”

Keep the ultimatumTimer running. If the timer expires before you

drop your guns, show her fire, you collapse to the floor. Bang, you’re

dead. EndGame.



<a name="br96"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 96

If you click the Hand on her, print “There’s no way you’ll be able to

grab her gun before she can pull the trigger.”

If you Use your guns on her:

Begin Freddy’s “draw gun” animation. But before he can get

his gun out, she fires. Bang, you’re dead. Freddy collapses to the

schoolhouse floor. EndGame.

If you Use any other Inventory object:

It just makes her mad. Show her fire, show you collapse to the

floor. Bang, you’re dead. EndGame.

If you click the Hand on the slate before lowering your guns:

Penelope says, “When I say ‘Drop ’em,’ I mean ‘Drop ’em!’” as

she shoots. Bang, you’re dead. Freddy collapses to the school-

house floor. EndGame.

If you click the Hand on your guns in the Inventory window:

Print “Sometimes discretion is the better part of valor!” Show

Freddy unbuckle his belt and his guns drop to the floor. Start a

20” gunsOnFloorTimer, bump localPuzzle to “guns on floor.”

If localPuzzle == “guns on floor:”

Keep the gunsOnFloorTimer running. If the timer expires before you

grab the slate, Penelope cries, “Sucker!”, show her fire, show you collapse

to the floor. Bang, you’re dead. EndGame.

If you click the Hand on the slate after lowering your guns:

You automatically raise it to protect your heart as she auto-

matically fires her one and only bullet. (You don’t have to “Use the

slate,” although you can; you just need to Take it to be protected.)

Her bullet shatters the slate, usurping its energy. In its dissi-

pated state, it bounces off your chest without harming you. You

bend over to pick up your guns and as you do, Penelope hurls her

now useless gun, scoring a direct hit on your head, knocking you

out. We fade to black as you crumple in a heap on the floor, un-

conscious, but not shot.

Bump curPuzzle to “trapped in the basement,” print a few

messages, and go to “730 Schoolhouse basement” below.

If curPuzzle == “sword fight:”

If you click the Hand on the door to the basement, print “You have no desire

to return to a place that’s about to explode!”

After you’ve escaped from the basement, you return here to find Penelope

packing. You enter up the stairs, close the basement door behind you, turn to

face Penelope and announce, “Justice will be done, madam!” “I knew I shouldn’t

have wasted my time packing these ‘cum’ folders!” she says. Penelope grabs a

saber from the Civil War lesson display on the wall beside her, bumping local-

Puzzle to “en garde.”

If localPuzzle == “en garde:”

She slowly advances toward you.

If you fail to grab the other saber before she gets to you:



<a name="br97"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 97

She “runs you through,” we see you collapse, you die again.

EndGame. “Shish-kabobs, anyone?” “Get your mind out of the

skewer!”

If you click the Hand on the other saber:

Show Fred reach up, take saber as Penelope backs up until

she is again behind the desk. Add it to Inventory and make

curObject automatically. When she is behind the desk, she tosses

her saber high into the air while doing a Ninja-schoolmarm one-

armed cartwheel across the desk to the floor in front of the stage,

catching the sword as she assumes the classic “en garde” posi-

tion. “Did I forget to mention downstairs that Meadville Normal

had the nation’s first female fencing team?” she says.

We automatically walk you to the front of the stage, where you

trip stepping down. You also assume the “en garde” position.

Bump localPuzzle to “swordfight” and begin the fighting.

If localPuzzle == “swordfight:”

You are both always on the floor.

If you try to move on the stage or down-screen towards the stove:

Revert to a “walking with sword held lamely downwards” view.

Penelope presses forward quickly, runs you through. EndGame.

If you fail to press forward:

Penelope “runs you through,” we see you collapse, you die

again. EndGame. “Shish-kabobs, anyone?” “Get your mind out of

the skewer!”

If you push her back far enough:

“Say, Freddy. You’re not bad!” “So much for Title 9 sports,

Penelope!” Stirring music! She trips, falls on her back, as you

slash her saber from her hand! As you stand above her, your sa-

ber aimed at her chest, you ready for the kill when we hear

“Kenny’s soundFX.” You pause, look in the direction of the

schoolhouse door as in walks… Kenny the Kid! Bump localPuzzle

to “Kenny entering” and freeze ego and Penelope in place.

If localPuzzle == “Kenny entering:”

Ego is frozen in place, staring at Kenny. Penelope, with the sword to

her chest, doesn’t do much either. He arrives, stops short of the stove,

and we bump localPuzzle to “Kenny talking.”

If localPuzzle == “Kenny talking:”

Since you’re no longer wearing your silver ear, he recognizes you! He’s

too surprised to shoot right away. “Why, it’s you! From the old neighbor-

hood. Freddy!” “Good to see you again, Kenny. I hope I didn’t hurt your

hand out there in the street.” “Whoa! That was you, out there? I didn’t

recognize you. Have you done something with your hair?”

If, by this point in his revelation exposition, you haven’t clicked the

silver ear on him, he says, “It’s funny, Pharkas! I thought I killed your

sorry ass back in Pecos!” as he shoots. Bang, you’re dead! EndGame.

If you do click the silver ear on Kenny during the pauses between

speeches:



<a name="br98"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 98

Rush through Freddy’s and Kenny’s lines, “Good to see you

again, Kenny. I hope I didn’t hurt your hand out there in the

street.” and “Whoa! That was you, out there? I didn’t recognize

you. Have you done something with your hair?” Freddy now re-

plies, “Not my hair, Kenny, but with THIS!”

Show Freddy keep his saber aimed at Penelope’s chest, reach

inside his shirt with his left hand and fling the silver ear across

the room, directly into Kenny’s jugular vein! Even more-stirring

music! Kenny says, “Freddy Pharrrrrrggggh!!” and falls to the

floor.

Print a congratulatory message, then show Fred turn again to

Penelope as we cut to “740 Penelope C.U.” below.

If curPuzzle == “end game cartoon:”

Show Fred’s sword lying beside Penelope’s body. Crank gameSpeed as fast as

possible (aniInterval of 0 or 1 ??), show him quickly walk past the dead Kenny,

and cut to “750 “Lethal Weapon” Schoolhouse” below.



<a name="br99"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 99

740 Penelope C.U.

Props

about 7 slashes

Only shown as part of end of game cartoon. Penelope is wearing a bodice perfectly

suited for slashing an “Rx” into. Print “Without thinking, you quickly slice “the sign of

the Rx” into her quaking bodice!” Animate the slashes in order. Pause a moment. Print

“Suddenly you remember, “The OIL!.” Bump curPuzzle to “end game cartoon” and cut

back to “720 Schoolhouse Interior” above.

750 “Lethal Weapon” Schoolhouse

Dramatic close-up of Freddy flying through the air Mel Gibson-style from the

schoolhouse porch. Center the open doorway on the screen, so we can do a center-out

showStyle to the “760 Explosion” pic below.

Only shown as part of end of game cartoon. Preload 760.p56 and the huge explosion

soundFX. Display 750.p56, start the soundFX, showPic 760.p56 with center-out show-

Style, then immediately fade to black. Print a few “wrap up the game” messages and go

to “170 Closing cartoon” below.

760 Explosion

Can come here from Lab Screen or Schoolhouse explosions. Cartoon-y boom screen.

Huge soundFX. Fade to black. EndGame. Another Dead Fred. “That’s you all over,

Freddy!”



<a name="br100"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 100

730 Schoolhouse basement

Physical Description

Dirt floor. Dark, dank. A large stone column (but not as large as it was originally

drawn) in the center of the basement holds up the floor above. A lantern rests on the

stairway post. A stream of oil runs from near the stairs to a big pool of oil in the left

front corner.

You only get here under playerControl during the closing schoolhouse sequence. We

fade in from black to find you sitting in a wooden chair, completely tied up, with rope

wrapped around and around your body from ankles to neck, with your arms completely

immobilized at your sides, and just your hands protruding at the wrists. Penelope

stands beside you.

Features

pool of oil, trail of oil, stairs, pillar, books, old piano, column, foreground clutter

Props

oil pool bubbles,

Actors

Penelope, silver ear, burning lantern, Mr. Flame-O

Objects Found Here

silver ear

Objects Used Here

silver ear

Description of Events

The lantern burns on the stairway post. Oils bubbles bubble in random locations at

random intervals in the foreground oil. Rats scurry about in the dark corners (or at

least blink their eyes).

The first part of this scene is the motivation-explaining cartoon:

Penelope stands before you. “Now, we’ll just find out just exactly who you

are, Mr. Gunslingin’ Stranger!” she cries, dropping her final G as she rips your

silver ear from your head and flings it to the floor. “FREDDY! You?!” A conver-

sation ensues.

You ask her why she’s done all this. She reveals her back story. “I had just

finished my education back in western Pennsylvania at the local Meadville Nor-

mal School when I saw a small ad on the school bulletin board seeking teachers

‘for a lovely little village, way out West.’ I wrote a letter of inquiry and was offered

the position sight-unseen by the Coarsegold Board of Education. They even sent

me stagecoach fare! Soon after my arrival (which you saw in the Prologue, I be-

lieve), I noticed the oily swamp behind the schoolhouse. Being a good Pennsyl-

vania oil country girl, I grasped immediately that Coarsegold was literally oozing

money! But I could never afford to buy mineral rights on the meager pittance

they pay a single unwed female teacher, so I made a little arrangement with the

Mr. Balance. He foreclosed the mortgages he could, and convinced the sheriff to

shut down the others. P.H. would get the land and buildings for a song and give

me the mineral rights I wanted, as long as I gave him what he wanted!”

You are aghast. Penelope walks to the stairs. “But Penelope! To me you’ve

seemed to be a sweet innocent young woman. How could you be such a sleaze?”

She climbs to the landing. “It was easy, Freddy. But don’t feel too superior. Re-



<a name="br101"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 101

member—you weren't too noble upstairs! But, please: don’t spend the rest of

your life worrying about me.”

“Oops! How clumsy of me!” Penelope says mockingly, just before she knocks

the lantern off the post into the stream of oil. Show the lantern tumble to the

ground, burst in the oil, and catch it aflame. AddToPic a cel of the broken lan-

tern crashed on the floor. Convert the lantern into the flame and move it slowly

along the oil trail, flickering its way across the room like a giant fuse.

“Oh, well. Coarsegold could use a new schoolhouse!” Penelope moves up-

stairs. As she disappears from the cast list, she says, “…And a new pharmacist!”

We return to playerControl with you trapped in the basement, tied securely

to a chair, with the classic “fuse to the dynamite” burning away.

If you click Exit while tied to the chair, print “Exiting this basement is an excellent

idea. Your problem is how!”

If you click on Inventory while tied to the chair, don’t bring up the normal Inventory

window. Instead, print “You are unable to use your Inventory since you tied up.”

If you Look at the column, print “The column and basement walls are built from lo-

cal granite, rough-hewn and sturdy enough to last for hundreds of years.”

While Fred is tied to the chair in sitting position:

If you click the Hand on the fallen silver ear, print “You are unable to reach

your ‘disguise’ while bound to that chair.”

If you click the Hand on ego while he’s sitting still:

Rock ego back and forth on his chair, using the same Cycler as the

schoolyard swing. Go one cel each way for a few loops, back and forth,

stopping with him at center.

If you click the Hand on ego while he’s rocking back and forth:

If you click while he’s rocking “in” (i.e., lastCel was farther from cen-

ter cel):

He rocks a little less and stops sooner.

If you click while he’s rocking “out” (i.e., lastCel was closer to center

cel):

He rocks a little more.

When he gets up enough momentum to fall over, freeze on his

most extreme cel to the west for a few cycles, then cycle all the

way over the opposite direction to the most extreme cel to the

east. Make him hover in place for a few cycles, print “Watch your

head, Fred!” then crash him to the ground with his head almost

touching the stone column. “Whew! That was a close one. But

now what are you going to do?” Now he’s tied to the chair in the

downed position.

While Fred is tied to the chair in the downed position:

If you click the Hand on the fallen silver ear:

Print “He walks… he talks… he…” and show him wriggle on his belly

like a reptile until his left hand is beside the fallen silver ear. (His head

disappears behind the stone column in the process.) He Takes it and it

automatically becomes the currently selected Inventory object. (Clicking

Inventory still gives the “tied up” message above.)



<a name="br102"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 102

If you Use the silver ear on yourself, print “You have no need to disguise

yourself, now, Freddy. She knows who you are!”

If you Use the silver ear on the stone column:

Show him wriggle again, so his hands are beside the column, then

show him rapidly rub the ear back and forth on the rough rock to

sharpen it. Print “It’s a good thing silver is so soft. It sharpens easily on

these rocks.” Change curObject to “sharpened silver ear.”

If you Use the now-razor-sharp silver ear on yourself:

We see you saw away for a while, finally cutting through the ropes, a

quick loop of cartoonish blurs to cover removing the ropes, and you

stand up, a free man. You then run up the stairs under programControl.

Bump curPuzzle to “sword fight” and cut to “720 Schoolhouse Interior”

above.

If at any time during this scene the moving flame reaches the large pool of oil, im-

mediately cut to “760 Explosion” above. EndGame. Another Dead Fred.



<a name="br103"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 103

Closing Sequence

170 Closing Cartoon

The Epilogue begins with the same sepia-toned Pharmacy exterior pic that served as

background for the ballad in the opening, with the text, “Epilogue—Go Rest, Young

Man” overlaid. It recapitulates “The Ballad of Freddy Pharkas” with a few more cho-

ruses that wrap up our loose ends. We see just a few quick vignettes this time: the

burned-down school (“…although her body was never found…”); the banker tarred and

feathered (“…Hey, I don’t have to put up with this. I think I’ll invent savings and

loans!”); Srini in a Native American setting and dress but still wearing his turban (“…his

training let him become an Indian medicine man…”); and townsfolk abuzz with talk

about the incident (“…our protector,” “…will he ever return?” and “Who in the hell was

that weirdo with the silver ear?”); and you, smiling knowingly. Then the sepia pic dis-

solves into…

175 Closing L.S.

…which shows how different Coarsegold now is. The town is now all bright colors

and activity, the schoolhouse has been rebuilt into a large two-story city school, the

railroad tracks are complete and shiny, the former Chinatown is filled with oil derricks

pumping away, and we see a large metal software building at the right edge of the

screen. (We don’t fly back to Half Dome.) We dissolve to…

180 Closing Credits

Freddy on horseback, on top of Half Dome, with the sun setting behind him. His

horse rears up, and as he waves his hat, we freeze the action and dissolve to a sepia-

toned version of the same pic as the closing credits float upward to dramatic “How the

West Was Won” music. Fade that screen’s palette, do the “whip crack” animation to a

random location on the screen, at which point the next credit appears. Reuse the same

credit views from the game’s opening.



<a name="br104"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 104

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Map



<a name="br105"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 105



<a name="br106"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 106

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Resources

Lines

Wells Cargo stage line driver says, “I’ll do anything for a career on the stage!”

Hero bit by rattler. Srini says, “The Doc says you’re gonna die, Kemosabe!”

“How come you never get hit by those bullets?” “It’s my karma, I guess!”

“You know, she just doesn’t get into the ’hole’ thing!” “Of course not! I gave up

that life!!”

“He wears a ’silver REAR??” “That’s EAR, stupid!”

“I won a merit badge in gun slingin’.”

“I’m going INTO the closet!”

“It smells like he stepped in the cowslip again!” (cowslip tea, oil of cowslip, es-

sence of cowslip)

“Why does that stage coach have only 2 horses?” “I feed ’em oats laced with re-

fried beans!” “You mean…” “Yep—‘turbo-charged!’”

Anachronisms

“Wait until all this is an enclosed, air-conditioned shopping mall and amusement

park.”

“I have a dream! Someday all this will be paved with concrete!”

“Lawyers will control the new West.”

“I see men talking on telephones without any wires!”

“I think I’ma gonna call it ‘bungee jumping’!’”

Western phrases

by gum, by golly, by crackie, by jingo, dad gum it, I reckon, consarn it, candy ass, piss-

ant, cow-lickin’, horn suckin’, bush wackin’, side windin’, horn swagglin’, lilly-livered,

scum suckin’, varmint

Indian Tribes

Apache, Arapahoe, Blackfoot, Cheyenne, Chickasaw, Chinook, Chippewa , Choctaw,

Comanche, Creek, Crow, Hopi, Hupa, Kiowa, Navajo, Nez Perce, Osage, Paiute, Papago,

Plains Indians , Pomo, Seminole, Shoshone, Sioux, Ute, Yaqui, Yurok, Zuni

Historic Places

Carson City, NV, Colorado Territory, Comstock Lode, Deadwood, SD, Dodge City, KS,

Fort Laramie, Homestake Mine, SD, Jackson Hole, Laramie, WY, Montana Territory,

Promontory Point, UT, Sacramento, CA, San Francisco, CA, Virginia City, NV

Geographic Features

Black Hills, Chisholm Trail, Death Valley, Donner Pass, Little Bighorn River, Oregon

Trail, Santa Fe Trail, Trail of Tears

Historic Events

Custer's Last Stand, 1876

driving of the Golden Spike, 1869

Lewis & Clark expedition, 1803-1806



<a name="br107"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 107

People/Animals

bronc buster, buckaroo, buffalo (bison), cardsharp (cheater), chuck-wagon cook (cookie),

cowpuncher, coyote, crack shot, desperado, dogie (stray calf), drover (cattle

driver/sheep driver), dude, gold prospector, gunslinger, half-breed, hired gun, hombre,

horse thief, jackass, madam, maverick (unbranded calf), medicine man, mountain man,

mustang, old-timer, outlaw, pack horse, pack mule, pack train, paleface, Palomino, pa-

poose, prairie dog, prospector, prospector's mule, roughneck, rustler, saddle horse, sa-

loonkeeper, schoolmarm, scouting party, sharpshooter, stagecoach driver, team of

horses, team of oxen, tenderfoot

Things & Places

blasting powder, breeches, brothel, buckboard, buckskin jacket, buffalo chips, buffalo,

robe (carriage robe or rug), bunkhouse, calico dress, canyon, chamber pot, chuck

wagon, cigar store Indian, circle of covered wagons, Conestoga wagon, corral, covered

wagon, cowboy boots, cowboy hat, dance hall, deadman's hand (poker hand), diggings

(digging or mining site), dried beans, dry-goods store, dusty street, false front on a

building, feather bed, fiddle, firewater (liquor), flapjacks, gambling hall, general store,

gingham, grub (food), guitar, gunbelt, gunpowder, hangman's noose, holster, honky-

tonk, kerosene lantern, lariat, livery stable, locoweed, long johns, moccasins, necker-

chief, outhouse, peace pipe, pelt (untanned animal skin), poncho, promontory, saddle-

bags, saddle, sagebrush, saloon, sarsaparilla (beverage), sawdust floor, sidesaddle,

sleeve garter, snake oil, spittoon, Stetson hat, string tie, sunbonnet, swinging doors,

telegraph, opera house, tintype photograph, tomahawk, totem pole, train depot, wam-

pum, wagon train, WANTED: Dead or Alive poster, water trough

Verbs

bite the bullet, bite the dust, deal from the bottom of the deck, die with your boots on,

have an ace up your sleeve, herd animals (verb), hit pay dirt, hobble (fetter/limit),

hornswoggle, hunker down, palm a card, shoot an injured horse, shoot at person's feet

& say DANCE!, shoot to kill, sign your name with an X, stack the deck, up the ante

Activities

barroom brawl, branding, bronc busting, calf roping, cattle rustling, gunplay, hoedown,

horse-stealing, lariat twirling, medicine show, poker (card game), roundup (cattle drive),

shoot-out, showdown (poker hands faceup), stampede, trick riding, trick roping

Descriptors

armed to the teeth, bareback, highfalutin, on the warpath, railroaded, ridden out of

town on a rail

Famous/Fictional Westerners

Annie Oakley, Antonio Lopez de Santa Anna, Babe the Blue Ox, Bat (William Masterson)

Masterson, Belle Starr, Billy the Kid (William H. Bonney), Black Bart (Charles E. Bol-

ton), Brigham Young, Buffalo Bill (William F. Cody), Butch Cassidy & the Sundance Kid,

Cochise, Crazy Horse, Dalton gang, Dangerous Dan McGrew, Daniel Boone, Davy

Crockett, Doc (John Henry Holliday) Holliday, Donner party, General George Armstrong

Custer, Geronimo, Henry Plummer, Hopalong Cassidy, Frank James, Jesse James, Jim

Bowie, Jim Bridger, John C. Fremont (The Pathfinder), John Colter, Joseph (Nez Perce

chief), Judge Roy Bean, Kit Carson (Christopher Carson) , Lewis and Clark (Meriwether

and Wm), Lillie Langtry, Lola Montez, Lone Ranger, Mangas Coloradas, Marcus A. Reno,

Nat Love, Pancho (Francisco Villa) Villa, Paul Bunyan, Pecos Bill, Red Cloud, Red Ryder,

Sacajawea, Sam Bass, Sam Houston, Sheriff Matt Dillon, Sheriff Pat Garrett, Sitting

Bull, The Outlaw Josey Wales, Tonto, Wild Bill (James B. Hickok) Hickok, Wyatt Earp,

Yosemite Sam, Zebulon Pike, Zorro



<a name="br108"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 108

Western Songs, Movies, TV Shows

(I’m Headin for) The Last Roundup, Blazing Saddles, Blood on the Saddle, Bonanza,

Bury Me Not on the Lone Prairie, Butch Cassidy & the Sundance Kid, Cat Ballou, City

Slickers, Cool Water, Custer's Last Stand, Dances With Wolves, Deep in the Heart of

Coarsegold , Don't Fence Me In, Ghost Riders in the Sky, Gunsmoke, Hang 'Em High,

Happy Trails to You, Have Gun Will Travel, Home on the Range, How the West Was

Won, I'm an Old Cowhand (from the Rio Grande), Life & Times of Judge Roy Bean, Little

Big Man, Lonesome Dove, Maverick, On The Trail of the Lonesome Pine, Paint Your

Wagon, Ragtime Cowboy Joe, Rawhide, Red River Valley, Ridin' Down the Canyon, She

Wore a Yellow Ribbon, Shenandoah, Silverado, Stagecoach, Streets of Laredo, The Big

Sky, The Good, The Bad, and the Ugly, The Lone Ranger, The Outlaw Josey Wales, The

Perils of Penelope, The Rifleman, The Shootist, The Sons of Katie Elder, The Train Rob-

bers, The Unforgiven, True Grit, Tumblin' Tumbleweed, Yippee-Oi-Vey, Young Guns



<a name="br109"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 109

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_Documentation

The following lines in boldface are for information only. Bury the following infor-

mation in similiar-sounding spurious bullshit.

Instructions for preparation of “Medication #1”

Tyloxapolynide

effective aid in treatment of the vapors. Available from D. B. Aze & Sons, Baltimore.

Pepticlymacine Tetrazole

effective aid in treatment of the vapors. Available from Furnette Formulas, Cin-

cinatti. Pepticlymacine Tetrazole is an acceptable substitute for Tyloxapolynide.

Instructions for preparation of “Medication #2”

Quinotrazate

To 12 ccs of Bismuth Enterosalicyline, add 30 gms of Phenodol Oxytriglychlorate to

produce enough Quinotrazate to make 4200 mgs. Mix together in a glass beaker. Stir

the mixture well using only a pure clean glass rod. Process into pill form. Recommended

dosage, NTE 60 mgs/day.

Instructions for preparation of “Incorrect Medication #3”

Testosterate

25 mgs of Testosterate powder administered orally twice daily will add masculinity

to the lightest male.

Preparation: Combine 8 ccs of Phenolsulphonphthalein Enteromagneline powder

Instructions for preparation of “Correct Medication #3”

Estrosterane

25 mgs of Estrosterane powder following marital relations aid in the prevention of

undesirable future side effects.

Preparation: Grind 100 mgs of Bimethylquinoline crystals and 50 mgs of powdered

Metyraphosphate in a mortar. Prepare 1 cc dosages on pure sheets of medicinal dis-

pensing paper. Recommended maximum dosage: 1 box of six.

Instructions for testing the bag of Horse flatulence

Spectroscope, gaseous, (spek’ tra skop’), n. an optical device for producing and ob-

serving a spectrum of light or radiation from any source, consisting essentially of a slit

through which the radition passes, a collimating lens, and an Amici prism. The follow-

ing photographic tin-types reveal various contents:

hydrogen

oxygen

(place simulated b&w spectra photos here)

carbon

carmel

meaty by-products

lentils

Instructions for preparation of Horse Deflatulizer

Aminophyllic Citrate

An extremely powerful cure for temporary (non-acute) flatulence, in man or beast.



<a name="br110"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 110

Preparation: Combine 40 grams of Sodium Bicarbonate with 16 ml of Furachlor-

done. Pour into large brown glass jar. Dilute with water to make 100 ml. Add 2 grams

Magnesium Sulfate. Stopper. Shake. Mix 1:1000 with water.

Instructions for preparation of “Contaminated Water” de-contaminator

Bisalicylate Antitoxidene

Bisalicylate Antitoxidene has been found to be an effective, albeit highly powerful,

compound in the correction of diarrhea, although it is not normally recommended for

individuals due to its extreme concentration and possibility for overdosage, with sub-

sequent dire consequences. Best when taken with vast quantities of water. Storage may

be a problem due to short shelf life.

Preparation: Combine 3 ml of Bismuth Subsalicylate with 4 ml of Orphenamethihy-

dride in a test tube. Heat over flame until mixture begins to boil. Remove from flame

and dilute with one thousand gallons of water (approximately). Makes enough Bisalicy-

late Antitoxidene for four thousand doses.

Phony home remedies

Learn to rename standard home remedies and common everyday ingredients for in-

creased store traffic and greater profits! Advanced study includes moving inexpensive

common chemicals into tiny bottles and jars, while keeping the same pricing structure.

Phony chemical names

Include fakes so the stuff we need doesn’t stand out.

Phony preparations

Possible starting points: analgesic rub, anesthetic, antacid, balm, bleach, boric acid,

cough drop, cough syrup, diuretic, ear drops, elixir, eye drops, eyewash, isopropyl alco-

hol, laxative, liniment, lotion, lozenge, mineral bath, mineral oil, mineral water, nose

drops, ointment, pill, petroleum jelly, potion, poultice, salve, sedative, smelling salts,

suppository

Real drugstore products: 20 Mule Team Borax, aspirin, bicarbonate of soda, calamine

lotion, castor oil, chamomile tea, chloroform, cod-liver oil, dandelion tea, ether, Epsom

salts, eucalyptus oil, herbal tea, Mercurochrome, mineral salt, milk of magnesia, mus-

tard plaster, nitroglycerin, oil of wintergreen, peroxide, quinine, rock salt, saline solu-

tion, silver nitrate, snake oil, styptic pencil, sulfa drug, syrup of ipecac, witch hazel

Funny phony illnesses

Or not.



<a name="br111"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 111

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_Lab Screen Chemicals

Label

Form

Comment

Aminophyllic Citrate

Bimethylquinoline

Bisalicylate Antitoxidene

liquid

crystals

liquid

formal name of Deflatulizer™

used to make Medication #3

formal name of water purification

solution

Bismuth Enterosalicyline

Bismuth Subsalicylate

(Pepto Bismol)

Caffeine

liquid

liquid

used to make Medication #2

used to make water purification

solution

powder

powder

unused

unused

Calcium Carbonate

(Chalk)

Calcium Citrate

Carbon

crystals

granules

unused

obtain from blacksmith

(Charcoal)

Chloroform

Codeine

Copper Sulphate

liquid

liquid

crystals

unused

unused

unused

(Blue stone)

Enteromagneline

powder

used to make INcorrect Medica-

tion #3

Estrosterane

Ethyl Alcohol

powder

liquid

correct Prescription #3

unused

Formaldehyde

liquid

unused

Furachlordone

Magnesium Sulfate

(Epson Salts)

liquid

granules

used to make Deflatulizer™

unused

Mercuric Chloride

(Zenker’s Solution)

Metyraphosphate

Nitrabylocynine

Orphenamethihydride

liquid

unused

powder

powder

used to make Medication #3

unused

used to make water purification

solution

Pepticlymacine Tetrazole

liquid

substituted for the Ty-

loxapolynide prescribed in

Prescription #1

Phenodol Oxytriglychlorate

Phenolsulphonphthalein

powder

liquid

used to make Medication #2

used to make INcorrect Medica-

tion #3

Potassium Cupri-tartate

(Fehling’s Solution)

Potassium Nitrate

Quicksilver

liquid

unused

powder

liquid

unused

unused

(Mercury)

Quinotrazate

Reserpicline Oxide

pills

powder

correct Prescription #2

unused



<a name="br112"></a> 

Freddy Pharkas, Frontier Pharmacist Design Document

Copyright 1992 by Al Lowe

Page 112

Label

Saltpeter

Form

powder

Comment

unused

Sodium Bicarbonate (baking soda) powder

used to correct flatulence & diar-

rhea; useful on flames

used on tomatoes

unused

INcorrect Prescription #3

500 mg 4x daily / 10 days

unused

prescribed in Prescription #1,

but always out of stock

unused

Sodium Chloride

Sorbitalic Acid

Testosterate

liquid

powder

Tetracycline

Thiouracilium

Tyloxapolynide

liquid

liquid

Ureaphilofine

liquid

Valerectal Dinoctum

Wismutoxyjodogenomylon

granules

powder

unused

unused

