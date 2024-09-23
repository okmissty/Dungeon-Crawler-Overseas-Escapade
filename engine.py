import random 
import arcade
import character
from character import _character, _enemy

def battle(player : _character, enemy: _enemy):
    '''
    This function is for when the player enters combat 
    ---
    char_stats: list of values
    enemy_stats: list of values

    Returns
    ---
    battle result, in either a loss or a win
    '''
    while player.stats['HP'] > 0: # Checking Player HP
        if enemy.stats['HP'] >= 0: # Checking Enemy HP
            player_choice = player_turn()
            enemy_ai = enemy_turn()
            outcome(player_choice, enemy_ai, player, enemy)
        else: 
            print('You win!')
            player.stats['HP'] = 10 #Restocking health
            return 1
    print('You lost...')
    return 0   
    
    
   

# Player Choice
def player_turn():
    player_choice = input('What do you want to do?: ATK, DEF: ')
    if player_choice == 'ATK':
        #print('You decide to attack')
        return player_choice
    elif player_choice == 'DEF':
        #print('You decide to defend')
        return player_choice

# Enemy AI  
def enemy_turn():
    enemy_choice = random.randint(1,2)
    if enemy_choice == 1:
        #Attack
        #print('Enemy trys to attack!')
        return enemy_choice
    elif enemy_choice == 2:
        #Defend
        #print('Enemy trys to defend!')
        return enemy_choice
   

# Outcome 
def outcome(player_choice, enemy_choice, player, enemy):
    if (player_choice == 'ATK') and (enemy_choice == 1 or enemy_choice == 3): # Both attack
        attack(player, enemy)
    elif player_choice == 'DEF' and enemy_choice == 2: # Both Defend 
        defense(player, enemy)
    elif player_choice == 'ATK' and enemy_choice == 2: #Player attacks, enemy defends
        print('Player attacks, enemy defends!')
    elif player_choice == 'DEF' and (enemy_choice == 1 or enemy_choice == 3): #Player defends, enemy attacks
        print('Player Defends, enemy attacks!')
        
    

## ------------------------------------------------------------------------------------------------[]


# Calculating Damage
def damage(char_stats):
    '''
    This function is to calculate damage based on the players weapon and modifer
    ---
    weapon: str
    char_stats: list of values

    Returns
    ---
    A value representing the amount of damage done.
    '''
    
    if char_stats.weapon == 'Sword':
        return 4 + char_stats.stats['AP'] 
    elif char_stats.weapon == 'Staff':
        return 2 + char_stats.stats['MP']
     
    elif char_stats.weapon == 'Rod':
        return 3 + char_stats.stats['AP']

        

# Defending as an ACTION 
def defense(char_stats, enemy_stats):
    '''
    Allows the player to block an enemy attack by temporarily increasing their defense for a round to prepare for an attack.
    ---
    char_stats: list of values
    enemy_stats: list of values

    Returns
    ---
    If the block is sucessful nothing happens and if it isnt the player is hit by the enemy attack
    '''
    if ((random.randint(1,20)) + char_stats.stats['DP'] + 5) >= ((random.randint(1,20)) + enemy_stats.stats['DP']):
        #Player suceeds defend
        print('Successful Block!')
    else:
        print('Failed Block')
        char_stats.stats['HP'] -= 5
        print(f"Character HP: {char_stats.stats['HP']}")
        return char_stats


    
#Attacking
def attack(char_stats, enemy_stats):
    '''
    Attack an enemy
    ---
    char_stats: list of values
    enemy_stats: list of values
    weapon: str

    Returns
    ---
    If a hit is sucessful the enemy takes damage, otherwise nothing happens
    '''
     
    if ((random.randint(1,20)) + char_stats.stats['AP']) >= ((random.randint(1,20)) + enemy_stats.stats['AP']):
        #Player suceeds hit
        print('Successful hit!')
        enemy_stats.stats['HP'] -= damage(char_stats)
        print(f"Enemy HP: {enemy_stats.stats['HP']}")
    else:
        # Nothing happens, enemy does not lose HP
        battle(char_stats, enemy_stats)






# tutorial grid
'''
Outer index - y-axis!
Inner index - x-axis!
'''

game_grid = [ 
['', '', 'e', '', 'e'], # row 1
['', 'e', '', 'l', ''], # row 2
['e', '', 'l', 'e', ''], # row 3
['', 'e', 'l', '', 'b'] # row 4
]



def move_right(char_x, char_y, grid):
    '''
    It is easier to manage your indices inside of here.
    If you don't hit a wall, then you can increment the x value.
    '''
    if char_x + 1 < len(grid[char_y]):
        return char_x + 1, char_y
    else:
        return char_x, char_y

def move_up(char_x, char_y, grid):
    '''
    Same idea here, but for y. Moving up is reducing the index!
    '''
    if char_y - 1 >= 0:
        return char_x, char_y - 1
    else:
        return char_x, char_y

def move_left(char_x, char_y, grid):
    '''
    If you don't hit a wall, then you can increment the x value.

    '''
    if char_x + 1 < len(grid[char_y]):
        return char_x - 1, char_y
    else:
        return char_x, char_y
    
def move_down(char_x, char_y, grid):
    '''
    It is easier to manage your indices inside of here.
    If you don't hit a wall, then you can increment the x value.
    '''
    if char_x + 1 < len(grid[char_y]):
        return char_x , char_y + 1
    else:
        return char_x, char_y



# Navigate Function : Core gameplay
def navigate(user_input, player, game_grid):    
    
    if user_input == 'right': # Moving Right
        char_x, char_y = move_right(player.x, player.y, game_grid)
        player.x = char_x
        player.y = char_y

    elif user_input == 'left': # Moving Left
        char_x, char_y = move_left(player.y, player.y, game_grid)
        player.x = char_x
        player.y = char_y

    elif user_input == 'up': # Moving up
        char_x, char_y = move_up(player.y, player.y, game_grid)
        player.x = char_x
        player.y = char_y

    elif user_input == 'down': # Moving down
        char_x, char_y = move_down(player.y, player.y, game_grid)
        player.y = char_x
        player.y = char_y
    else:
        pass

    # Now handle what is in that cell!
    event_value = game_grid[player.y][player.y]
    # Do something! Fight a battle, get some loot, or nothing!
    # ...
    if event_value == '': # nothing
        return None
    elif event_value == 'e': # enemy
        print(f"You've encountered an enemy!")
        opponent = character.generate_enemy()
        final = battle(player, opponent)
        if final == '0':
            status = 'lose'
            return status

    elif event_value == 'b': # boss
        print(f"You've encountered a boss!")
        opponent = character.generate_enemy()
        if battle(player, opponent) == '0':
            status = 'lose'
            return status 
    
    elif event_value == 'l': # loot 
        loot()
 
# loot function i havent worked out yet

def loot():
    lucky = (random.randint(1,100))

             


## XP System
def check_level(XP, level):
    '''
    This function will check for the players XP
    lvl 0: 0 XP
    lvl 1: 10 XP
    lvl 2: 100 XP
    lvl 3: 1000 XP 
    ---
    XP: int 
    
    Returns
    ---
    Will return the XP of the character
    Depending on where the XP is it can also potentially increase the character's level and output it
    '''

    if XP == 10:
        level = 1
        print(f'You leveled up! Level: {level}')
        return level
    elif XP == 100:
        level = 2
        print(f'You leveled up! Level: {level}')
        return level
    elif XP == 1000:
        level = 3
        print(f'You leveled up! Level: {level}')
        return level
    else: 
        print(f'XP:{XP}')