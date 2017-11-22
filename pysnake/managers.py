from os.path import join, dirname

import pygame
import pygame.image


class CommonManager(object):
    RESOURCES = {}

    def __init__(self):
        self.resources = {}
        for k, v in self.RESOURCES.items():
            r = self.load_item(**v) if type(v) is dict else self.load_item(v)
            self.resources[k] = r

    def __getitem__(self, i):
        if type(i) is not str:
            raise ValueError('Index must be a string')
        if i not in self.resources:
            raise KeyError('This resource does not exist')
        return self.resources[i]

    @staticmethod
    def load_item(name, **kwargs):
        raise NotImplementedError


class ImageMan(CommonManager):
    RESOURCES = {
        'snake_tiles_64': join('snake-tiles', 'snake-graphics-64.png'),
        'snake_tiles_32': join('snake-tiles', 'snake-graphics-32.png'),
        'ui': join('ui', 'ui.png'),
    }

    @staticmethod
    def load_item(name, **kwargs):
        img = pygame.image.load(join(dirname(__file__), 'data', name))
        return img.convert() if img.get_alpha is None else img.convert_alpha()


image_man = ImageMan()
