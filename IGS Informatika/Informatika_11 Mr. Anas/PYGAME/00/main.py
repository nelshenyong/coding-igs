import sys
import pygame

pygame.init()

screen = pygame.display.set_mode([500, 500])
screen_rect = screen.get_rect()

bird = pygame.image.load("assets/bird.png")
bird_rect = bird.get_rect()
bird_rect.center = screen_rect.center

platform = pygame.image.load("assets/land.png")
platform = pygame.transform.scale(platform, (2 * screen_rect.width, platform.get_height()))
platform_rect = platform.get_rect()
platform_rect.midbottom = screen_rect.midbottom

life = pygame.image.load("assets/life.png")
life_rect = life.get_rect()
life_rect.topleft = (screen_rect.left + 10, screen_rect.top + 10)

pipe_top = pygame.Rect(0, 0, 0.15*screen_rect.width, 0.4*screen_rect.height)
pipe_top.topright = screen_rect.topright
pipe_head_top = pygame.Rect(0, 0, 1.2*pipe_top.width, 0.15*pipe_top.height)
pipe_head_top.midbottom = pipe_top.midbottom

pipe_bottom = pygame.Rect(0, 0, 0.15*screen_rect.width, 0.4*screen_rect.height)
pipe_head_bottom = pygame.Rect(0, 0, 1.2 *pipe_bottom.width, 0.15*pipe_bottom.height)
pipe_bottom.bottomright = screen_rect.bottomright
pipe_head_bottom.midtop = pipe_bottom.midtop

def setup_screen():
    screen.fill((107, 53, 235))

def show_bird():
    screen.blit(bird, bird_rect)
    
bird_fly = False

def move_bird():
    global bird_fly
    if bird_fly:
        bird_rect.y -= 3
    else:
        bird_rect.y += 1

def draw_pipe():
    global pipe_top, pipe_head_top, pipe_bottom, pipe_head_bottom
    pipe_top.x -= 5
    pipe_head_top.x -= 5
    pipe_bottom.x -= 5
    pipe_head_bottom.x -= 5

    if pipe_top.right < 0:
        pipe_top.left = screen_rect.right
        pipe_bottom.left = screen_rect.right
        pipe_head_top.centerx = pipe_top.centerx
        pipe_head_bottom.centerx = pipe_bottom.centerx

    pygame.draw.rect(screen, (0, 200, 0), pipe_top)
    pygame.draw.rect(screen, (0, 200, 0), pipe_head_top)
    pygame.draw.rect(screen, (0, 200, 0), pipe_bottom)
    pygame.draw.rect(screen, (0, 200, 0), pipe_head_bottom)
    
def show_platform():
    screen.blit(platform, platform_rect)

def move_platform():
    platform_rect.x -= 5
    if platform_rect.centerx <= 0:
        platform_rect.left = screen_rect.left

def show_heart():
    screen.blit(life, life_rect)

def setup_fps():
    pygame.time.Clock().tick(25)
    pygame.display.flip()
    
def check_event():
    global bird_fly
    
    for every_event in pygame.event.get():
        if every_event.type == pygame.QUIT:
            sys.exit()
        
        elif every_event.type == pygame.KEYDOWN:
            if every_event.key == pygame.K_SPACE:
                bird_fly = True
        elif every_event.type == pygame.KEYUP:
            if every_event.key == pygame.K_SPACE:
                bird_fly = False

def loop():
    while True:
        setup_screen()
        show_bird()
        draw_pipe()
        show_heart()
        show_platform()
        move_platform()
        move_bird()
        setup_fps()
        check_event()

if __name__ == '__main__':
    loop()