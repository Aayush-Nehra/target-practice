import pygame

class Target:
    def __init__(self, target_practice) -> None:
        self.settings = target_practice.settings
        self.screen = target_practice.screen

        self.image = pygame.transform.scale_by(
            pygame.image.load("images/target_dummy.png").convert_alpha(),2)  
        self.rect = self.image.get_rect()

        self.bounding_rect = self.image.get_bounding_rect()
        self.trimmed_image = pygame.Surface(self.bounding_rect.size, pygame.SRCALPHA)
        self.trimmed_image.blit(self.image,(0,0), self.bounding_rect)

        self.bounding_rect.topright = (self.screen.get_width(), 0)
        print(self.bounding_rect)

    def blitme(self):
        self.screen.blit(self.trimmed_image, self.bounding_rect)