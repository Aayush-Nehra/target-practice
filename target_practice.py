import pygame
import sys

from settings import Settings
from target import Target

class TargetPracticeGame:
    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Target Practice")
        self.clock = pygame.time.Clock()
        self.target = Target(self)

    def run_game(self):
        """Start game"""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.target.blitme()

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    targetPracticeGame = TargetPracticeGame()
    targetPracticeGame.run_game()
