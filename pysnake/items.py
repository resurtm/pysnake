import random

from pysnake.field import Field


class Items:
    APPLES_SPAWN_INTERVAL_START = 1
    APPLES_SPAWN_INTERVAL_END = 500

    snake = None

    def __init__(self):
        self.apples = []

    def update(self):
        self.__spawn_apples()
        self.__check_apples()

    def __spawn_apples(self):
        if random.randint(self.APPLES_SPAWN_INTERVAL_START, self.APPLES_SPAWN_INTERVAL_END) == 1:
            while True:
                pos_x = random.randrange(1, Field.BOARD_WIDTH)
                pos_y = random.randrange(1, Field.BOARD_HEIGHT)

                for body_part in self.snake.body:
                    if body_part[0] == pos_x and body_part[1] == pos_y:
                        continue

                self.apples.append((pos_x, pos_y))
                break

    def __check_apples(self):
        for body_part in self.snake.body:
            for i, apple in enumerate(self.apples):
                if body_part[0] == apple[0] and body_part[1] == apple[1]:
                    del self.apples[i]
                    self.snake.grow_body()
