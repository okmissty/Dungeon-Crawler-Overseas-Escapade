import arcade
import arcade.gui
import random



## Base Stats for Every Entity
# HP: Health Points / MP: Magics Points / AP: Ability Points / XP: Experience Points 

# Side characters creation call
#character_creation('Pirate Octavia', 'Gunslinger')
#character_creation('Sailor Jack', 'Sea Sorcerer')


## Character Creation 
    # Depending on the User's input prior will determine their class here. 

def character_creation(name, card_class):
    '''
    This function will create a new character for the player
    ---
    Name: A string
    card_class: A string
    
    Returns
    ---
    Will output a character card listing the name, lvl, class, XP, stats, and the inventory of that character.
    '''
   
    if card_class == 'Duelist':
    
        player = duelist(name, card_class)
        player.stats = {'HP': 30, 'MP':10, 'AP': 10, 'DP':10}
        player.weapon = 'Sword'

    
        return player
        
    elif card_class == 'Sea Sorcerer':

        player = Sea_Sorcerer(name, card_class)
        player.stats = {'HP': 30, 'MP':10, 'AP': 10, 'DP':10}
        player.weapon = 'Staff'
       
        return player
       
    elif  card_class == 'Gunslinger':

        player = Gunslinger(name, card_class)
        player.stats = {'HP': 30, 'MP':10, 'AP': 10, 'DP':10}
        player.weapon = 'Rod'

        return player
    
    else:
        print('Type it exactly!')
    
    return 


def generate_enemy():
    '''
    This function generates an enemy!
    ---
    enemy_type: str

    Returns
    ---
    Will output an enemy if the qualifications are met 

    '''

    enemy = {'name': '', 'level': 0, 'class': '','XP': 0, 'weapon': '', 'stats':[]}

    # Tutorial 
    enemy_type = random.randint(1,2)
    if enemy_type == 1:

        #enemy['class'] = 'Fighter'
        enemy = Pirate()
        enemy.stats = {'HP': 30, 'MP':10, 'AP': 10, 'DP':10}
        enemy.weapon = 'Sword'

        return enemy
    
    # Random Generated enemies
    elif enemy_type == 2:
      
        enemy = Siren()
       

        return enemy
    
    # Mini bosses
    elif  enemy_type == 3:
       
        enemy = Siren_Sisters()
        enemy.stats = {'HP': 30, 'MP':15, 'AP': 8, 'DP':10} 
        enemy.weapon = 'Song wave'
    
        return enemy

    else:
        return None



# Character 
class _character:
    
    def __init__(self, name, card_class='', level=0, XP =0, weapon='twig', stats={}, x=0 , y=0, inventory=[]):
        self.name = name
        self.level = level
        self.card_class = card_class
        self.XP = XP
        self.weapon = weapon
        self.stats = stats
        self.x = x
        self.y = y
        self.inventory = inventory
    def __str__(self):
        return f'Name: {self.name} /n level:{self.level} XP: {self.XP} /n class:{self.card_class} /n weapon: {self.weapon} /n Stats:{self.stats}'
class duelist(_character):
        def __init__(self, name, card_class='', level=0, XP=0, weapon='sword', stats={}, x=0, y=0, inventory=[]):
            self.name = name
            self.level = level
            self.card_class = card_class
            self.XP = XP
            self.weapon = weapon
            self.x = x
            self.y = y
            self.inventory = inventory
            self.stats = stats
class Sea_Sorcerer(_character):
        def __init__(self, name, card_class='', level=0, XP=0, weapon='sword', stats={}, x=0, y=0, inventory=[]):
            self.name = name
            self.level = 0
            self.card_class = card_class
            self.XP = 0
             
            self.x = 0
            self.y = 0
            self.inventory = []
class Gunslinger(_character):
        def __init__(self, name, card_class='', level=0, XP=0, weapon='sword', stats={}, x=0, y=0, inventory=[]):
            self.name = name
            self.level = 0
            self.card_class = card_class
            self.XP = 0  
            self.x = 0
            self.y = 0
            self.inventory = []

# Enemies

class _Enemy:

    def __init__(self, name, weapon, stats):
        self.name = name
        self.weapon = weapon
        self.stats = stats 

    def __str__(self):
        return f'Name: {self.name} /n weapon: {self.weapon} /n Stats:{self.stats}'  
    
class Pirate(_Enemy):
    def __init__(self):

        self.stats = {'HP': 30, 'MP':10, 'AP': 10, 'DP':10}
        self.weapon = 'sword'
        self.name = 'anrgy pirate'
class Siren(_Enemy):

    def __init__(self):
        self.name = 'Siren'
        self.weapon = 'magic pearl'
        self.stats = {'HP': 30, 'MP':10, 'AP': 10, 'DP':10}

    
#Boss
class Siren_Sisters(Siren):
    def __init__(self, name, weapon, stats):
        self.name = name
        self.weapon = weapon
        self.stats = stats 



class DungeonCrawler(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE_SMOKE)

    def on_draw(self):
        arcade.start_render()
        ###
        #   Bring back your welcome message.
        ###
        welcome = "Welcome to Dungeon Crawler!"
        ###
        #   A little early: looking at class attributes with self.width and self.height!
        ###
        #draw_message(welcome, arcade.csscolor.BISQUE, self.width, self.height)

    def on_key_press(self, symbol, modifiers):
        # You will modify this function to respond to your Up, Down, Left, Right keys.
        # Each key should print something about your character moving.
        #   Ex: "Moved up 1 space"


        pass



    