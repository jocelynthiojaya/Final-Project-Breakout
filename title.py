import pygame

class Title():    
    def __init__(self, ai_settings, screen):
        # Initialize the title and set its starting position.
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the title image and get its rect.
        self.image = pygame.image.load('images/main.png') 
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.x = self.screen_rect.left + ai_settings.title_x
        self.rect.y = self.screen_rect.bottom +ai_settings.title_y
    
    def blitme(self): 
        # draw the title image
        self.screen.blit(self.image, self.rect)