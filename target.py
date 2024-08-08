import pygame
from utility import _get_scaled_image

class Target:
    def __init__(self, target_practice) -> None:
        self.settings = target_practice.settings
        self.screen = target_practice.screen
        self.screen_rect = self.screen.get_rect()

        self.image = _get_scaled_image("images/target_dummy.png", 3) 
        self.rect = self.image.get_rect()
        self.rect.topright = (self.screen.get_width(), 0)

        # +1 represents down, -1 represents up
        self.target_direction = 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self._update_direction()
        self.rect.y += self.settings.target_speed * self.target_direction
        
    def _update_direction(self):
        if self.rect.y <= 0: 
            self.target_direction = 1
        elif self.rect.y >= self.screen_rect.height - self.rect.height:
            self.target_direction = -1

   