import pygame
import os

from conf import Conf

class Playbutton:

    def  __init__(self,Game):
        self.Screen = Game.screen
        self.Screen_rect = Game.screen_rect

        image_path = os.path.join(Conf.BASE_DIR,"assets","play.png")
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

        self.image = pygame.transform.scale(self.image,(self.rect.width//10,  self.rect.height//10))
        self.rect = self.image.get_rect()

        self.rect.center = self.Screen_rect.center
        self.rect.y += 100

    def show(self):
        self.Screen.blit(self.image,self.rect)

class Button:
    def __init__(self, Game, text):
        self.screen = Game.screen
        self.screen_rect = Game.screen_rect

        # Increase button size for better clickability
        width = max(200, (len(text) + 4) * Conf.BUTTON_FONT_SIZE)
        height = Conf.BUTTON_HEIGHT + 20  # Make buttons taller
        
        self.rect = pygame.Rect(0, 0, width, height)
        self.font_path = os.path.join(Conf.BASE_DIR, "assets/fonts", Conf.FONT_FAMILY)
        self.color = Conf.BUTTON_COLOR
        self.hover_color = (150, 255, 50)  # Lighter color for hover effect
        self.is_hovered = False
        self.text_to_image(text)

    def text_to_image(self, text):
        self.font = pygame.font.Font(self.font_path, Conf.BUTTON_FONT_SIZE)
        self.text_image = self.font.render(text, True, Conf.FONT_COLOR)
        
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def show(self):
        # Draw button with hover effect
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(self.screen, color, self.rect, border_radius=10)  # Rounded corners
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect, 2, border_radius=10)  # Border
        
        # Draw text
        self.screen.blit(self.text_image, self.text_image_rect)
