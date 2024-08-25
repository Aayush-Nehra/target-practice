import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, target_practice_game) -> None:
        super().__init__()
        self.screen = target_practice_game.screen
        self.settings = target_practice_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0,0,self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = target_practice_game.shooter.rect.midright
        self.rect.y = self.rect.y + 16
        self.rect.x = self.rect.x + 10

        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet to right of the screen"""
        #Update the exact postion of the bullet
        self.x += self.settings.bullet_speed
        #Update the rect position
        self.rect.x = self.x
    
    def draw_bullet(self):
        """Draw bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect) 
