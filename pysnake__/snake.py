from random import randrange

import pygame

from pysnake.field import Field


class Snake:
    INITIAL_BODY_LENGTH = 3

    def __init__(self):
        self.__reset()

    def update(self):
        self.x += self.vx
        self.y += self.vy

        self.__assert_borders()

        for i, v in reversed(list(enumerate(self.body))):
            if i == 0:
                continue
            curr = self.body[i]
            prev = self.body[i - 1]
            if curr[0] == prev[0] and curr[1] == prev[1]:
                continue
            self.body[i] = self.body[i - 1]

        self.body[0] = (self.x, self.y)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.__move_up()
            elif event.key == pygame.K_DOWN:
                self.__move_down()
            elif event.key == pygame.K_LEFT:
                self.__move_left()
            elif event.key == pygame.K_RIGHT:
                self.__move_right()

    def __reset(self):
        if self.INITIAL_BODY_LENGTH < 3:
            raise RuntimeError('Snake body length must be 3 or more segments')

        self.x = int(Field.BOARD_WIDTH / 2)
        self.y = int(Field.BOARD_HEIGHT / 2)

        dr = randrange(0, 4)
        self.vx = 0 if dr == 0 or dr == 1 else (-1 if dr == 2 else 1)
        self.vy = 0 if dr == 2 or dr == 3 else (-1 if dr == 0 else 1)

        self.length = self.INITIAL_BODY_LENGTH
        self.body = []

        for i in range(0, self.length):
            self.body.append((self.x, self.y))

    def __move_up(self):
        if abs(self.vy) > 0:
            return
        self.vx = 0
        self.vy = -1

    def __move_down(self):
        if abs(self.vy) > 0:
            return
        self.vx = 0
        self.vy = 1

    def __move_left(self):
        if abs(self.vx) > 0:
            return
        self.vx = -1
        self.vy = 0

    def __move_right(self):
        if abs(self.vx) > 0:
            return
        self.vx = 1
        self.vy = 0

    def __assert_borders(self):
        if self.x > Field.BOARD_WIDTH - 1:
            self.x = 0
        if self.x < 0:
            self.x = Field.BOARD_WIDTH - 1
        if self.y > Field.BOARD_HEIGHT - 1:
            self.y = 0
        if self.y < 0:
            self.y = Field.BOARD_HEIGHT - 1

    def grow_body(self):
        self.body.append(self.body[self.length - 1])
        self.length += 1
