import pygame

from settings import Settings
from bat import Bat
from ball import Ball
import game_functions as gf

def run_game():    
    # Initialize pygame, settings and create a screen object. 
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Breakout")

    # Make a bat
    bat = Bat(ai_settings, screen)
    ball = Ball(ai_settings, screen) 

    # Start the main loop for the game. 
    while True:
        gf.check_events(bat)
        if gf.is_collition(ball, bat):
            ball.collision()
        bat.update()
        ball.update()
                                  
        gf.update_screen(ai_settings, screen, bat, ball)

run_game()