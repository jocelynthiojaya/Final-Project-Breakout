import sys
import pygame

from brick import Brick
from ball import Ball

def check_keydown_events(event, bat):
    # Respond to keypresses
    if event.key == pygame.K_RIGHT:
        bat.moving_right = True
    elif event.key == pygame.K_LEFT:
        bat.moving_left = True

def check_keyup_events(event, bat):
    # Respond to key releases
    if event.key == pygame.K_RIGHT:
        bat.moving_right = False
    elif event.key == pygame.K_LEFT:
        bat.moving_left = False

def check_events(bat):    
    # Respond to keypresses and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:            
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, bat)
        
        elif event.type == pygame.KEYUP:            
            check_keyup_events(event, bat)

def is_collision_bat(ball, bat):
    return ball.rect.colliderect(bat.rect)

def collision_brick(ball, bricks):
    #score = 0
    # detect collisions
    for brick in pygame.sprite.spritecollide(ball, bricks, True): 
        ball.brick_collision()
    #for brick in bricks_hit_list:
    #    score += 1
    #    print(score)

def update_screen(ai_settings, screen, bat, ball, bricks):    
    # Update images on the screen and flip to the new screen.
    # Redraw the screen during each pass through the loop.    
    screen.fill(ai_settings.bg_color)    
    bat.blitme()
    ball.blitme()
    bricks.draw(screen)
    
    # Make the most recently drawn screen visible.
    pygame.display.flip()

def get_number_bricks_x(ai_settings, brick_width):
    #Determine the number of aliens that fit in a row.
    available_space_x = ai_settings.screen_width - 2 * brick_width
    number_bricks_x = int(available_space_x / (brick_width))
    return number_bricks_x

def get_number_rows(ai_settings, brick_height):
    # Determine the number of rows of aliens that fit on the screen.
    available_space_y = (ai_settings.screen_height - (8 * brick_height))   
    number_rows = int(available_space_y / (2 * brick_height))    
    return number_rows

def create_brick(ai_settings, screen, bricks, brick_number, row_number):
    # Create a brick and place it in the row
    brick = Brick(ai_settings, screen)
    brick_width = brick.rect.width

    brick.x = brick_width + brick_width * brick_number        
    brick.rect.x = brick.x
    brick.rect.y = brick.rect.height + 1.5 * brick.rect.height * row_number      
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

             
        