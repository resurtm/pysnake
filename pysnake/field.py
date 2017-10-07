class Field:
    BOARD_WIDTH = 20
    BOARD_HEIGHT = 20

    TILE_WIDTH = 32
    TILE_HEIGHT = 32

    sprite_man = None
    snake = None
    items = None

    def __init__(self):
        self.__reset_cells()

    def draw(self):
        self.__reset_cells()
        self.apply_snake_to_field()
        self.apply_items_to_field()

        for i, row in enumerate(self.cells):
            for j, cell in enumerate(row):
                if type(cell) is str:
                    self.sprite_man.draw(cell, (i * self.TILE_WIDTH, j * self.TILE_HEIGHT))

    def apply_items_to_field(self):
        for apple in self.items.apples:
            self.cells[apple[0]][apple[1]] = 'apple'

    def apply_snake_to_field(self):
        sn = self.snake
        self.__snake_head(sn)
        self.__snake_body(sn)
        self.__snake_tail(sn)

    def __snake_body(self, sn):
        for i in range(1, sn.length - 1):
            m = sn.body[i - 1]
            n = sn.body[i]
            p = sn.body[i + 1]
            self.__snake_body_internal(m, n, p)

    def __snake_body_internal(self, m, n, p):
        if m[0] == n[0] == p[0]:
            self.cells[n[0]][n[1]] = 'snake_body_v'
        elif m[1] == n[1] == p[1]:
            self.cells[n[0]][n[1]] = 'snake_body_h'
        elif m[0] == n[0] and n[1] == p[1]:
            if m[1] < n[1]:
                self.cells[n[0]][n[1]] = 'snake_body_t_l' if n[0] > p[0] else 'snake_body_t_r'
            else:
                self.cells[n[0]][n[1]] = 'snake_body_b_l' if n[0] > p[0] else 'snake_body_b_r'
        elif m[1] == n[1] and n[0] == p[0]:
            if m[0] < n[0]:
                self.cells[n[0]][n[1]] = 'snake_body_t_l' if n[1] > p[1] else 'snake_body_b_l'
            else:
                self.cells[n[0]][n[1]] = 'snake_body_t_r' if n[1] > p[1] else 'snake_body_b_r'

    def __snake_head(self, sn):
        head = sn.body[0]
        n1 = sn.body[1]
        n2 = sn.body[2]
        self.__snake_head_or_tail(head, n1, n2, 'head')

    def __snake_tail(self, sn):
        head = sn.body[sn.length - 1]
        n1 = sn.body[sn.length - 2]
        n2 = sn.body[sn.length - 3]
        self.__snake_head_or_tail(head, n1, n2, 'tail')

    def __snake_head_or_tail(self, head, n1, n2, type):
        if head[0] == n1[0] == n2[0]:
            if head[1] > n1[1] > n2[1]:
                self.cells[head[0]][head[1]] = 'snake_{}_b'.format(type)
            else:
                self.cells[head[0]][head[1]] = 'snake_{}_t'.format(type)
        elif head[1] == n1[1] == n2[1]:
            if head[0] > n1[0] > n2[0]:
                self.cells[head[0]][head[1]] = 'snake_{}_r'.format(type)
            else:
                self.cells[head[0]][head[1]] = 'snake_{}_l'.format(type)
        elif head[0] == n1[0] and (n1[0] == n2[0] - 1 or n1[0] == n2[0] + 1):
            if head[1] == n1[1] - 1:
                self.cells[head[0]][head[1]] = 'snake_{}_t'.format(type)
            elif head[1] == n1[1] + 1:
                self.cells[head[0]][head[1]] = 'snake_{}_b'.format(type)
        elif head[1] == n1[1] and (n1[1] == n2[1] - 1 or n1[1] == n2[1] + 1):
            if head[0] == n1[0] - 1:
                self.cells[head[0]][head[1]] = 'snake_{}_l'.format(type)
            elif head[0] == n1[0] + 1:
                self.cells[head[0]][head[1]] = 'snake_{}_r'.format(type)

    def __reset_cells(self):
        self.cells = [[False for _ in range(self.BOARD_WIDTH)] for _ in range(self.BOARD_HEIGHT)]
