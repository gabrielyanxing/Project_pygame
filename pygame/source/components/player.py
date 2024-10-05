import pygame
from .. import tools, setup
from .. import constants as C

class Player(pygame.sprite.Sprite):
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.sock_count = 0

        self.setup_states()
        self.setup_velocities()
        self.setup_timers()
        self.load_images()

        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()

    def setup_states(self):
        self.face_right = pygame.sprite.Group()
        self.dead = False
        self.big = False

    def setup_velocities(self):
        self.x_vel = 0
        self.y_vel = 0

    def setup_timers(self):
        self.walking_timer = 0
        self.transition_timer = 0

    def load_images(self):
        sheet = setup.GRAPHICS['player']
        self.right_frames = []
        self.left_frames = []
        self.up_frames = []
        self.down_frames = []

        frame_rects = [
            (0, 0, 25, 25),
            (30, 0, 25, 25),
            (60, 0, 25, 25),
            (94, 0, 25, 25)
        ]

        for frame_rect in frame_rects:
            right_image = tools.get_image(sheet, *frame_rect, (0, 0, 0), C.PLAYER_MULTI)
            left_image = pygame.transform.flip(right_image, True, False)
            up_image = pygame.transform.rotate(right_image, 0)
            down_image = pygame.transform.rotate(right_image, 0)

            self.right_frames.append(right_image)
            self.left_frames.append(left_image)
            self.up_frames.append(up_image)
            self.down_frames.append(down_image)

        self.frame_index = 0
        self.frames = self.right_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()

    def update(self, keys):
        self.current_time = pygame.time.get_ticks()

        self.x_vel = 0
        self.y_vel = 0

        if keys[pygame.K_RIGHT]:
            self.x_vel = 10
            self.frames = self.right_frames
        elif keys[pygame.K_LEFT]:
            self.x_vel = -10
            self.frames = self.left_frames
        elif keys[pygame.K_UP]:
            self.y_vel = -10
            self.frames = self.up_frames
        elif keys[pygame.K_DOWN]:
            self.y_vel = 10
            self.frames = self.down_frames

        if self.current_time - self.walking_timer > 100:
            self.walking_timer = self.current_time
            self.frame_index += 1
            self.frame_index %= len(self.frames)

        self.image = self.frames[self.frame_index]


