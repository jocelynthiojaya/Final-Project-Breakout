import pygame

class Bat(pygame.sprite.Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()

        # Initialize the bat and set its starting position.
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Load the bat image and get its rect.
        self.image = pygame.image.load('images/bat.bmp') 
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Start each new bat at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx        
        self.rect.bottom = self.screen_rect.bottom - 25

        # Store a decimal value for the bat's center.
        self.center = float(self.rect.centerx)

        # Movement flag 
        self.moving_right = False
        self.moving_left = False
    
    def update(self):        
        # Update the bsts's position based on the movement flags.
        # Update the ship's center value, not the rect. 
        if self.moving_right and self.rect.right < self.screen_rect.right:            
            self.center += self.ai_settings.bat_speed_factor
        if self.moving_left and self.rect.left > 0:            
            self.center -= self.ai_settings.bat_speed_factor
        
        # Update rect object from self.center.
        self.rect.centerx = self.center
        
    def blitme(self):        
        # Draw the bat at its current location.
        self.screen.blit(self.image, self.rect)