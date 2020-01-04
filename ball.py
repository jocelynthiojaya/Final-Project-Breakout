import pygame
import random
 
class Ball(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, ai_settings, screen):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Initialize the ball and set its starting position.
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ball image and get its rect.
        self.image = pygame.image.load('images/ball.png') 
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.x = self.screen_rect.centerx 
        self.rect.y = self.screen_rect.bottom -60

        self.change_x = random.randrange(-1, 2)
        self.change_y = random.randrange(-1, 2)
        
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

    def collision_wall(self):
        if self.rect.x>=self.screen_rect.right or self.rect.x<=0:
            self.change_x *= -1
        if self.rect.y>self.screen_rect.bottom or self.rect.y<0:
            self.change_y *= -1
    
    def bat_collision(self):
        self.change_x = random.randrange(-1, 2)
        self.change_y = - self.change_y
    
    def brick_collision(self):
        self.change_x = random.randrange(-1, 2)
        self.change_y = random.randrange(1, 2)
    
    def blitme(self): 
        self.screen.blit(self.image, self.rect)
    
    def center_ball(self):        
        # Center the ship on the screen.
        self.rect.x = self.screen_rect.centerx 
        self.rect.y = self.screen_rect.bottom -60