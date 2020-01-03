import pygame
BLACK = (0,0,0)
RED = (255,0,0)
 
class BottomLine(pygame.sprite.Sprite):
    
    def __init__(self, ai_settings, screen):
        super().__init__()

        # Initialize the bat and set its starting position.
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Load the bat image and get its rect.
        self.image = pygame.image.load('images/bottom line.bmp') 
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Start each new bat at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx        
        self.rect.bottom = self.screen_rect.bottom + 10
    
    def blitme(self):        
        # Draw the alien at its current location.
        self.screen.blit(self.image, self.rect)