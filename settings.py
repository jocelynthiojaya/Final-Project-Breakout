class Settings():    
    #A class to store all settings for Breakout
    
    def __init__(self):        
        #Initialize the game's settings.
        # Screen settings        
        self.screen_width = 1000
        self.screen_height = 700       
        self.bg_color = (230, 230, 230)

        # Bat settings
        self.bat_speed_factor = 2