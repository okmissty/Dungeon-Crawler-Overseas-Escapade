# Design

This document will maintain the design of your game.
It may evolve into multiple pages based on the needs of the project.

# Dungeon Crawler
Welcome! This repository maintains your game project!

# Overseas Escapade

The once pushover and dull young pirate Suleiman realizes he could(should) be destined for greatness after coming across a legendary treasure map that could change his entire life. Will he be able to face the dangers of the sea, secure the path to riches, and join the pirate hall of fame? or remain a forgotten sailor of the seas?


## How to Play
- Up arrow = forward
- down arrow = backward
- left arrow = left
- right arrow = right

- i key = investigate
- e key = display character card and inventory

### Navigation
The game is set on a grid where the character can move and encounter randomly generated enemies, loot, or a boss to fight. If they move into a space with nothing in it, nothing will happen! 


**Goal**: Find the Legendary Treasure and become a renowned pirate
## Setting
Setting: Medieval fantasy, specifically on the ocean primarily

Ships, beaches, Underwater, ports


## Storyline


### Game Events (In order)
[Act 0: Tutorial]
- Upon visiting on the beaches of a small port town and wandering away from his pirate crew, **Sully** encounters a treasure map in a glass bottle with the signature of a legendary pirate. 
- A spark ignited in Sully as he prepared to sneak away from his current crew
- He gets caught by his crewmate and good friend, **Octavia**. 
- Octavia stops and attacks him thinking Sully was attempting to run off without a word!

[The Tutorial Commences from here]

- After the tutorial fight, Sully explains to Octavia of the treasure map and she becomes immedietely on board . 
- As soon as both of them were about to sneak off... their crewmate, **Sailor Jack** appeared from a shaky illusion of water droplet, admiting that he was easedropping the whole time.

- Sully and Octavia had no choice but to bring Sailor Jack onboard with their plan to conquer the treasure. Or else they'd be hunted down for life if they get snitched on. 

[End of act 0]

[Act 1: Siren Sisters]

[Act 2: Captain Eugene]

[Act 3: King Kraken]

## System / Mechanics
### Base classes:
- Duelist (fighter)
- Sea sorcerer (mage)
- Gunslinger (archer)

(These stats are just random numbers for right now)
Base Stats: 
- HP(Health Points): 10
- MP(Magic Power): 10
- AP(Ability Power): 10

Ability power is for Gunslingers and Duelists

### Combat:
Display Stats somewhere
Display Enemy Health somewhere (or don't)
Display Actions [ Could be locked depending on class ]:

- Duelist -> Fighter -> fighting Moves -> AP
- Sea Sorcerer -> Mage -> magic spells -> MP
- Gunslinger -> Ranger -> Ranged attacks -> AP


### Visuals:
Probably a mix of my own art and free use assets, but I want to stick to a certain color palette

## Characters
### Main Character: Suleiman (Sully)

Main Side Characters: 
- Pirate Octavia
- Captain Leon
- Sailor Jack
- Mermaid Melody

NPCs (Resuable):
- Sailors
- Travelling Merchant 
- Pirate 


Antagonists/Monsters: (in order)
- Pirate Octavia (tutorial)
    - Quick attack
- Siren Sisters
    - Alluring Voice
- Captain Eugene
    - Ghastly Strike
- Final Boss: King Kraken
    - Tentacle Slam


## Items 
### Inventory / loot:

Players will be able to choose what their weapon and class is. 

The better the weapon level is the better the modifer for that weapon will be. For example, A legendary Cutlass will give the player an additional +3 to their ability power stat. This is helpful for players who chose duelist as their class. 


#### Starter Items [ Depending on Class ]
- Sword +0 
- Staff +0
- Rod +0
#### Lvl 1 Loot (After beating Siren Sisters)
- Better Sword +1
- Better Staff +1
- Better Rod +1 
#### Lvl 2 Loot (After beating Captain Eugene)
- Cooler Sword +2 
- Cooler Staff +2
- Cooler Rod +2
#### OPTIONAL Lvl 3 Loot (Right before Final boss)
The lvl 3 loot will require more effort to get, likely through puzzles!!

- Legendary Cutlass +3
- Mystical Trident of Moomoo the Great +3
- Heartward Piercer +3 



# Function Flow charts


## Character/Enemy creation

![alt text](<Deliverable 1.drawio (1).png>)
![alt text](<enemy generation.drawio.png>)
## XP leveling

![alt text](<XP system.drawio.png>)


## Battle System

### The Battle Function(char_stats,enemy_stats):
- The system will be primarly dependent on dice (Random d20)
- The player will have opprotunities such as weapons or an advantage to boost their rolls through modifers. Damage will depend on weapons and stats!

    - Based on their stats it is the same for each categorty:
    - 12+ = +3 modifer
    - 10-12 = +2 modifer
    - 8-9 = +1 modifer
    - 6-7 = +0 modifer
    - 4-5 = -1 modifer
    - 2-3 = -2 modifer
    - 1-2 = -3 modifer

- The player will have the choice to choose how they would like to respond to an enemy
-       Attack
-       Flee (Cannot do this for boss battles)
-       Defend (This is great for when the player is going to get hit with a        special move)
-       Item

- A typical player turn order would be like:
-       Players Choice: Listed Aboved
-       Execute the players choice:
        - Attack [d20 + AP Modifers] against Enemy's defense [DF]
        - Defend [d20 + DF Modifers + 5] against Enemy's attack [AP]
        - Flee [Pure d20] against Enemy's [d20]
        - Item [This would vary on the item being used but the player would choose one from their inventory and apply it to the battle. Ex. a health potion]
    
- A typical enemy turn order would be like:
  Enemy's Choice: Random roll of d3 to decide
-       Execute the Enemy's choice:
        - Attack [d20 + AP Modifers] against players's defense [DF]
        - Defend [d20 + DF Modifers + 5] against players's attack [AP]'
        - Special Move [MP: Would vary depending on enemy]

After all executions are made to that turn, it will resolve by checking the HP of both sides and keep looping until someone's HP == 0. 


#### The Loot Function:
 At the end of the battle, the loot function will commence gifting the player with what they have earned, depending on the battle I could commence this function to give out randomized loot. 
  

#### The Check Level Function:
- +10 XP will always be earned if they win. If they lose no XP or rewards are earned.

![alt text](image.png)

#### The Main & Navigate Loops 
![!\[alt text\](<Untitled Diagram.drawio.png>)](mainloop.png)

## Resources
- General lore
    - https://www.thoughtco.com/pirates-truth-fact  s-legends-and-myths-2136280
- Antagonist lore
    - https://study.com/learn/lesson/siren-mythology.html#:~:text=The%20Sirens%20were%20mythical%20creatures,waters%20with%20their%20irresistible%20song.
    - https://science.howstuffworks.com/science-vs-myth/strange-creatures/kraken.htm
- Misc: Helpful tips
    - https://api.arcade.academy/en/latest/arcade.color.html

- **USED CODE**
    -Sample code from blackboard


If you ever need new libraries, you add them into this file.

## Project Components

In this project, you will develop your game in Python and *document* its design and how to play it.
All components will be placed into this repository and will evolve during the semester.

Documentation will be written in markdown, a very simple markup language that Github renders as webpages.
The Github [markdown reference](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github) is clutch!

You will see in this repository a `requirements.txt` file.
This file holds onto the libraries that your game needs to run.

# Curious things for me to research
- Parallax Background: https://api.arcade.academy/en/latest/examples/parallax.html#parallax
- Title screen: https://api.arcade.academy/en/latest/examples/view_screens_minimal.html#view-screens-minimal or https://api.arcade.academy/en/latest/examples/view_instructions_and_game_over.html#view-instructions-and-game-over
- Game Framework: https://github.com/pythonarcade/roguelike
- Sprite Behavior
- leveling: https://api.arcade.academy/en/latest/examples/sprite_rooms.html#sprite-rooms
- Buttons: https://api.arcade.academy/en/latest/examples/gui_flat_button_styled.html#gui-flat-button-styled

