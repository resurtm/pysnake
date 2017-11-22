import os

import pygame

from pysnake.manager import Manager


class ImageMan(Manager):
    resource_names = {
        'snake_tiles_64': os.path.join('snake-tiles', 'snake-graphics-64.png'),
        'snake_tiles_32': os.path.join('snake-tiles', 'snake-graphics-32.png'),
        'ui': os.path.join('ui', 'ui.png')
    }

    @staticmethod
    def load_resource(name: str, **kwargs):
        image = pygame.image.load(os.path.join('pysnake', 'data', name))
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
        return image
