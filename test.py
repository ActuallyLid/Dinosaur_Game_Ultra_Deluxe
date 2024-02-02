import pygame
import random
import os
from but import Button

# constants
running = False
is_running = False
close = False
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
heart = 3

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

cac1 = pygame.image.load('dino sprites/cactus1-1.png')
cac1 = pygame.transform.scale(cac1, (50, 80))
cac1_rect = cac1.get_rect()
cac1_rect.left = SW
cac1_rect.bottom = ground
cac2 = pygame.image.load('dino sprites/cactus2-1.png')
cac2 = pygame.transform.scale(cac2, (100, 80))
cac2_rect = cac2.get_rect()
cac2_rect.left = SW
cac2_rect.bottom = ground
cac3 = pygame.image.load('dino sprites/cactus3-1.png')
cac3 = pygame.transform.scale(cac3, (150, 80))
cac3_rect = cac3.get_rect()
cac3_rect.left = SW
cac3_rect.bottom = ground

cac_list = [cac1_rect, cac2_rect, cac3_rect]
cac_onscreen = False
cac1_move = False
cac2_move = False
cac3_move = False

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


# misc
def move(n):
    pass


class Button:
    def __init__(self, x, y, width, height, text, action=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.action = action
        self.font = pygame.font.SysFont('Cooper Black', 35)

    def draw(self):
        global running, close, is_running
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if click[0] == 1 and self.action:
            self.action()
        else:
            pygame.draw.rect(screen, (243, 218, 26), (self.x, self.y, self.width, self.height))
        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            if self.text == 'Start':
                running = True
            elif self.text == 'Enter':
                is_running = True

        text_surface = self.font.render(self.text, True, (130, 130, 130))
        text_rect = text_surface.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
        screen.blit(text_surface, text_rect)


start_but = Button(50, 380, 105, 50, 'Start')
quit_but = Button(50, 460, 105, 50, 'Enter')
rule_but = Button(200, 380, 105, 50, 'Rules')
translate_but = Button(50, 530, 250, 50, 'Settings')
shop_but = Button(200, 460, 105, 50, 'Shop')

while start:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False

        if event.type == pygame.MOUSEBUTTONDOWN and running:
            start = False
            SW = 800
            SH = 600
            os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (200, 200)
            os.environ['SDL_VIDEO_CENTERED'] = '0'
            screen1 = pygame.display.set_mode((SW, SH))

        if event.type == pygame.MOUSEBUTTONDOWN and close:
            start = False

        screen.blit(logo, logo_rect)
        start_but.draw()
        quit_but.draw()
        rule_but.draw()
        translate_but.draw()
        shop_but.draw()

        pygame.display.update()

while running:
    timer.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            time_elapsed = 0

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and on_ground:
            on_ground = False
            direction = True
            dino_rect.bottom -= 1

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            time_down = pygame.time.get_ticks()

    # bg
    for i in range(len(bg_list)):
        bg_list[i].x -= bg_speed
        if bg_list[i].right < 0:
            bg_list[i].left = SW
        screen1.blit(desert, bg_list[i])

    # cactus
    if not cac_onscreen:
        if random.randint(0, 5) == 5:
            if random.randint(1, 3) == 1:
                cac_onscreen = True
                cac1_move = True
            if random.randint(1, 3) == 2:
                cac_onscreen = True
                cac2_move = True
            if random.randint(1, 3) == 3:
                cac_onscreen = True
                cac3_move = True

    if cac1_move:
        cac1_rect.x -= bg_speed
        screen1.blit(cac1, cac1_rect)
    if cac2_move:
        cac2_rect.x -= bg_speed
        screen1.blit(cac2, cac2_rect)
    if cac3_move:
        cac3_rect.x -= bg_speed
        screen1.blit(cac3, cac3_rect)

    for i in cac_list:
        if i.right < -20:
            i.left = SW
            cac_onscreen = False
            cac1_move = False
            cac2_move = False
            cac3_move = False

    # cac1_rect.x -= bg_speed
    # if cac1_rect.right < 0:
    #     cac1_rect.left = SW
    # screen1.blit(cac1, cac1_rect)

    # ten seconds at a time
    ten_seconds += 1
    if ten_seconds % 5 == 0:
        if frame < len(dino_walk_list) - 1:
            frame += 1
        else:
            frame = 0

    if ten_seconds % 10 == 0:
        score += 1

        if score >= 100 and score % 100 == 0:
            bg_speed += 1

    if ten_seconds % 1 == 0:
        if direction and dino_rect.bottom <= ground:
            jump_speed -= 1
        else:
            jump_speed = 20

    # dino physics
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

    # print(cac_onscreen_list_rect, cac_onscreen_list_pic)

    # misc
    score_text = pixel_font.render(f'{score}', True, BLACK)
    screen1.blit(score_text, (720, 12))

    pygame.display.update()
