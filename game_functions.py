import sys
import pygame
from time import sleep

from brick import Brick
from ball import Ball


def check_keydown_events(ai_settings, event, bat):
    # Respond to keypresses
    if event.key == pygame.K_RIGHT:
        bat.moving_right = True
    elif event.key == pygame.K_LEFT:
        bat.moving_left = True
    elif event.key == pygame.K_SPACE:
        ai_settings.bat_speed_factor += 1

def check_keyup_events(ai_settings, event, bat):
    # Respond to key releases
    if event.key == pygame.K_RIGHT:
        bat.moving_right = False
    elif event.key == pygame.K_LEFT:
        bat.moving_left = False
    elif event.key == pygame.K_SPACE:
        ai_settings.bat_speed_factor -= 1

def check_events(ai_settings, screen, stats, sb, bat, bricks, play_button):    
    # Respond to keypresses and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:            
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ai_settings, event, bat)
        
        elif event.type == pygame.KEYUP:            
            check_keyup_events(ai_settings, event, bat)
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, bat, bricks, play_button, 
                mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, bat, bricks, play_button, 
    mouse_x, mouse_y):
    # Start a new game when the player clicks Play.
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
        
        # Reset the game statistics.
        stats.reset_stats()      
        stats.game_active = True

        # Empty the list of bricks and reset brick settings
        bricks.empty()
        ai_settings.reset_bricks()

        # Create a new rows of bricks and center the bat.
        create_rowbricks(ai_settings, screen, bricks)
        bat.center_bat()

        # Reset the scoreboard images
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_balls()

def is_collision_bat(ball, bat):
    # for check if ball is collide with bat
    return ball.rect.colliderect(bat.rect)

def ball_die(ai_settings, stats, screen, sb, bat, bricks, ball, bottom_line):    
    # Respond to ball dying, aka player loses a life.
    if stats.balls_left > 0:
        col = pygame.sprite.collide_rect(ball, bottom_line)
        if col == True:
            # Decrement balls_left. 
            print('hit bottom')
            stats.balls_left -= 1

            # Update scoreboard
            sb.prep_balls()

            # center bat and ball
            bat.center_bat()
            ball.center_ball(ai_settings)

            # pause
            sleep(0.5)
        
        if len(bricks) == 0:
            # Destroy existing bricks
            bricks.empty()

            # center bat and ball
            bat.center_bat()
            ball.center_ball(ai_settings)

            # change settings to be harder
            ai_settings.level_up()
            
            # Increase level.
            stats.level += 1
            sb.prep_level()
            
            # create new smaller bricks
            create_rowbricks(ai_settings, screen, bricks)
            
    else:        
        stats.game_active = False
        pygame.mouse.set_visible(True)

def do_collision_brick(ai_settings, stats, sb, ball, bricks):
    # sequence for collisions with brick
    if pygame.sprite.spritecollide(ball, bricks, True):
    #for brick in pygame.sprite.spritecollide(ball, bricks, True): 
        ball.brick_collision()
        
        stats.score += ai_settings.brick_points        
        sb.prep_score()
        check_high_score(stats, sb)

def update_screen(ai_settings, screen, stats, sb, bat, ball, bricks, 
    bottom_line, play_button, title):    
    # Update images on the screen and flip to the new screen.
    # Redraw the screen during each pass through the loop.    
    screen.fill(ai_settings.bg_color)    
    bat.blitme()
    ball.blitme()
    bottom_line.blitme()
    bricks.draw(screen)

    # Draw the score information.    
    sb.show_score()

    # Draw the play button if the game is inactive.
    if not stats.game_active:        
        title.blitme()
        play_button.draw_button()
    
    # Make the most recently drawn screen visible.
    pygame.display.flip()

def get_number_bricks_x(ai_settings, brick_width):
    #Determine the number of bricks that fit in a row.
    available_space_x = ai_settings.screen_width - 2 * brick_width
    number_bricks_x = int(available_space_x / (brick_width))
    return number_bricks_x

def get_number_rows(ai_settings, brick_height):
    # Determine the number of rows of bricks that fit on the screen.
    available_space_y = (ai_settings.screen_height - (3 * brick_height))   
    number_rows = int(available_space_y / (2 * brick_height))    
    return number_rows

def create_brick(ai_settings, screen, bricks, brick_number, row_number):
    # Create a brick and place it in the row
    brick = Brick(ai_settings, screen)
    brick_width = brick.rect.width

    brick.x = brick_width + brick_width * brick_number        
    brick.rect.x = brick.x
    brick.rect.y = brick.rect.height + 1 * brick.rect.height * row_number      
    bricks.add(brick)

def create_rowbricks(ai_settings, screen, bricks):    
    # Create a full row of bricks.
    # Create an brick and find the number of bricks in a row.    
    brick = Brick(ai_settings, screen)
    number_bricks_x = get_number_bricks_x(ai_settings, brick.rect.width)
    number_rows = get_number_rows(ai_settings, brick.rect.height)
    
    # Create the first row of bricks.
    for row_number in range(number_rows):
        for brick_number in range(number_bricks_x):        
            create_brick(ai_settings, screen, bricks, brick_number, row_number)

def check_high_score(stats, sb):
    # Check to see if there's a new high score.
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        f = open("highscore.txt", "w")
        f.write(str(stats.high_score))
        sb.prep_high_score()
        