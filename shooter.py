import pygame
from utility import _get_scaled_image

class Shooter:
    def __init__(self, target_practice) -> None:
        self.settings = target_practice.settings
        self.screen = target_practice.screen
        self.screen_rect = self.screen.get_rect()

        self.image = _get_scaled_image("images/shooter.png",0.2) 
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft

    def blitme(self):
        self.screen.blit(self.image, self.rect)