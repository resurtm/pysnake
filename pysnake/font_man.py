import os

import pygame

from pysnake.manager import Manager


class FontMan(Manager):
    resource_names = {
        'menu_header': {
            'name': os.path.join('fonts', 'liberation-fonts', 'LiberationSans-Bold.ttf'),
            'size': 52,
        },
        'menu_item': {
            'name': os.path.join('fonts', 'liberation-fonts', 'LiberationSans-Regular.ttf'),
            'size': 28,
        },
    }

    @staticmethod
    def load_resource(name: str, **kwargs):
        return pygame.font.Font(os.path.join('pysnake', 'data', name), kwargs['size'])
