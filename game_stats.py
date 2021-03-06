import pygame

class GameStats():    
    # Track statistics for Breakout.
    def __init__(self, ai_settings):        
        # Initialize statistics.
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Breakout in an inactive state.
        self.game_active = False

        # High score should never be reset.
        f = open("highscore.txt", "r")
        self.high_score = int(f.read())
    
    def reset_stats(self):        
        # Initialize statistics that can change during the game.
        self.balls_left = self.ai_settings.ball_limit
        self.score = 0
        self.level = 1
