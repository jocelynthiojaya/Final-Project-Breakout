import pygame

from settings import Settings
from bat import Bat
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

    # Start the main loop for the game. 
    while True:
        gf.check_events(bat)
        bat.update()                       
        gf.update_screen(ai_settings, screen, bat)

run_game()