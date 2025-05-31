import pygame
import os
from conf import Conf
from sprite.basic.button import Button

class SkinSelector:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.skins = ["burung.png", "bird_blue.png", "bird_red.png", "bird_yellow.png"]
        self.current_skin_index = 0
        
        # Create navigation buttons
        self.prev_button = Button(game, "◀ PREV")
        self.next_button = Button(game, "NEXT ▶")
        self.select_button = Button(game, "SELECT")
        self.back_button = Button(game, "BACK")
        
        # Position buttons
        center_x = self.screen_rect.centerx
        center_y = self.screen_rect.centery
        
        # Position preview area
        self.preview_rect = pygame.Rect(0, 0, 250, 250)  # Larger preview area
        self.preview_rect.center = (center_x, center_y - 30)
        
        # Position buttons around preview
        self.prev_button.rect.centerx = center_x - 180
        self.prev_button.rect.centery = center_y + 120
        self.prev_button.text_image_rect.center = self.prev_button.rect.center
        
        self.next_button.rect.centerx = center_x + 180
        self.next_button.rect.centery = center_y + 120
        self.next_button.text_image_rect.center = self.next_button.rect.center
        
        self.select_button.rect.centerx = center_x
        self.select_button.rect.centery = center_y + 120
        self.select_button.text_image_rect.center = self.select_button.rect.center
        
        self.back_button.rect.centerx = center_x
        self.back_button.rect.centery = center_y + 200
        self.back_button.text_image_rect.center = self.back_button.rect.center
        
        # Load preview image
        self.update_preview()
        
    def update_preview(self):
        skin_path = os.path.join(Conf.BASE_DIR, "assets", self.skins[self.current_skin_index])
        self.preview_image = pygame.image.load(skin_path)
        # Scale the preview image to fit the preview rect
        self.preview_image = pygame.transform.scale(self.preview_image, (self.preview_rect.width, self.preview_rect.height))
        
    def next_skin(self):
        self.current_skin_index = (self.current_skin_index + 1) % len(self.skins)
        self.update_preview()
        
    def prev_skin(self):
        self.current_skin_index = (self.current_skin_index - 1) % len(self.skins)
        self.update_preview()
        
    def get_current_skin(self):
        return self.skins[self.current_skin_index]
        
    def show(self):
        # Draw background overlay
        overlay = pygame.Surface((self.screen_rect.width, self.screen_rect.height))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(180)  # Darker overlay
        self.screen.blit(overlay, (0, 0))
        
        # Draw preview area background with gradient
        pygame.draw.rect(self.screen, (255, 255, 255), self.preview_rect, border_radius=20)
        pygame.draw.rect(self.screen, (0, 0, 0), self.preview_rect, 3, border_radius=20)
        
        # Show preview
        self.screen.blit(self.preview_image, self.preview_rect)
        
        # Update button hover states
        mouse_pos = pygame.mouse.get_pos()
        self.prev_button.check_hover(mouse_pos)
        self.next_button.check_hover(mouse_pos)
        self.select_button.check_hover(mouse_pos)
        self.back_button.check_hover(mouse_pos)
        
        # Show buttons
        self.prev_button.show()
        self.next_button.show()
        self.select_button.show()
        self.back_button.show()
        
        # Show title with shadow
        font = pygame.font.Font(os.path.join(Conf.BASE_DIR, "assets/fonts", Conf.FONT_FAMILY), Conf.FONT_SIZE)
        title = font.render("Select Bird Skin", True, (0, 0, 0))  # Shadow
        title_rect = title.get_rect()
        title_rect.centerx = self.screen_rect.centerx + 2
        title_rect.centery = self.screen_rect.centery - 220
        self.screen.blit(title, title_rect)
        
        title = font.render("Select Bird Skin", True, Conf.FONT_COLOR)  # Main text
        title_rect = title.get_rect()
        title_rect.centerx = self.screen_rect.centerx
        title_rect.centery = self.screen_rect.centery - 220
        self.screen.blit(title, title_rect)
        
        # Show skin name with shadow
        skin_name = self.skins[self.current_skin_index].replace('.png', '').replace('_', ' ').title()
        skin_font = pygame.font.Font(os.path.join(Conf.BASE_DIR, "assets/fonts", Conf.FONT_FAMILY), Conf.FONT_SIZE // 2)
        skin_text = skin_font.render(skin_name, True, (0, 0, 0))  # Shadow
        skin_rect = skin_text.get_rect()
        skin_rect.centerx = self.screen_rect.centerx + 1
        skin_rect.centery = self.screen_rect.centery + 70
        self.screen.blit(skin_text, skin_rect)
        
        skin_text = skin_font.render(skin_name, True, Conf.FONT_COLOR)  # Main text
        skin_rect = skin_text.get_rect()
        skin_rect.centerx = self.screen_rect.centerx
        skin_rect.centery = self.screen_rect.centery + 70
        self.screen.blit(skin_text, skin_rect) 