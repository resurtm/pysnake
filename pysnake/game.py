from enum import Enum

import pygame
import time


class GameState(Enum):
    MAIN_MENU = 1
    GAME_PLAY = 2
    GAME_MENU = 3


class Game:
    WND_WIDTH = 1280
    WND_HEIGHT = 800
    WND_CAPTION = 'pysnake'
    BG_COLOR = 50, 50, 50

    main_menu = None
    field = None
    snake = None

    def __init__(self):
        self.game_state = GameState.MAIN_MENU
        self.clock = None
        self.main_loop_active = False

        pygame.init()
        self.screen = pygame.display.set_mode((self.WND_WIDTH, self.WND_HEIGHT))
        pygame.display.set_caption(self.WND_CAPTION)

        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill(self.BG_COLOR)

    def run(self):
        self.clock = pygame.time.Clock()
        self.main_loop_active = True

        prev_time = time.perf_counter()
        time_accum = 0

        while self.main_loop_active:
            curr_time = time.perf_counter()
            time_diff = curr_time - prev_time
            prev_time = curr_time
            time_accum += time_diff

            self.clock.tick(60)

            for event in pygame.event.get():
                if self.game_state is GameState.MAIN_MENU:
                    self.main_menu.handle_event(event)
                if self.game_state is GameState.GAME_PLAY:
                    self.snake.handle_event(event)
                if event.type == pygame.QUIT:
                    self.main_loop_active = False

            self.screen.blit(self.background, (0, 0))

            if self.game_state is GameState.MAIN_MENU:
                self.main_menu.draw()
            if self.game_state is GameState.GAME_PLAY:
                self.field.draw()

            if time_accum >= 0.25:
                if self.game_state is GameState.GAME_PLAY:
                    self.snake.update()
                time_accum = 0

            pygame.display.update()
