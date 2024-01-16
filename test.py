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
ground = 420
fps = 60
bg_speed = 5
score = 0
ten_seconds = 0
# color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
frame = 0
on_ground = True

screen = pygame.display.set_mode((SW, SH))
background = (0, 150, 150)
screen.fill(background)
timer = pygame.time.Clock()

pygame.init()

bg_list = []
desert = pygame.image.load('resources/desert.png')
for i in range(0, 1920, 960):
    desert_rect = desert.get_rect()
    desert_rect.bottom = SH
    desert_rect.left = i
    bg_list.append(desert_rect)

cac_onscreen_list = []
cac1 = pygame.image.load('dino sprites/cactus1.png')
cac1_rect = cac1.get_rect()
cac2 = pygame.image.load('dino sprites/cactus2.png')
cac2_rect = cac2.get_rect()
cac3 = pygame.image.load('dino sprites/cactus3.png')
cac3_rect = cac3.get_rect()

try:
    logo = pygame.image.load('dinosaur game ultra deluxe logo.png')
except Exception as e:
    print("Logo image not found or is not png.")
logo = pygame.image.load('dinosaur game ultra deluxe logo.jpg')
logo = pygame.transform.scale(logo, (1280, 633))
logo_rect = logo.get_rect()
logo_rect.center = (SW / 2, SH/2)

dino_walk_list = []  # 1 направление, 2 номер кадра
for i in range(1, 3):
    dino = pygame.image.load('dino sprites/dino walk' + str(i) + '.png')
    dino = pygame.transform.scale(dino, (80, 80))
    dino_walk_list.append(dino)
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

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
            on_ground = False

    for i in range(len(bg_list)):
        bg_list[i].x -= bg_speed
        if bg_list[i].right < 0:
            bg_list[i].left = SW
        screen1.blit(desert, bg_list[i])

    ten_seconds += 1
    if ten_seconds == 10:
        if frame < len(dino_walk_list) - 1 and on_ground:
            frame += 1
        else:
            frame = 0

        score += 1
        ten_seconds = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(len(bg_list)):
        bg_list[i].x -= bg_speed
        if bg_list[i].right < 0:
            bg_list[i].left = SW
        screen1.blit(desert, bg_list[i])

    screen1.blit(dino_walk_list[frame], dino_rect)

    score_text = pixel_font.render(f'{score}', True, BLACK)
    screen1.blit(score_text, (720, 12))

    pygame.display.update()
