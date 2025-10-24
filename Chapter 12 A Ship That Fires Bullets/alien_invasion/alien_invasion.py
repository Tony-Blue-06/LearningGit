import sys 
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet




class AlienInvasion:
    """Overall class to manage game assets and behaviour
    """
    
    def __init__(self):
        
        """Initialize the game, and greate game resources
        """
        pygame.init()
        
        #Controlling the frame rate 
        
        self.clock = pygame.time.Clock()
        
        #Display Settings (Dimension, Caption, Background Color)
        self.settings  = Settings()   
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
        #Trying full mode
        #self.screen = pygame.display.set_mode(((0,0)), pygame.FULLSCREEN)
        
        pygame.display.set_caption("Alien Invasion")
        
        #Initializiation player ship
        self.ship = Ship(self)
        #Init bullets group
        self.bullets = pygame.sprite.Group()
        
        
    def run_game(self):
        """Start the main loop for the game
        """
        
        while True:
            
            #Watch for keyboard and mouse events.
            self._check_events()
                    
            #Rendering
            self.ship.update()
            self.bullets.update()
            self._update_screen()
                        
            #Set the frame rate to 120 frames per second
            self.clock.tick(120)
    
    def _check_events(self):
        """Handles how to respond to keypress and mouse events
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:          #Check if event is button down event
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:             #Stop move
                self.check_keyup_events(event)
            
                
                     
     
     
    #Refacroring movement left right up down
    
    def check_keydown_events(self,event):
        
        """Respond to keypress"""
                           
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:         #MOVE RIGHT
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:         #MOVE LEFT
            self.ship.moving_left = True                       
        elif event.key == pygame.K_UP or event.key == pygame.K_w:           #MOVE UP
            self.ship.moving_up = True               
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:         #MOVE DOWN
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self.firing_bullets()
        elif event.key == pygame.K_ESCAPE:
            sys.exit() 
    
    def check_keyup_events(self, event):
        
        """Respond to keyup"""
        
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:        
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:         #MOVE LEFT
            self.ship.moving_left = False                       
        elif event.key == pygame.K_UP or event.key == pygame.K_w:           #MOVE UP
            self.ship.moving_up = False               
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:         #MOVE DOWN
            self.ship.moving_down = False    
    
    #Bullet creation
    def firing_bullets(self):
        """Create a new bullet and adds it to the bullet group"""
        
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
                                    
    def _update_screen(self):
        """does what the name indicates
        """
        self.screen.fill(self.settings.bg_colour)
       
        try: 
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
        except Exception as e:                           # /* This is the cheat code */
            print("Si è verificata un'eccezione!")
            print(f"Tipo: {type(e)}")
            print(f"Messaggio: {e}")
            sys.exit()
            
        self.ship.blitme()
        
        pygame.display.flip()
        
    
if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()