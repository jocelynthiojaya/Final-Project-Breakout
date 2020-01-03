import pygame
from random import randint
 
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

        self.velocity = [randint(1,1),randint(-1,1)]
        #self.velocity =[-1,1]
        
        self.rect.x = self.screen_rect.centerx 
        self.rect.y = self.screen_rect.bottom -55
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        if self.rect.x>=self.screen_rect.right:
            self.velocity[0] = -self.velocity[0]
        if self.rect.x<=0:
            self.velocity[0] = -self.velocity[0]
        if self.rect.y>self.screen_rect.bottom:
            self.velocity[1] = -self.velocity[1]
        if self.rect.y<0:
            self.velocity[1] = -self.velocity[1] 
    
    def bat_collision(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-1,1)
    
    def brick_collision(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-1,1)
    
    def blitme(self): 
        self.screen.blit(self.image, self.rect)
    
    def center_ball(self):        
        # Center the ship on the screen.
        self.rect.x = self.screen_rect.centerx 
        self.rect.y = self.screen_rect.bottom -55