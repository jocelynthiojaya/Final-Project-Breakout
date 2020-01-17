import pygame
BLACK = (0,0,0)
RED = (255,0,0)
 
class BottomLine(pygame.sprite.Sprite):
    
    def __init__(self, ai_settings, screen):
        super().__init__()

        # Initialize screen and ai_settings
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Load the bottomline image and get its rect and screen rect.
        self.image = pygame.image.load('images/bottom line.bmp') 
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # position bottomline at the bottom, below the screen.
        self.image_height = 10
        self.rect.centerx = self.screen_rect.centerx        
        self.rect.bottom = self.screen_rect.bottom + self.image_height
    
    def blitme(self):        
        # Draw the bottomline at its current location.
        self.screen.blit(self.image, self.rect)