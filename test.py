import pygame
import random
import os

# constants
running = False
start = True
SW = 1280
SH = 633
LEFT = 1
RIGHT = 0
fps = 60
score = 0
ten_seconds = 0
frame = 0
# color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# physics consts misc
ground = 420
bg_speed = 7
# movement consts
on_ground = True
long_jump = False
short_jump = False
direction = None  # True - вверх, False - вниз
jump_speed = 20
time_down = 0
time_elapsed = 0

key = 0

# main game settings
screen = pygame.display.set_mode((SW, SH))
background = (0, 150, 150)
screen.fill(background)
timer = pygame.time.Clock()

pygame.init()
# sprites and rect
bg_list = []
desert = pygame.image.load('resources/desert.png')
for i in range(0, 1920, 960):
    desert_rect = desert.get_rect()
    desert_rect.bottom = SH
    desert_rect.left = i
    bg_list.append(desert_rect)

ground_rect = (0, ground, SW, SH - ground)

cac_onscreen_list = []
cac1 = pygame.image.load('dino sprites/cactus1-1.png')
cac1_rect = cac1.get_rect()
cac2 = pygame.image.load('dino sprites/cactus2-1.png')
cac2_rect = cac2.get_rect()
cac3 = pygame.image.load('dino sprites/cactus3-1.png')
cac3_rect = cac3.get_rect()

logo = pygame.image.load('dinosaur game ultra deluxe logo.png')
logo = pygame.transform.scale(logo, (1280, 633))
logo_rect = logo.get_rect()
logo_rect.center = (SW / 2, SH / 2)

dino_walk_list = []  # 1 направление, 2 номер кадра
for i in range(1, 3):
    dino = pygame.image.load('dino sprites/dino walk' + str(i) + '-1.png')
    dino = pygame.transform.scale(dino, (80, 80))
    dino_walk_list.append(dino)
dino_jump = pygame.image.load('dino sprites/dino jump-1.png')
dino_jump = pygame.transform.scale(dino_jump, (80, 80))
dino_rect = dino.get_rect()
dino_rect.x = 0
dino_rect.bottom = ground + 1
dino_rect.left = 100

font = pygame.font.SysFont('arial', 30)
pixel_font = pygame.font.SysFont('OCR A Extended', 30)

start_text = font.render('Start', True, BLACK)
start_text_rect = start_text.get_rect()
start_text_rect.center = (SW // 2, 375)

quit_text = font.render('Exit', True, BLACK)
quit_text_rect = quit_text.get_rect()
quit_text_rect.center = (SW // 2, 450)

controls_text = font.render('SPACE - Jump', True, BLACK)
controls_text_rect = controls_text.get_rect()
controls_text_rect.center = (SW // 2, 550)

# misc functions

while start:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False

        if event.type == pygame.MOUSEBUTTONDOWN and start_text_rect.collidepoint(event.pos):
            start = False
            running = True
            SW = 800
            SH = 600
            os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (200, 200)
            os.environ['SDL_VIDEO_CENTERED'] = '0'
            screen1 = pygame.display.set_mode((SW, SH))

        if event.type == pygame.MOUSEBUTTONDOWN and quit_text_rect.collidepoint(event.pos):
            start = False

        screen.blit(logo, logo_rect)
        screen.blit(start_text, start_text_rect)
        screen.blit(quit_text, quit_text_rect)
        screen.blit(controls_text, controls_text_rect)

        pygame.display.update()

while running:
    timer.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            time_elapsed = 0

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and on_ground:
            key += 1
            time_elapsed = (pygame.time.get_ticks() - time_down) / 1000.0
            print("number: ", key, "duration: ", time_elapsed)
            on_ground = False
            direction = True
            dino_rect.bottom -= 1
            # if time_elapsed < 0.2:
            #     short_jump = True
            # else:
            #     long_jump = True

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            time_down = pygame.time.get_ticks()

    for i in range(len(bg_list)):
        bg_list[i].x -= bg_speed
        if bg_list[i].right < 0:
            bg_list[i].left = SW
        screen1.blit(desert, bg_list[i])

    ten_seconds += 1
    if ten_seconds % 5 == 0:
        if frame < len(dino_walk_list) - 1:
            frame += 1
        else:
            frame = 0
    if ten_seconds == 10:
        score += 1
        ten_seconds = 0
    if ten_seconds % 1 == 0:
        if direction:
            jump_speed -= 1
        else:
            jump_speed = 20

    if on_ground:
        screen1.blit(dino_walk_list[frame], dino_rect)

    if not on_ground:
        screen1.blit(dino_jump, dino_rect)

    if dino_rect.colliderect(ground_rect):
        on_ground = True
        direction = None

    if (ground - dino_rect.bottom) < 0:
        dino_rect.bottom = ground + 1

    if not on_ground:
        if direction and dino_rect.top > 100:
            dino_rect.bottom -= jump_speed
        else:
            direction = False
            dino_rect.bottom += jump_speed

    score_text = pixel_font.render(f'{score}', True, BLACK)
    screen1.blit(score_text, (720, 12))

    pygame.display.update()
