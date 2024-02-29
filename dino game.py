import random

import pygame


def music_player():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()


def sandgen(sand_count, dino_x, dino_y, RL):
    sandlist = []
    sandcolor = [YELLOW, ORANGE]
    sandsize = 5
    sand_area = (100, 50)
    sandreaction = 20
    dx = -50
    if RL == 1:
        dx = 70
    for i in range(sand_count):
        pygame.draw.rect(screen, random.choice(sandcolor),
                         (dino_x + dx + random.randint(-sandreaction, sandreaction),
                          dino_y - random.randint(0, 20), sandsize, sandsize))


SW = 800
SH = 600
x = SW // 2
y = SH // 2
# RAD = 100
cac_speed = 5
dino_speed = 5
Dy = 0
Dx = 0
ground = 500
on_ground = True
on_jump = False
air = 250
jump = 0
# Djump = 2
LEFT = 1
RIGHT = 0
move = RIGHT
frame = 0
# mimi_frame = 0
moving = False
WHITE = (255, 255, 255)
invincible_timer = 0
fps = 60
invincible_ui = ""
surv_time = 0
top_surv_time = 0

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
DARK_YELLOW = (25, 25, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 100, 0)
ORANGE = pygame.color.Color("Orange")

screen = pygame.display.set_mode((SW, SH))

running = False
background = (0, 150, 150)
screen.fill(background)
timer = pygame.time.Clock()
start = True

pygame.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

sound_buttons = []
button = pygame.image.load('Mute-Sound-PNG-Clipart.png')
button = pygame.transform.scale(button, (50, 50))
sound_buttons.append(button)
button = pygame.image.load('sound_on.png')
button = pygame.transform.scale(button, (50, 50))
sound_buttons.append(button)
button_rect = button.get_rect()
button_rect.center = (30, 30)

sound1 = pygame.mixer.Sound('saber-crushing-blow.mp3')
sound1.set_volume(0.1)

coin_sfx = pygame.mixer.Sound('resources/coin_pick_up.mp3')
coin_sfx.set_volume(0.2)

dino_walk_list = [[], []]  # 1 направление, 2 номер кадра
for i in range(1, 11):
    dino = pygame.image.load('resources/walk' + str(i) + '.png')
    dino = pygame.transform.scale(dino, (100, 100))
    dino_walk_list[RIGHT].append(dino)
for i in range(1, 11):
    dino = pygame.image.load('resources/walk' + str(i) + '.png')
    dino = pygame.transform.scale(dino, (100, 100))
    dino = pygame.transform.flip(dino, True, False)
    dino_walk_list[LEFT].append(dino)
dino_rect = dino.get_rect()
dino_rect.x = 0
dino_rect.bottom = ground + 1
dino_rect.left = 200

desert = pygame.image.load('resources/desert.png')
desert_rect = desert.get_rect()

cac_list = []
cac = pygame.image.load('resources/cactus.png')
cac = pygame.transform.scale(cac, (70, 70))
for i in range(100, SW, 350):
    cac_rect = cac.get_rect()
    cac_rect.bottom = ground
    cac_rect.left = i
    cac_list.append(cac_rect)

ground_rect = (0, ground, SW, SH - ground)

# mini_dino_list = []
# mini_dino = pygame.image.load('resources/dino1.png')
# for i in range(0, 576, 24):
#     mini_dino_image_rect = pygame.Rect((i, 0, 24, 24))  # Рзметка прямоугольников картинки
#     mini_dino_image = mini_dino.subsurface(mini_dino_image_rect)  # Картинки
#     mini_dino_list.append(mini_dino_image)
# mini_dino_rect = mini_dino_image.get_rect()
# mini_dino_rect.bottom = ground + 1

coin_list = []
coin_in_inv = []
coin = pygame.image.load('coin.png')
coin = pygame.transform.scale(coin, (50, 50))
for i in range(50, 750, 100):
    coin_rect = coin.get_rect()
    coin_rect.bottom = ground + 1
    coin_rect.left = i
    coin_list.append(coin_rect)
coin_ui_rect = coin.get_rect()
coin_ui_rect.center = (770, 30)

shield = pygame.image.load('force_field.png')
shield = pygame.transform.scale(shield, (100, 100))
shield_rect = shield.get_rect()

# light = pygame.image.load('light (1).png')
# light = pygame.transform.scale(light, (200, 200))
# light_rect = light.get_rect()

font = pygame.font.SysFont('arial', 30)

start_text = font.render('Start', True, BLACK)
start_text_rect = start_text.get_rect()
start_text_rect.center = (SW // 2, 200)

quit_text = font.render('Exit', True, BLACK)
quit_text_rect = quit_text.get_rect()
quit_text_rect.center = (SW // 2, 400)

controls_text = font.render('W - Jump, A - Move left, D - Move right, SPACE - Mute/Unmute Music', True, BLACK)
controls_text_rect = controls_text.get_rect()
controls_text_rect.center = (SW // 2, 500)

while start:
    screen.fill(YELLOW)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False

        if event.type == pygame.MOUSEBUTTONDOWN and start_text_rect.collidepoint(event.pos):
            start = False
            running = True

        if event.type == pygame.MOUSEBUTTONDOWN and quit_text_rect.collidepoint(event.pos):
            start = False

    # for x in range(0, SW, 20):
    #     pygame.draw.line(screen, GREEN, (x, 0), (x, SH), 10)
    #
    # filter_layer = pygame.surface.Surface((SW, SH))
    # filter_layer.fill(pygame.color.Color('Gray'))
    # light_rect.center = pygame.mouse.get_pos()
    # filter_layer.blit(light, light_rect)
    #
    # screen.blit(filter_layer, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
    screen.blit(start_text, start_text_rect)
    screen.blit(quit_text, quit_text_rect)
    screen.blit(controls_text, controls_text_rect)

    pygame.display.update()

while running:
    timer.tick(fps)

    if len(coin_list) == 0:
        surv_time += 1

    if invincible_timer > 0:
        invincible_timer -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
            music_player()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and on_ground:
                on_ground = False
                on_jump = True
                dino_rect.bottom -= 1
            if event.key == pygame.K_d:
                Dx = dino_speed
                moving = True
                move = RIGHT
            if event.key == pygame.K_a:
                Dx = -dino_speed
                move = LEFT
                moving = True
            if event.key == pygame.K_SPACE:
                music_player()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                Dy = 0
            if event.key == pygame.K_d or event.key == pygame.K_a:
                Dx = 0
                moving = False

        # print(event)
    jump = 150 - (ground - dino_rect.bottom + 1) * 0.8
    # print(jump, ground - dino_rect.bottom)
    if (ground - dino_rect.bottom) < 0:
        dino_rect.bottom = ground + 1

    screen.blit(desert, desert_rect)
    for i in range(len(cac_list)):
        cac_list[i].x += cac_speed
        if cac_list[i].right > SW:
            cac_list[i].left = 0
        screen.blit(cac, cac_list[i])

    dino_rect.y += Dy
    dino_rect.x += Dx

    # light_rect.center = dino_rect.center
    # screen.blit(light, light_rect)

    screen.blit(dino_walk_list[move][frame], dino_rect)

    # screen.blit(mini_dino_list[mimi_frame], mini_dino_rect)

    screen.blit(sound_buttons[pygame.mixer.music.get_busy()], button_rect)

    screen.blit(coin, coin_ui_rect)

    coin_count = font.render(str(len(coin_in_inv)), True, BLACK)
    screen.blit(coin_count, (720, 12))

    invincible_text = font.render(invincible_ui, True, YELLOW)
    screen.blit(invincible_text, (550, 60))

    survived_text = font.render(f"ВРЕМЯ: {str(surv_time)}", True, GREEN)
    screen.blit(survived_text, (10, 60))

    top_survived_text = font.render(f"ЛУЧШЕЕ ВРЕМЯ: {str(top_surv_time)}", True, GREEN)
    screen.blit(top_survived_text, (10, 100))

    if invincible_timer != 0:
        invincible_ui = "НЕУЯЗВИМОСТЬ:" + str(invincible_timer)
        shield_rect.center = dino_rect.center
        screen.blit(shield, shield_rect)
    else:
        invincible_ui = ""

    for i in coin_list:
        screen.blit(coin, i)

    if frame < len(dino_walk_list[0]) - 1 and moving:
        frame += 1
    else:
        frame = 0

    # if mimi_frame < len(mini_dino_list) - 1:
    #     mimi_frame += 1
    # else:
    #     mimi_frame = 0

    if dino_rect.collidelistall(cac_list) and invincible_timer == 0:
        n = dino_rect.collidelistall(cac_list)
        if (cac_list[n[0]].right - dino_rect.left) < 10:
            dino_rect.left += 20
        elif (dino_rect.right - cac_list[n[0]].left) < 10:
            dino_rect.right -= 20
        dino_rect.y += 20
        invincible_timer = fps
        if surv_time > top_surv_time:
            top_surv_time = surv_time
            surv_time = 0
        # dino_rect.bottom -= 200
        # on_ground = False
        # print('cactus')

        for i in coin_in_inv:
            coin_list.append(i)
        # print(coin_list, "после выброса")
        coin_in_inv = []
        sound1.play()

    if dino_rect.colliderect(ground_rect):
        on_ground = True
        if moving:
            sandgen(20, dino_rect.centerx, dino_rect.bottom, move)

    if dino_rect.collidelistall(coin_list):
        coin_sfx.play()
        # print(dino_rect.collidelistall(cac_list))
        coin_collide = dino_rect.collidelistall(coin_list)
        # print(coin_collide, 'собираем')
        # print(coin_collide[0])
        coin_in_inv.append(coin_list.pop(coin_collide[0]))
        # print(coin_in_inv)

    if not on_ground:
        if on_jump and jump > 7:
            dino_rect.bottom -= 10
        else:
            on_jump = False
            dino_rect.bottom += 5

    pygame.display.update()
