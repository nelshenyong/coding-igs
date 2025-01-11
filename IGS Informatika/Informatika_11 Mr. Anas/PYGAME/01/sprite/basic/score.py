import pygame
import os

class Score:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.game = game
        self.score = 0
        self.high_score = 0
        self.color = (9, 16, 87)
        self.font_size = 30
        self.font = pygame.font.Font(None, self.font_size)

    def increase(self, amount=10):
        self.score += amount

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0

    def show(self):
        high_score_text = self.font.render(f"High Score: {self.high_score}", True, self.color)
        score_text = self.font.render(f"Score: {self.score}", True, self.color)
       
        score_rect = score_text.get_rect()
        score_rect.midtop = (self.screen_rect.centerx, 10) 
        high_score_rect = high_score_text.get_rect()
        high_score_rect.midtop = (self.screen_rect.centerx, score_rect.bottom + 5)
        self.game.screen.blit(high_score_text, high_score_rect)
        self.game.screen.blit(score_text, score_rect)
        

