import pygame
import sys

class TargetPracticeGame:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((500, 800))
        pygame.display.set_caption("Target Practice")
        self.clock = pygame.time.Clock()
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start game"""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
                
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    targetPracticeGame = TargetPracticeGame()
    targetPracticeGame.run_game()
