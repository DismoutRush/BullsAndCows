import pygame
import sys
import config as c

from collections import defaultdict


class Game:
    def __init__(self, caption, width, height, back_image_filename, frame_rate):
        self.background_image = pygame.image.load(back_image_filename)
        self.frame_rate = frame_rate
        self.game_over = False
        self.objects = []
        self.play_sound = True
        self.win_sound_play = False
        self.icon = pygame.image.load("images/icon.png")
        pygame.mixer.init(44100, -16, 2, 16384)
        pygame.init()
        self.sound_menu = pygame.mixer.Sound(c.sound_effects['menu'])
        self.sound_win = pygame.mixer.Sound(c.sound_effects['win'])
        pygame.font.init()
        self.surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []

    def update(self):
        for o in self.objects:
            o.update()

    def draw(self):
        for o in self.objects:
            o.draw(self.surface)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
            elif event.type == pygame.KEYUP:
                for handler in self.keyup_handlers[event.key]:
                    handler(event.key)
            elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)

    def run(self):

        pygame.display.set_icon(pygame.image.load("images/icon.png"))
        while not self.game_over:
            self.surface.blit(self.background_image, (0, 0))
            if self.play_sound and not self.win_sound_play:
                self.sound_menu.set_volume(0.02)
                self.sound_menu.play()
            else:
                self.sound_menu.stop()
            if self.win_sound_play:
                self.sound_win.set_volume(0.2)
                self.sound_win.play()
                self.win_sound_play = False
            self.handle_events()
            self.update()
            self.draw()


            pygame.display.update()
            self.clock.tick(self.frame_rate)


