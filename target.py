import pygame

class Target:
    def __init__(self, target_practice) -> None:
        self.settings = target_practice.settings
        self.screen = target_practice.screen
        self.screen_rect = self.screen.get_rect()

        self.image = self._get_image() 
        self.rect = self.image.get_rect()
        self.rect.topright = (self.screen.get_width(), 0)

        # +1 represents down, -1 represents up
        self.target_direction = 1

    def blitme(self):
        self.screen.blit(self.trimmed_image, self.rect)

    def update(self):
        self._update_direction()
        self.rect.y += self.settings.target_speed * self.target_direction
        
    def _update_direction(self):
        if self.rect.y <= 0: 
            self.target_direction = 1
        elif self.rect.y >= self.screen_rect.height - self.rect.height:
            self.target_direction = -1

    def _get_image(self):
        self.image = pygame.transform.scale_by(
            pygame.image.load("images/target_dummy.png").convert_alpha(),3) 
        self.rect = self.image.get_bounding_rect()
        self.trimmed_image = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        self.trimmed_image.blit(self.image,(0,0), self.rect)
        return self.trimmed_image