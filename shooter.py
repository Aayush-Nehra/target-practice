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
        self.y = float(self.rect.y)
        self.move_down = False
        self.move_up = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.move_down and self.rect.bottom <= self.settings.screen_height:
            self.y += self.settings.shooter_speed
            #boundry condition
            if self.y > self.settings.screen_height - self.rect.height:
                self.y = self.settings.screen_height - self.rect.height
        if self.move_up and self.rect.top >= 0 :
            self.y -= self.settings.shooter_speed
            #boundry condition
            if self.y < 0:
                self.y = 0
        self.rect.y = self.y

