import pygame
import os
from conf import Conf

class Bird():

    def __init__(self, Game):
        self.screen = Game.screen
        self.screen_rect = Game.screen_rect
        
        image_path = os.path.join(Conf.BASE_DIR, "assets", "burung.png")
        self.image = pygame.image.load(image_path)
        self.original_image = self.image  # Save the original image for rotation
        self.rect = self.image.get_rect()
        self.fly = False
        self.pass_pipe = False
        self.rotation_angle = 0  # Rotation angle for the bird

        # Start position of the bird
        self.rect.center = self.screen_rect.center

    def move(self):
        # Move the bird up if flying, otherwise let gravity pull it down
        if self.fly:
            self.rect.y -= Conf.BIRD_FLY_SPEED
            # Tilt the bird up to a max of -30 degrees when flying
            self.rotation_angle = max(-30, self.rotation_angle - 5)
        else:
            self.rect.y += Conf.GRAVITY
            # Gradually tilt the bird down to a max of 30 degrees when falling
            self.rotation_angle = min(30, self.rotation_angle + 3)

    def show(self):
        # Rotate the image and update rect position based on rotation
        rotated_image = pygame.transform.rotate(self.original_image, self.rotation_angle)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        self.screen.blit(rotated_image, rotated_rect)
