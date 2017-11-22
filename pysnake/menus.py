from collections import OrderedDict

class MainMenu:
    ITEMS = OrderedDict([
        ('new_game', {'title': 'New Game', 'action': 'start_new_game'}),
        ('about', {'title': 'About', 'action': 'show_about'}),
        ('exit', {'title': 'Exit', 'action': 'exit_from_game'}),
    ])