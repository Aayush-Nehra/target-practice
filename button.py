import pygame.font

class Button:
    def __init__(self, target_practice_game, txt) -> None:
        """A class to build buttons for game"""
        self.screen = target_practice_game.screen
        self.screen_rect = self.screen.get_rect()

        #Set the dimensions and properties of button
        self.width, self.height = 200, 50
        self.button_color = (0,125,0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #Create button rect and put it in the center of the screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_btn_text(txt)

    def _prep_btn_text(self, text):
        """Turn text inot a rendered image and center toext on the button"""
        self.msg_image = self.font.render(text, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
