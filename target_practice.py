import pygame
import sys

from settings import Settings
from target import Target
from shooter import Shooter

class TargetPracticeGame:
    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Target Practice")
        self.clock = pygame.time.Clock()
        self.target = Target(self)
        self.shooter = Shooter(self)

    def run_game(self):
        """Start game"""
        while True:
            # Watch for keyboard and mouse events
            self._check_events()

            self.target.update()
            self.shooter.update()

            self._render_elements()
            
    def _render_elements(self):
        self.screen.fill(self.settings.bg_color)
        self.target.blitme()
        self.shooter.blitme()
        pygame.display.flip()
        self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event):
        if event.key == pygame.K_DOWN:
            self.shooter.move_down = False
        elif event.key == pygame.K_UP:
            self.shooter.move_up = False

    def _check_keydown_events(self, event):
        if event.key == pygame.K_DOWN:
            self.shooter.move_down = True
        elif event.key == pygame.K_UP:
            self.shooter.move_up = True

if __name__ == '__main__':
    targetPracticeGame = TargetPracticeGame()
    targetPracticeGame.run_game()
