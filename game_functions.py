import sys

import pygame

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

def update_screen(ai_settings, screen, bat):    
    # Update images on the screen and flip to the new screen.
    # Redraw the screen during each pass through the loop.    
    screen.fill(ai_settings.bg_color)    
    bat.blitme()
    
    # Make the most recently drawn screen visible.
    pygame.display.flip()