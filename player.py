"""
connect4 players using inheritance implementation

"""

import random


class Player:
    def __init__(self, letter, name):
        self.letter = letter
        self.name = name

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter, name):
        super().__init__(letter, name)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-7): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val


class RandomBotPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter, "RandomRobot")

    def get_move(self, game):
        column = random.choice(game.available_moves())
        return column


class SmartBotPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter, "SmartRobot")

    def get_move(self, game):
        move = self.minimax(game, self.letter)
        return move

    def minimax(self, state, player):
        return 0
