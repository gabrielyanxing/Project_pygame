import pygame
from .. import tools, setup
from .. import constants as C

class Sock(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = tools.get_image(setup.GRAPHICS['bell_flash'], 0, 0, 16, 16, (0, 0, 0), 3)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass