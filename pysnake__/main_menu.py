from collections import OrderedDict

import pygame

from pysnake.game import GameState


class MainMenu:
    HEADER_COLOR = 0, 255, 0
    HEADER_TITLE = 'PySnake'
    HEADER_POS_Y = 125

    ITEMS_COLOR = 0, 255, 0
    ITEMS_POS_Y = 350
    ITEMS_DELTA_Y = 60

    CURSOR_LEFT_MARGIN = 30
    CURSOR_TOP_MARGIN = 20

    font_man = None
    sprite_man = None
    game = None

    menu_items = None

    def __init__(self):
        self.menu_items = OrderedDict()
        self.menu_items['new_game'] = {
            'title': 'New Game',
            'action': 'start_new_game',
        }
        self.menu_items['about'] = {
            'title': 'About',
            'action': 'show_about',
        }
        self.menu_items['exit'] = {
            'title': 'Exit',
            'action': 'exit_from_game',
        }

        self.active_item = 0

        font = self.font_man['menu_header']
        self.menu_header = font.render(self.HEADER_TITLE, True, self.HEADER_COLOR)

        font = self.font_man['menu_item']
        for k, v in self.menu_items.items():
            self.menu_items[k]['text'] = font.render(v['title'], True, self.ITEMS_COLOR)

    def draw(self):
        screen = self.game.screen
        self.__draw_menu_header(screen)
        self.__draw_menu_items(screen)
        self.__draw_cursor(screen)

    def __draw_menu_header(self, screen):
        pos_x = int(self.game.WND_WIDTH / 2 - self.menu_header.get_rect().width / 2)
        screen.blit(self.menu_header, (pos_x, self.HEADER_POS_Y))

    def __draw_menu_items(self, screen):
        pos_x = int(self.game.WND_WIDTH / 2 - self.__menu_item_max_width() / 2)
        index = 0
        for k, v in self.menu_items.items():
            screen.blit(v['text'], (pos_x, self.ITEMS_POS_Y + index * self.ITEMS_DELTA_Y))
            index += 1

    def __draw_cursor(self, screen):
        pos_x = int(self.game.WND_WIDTH / 2 - self.__menu_item_max_width()) - self.CURSOR_LEFT_MARGIN
        pos_y = self.ITEMS_POS_Y + self.active_item * self.ITEMS_DELTA_Y - self.CURSOR_TOP_MARGIN
        self.sprite_man.draw('apple_menu', (pos_x, pos_y))

    def __menu_item_max_width(self):
        max_width = 0
        for k, v in self.menu_items.items():
            if v['text'].get_rect().width > max_width:
                max_width = v['text'].get_rect().width
        return max_width

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.__prev_item()
            elif event.key == pygame.K_DOWN:
                self.__next_item()
            elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                self.__select_item()

    def __next_item(self):
        self.active_item += 1
        if self.active_item > len(self.menu_items) - 1:
            self.active_item = 0

    def __prev_item(self):
        self.active_item -= 1
        if self.active_item < 0:
            self.active_item = len(self.menu_items) - 1

    def __select_item(self):
        for k, v in enumerate(self.menu_items.items()):
            if k == self.active_item:
                getattr(self, v[1]['action'])()

    def start_new_game(self):
        self.game.game_state = GameState.GAME_PLAY

    def show_about(self):
        print('about')

    def exit_from_game(self):
        self.game.main_loop_active = False
