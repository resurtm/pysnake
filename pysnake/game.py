import enum
import time

import pygame


class GameState(enum.Enum):
    MAIN_MENU = 1
    GAME_PLAY = 2
    GAME_MENU = 3


class Timer(object):
    def __init__(self):
        self.prev_time = time.perf_counter()
        self.curr_time = self.delta = None

    def update(self):
        self.curr_time = time.perf_counter()
        self.delta = self.curr_time - self.prev_time
        self.prev_time = self.curr_time


class Game(object):
    WND_WIDTH = 1280
    WND_HEIGHT = 800
    WND_CAPTION = 'pysnake'
    BG_COLOR = 50, 50, 50
    CLOCK_TICK = 45

    def __init__(self):
        self.game_state = GameState.MAIN_MENU
        self.main_loop = False
        self.clock = pygame.time.Clock()
        self.timer = Timer()
        self.screen = self.background = None

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WND_WIDTH, self.WND_HEIGHT))
        pygame.display.set_caption(self.WND_CAPTION)

        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill(self.BG_COLOR)

        self.timer.update()
        self.main_loop = True

        while self.main_loop:
            self.clock.tick(self.CLOCK_TICK)
            self.timer.update()

            self.handle_events()
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.main_loop = False

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        pygame.display.update()


game = Game()
