import pygame


class ButtonSprite(pygame.sprite.Sprite):
    # image = pygame.image.load('coin.png')

    def __init__(self, group, x, y, w, h, text):
        super().__init__(group)
        self.image = pygame.Surface((w, h), pygame.SRCALPHA)
        self.image.fill((243, 218, 26))
        self.text = text
        self.font = pygame.font.SysFont('Cooper Black', 35)
        text_surface = self.font.render(self.text, True, (130, 130, 130))
        text_rect = text_surface.get_rect(center=(w / 2, h / 2))
        self.image.blit(text_surface, text_rect)
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y



