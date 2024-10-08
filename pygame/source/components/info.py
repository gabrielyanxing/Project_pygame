import pygame
from .. import constants as C
from . import coin
from .. import setup, tools
pygame.font.init()

class Info:
    def __init__(self, state):
        self.state = state
        self.create_state_labels()
        self.create_info_labels()
        self.flash_coin = coin.FlashingCoin()

    def create_state_labels(self):
        self.state_labels = []
        if self.state == 'main_menu':
            self.state_labels.append((self.create_label('1 PLAYER GAME'), (560, 280)))
            self.state_labels.append((self.create_label('QUIT'), (575, 310)))
            self.state_labels.append((self.create_label('TOP - '), (530, 340)))
            self.state_labels.append((self.create_label('OOOOOO'), (620, 340)))
        elif self.state == 'load_screen':
            self.state_labels.append((self.create_label('Helsinki'), (350, 200)))
            self.state_labels.append((self.create_label('1 - 1'), (370, 230)))
            self.state_labels.append((self.create_label('x 3'), (400, 290)))
            self.player_image = tools.get_image(setup.GRAPHICS['player'], 1,1, 25, 25, (0,0,0), C.BG_MULTI)

    def create_info_labels(self):
        self.info_labels = []
        self.info_labels.append((self.create_label('PLAYER'), (55, 30)))
        self.info_labels.append((self.create_label('WORLD'), (550, 30)))
        self.info_labels.append((self.create_label('TIME'), (700, 30)))
        self.info_labels.append((self.create_label('OOOOOO'), (50, 55)))
        self.info_labels.append((self.create_label('1 - 1'), (570, 55)))

    def create_label(self, label, size=25, width_scale=1.25, height_scale=1):
        font = pygame.font.SysFont(C.FONT, size)
        label_image = font.render(label, 1, (255, 255, 255))
        rect = label_image.get_rect()
        label_image = pygame.transform.scale(label_image,
                                             (int(rect.width * width_scale), int(rect.height * height_scale)))

        return label_image

    def update(self):
        self.flash_coin.update()


    def draw(self, surface, player_sock_count):
        for label in self.state_labels:
            surface.blit(label[0], label[1])
        for label in self.info_labels:
            surface.blit(label[0], label[1])
        surface.blit(self.flash_coin.image, self.flash_coin.rect)

        socks_label = self.create_label(f' x {player_sock_count}', size=25)
        surface.blit(socks_label, (200, 55))
        if self.state == 'load_screen':
            surface.blit(self.player_image, (330, 270))