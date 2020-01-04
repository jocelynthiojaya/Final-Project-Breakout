import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from bat_copy import Bat
from ball import Ball
from brick import Brick
from bottom_line import BottomLine
from button import Button
from scoreboard import Scoreboard

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
    bottom_line = BottomLine(ai_settings, screen)
    bricks = Group()

    gf.create_rowbricks(ai_settings, screen, bricks)

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make play button
    play_button = Button(ai_settings, screen, "Play") 

    # Start the main loop for the game. 
    while True:
        gf.check_events(ai_settings, screen, stats, sb, bat, bricks, play_button)
        
        if stats.game_active:
            gf.ball_die(ai_settings, stats, screen, sb, bat, bricks, ball, bottom_line)

            if gf.is_collision_bat(ball, bat):
                ball.bat_collision()

            gf.collision_brick(ai_settings, stats, sb, ball, bricks)

            bat.update()
            ball.update()

            ball.collision_wall()

        gf.update_screen(ai_settings, screen, stats, sb, bat, ball, bricks, 
            bottom_line, play_button)

run_game()