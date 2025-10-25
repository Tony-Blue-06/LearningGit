class Settings:
    """A class to sto all the settings for Alien Invasion
    """
    def __init__(self):
        """Initialize game settings
        """
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230,230,230)
        #Bullet Settings
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (0, 235, 0)
        
        
        #Ship Speed Settings
        self.ship_speed = 1.5
        self.ship_ammo = 5
        