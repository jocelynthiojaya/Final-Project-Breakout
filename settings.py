colors = [(255,0,0), (255,128,0), (255,217,25), (102,204,0), (0,77,0), (0,255,128), 
    (0,128,255), (0,0,255), (234,128,255), (255,0,255), (255,0,127)]

class Settings():    
    #Store all settings that i would like to access across all files
    def __init__(self):        
        #Initialize the game's static settings.
        # Screen settings        
        self.screen_width = 1000
        self.screen_height = 700       
        self.bg_color = (230, 230, 230)

        # Bat settings
        self.bat_speed_factor = 3
        self.bat_width = 1000
        self.bat_height = 7.5

        # Ball settings
        self.ball_limit = 5

        # Brick settings
        self.brick_width = 160
        self.brick_height = 120
        self.color_code = 0
        self.brick_color = colors[self.color_code]
    
        # Scoring
        self.brick_points = 100
    
    def level_up(self):
        # sequence when player reaches a new level
        self.brick_width *= 0.8
        self.brick_height *= 0.8
        if self.color_code == 10:
            self.color_code = 0
            self.brick_color = colors[self.color_code]
        else:
            self.color_code += 1
            self.brick_color = colors[self.color_code]
    
    def reset_bricks(self):
        # reset brick settings to initial ones
        self.brick_width = 160
        self.brick_height = 120
        self.color_code = 0
        self.brick_color = colors[self.color_code]
        