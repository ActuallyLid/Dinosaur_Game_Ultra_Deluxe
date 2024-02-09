# import pygame
# import settings
#
#
# class Button:
#     def __init__(self, screen, x, y, width, height, text, action=None):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.text = text
#         self.action = action
#         self.font = pygame.font.SysFont('Cooper Black', 35)
#         self.screen = screen
#
#     def draw(self):
#         global  , close, is_running
#         mouse = pygame.mouse.get_pos()
#         click = pygame.mouse.get_pressed()
#
#         if click[0] == 1 and self.action:
#             self.action()
#         else:
#             pygame.draw.rect(self.screen, (243, 218, 26), (self.x, self.y, self.width, self.height))
#         if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
#             if self.text == 'Start':
#                 running = True
#             elif self.text == 'Enter':
#                 is_running = True
#
#         text_surface = self.font.render(self.text, True, (130, 130, 130))
#         text_rect = text_surface.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
#         self.screen.blit(text_surface, text_rect)
