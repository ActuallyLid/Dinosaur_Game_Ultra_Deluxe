import pygame
import pygame_gui
import pygame.font
from pygame.rect import Rect
from pygame_gui.elements.ui_text_entry_line import UITextEntryLine


WHITE = (255, 255, 255)
pygame.init()
pygame.font.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((400, 300))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600))
text_input = UITextEntryLine(relative_rect=Rect(125, 100, 150, 50), manager=manager)

hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 175), (100, 50)),
                                            text='Войти',
                                            manager=manager)

clock = pygame.time.Clock()

pixel_font = pygame.font.SysFont('OCR A Extended', 30)

is_running = True

while is_running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():

        if event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
            c = event.text
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                print(c)
                is_running = False

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)
    score_text = pixel_font.render('Enter name', True, WHITE)
    window_surface.blit(score_text, (115, 60))

    pygame.display.update()


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


is_running = True

while is_running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():

        if event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
            c = event.text
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                print(c)
                is_running = False

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background_enter, (0, 0))
    manager.draw_ui(window_surface)
    score_text = pixel_font.render('Enter name', True, WHITE)
    window_surface.blit(score_text, (115, 60))

    pygame.display.update()

