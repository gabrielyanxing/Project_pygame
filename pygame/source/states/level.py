
from .. components import info
import pygame
from .. import tools, setup
from .. import constants as C
from .. components import player
from ..components.sock import Sock

class Level:
    def __init__(self):
        self.finished = False
        self.next = None
        self.info = info.Info('level')
        self.setup_background()
        self.setup_player()
        self.socks = pygame.sprite.Group()
        self.create_socks()


    def setup_background(self):
        self.background = setup.GRAPHICS['background1-1']
        rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background,
                                                 (int(rect.width * C.BG_MULTI),
                                                  int(rect.height * C.BG_MULTI)))
        self.background_rect = self.background.get_rect()
        self.game_window = setup.SCREEN.get_rect()
        self.game_ground = pygame.Surface((self.background_rect.width, self.background_rect.height))

    def create_socks(self):
        sock1 = Sock(600, 280)
        sock2 = Sock(1000, 200)
        sock3 = Sock(1200, 300)
        sock4 = Sock(1400, 400)
        sock5 = Sock(1600, 250)
        sock6 = Sock(1800, 300)
        sock7 = Sock(2000, 400)
        sock8 = Sock(2300, 200)
        sock9 = Sock(2200, 300)
        sock10 = Sock(2500, 400)
        sock11 = Sock(2700, 250)
        sock12 = Sock(2900, 310)
        sock13 = Sock(3100, 430)
        sock14 = Sock(3200, 200)
        sock15 = Sock(3400, 150)
        sock16 = Sock(3600, 450)
        sock17 = Sock(3900, 330)
        sock18 = Sock(4100, 250)
        sock19 = Sock(4300, 450)
        sock20 = Sock(4500, 200)
        sock21 = Sock(4800, 150)

        self.socks.add(sock1, sock2, sock3, sock4, sock5, sock6, sock7, sock8, sock9, sock10, sock11, sock12, sock13, sock14, sock15, sock16, sock17, sock18, sock19, sock20, sock21)  # 添加到袜子组中

    def setup_player(self):
        self.player = player.Player("player")
        self.player.rect.x = 100
        self.player.rect.y = 300

    def update(self, surface, keys):
        self.player.update(keys)
        self.update_player_position()
        self.update_game_window()

        collected_socks = pygame.sprite.spritecollide(self.player, self.socks, True)
        if collected_socks:
            self.player.sock_count += len(collected_socks)

        self.info.update()
        self.draw(surface)


    def update_player_position(self):
        self.player.rect.x += self.player.x_vel
        self.player.rect.y += self.player.y_vel

    def update_game_window(self):
        third = self. game_window.x + self. game_window.width / 3
        if self.player.x_vel > 0 and self.player.rect.centerx > third:
            self.game_window.x += self.player.x_vel

        self.game_window.x = max(0, self.game_window.x)
        self.game_window.x = min(self.game_window.x, self.background_rect.width - self.game_window.width)

    def draw(self, surface):
        self.game_ground.blit(self.background, self.game_window, self.game_window)
        self.game_ground.blit(self.player.image, self.player.rect)

        self.socks.draw(self.game_ground)

        surface.blit(self.game_ground, (0,0), self.game_window)

        self.info.draw(surface, self.player.sock_count)
