import pygame
import random
import os
import sqlite3
from button import ButtonSprite
import pygame_gui
from pygame_gui.elements.ui_text_entry_line import UITextEntryLine

pygame.init()

# constants

sound1 = pygame.mixer.Sound('resources/pryjok.mp3')
sound2 = pygame.mixer.Sound('resources/damage.mp3')
sound3 = pygame.mixer.Sound('resources/death.mp3')
sound4 = pygame.mixer.Sound('resources/coin_pick_up.mp3')
sound_of_my_life = pygame.mixer.Sound('resources/IW2BF.mp3')

pygame.mixer.music.load('resources/menumusic.mp3')
pygame.mixer.music.play(-1)
running = False
close = False
game_over = False
start = False
coin_factor = False
is_running = True

WHITE = (255, 255, 255)


pixel_font = pygame.font.SysFont('OCR A Extended', 30)
large_pixel_font = pygame.font.SysFont('OCR A Extended', 40)
medium_pixel_font = pygame.font.SysFont('OCR A Extended', 70)
big_pixel_font = pygame.font.SysFont('OCR A Extended', 100)


pygame.font.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((400, 300))

background_enter = pygame.Surface((400, 300))
background_enter.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((400, 300))
text_input = UITextEntryLine(relative_rect=pygame.Rect(125, 100, 150, 50), manager=manager)

hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 175), (100, 50)),
                                            text='Войти',
                                            manager=manager)

clock = pygame.time.Clock()


while is_running:

    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute('''DELETE FROM popytki''')
    con.commit()
    con.close()
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():

        if event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
            c = event.text
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                print(c)
                con = sqlite3.connect('users.db')
                cur = con.cursor()
                cur.execute('''INSERT INTO users(name,record,coins,skin1) VALUES('%s',0,0,0);''' % (c))

                con.commit()
                con.close()
                start = True
                is_running = False

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background_enter, (0, 0))
    manager.draw_ui(window_surface)
    score_text = pixel_font.render('Enter name', True, WHITE)
    window_surface.blit(score_text, (115, 60))

    pygame.display.update()



LEFT = 1
RIGHT = 0
fps = 60
coins = 0
score = 0
ten_seconds = 0
frame = 0
y0 = 50
# color constants
BLACK = (0, 0, 0)
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
heart = 5
invincible_timer = 0
sp_timer = 0
freddie_timer = 0
key = 0

# main game settings
SW = 1280
SH = 633
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (200, 200)
os.environ['SDL_VIDEO_CENTERED'] = '0'
screen = pygame.display.set_mode((SW, SH))
screen1 = pygame.display.set_mode((SW, SH))
background = (0, 150, 150)
screen.fill(background)
timer = pygame.time.Clock()

# sprites and rect
bg_list = []
desert = pygame.image.load('resources/desert.png')
for i in range(0, 1920, 960):
    desert_rect = desert.get_rect()
    desert_rect.bottom = SH
    desert_rect.left = i
    bg_list.append(desert_rect)

ground_rect = (0, ground, SW, SH - ground)

heart1_picture = pygame.image.load('heart1.png')
heart1_picture = pygame.transform.scale(heart1_picture, (30, 40))
heart1_picture_rect = heart1_picture.get_rect()
heart1_picture_rect.bottom = 50
heart1_picture_rect.top = 10
heart1_picture_rect.right = 35

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
cac3 = pygame.transform.scale(cac3, (100, 60))
cac3_rect = cac3.get_rect()
cac3_rect.left = SW
cac3_rect.bottom = ground

coinspic = pygame.image.load('resources/coin.png')
coinspic = pygame.transform.scale(coinspic, (40, 40))
coinspic_rect = coinspic.get_rect()
coinspic_rect.left = 610
coinspic_rect.top = 12
coin = pygame.image.load('resources/coin.png')


cac_list = [cac1_rect, cac2_rect, cac3_rect]
cac_onscreen = False
cac1_move = False
cac2_move = False
cac3_move = False

freddie = pygame.image.load('love_of_my_life.png')
freddie = pygame.transform.scale(freddie, (70, 90))
freddie_rect = freddie.get_rect()
freddie_rect.left = SW
freddie_rect.bottom = ground
freddie_onscreen = False
freddie_moving = False
freddie_score = [random.randint(15, 150), random.randint(250, 350), random.randint(450, 550),
                 random.randint(650, 850)]

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

# misc
SCORE = pygame.USEREVENT + 1
pygame.time.set_timer(SCORE, 100)
WALK = pygame.USEREVENT + 2
pygame.time.set_timer(WALK, 200)
JUMP = pygame.USEREVENT + 3
pygame.time.set_timer(JUMP, 15)
COINS = pygame.USEREVENT + 4
pygame.time.set_timer(COINS, 50)

buttons = pygame.sprite.Group()
start_button = ButtonSprite(buttons, 50, 380, 105, 50, "Start")
rule_button = ButtonSprite(buttons, 200, 380, 105, 50, 'Rules')
translate_button = ButtonSprite(buttons, 50, 530, 250, 50, 'Settings')


class Coins(pygame.sprite.Sprite):
    def __init__(self, coin):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(coin, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = SW
        self.rect.bottom = ground - 10

    def update(self):
        self.kill()


coin_object = Coins(coin)


def show_end_screen():

    screen1.fill(BLACK)
    you_lose = big_pixel_font.render('GAME OVER!', True, WHITE)
    screen1.blit(you_lose, (100, 30))
    your_coins = medium_pixel_font.render(f'Coins: {coins}', True, WHITE)
    screen1.blit(your_coins, (200, 300))
    your_points = medium_pixel_font.render(f'Score: {score}', True, WHITE)
    screen1.blit(your_points, (200, 350))
    retry = large_pixel_font.render(f'Press any key to retry', True, WHITE)
    screen1.blit(retry, (140, 430))

    waiting = True
    pygame.display.flip()
    while waiting:
        timer.tick(fps)
        for event1 in pygame.event.get():
            if event1.type == pygame.QUIT:
                pygame.quit()
            if event1.type == pygame.KEYUP:
                waiting = False


while start:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.rect.collidepoint(event.pos):
                print("Start Game")
                running = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load('resources/backgroundmusic.mp3')
                pygame.mixer.music.play(-1)
                start = False
                SW = 800
                SH = 600
                os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (200, 200)
                os.environ['SDL_VIDEO_CENTERED'] = '0'
                screen1 = pygame.display.set_mode((SW, SH))

            if rule_button.rect.collidepoint(event.pos):

                screen.fill(BLACK)
                for i in open('rules.txt').readlines():
                    rule = medium_pixel_font.render(f'{i}', True, WHITE)
                    screen.blit(rule, (20, y0))
                    y0 += 50

                waiting = True
                pygame.display.flip()
                while waiting:
                    timer.tick(fps)
                    for event1 in pygame.event.get():
                        if event1.type == pygame.QUIT:
                            pygame.quit()
                        if event1.type == pygame.KEYUP:
                            waiting = False
                            print("Start Game")
                            running = True
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load('resources/backgroundmusic.mp3')
                            pygame.mixer.music.play(-1)
                            start = False
                            SW = 800
                            SH = 600
                            os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (200, 200)
                            os.environ['SDL_VIDEO_CENTERED'] = '0'
                            screen1 = pygame.display.set_mode((SW, SH))
        if event.type == pygame.MOUSEBUTTONDOWN and close:
            start = False

        screen.blit(logo, logo_rect)

        buttons.draw(screen)

        pygame.display.update()

while running:
    timer.tick(fps)
    if invincible_timer > 0:
        invincible_timer -= 1
    if freddie_timer > 0:
        freddie_timer -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            time_elapsed = 0
        if event.type == SCORE:
            score += 1
            if score >= 100 and score % 100 == 0:
                bg_speed += 2
        if event.type == COINS:
            coin_factor = True
            coin_thing = True
        if event.type == WALK:
            if frame < len(dino_walk_list) - 1:
                frame += 1
            else:
                frame = 0
        if event.type == JUMP:
            if direction and not on_ground:
                jump_speed -= 1
            elif on_ground:
                jump_speed = 22

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and on_ground:
            sound1.play()
            on_ground = False
            direction = True
            dino_rect.bottom -= 1
        if event.key == pygame.K_DOWN:
            bg_speed = bg_speed - 5

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN:
            bg_speed = 7

    # bg
    for i in range(len(bg_list)):
        bg_list[i].x -= bg_speed
        if bg_list[i].right < 0:
            bg_list[i].left = SW
        screen1.blit(desert, bg_list[i])

    for i in range(1, heart + 1):
        heart1_picture_rect.bottom = 50
        heart1_picture_rect.top = 10
        heart1_picture_rect.right = 35

        heart1_picture_rect.right *= i
        screen1.blit(heart1_picture, heart1_picture_rect)

    # cactus
    if not cac_onscreen:
        if random.randint(0, 5) == 5:
            if random.randint(1, 3) == 1:
                cac_onscreen = True
                cac1_move = True
            elif random.randint(1, 3) == 2:
                cac_onscreen = True
                cac2_move = True
            elif random.randint(1, 3) == 3:
                cac_onscreen = True
                cac3_move = True

    if (cac1_rect.x < SW // 2 or cac2_rect.x < SW // 2 or cac3_rect.x < SW // 2) \
            and (not freddie_onscreen) and freddie_timer == 0:
        if random.randint(0, 1000) % 50 == 0:
            freddie_onscreen = True
            freddie_moving = True
            freddie_timer = random.randint(1000, 2000)
            invincible_timer = 200

    if freddie_moving:
        freddie_rect.x -= bg_speed
        screen1.blit(freddie, freddie_rect)

    if cac1_move:
        cac1_rect.x -= bg_speed
        screen1.blit(cac1, cac1_rect)
    if cac2_move:
        cac2_rect.x -= bg_speed
        screen1.blit(cac2, cac2_rect)
    if cac3_move:
        cac3_rect.x -= bg_speed
        screen1.blit(cac3, cac3_rect)

    if freddie_rect.right < -20:
        freddie_rect.left = SW
        freddie_onscreen = False
        freddie_moving = False

    for i in cac_list:
        if i.right < -20:
            i.left = SW
            cac_onscreen = False
            cac1_move = False
            cac2_move = False
            cac3_move = False

    if coin_factor:
        screen1.blit(coin_object.image, coin_object.rect)
        coin_object.rect.x -= bg_speed

    if coin_object.rect.right < 20:
        coin_object.rect.left = SW
        coin_factor = False

    # dino physics
    if on_ground:
        screen1.blit(dino_walk_list[frame], dino_rect)
    else:
        screen1.blit(dino_jump, dino_rect)

    if dino_rect.colliderect(ground_rect):
        on_ground = True
        direction = False

    if dino_rect.colliderect(freddie_rect):
        heart += 1
        sound4.stop()
        sound_of_my_life.play()
        freddie_onscreen = False
        freddie_moving = False
        freddie_rect.left = SW

    if (ground - dino_rect.bottom) < 0:
        dino_rect.bottom = ground

    if not on_ground:
        if direction:
            dino_rect.bottom -= jump_speed
        else:
            direction = False
            dino_rect.bottom += jump_speed
    if dino_rect.collidelistall(cac_list) and invincible_timer == 0:
        print(invincible_timer)
        invincible_timer = 60
        heart -= 1
        sound2.play()
        if heart == 0:
            game_over = True
    if game_over:
        con = sqlite3.connect('users.db')
        cur = con.cursor()
        cur.execute('''INSERT INTO popytki(points, coins) VALUES('%s','%s');''' % (score, coins))
        cur.execute('''UPDATE users
                                            SET coins = (SELECT SUM(coins) FROM popytki)
                                            WHERE name == '%s' ''' % c)

        cur.execute('''UPDATE users 
                                            SET record = (SELECT MAX(points) FROM popytki)
                                            WHERE name == '%s' ''' % c)
        con.commit()
        con.close()
        sound3.play()
        pygame.mixer.music.stop()
        show_end_screen()
        pygame.mixer.music.load('resources/backgroundmusic.mp3')
        pygame.mixer.music.play(-1)
        score = 0
        coins = 0
        heart = 5
        bg_speed = 7

        game_over = False

    if dino_rect.colliderect(coin_object.rect):
        sound4.play()
        coin_object.update()
        coins += 1
    # misc
    screen1.blit(coinspic, coinspic_rect)
    coin_text = pixel_font.render(f'{coins}', True, BLACK)
    screen1.blit(coin_text, (650, 12))
    score_text = pixel_font.render(f'{score}', True, BLACK)
    screen1.blit(score_text, (720, 12))

    pygame.display.update()
