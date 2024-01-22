import pygame

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
long_jump = False
short_jump = False
time_down = 0
time_elapsed = 0
key = 0

screen = pygame.display.set_mode((SW, SH))
background = (0, 150, 150)
screen.fill(background)

pygame.init()


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
        global running, close
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if click[0] == 1 and self.action:
            self.action()
        else:
            pygame.draw.rect(screen, (243, 218, 26), (self.x, self.y, self.width, self.height))
        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            if self.text == 'start':
                running = True
            elif self.text == 'exit':
                close = True

        text_surface = self.font.render(self.text, True, (130, 130, 130))
        text_rect = text_surface.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
        screen.blit(text_surface, text_rect)
