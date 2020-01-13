import pygame
BLACK = (0,0,0)
RED = (255,0,0)

class Bat(pygame.sprite.Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()

        # Initialize the bat and set its starting position.
        self.screen = screen
        self.ai_settings = ai_settings
        
        self.width = ai_settings.bat_width
        self.height = ai_settings.bat_height

        # Pass in the color of the bat, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)
        self.image.set_colorkey(RED)
 
        # Draw the bat (a rectangle!)
        pygame.draw.rect(self.image, BLACK, [0, 0, self.width, self.height])
        
        # Get rect of image and screen.
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Start each new bat at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx        
        self.rect.bottom = self.screen_rect.bottom - 30

        # Store a decimal value for the bat's center.
        self.center = float(self.rect.centerx)

        # Movement flag 
        self.moving_right = False
        self.moving_left = False
    
    def update(self):        
        # Update the bats's position based on the movement flags.
        # Update the bat's center value, not the rect. 
        if self.moving_right and self.rect.right < self.screen_rect.right:            
            self.center += self.ai_settings.bat_speed_factor
        if self.moving_left and self.rect.left > 0:            
            self.center -= self.ai_settings.bat_speed_factor
        
        # Update rect object from self.center.
        self.rect.centerx = self.center
        
    def blitme(self):        
        # Draw the bat at its current location.
        self.screen.blit(self.image, self.rect)
    
    def center_bat(self):        
        # Center the bat on the screen.
        self.center = self.screen_rect.centerx