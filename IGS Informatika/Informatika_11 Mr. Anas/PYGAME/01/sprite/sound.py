import os 
import pygame

from conf import Conf

class Sound():
    def __init__(self, Game):
        self.game = Game
        self.is_muted = False
        sound_path = os.path.join(Conf.BASE_DIR, "assets", "year.mp3")
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.set_volume(Conf.SET_VOLUME)
        
    def play(self):
        if not self.is_muted:
            pygame.mixer.music.play(-1) 
    
    def mute(self):
        self.is_muted = True
        pygame.mixer.music.pause()

    def unmute(self):
        self.is_muted = False  # Unmute the music
        pygame.mixer.music.unpause()


