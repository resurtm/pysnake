class SpriteMan:
    image_man = None
    game = None

    sprites = {
        'apple_menu': {'image': 'snake_tiles_64', 'pos': (0, 192), 'size': (64, 64)},
        'apple': {'image': 'snake_tiles_32', 'pos': (0, 96), 'size': (32, 32)},

        'snake_body_h': {'image': 'snake_tiles_32', 'pos': (32, 0), 'size': (32, 32)},
        'snake_body_v': {'image': 'snake_tiles_32', 'pos': (64, 32), 'size': (32, 32)},

        'snake_body_b_r': {'image': 'snake_tiles_32', 'pos': (0, 0), 'size': (32, 32)},
        'snake_body_b_l': {'image': 'snake_tiles_32', 'pos': (64, 0), 'size': (32, 32)},
        'snake_body_t_l': {'image': 'snake_tiles_32', 'pos': (64, 64), 'size': (32, 32)},
        'snake_body_t_r': {'image': 'snake_tiles_32', 'pos': (0, 32), 'size': (32, 32)},

        'snake_head_t': {'image': 'snake_tiles_32', 'pos': (96, 0), 'size': (32, 32)},
        'snake_head_b': {'image': 'snake_tiles_32', 'pos': (128, 32), 'size': (32, 32)},
        'snake_head_l': {'image': 'snake_tiles_32', 'pos': (96, 32), 'size': (32, 32)},
        'snake_head_r': {'image': 'snake_tiles_32', 'pos': (128, 0), 'size': (32, 32)},

        'snake_tail_t': {'image': 'snake_tiles_32', 'pos': (128, 96), 'size': (32, 32)},
        'snake_tail_b': {'image': 'snake_tiles_32', 'pos': (96, 64), 'size': (32, 32)},
        'snake_tail_l': {'image': 'snake_tiles_32', 'pos': (128, 64), 'size': (32, 32)},
        'snake_tail_r': {'image': 'snake_tiles_32', 'pos': (96, 96), 'size': (32, 32)},
    }

    def draw(self, sprite_id, pos):
        screen = self.game.screen
        sprite = self.sprites[sprite_id]
        image = self.image_man[sprite['image']]
        screen.blit(image, pos, (sprite['pos'][0], sprite['pos'][1], sprite['size'][0], sprite['size'][1]))
