import pygame
from .. import setup
from .. import tools
from .. import constants as C
from .. components import info


class MainMenu:
 def __init__(self):
  self.setup_background()
  self.setup_player()
  self.setup_cursor()
  self.info = info.Info('main_menu')
  self.finished = False
  self.next = 'load_screen'


 def setup_background(self):
   self.background = setup.GRAPHICS['background1-1']
   self.background_rect = self.background.get_rect()
   self.background = pygame.transform.scale(self.background, (int(self.background_rect.width * C.BG_MULTI),
                                                              int(self.background_rect.height * C.BG_MULTI)))
   self.viewport = setup.SCREEN.get_rect()
   self.caption = tools.get_image(setup.GRAPHICS['title'], 0, 0, 128, 128, (0,0,0), C.BG_MULTI)


 def setup_player(self):
  self.player_image = tools.get_image(setup.GRAPHICS['player'], 0, 0, 25, 25, (0,0,0), C.PLAYER_MULTI)

 def setup_cursor(self):
  self.cursor = pygame.sprite.Sprite()
  self.cursor.image = tools.get_image(setup.GRAPHICS['cursor'], 0, 0, 16, 16, (0,0,0), 2)
  rect = self.cursor.image.get_rect()
  rect.x, rect.y = (520, 270)
  self.cursor.rect = rect
  self.cursor.state = '1P'

 def update_cursor(self, keys):
  if keys[pygame.K_UP]:
    self.cursor.state = '1P'
    self.cursor.rect.y = 270
  elif keys[pygame.K_DOWN]:
    self.cursor.state = 'QUIT'
    self.cursor.rect.y = 300
  elif keys[pygame.K_RETURN]:
    if self.cursor.state == '1P':
        self.finished = True
    elif self.cursor.state == 'QUIT':
        self.finished = True



 def update(self, surface, keys):

  self.update_cursor(keys)

  surface.blit(self.background, self.viewport)
  surface.blit(self.caption, (230, -30))
  surface.blit(self.player_image, (150, 230))
  surface.blit(self.cursor.image, self.cursor.rect)

  self.info.update()
  self.info.draw(surface, 0)