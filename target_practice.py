import pygame
import sys

from settings import Settings
from target import Target
from shooter import Shooter
from bullet import Bullet
from button import Button

class TargetPracticeGame:
    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Target Practice")
        self.clock = pygame.time.Clock()
        self.target = Target(self)
        self.shooter = Shooter(self)
        self.bullets = pygame.sprite.Group()
        #Keeps tracks of the bullets that did not hit the target
        self.target_missed = 0
        self.target_hit = 0

        #Start game in inactive state
        self.game_active = False
        
        #Make play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start game"""
        while True:
            # Watch for keyboard and mouse events
            self._check_events()
            if self.game_active:
                self.target.update()
                self.shooter.update()
                self._update_bullets()

            self._render_elements()

    def _update_bullets(self):
        self.bullets.update()
        #Get rid of bullets that have disappeared from the screen and
        #inrement the missed bullets
        for bullet in self.bullets.copy():
            if bullet.rect.right > self.settings.screen_width:
                self.bullets.remove(bullet)
                self.target_missed += 1
                print(self.target_missed)

        if self.target_missed == 3:
            self.game_active = False

        #Check if bullets have hit the target
        #If they have then delete the bullet
        for bullet in self.bullets.copy():
            if bullet.rect.colliderect(self.target.rect):
                self.bullets.remove(bullet)
                self.target_hit += 1
                print("Target Hit: ", self.target_hit)
            
    def _render_elements(self):
        self.screen.fill(self.settings.bg_color)
        self.target.blitme()
        self.shooter.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet() 
        if not self.game_active:
            self.play_button.draw_button()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when player clicks play"""
        if self.play_button.rect.collidepoint(mouse_pos):
            self.reset_game_options()

    def reset_game_options(self):
        self.target_hit = 0
        self.target_missed = 0
        self.game_active = True

        #Get rid of any remaining bullets
        self.bullets.empty()

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
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self.reset_game_options()

    def _fire_bullet(self):
        """Create a new bullet and add it to bullet group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

if __name__ == '__main__':
    targetPracticeGame = TargetPracticeGame()
    targetPracticeGame.run_game()
