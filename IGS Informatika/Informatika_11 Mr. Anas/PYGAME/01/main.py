import sys
import pygame
import os
from random import choice

from conf import Conf
from statistic import Statistic
from sprite.plat import plat
from sprite.bird import Bird
from sprite.pipe import Pipe
from sprite.life import Life
from sprite.basic.score import Score
from sprite.skin_selector import SkinSelector

from sprite.sound import Sound
from sprite.basic.label import Label
from sprite.basic.button import Playbutton,Button
from sprite.basic.entry import Entry
from sprite.mutebutton import MuteButton


  
class Game:

    pygame.init()
    screen = pygame.display.set_mode(Conf.SCREEN_SIZE)
    screen_rect = screen.get_rect()

    def __init__(self):
        self.game_title_label = Label(self,"FLAPPY BIRD")
        #self.player_entry = Entry (self,"player")
        self.login_button = Button(self, "MASUK")
        # self.play_button = Playbutton(self)
        self.play_button = Button(self,"PLAY NOW")
        self.play_again_button = Button(self,"PLAY AGAIN")
        self.exit_button = Button(self,"EXIT")
        self.skin_button = Button(self, "CHANGE SKIN")
        self.reposition_buttons()
        self.plat = plat(self)
        self.bird = Bird(self)
        self.life = Life(self)
        self.score = Score(self)
        self.pipes = [Pipe(self,position) for position in["top","bottom"]]
        self.sound = Sound(self)
        self.sound.play()
        self.mutebutton = MuteButton(self) 
        self.skin_selector = SkinSelector(self)
        #self.play_backsound("sound.mp3")
    #def play_backsound(self,song):
        #pygame.mixer.music.load(os.path.join(Conf.BASE_DIR, "assets/sound", "sound.mp3"))
        #pygame.mixer.music.set_volume(.05)
        #pygame.mixer.music.play(loops =-1)

    def reposition_buttons(self):
        # Position buttons vertically with proper spacing
        center_x = self.screen_rect.centerx
        start_y = self.screen_rect.centery + 50
        
        # Home screen buttons
        self.login_button.rect.centerx = center_x
        self.login_button.rect.centery = start_y
        self.login_button.text_image_rect.center = self.login_button.rect.center
        
        self.play_button.rect.centerx = center_x
        self.play_button.rect.centery = start_y + 70
        self.play_button.text_image_rect.center = self.play_button.rect.center
        
        self.skin_button.rect.centerx = center_x
        self.skin_button.rect.centery = start_y + 140
        self.skin_button.text_image_rect.center = self.skin_button.rect.center
        
        # Game over screen buttons
        self.play_again_button.rect.centerx = center_x
        self.play_again_button.rect.centery = start_y
        self.play_again_button.text_image_rect.center = self.play_again_button.rect.center
        
        self.exit_button.rect.centerx = center_x
        self.exit_button.rect.centery = start_y + 70
        self.exit_button.text_image_rect.center = self.exit_button.rect.center

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.fly = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.bird.fly = False 

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if self.mutebutton.rect.collidepoint(mouse_pos):
                    self.mutebutton.toggle_mute()

                if Statistic.show_skin_selector:
                    self.check_skin_selector_buttons(mouse_pos)
                elif Statistic.intro:
                    self.check_onclick_login_button(mouse_pos)
                    if self.skin_button.rect.collidepoint(mouse_pos):
                        Statistic.show_skin_selector = True
                elif Statistic.play_again:
                    self.check_onclick_exit_button(mouse_pos)
                    self.check_onclick_play_again_button(mouse_pos)
                    if self.skin_button.rect.collidepoint(mouse_pos):
                        Statistic.show_skin_selector = True
                elif not Statistic.game_active:
                    self.check_onclick_play_button(mouse_pos)
                    if self.skin_button.rect.collidepoint(mouse_pos):
                        Statistic.show_skin_selector = True

    def check_onclick_login_button(self, mouse_pos):
        if self.login_button.rect.collidepoint(mouse_pos):
            Statistic.intro = False
    def check_onclick_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            Statistic.game_active =True
          
    def check_onclick_exit_button(self, mouse_pos):
        if self.exit_button.rect.collidepoint(mouse_pos):
            sys.exit()
    def check_onclick_play_again_button(self,mouse_pos):
        if self.play_again_button.rect.collidepoint(mouse_pos):
            Statistic.life -= 1
            self.reset_pipes()
            self.bird.rect.center = self.screen_rect.center
            Statistic.play_again = False
            Statistic.game_active = True
            self.score.reset()

    def check_bird_get_point(self):
        for pipe in self.pipes:
            if pipe.rect.centerx <= self.bird.rect.centerx and not self.bird.pass_pipe:
                self.bird.pass_pipe = True
                self.score.increase(10) 
                #Statis.score += 10  # increase score
                #Statis.score = self.score.score
               # if Statis.high_score < Statis.score:
                   # Statis.high_score =Statis.score
                print("score : ", self.score.score)#statis.score

    def check_bird_hit_pipe_or_platform(self):
        collision_pipes = pygame.sprite.spritecollideany(self.bird, self.pipes)
        collision_platform = pygame.Rect.colliderect(self.bird.rect, self.plat.rect)

        if collision_pipes or collision_platform:
           Statistic.game_active = False
           Statistic.play_again = True
    def set_fps(self):
        pygame.time.Clock().tick(Conf.FPS)
        pygame.display.flip()
    
    def reset_pipes(self):
        #self.pipes[0].rect.topleft = self.screen_rect.topright
        #self.pipes[1].rect.bottomleft = self.screen_rect.bottomright

        random_height= choice([25, 50, 75, 100, 125, 150])
    
        minimum_height = self.plat.rect.height + (0.1*self.screen_rect.height)
        new_height_bottom = minimum_height + random_height
        new_height_top = self.screen_rect.height - new_height_bottom - self.screen_rect.height//5
        self.pipes[0].rect = pygame.Rect(self.screen_rect.right, 0, 0.10 * self.screen_rect.width, new_height_top)
        self.pipes[1].rect = pygame.Rect(self.screen_rect.right, new_height_top + self.screen_rect.height // 5, 0.10 * self.screen_rect.width, new_height_bottom)

    # Update head positions
        self.pipes[0].head_rect.midbottom = self.pipes[0].rect.midbottom  # Top pipe head
        self.pipes[1].head_rect.midtop = self.pipes[1].rect.midtop  


    
    def game_intro(self):
        self.game_title_label.show()
        self.login_button.show()
        self.skin_button.show()
        self.life.show() 
        self.mutebutton.show()

    def game_play(self):
        if Statistic.show_skin_selector:
            self.skin_selector.show()
        else:
            self.bird.show()
            for pipe in self.pipes:
                pipe.show()
            self.plat.show()
            self.life.show()
            self.mutebutton.show()
            self.score.show()
        

        if not Statistic.game_active and not Statistic.play_again:
            self.game_title_label.show()
            self.play_button.show()
            self.skin_button.show()
        elif Statistic.play_again:
            self.play_again_button.show()
            self.exit_button.show()
            self.skin_button.show()
        elif Statistic.game_active:
            self.update_bird_activity()
            self.update_pipes_activity()
            self.update_platform_activity()
        
    def update_bird_activity(self):
        self.bird.move()
        self.check_bird_get_point()
        self.check_bird_hit_pipe_or_platform()

    def update_pipes_activity(self):
        for pipe in self.pipes:
            if pipe.rect.right <= 0:
                self.reset_pipes()
                self.bird.pass_pipe = False
            pipe.move()

    def update_platform_activity(self):
        self.plat.move()

    def loop(self):
        while True:
            self.screen.fill(Conf.SCREEN_BG_COLOR)

            if Statistic.intro:
                self.game_intro()
            else :
                self.game_play()
                pygame.display.flip()
        
            self.set_fps() 
            self.check_event()

    def check_skin_selector_buttons(self, mouse_pos):
        if self.skin_selector.prev_button.rect.collidepoint(mouse_pos):
            self.skin_selector.prev_skin()
        elif self.skin_selector.next_button.rect.collidepoint(mouse_pos):
            self.skin_selector.next_skin()
        elif self.skin_selector.select_button.rect.collidepoint(mouse_pos):
            self.bird.change_skin(self.skin_selector.get_current_skin())
            Statistic.show_skin_selector = False
        elif self.skin_selector.back_button.rect.collidepoint(mouse_pos):
            Statistic.show_skin_selector = False

if __name__ == "__main__":
    game = Game()
    game.loop()
     
      