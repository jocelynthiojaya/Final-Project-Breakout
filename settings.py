colors = [(255,0,0), (255,128,0), (255,255,0), (128,255,0), (0,255,0), (0,255,128), 
    (0,255,255), (0,128,255), (0,0,255), (127,0,255,), (255,0,255), (255,0,127)]

class Settings():    
    #A class to store all settings for Breakout
    
    def __init__(self):        
        #Initialize the game's static settings.
        # Screen settings        
        self.screen_width = 1000
        self.screen_height = 700       
        self.bg_color = (230, 230, 230)

        # Bat settings
        self.bat_speed_factor = 1.5
        self.bat_width = 250
        self.bat_height = 7.5

        # Ball settings
        self.ball_limit = 5

        # Brick settings
        self.brick_width = 160 #60
        self.brick_height = 100 #30
        #self.color_code = 0
        #self.brick_color = colors[self.color_code]
    
        # Scoring
        self.brick_points = 100
    
    def level_up(self):
        # leveling up
        #self.bat_width -= 100
        self.brick_width -= 20
        self.brick_height -= 20
        #self.color_code += 1
        