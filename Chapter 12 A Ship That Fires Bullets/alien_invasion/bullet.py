import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    
    """Class to manage the bullets fired from the ship
    """
    def __init__(self, ai_game):
        
        """Create a bullet object at current position
        """
        super().__init__()
        
        self.screen = ai_game.screen
        try:
            self.settings = ai_game.settings
            self.color = self.settings.bullet_colour
        except Exception as e:                           # /* This is the cheat code */
            print("Si è verificata un'eccezione!")
            print(f"Tipo: {type(e)}")
            print(f"Messaggio: {e}")
            print("settings non preso")
            exit()
            
        
        """self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)"""  #With this values works but its not taking the values from settings
        
        

        
        #Create a bullet rect at (0, 0) and the set correct postion
        try:
            self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height )
            
            self.rect.midtop = ai_game.ship.rect.midtop
        except Exception as e:                           # /* This is the cheat code */
            print("Si è verificata un'eccezione!")
            print(f"Tipo: {type(e)}")
            print(f"Messaggio: {e}")
        
        #Store bullet position as a float
        try:
            self.y = float(self.rect.y)
        except Exception as e:                           # /* This is the cheat code */
            print("Si è verificata un'eccezione!")
            print(f"Tipo: {type(e)}")
            print(f"Messaggio: {e}")
        
    def update(self):
        """Update bullet position"""
        #if self.moving_up and self.rect.top > 0:     //Will add later the control for shooting
        try:
            self.y -= self.settings.bullet_speed
            #Update the rect position
            self.rect.y = self.y
        except Exception as e:                           # /* This is the cheat code */
            print("Si è verificata un'eccezione!")
            print(f"Tipo: {type(e)}")
            print(f"Messaggio: {e}")
        
    def draw_bullet(self):
        """Draw bullet in the screen
        """
        pygame.draw.rect(self.screen, self.color, self.rect)