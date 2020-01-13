import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from bat import Bat
from ball import Ball
from brick import Brick
from bottom_line import BottomLine
from button import Button
from scoreboard import Scoreboard
from title import Title

import game_functions as gf

def run_game():    
    # Initialize pygame, settings and create a screen object. 
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Brick Breaker")

    # Make a bat, ball, bottomline
    bat = Bat(ai_settings, screen)
    ball = Ball(ai_settings, screen)
    bottom_line = BottomLine(ai_settings, screen)
    
    # Make bricks
    bricks = Group()
    gf.create_rowbricks(ai_settings, screen, bricks)

    # Make stats, scoreboard, title, and play button
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    title = Title(ai_settings, screen)
    play_button = Button(ai_settings, screen, "Play") 

    # Start the main loop for the game. 
    while True:
        # check mouse and key events
        gf.check_events(ai_settings, screen, stats, sb, bat, bricks, play_button)
   
        if stats.game_active:
            # sequence when player loses a life
            gf.ball_die(ai_settings, stats, screen, sb, bat, bricks, ball, bottom_line)
            
            # sequence if ball collide with bat, and brick and wall 
            if gf.is_collision_bat(ball, bat):
                ball.bat_collision()

            gf.collision_brick(ai_settings, stats, sb, ball, bricks)
            ball.collision_wall()

            # updates ball and bat position
            bat.update()
            ball.update() 

        # updates the screen
        gf.update_screen(ai_settings, screen, stats, sb, bat, ball, bricks, 
            bottom_line, play_button, title)

run_game()