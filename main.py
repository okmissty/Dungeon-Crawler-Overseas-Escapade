import arcade
import arcade.gui
import engine
import character
import random




#Creating window
screen_width = 1200
screen_height = 600


class Player(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > screen_width - 1:
            self.right = screen_width- 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > screen_height - 1:
            self.top = screen_height - 1

class DungeonCrawler(arcade.Window):

    def __init__(self, width, height, title, game_grid, cell_size=50):
        '''
        Constructer
        '''
        
        # This allows us to align the game grid with our cell sizing.
        height = len(game_grid) * cell_size
        width = len(game_grid) * cell_size
        # Note we do not call the super() constructor until we compute the size of the window
        
        # The stuff you already have...
        self._player = player
        self._game_grid = engine.game_grid
        # When you make a sprite, you should set its height and width to your cell_size!
        

        #background
        self.background = arcade.load_texture('GUI/OE act 1 screen.png')

        
        
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.LIGHT_STEEL_BLUE)
        
        
        # Variables that will hold sprite lists
        self.player_list = None

        # Set up the player info
        self.player_sprite = None

        #setting up the player

        # Sprite lists
        self.player_list = arcade.SpriteList()

        
        self.player_sprite = Player('GUI/Zeroleft.png', 0.3)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        self.player_sprite.width = cell_size
        self.player_sprite.height = cell_size

    def setup(self):
        """ Set up the game and initialize the variables. """

        

        # Set up the player
        


    def on_draw(self):
        '''
        This function is used to draw on the window 
        ---
        delta_time: int

        Returns
        ---
        Displays basic welcome screen on the window
        '''
        

        self.clear()
        screen_width = 1200
        screen_height = 600
        arcade.draw_lrwh_rectangle_textured(0, 0, screen_width, screen_height, self.background)
        self.player_list.draw()
       
       

        welcome = "Welcome to Overseas Escapade"
       

    def update(self, delta_time):
        self.player_list.update()

    def on_key_press(self, key, modifiers):
        # You will modify this function to respond to your Up, Down, Left, Right keys.
        # Each key should print something about your character moving.
        #   Ex: "Moved up 1 space"
        if key == arcade.key.RIGHT:
            self.player_sprite.change_x += 1
            engine.navigate('right', player, engine.game_grid)
            print(f'{name} moved 1 right')
 
        if key == arcade.key.LEFT:
            
            engine.navigate('left', player, engine.game_grid)
            self.player_sprite.change_x -= 1 
            print(f'{name} moved 1 Left')

        if key == arcade.key.DOWN:
            
            engine.navigate('down', player, engine.game_grid)
            self.player_sprite.change_y -= 1 
            print(f'{name} moved 1 down')

        if key == arcade.key.UP:
            
            engine.navigate('up', player, engine.game_grid)
            self.player_sprite.change_y += 1
            print(f'{name} moved 1 upwards')
        pass




def main():

    window = DungeonCrawler(screen_width, screen_height, 'Overseas Escapade', engine.game_grid)
    window.setup()
    arcade.run()

    # Main Game Loop
    while game_condition == False:
        if player.stats['HP']> 0:
            engine.navigate(player, engine.game_grid)
            if treasure_found == True:
                status = 'win'
                # The Good Ending
                exit
            else:
                pass
        else: 
            status = 'lose'
            # The Bad ending
            exit

# Creating a message
def draw_message(message, color, screen_width, screen_height):

    '''
    This function draws a message 
    ---
    message: str
    color: str
    screen_width: int
    screen_height: int
    
    Returns
    ---
    Outputs a message
    '''
    
    msg_width = screen_width // 2
    msg_height = screen_height // 2
    left = msg_width // 2
    right = screen_width - msg_width // 2
    bottom = msg_height // 2
    top = screen_height - msg_height // 2
    arcade.draw_lrtb_rectangle_filled(left, right, top, bottom, color)
    arcade.draw_text(message, left, bottom + msg_height // 2, arcade.color.BLACK, 30, msg_width, 'left')

## ------------------------------------------------------------------------------------------------[]

if __name__ == '__main__':
        

    # Player creation call

    print('Welcome to Overseas Escapade!') 
    
    name = input('What is your name? ')
    card_class = input('What is your class: Duelist, Sea Sorcerer, Gunslinger? ')
   
    player = character.character_creation(name, card_class)

    game_condition = False
    treasure_found = False
    
    
    # Game 
    main()
    
    

   

## ------------------------------------------------------------------------------------------------[]