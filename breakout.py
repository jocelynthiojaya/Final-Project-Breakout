import pygame
from pygame.sprite import Group

from settings import Settings
from bat import Bat
from ball import Ball
from brick import Brick
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
    bricks = Group()

    gf.create_rowbricks(ai_settings, screen, bricks)

    # Start the main loop for the game. 
    while True:
        gf.check_events(bat)
        if gf.is_collision_bat(ball, bat):
            ball.bat_collision()

        gf.collision_brick(ball, bricks)

        bat.update()
        ball.update()        
        gf.update_screen(ai_settings, screen, bat, ball, bricks)

run_game()