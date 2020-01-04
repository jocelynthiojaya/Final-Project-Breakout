import pygame
BLACK = (0,0,0)
RED = (255,0,0)
 
class Brick(pygame.sprite.Sprite):
    
    def __init__(self, ai_settings, screen):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        #Initialize the alien and set its starting position.
        self.screen = screen        
        self.ai_settings = ai_settings

        self.width = 60
        self.height = 30

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the brick (a rectangle!)
        pygame.draw.rect(self.image, RED, [10, 10, self.width, self.height])
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
    
    def blitme(self):        # Draw the alien at its current location.
        self.screen.blit(self.image, self.rect)