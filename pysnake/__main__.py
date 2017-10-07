from pysnake.field import Field
from pysnake.font_man import FontMan
from pysnake.game import Game
from pysnake.image_man import ImageMan
from pysnake.main_menu import MainMenu
from pysnake.snake import Snake
from pysnake.sprite_man import SpriteMan
from pysnake.items import Items


def main():
    game = Game()

    font_man = FontMan()

    image_man = ImageMan()

    MainMenu.font_man = font_man
    MainMenu.image_man = image_man
    MainMenu.game = game
    main_menu = MainMenu()

    SpriteMan.image_man = image_man
    SpriteMan.game = game
    sprite_man = SpriteMan()
    MainMenu.sprite_man = sprite_man

    Field.sprite_man = sprite_man
    field = Field()

    snake = Snake()
    Field.snake = snake

    Items.snake = snake
    items = Items()
    Field.items = items

    Game.main_menu = main_menu
    Game.field = field
    Game.snake = snake
    Game.items = items
    game.run()


if '__main__' == __name__:
    main()
