import pygame

class Ship:
    """A class to manage the player ship
    """
    
    def __init__(self, ai_game):
        """initialize the ship and set its starting position

        Args:
            ai_game (AlienInvasion): Gives ship access to the current instance of AlienInvasion Class inheriting all the game resource defined in the class
        """
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        #Loading the ship image and get its rect.
        
        self.image = pygame.image.load('images/player.bmp')
        self.rect = self.image.get_rect()
        
        #Fixing initial postion of the player ship
        
        self.rect.midbottom = self.screen_rect.midbottom
        
        #Store a float for the ship's exact horizontal and vertical position
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
             
        #Indicatore di movimento
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        

        

        
    def blitme(self):
        """Draw the ship and its current postion
        """
        
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        """update the ship position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
              self.x += self.settings.ship_speed
              
        if self.moving_left and self.rect.left > 0 :
              self.x -= self.settings.ship_speed
              
        if self.moving_up and self.rect.top > 0:
              self.y -= self.settings.ship_speed
              
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
              self.y += self.settings.ship_speed
        
        #update rect object from self x,y
        self.rect.x = self.x
        self.rect.y = self.y      
        
        