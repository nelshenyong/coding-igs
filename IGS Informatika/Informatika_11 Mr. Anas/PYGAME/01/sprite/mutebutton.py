import pygame
import os
from conf import Conf
from sprite.basic.button import Button

class MuteButton(Button):
    def __init__(self, game):
        super().__init__(game, "MUTE")
        self.is_muted = False
        self.game = game
        self.mute_image = pygame.image.load(os.path.join(Conf.BASE_DIR, "assets","mute1.jpg"))
        self.unmute_image = pygame.image.load(os.path.join(Conf.BASE_DIR, "assets","unmute.webp"))
        
        # Position the button at the top-right corner
        self.rect.topright = (self.game.screen_rect.width - 10, 5)
        self.update_image()  # Initialize with the correct image based on mute state

    def toggle_mute(self):
        # Toggle mute status
        self.is_muted = not self.is_muted
        if self.is_muted:
            self.game.sound.mute()
            #print("Audio is muted")
        else:
            self.game.sound.unmute()
            #print("Audio is unmuted")
        
        # Update the button image to match the new state
        self.update_image()

    def update_image(self):
        # Choose the correct image based on mute status
        if self.is_muted:
            self.image = pygame.transform.scale(self.mute_image, (40, 40))
        else:
            self.image = pygame.transform.scale(self.unmute_image, (40, 40))
        
        # Set the button's rect to match the new image
        self.image_rect = self.image.get_rect()
        self.image_rect.topright = self.rect.topright

    def show(self):
        # Blit the current image onto the screen
        self.game.screen.blit(self.image, self.image_rect)
