# Imports
import math
import time

from player import HumanPlayer, RandomBotPlayer

"""
connect4 players using inheritance implementation

"""

# Game Constants
ROWS = 6
COLUMNS = 7

PIECE_NONE = ' '
PIECE_ONE = 'x'
PIECE_TWO = 'o'

PIECE_COLOR_MAP = {
    PIECE_NONE: 'white',
    PIECE_ONE: 'black',
    PIECE_TWO: 'red',
}

DIRECTIONS = (
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
)

class Connect4():
    def __init__(self):
        self.board = self.create_board()
        self.current_winner = None
        self.num_empty_slots = ROWS*COLUMNS

    # Board Functions
    def create_board(self, rows=ROWS, columns=COLUMNS):
        # Creates empty Connect 4 board
        board = []

        for row in range(rows):
            board_row = []
            for column in range(columns):
                board_row.append(PIECE_NONE)
            board.append(board_row)

        return board

    def print_board(self):
    # Prints Connect 4 board
        for row in self.board:
            print('|' + '|'.join(row) + '|')

    def drop_piece(self, column, piece):
    # Attempts to drop specified piece into the board at the
    # specified column
    # If this succeeds, return True, otherwise return False.
        for row in reversed(self.board):
            if row[column] == PIECE_NONE:
                row[column] = piece
                self.num_empty_slots -= 1
                return True

        return False

    def find_winner(self, length=4):
    # Return whether or not the board has a winner
        rows    = len(self.board)
        columns = len(self.board[0])

        for row in range(rows):
            for column in range(columns):
                if self.board[row][column] == PIECE_NONE:
                    continue

                if self.check_piece(row, column, length):
                    return self.board[row][column]

        return None

    def check_piece(self, row, column, length):
    # Return whether or not there is a winning sequence starting from
    # this piece

        rows    = len(self.board)
        columns = len(self.board[0])

        for dr, dc in DIRECTIONS:
            found_winner = True

            for i in range(1, length):
                r = row + dr*i
                c = column + dc*i

                if r not in range(rows) or c not in range(columns):
                    found_winner = False
                    break

                if self.board[r][c] != self.board[row][column]:
                    found_winner = False
                    break

            if found_winner:
                return True

        return False

    def available_moves(self):
        moves = []
        columns = len(self.board[0])
        for i in range(columns):
            if self.board[0][i] == PIECE_NONE:
                moves.append(i)

        return moves

    def num_empty_slots(self):
        return self.num_empty_slots

# Game Play Loop
def play(game, player1, player2, print_game=True):

    turn = 0
    players =[]
    players.append(player1)
    players.append(player2)
    Winner = None
    move = -1
    timers = []
    timers.append(0)
    timers.append(0)

    while not Winner:
        player_index = turn % 2
        start = time.perf_counter_ns()
        move = players[player_index].get_move(game)  # Player One
        timers[player_index] += time.perf_counter_ns() - start

        if game.drop_piece(move, players[player_index].letter):
            if print_game:
                print("Move # ", turn)
                game.print_board()

        time.sleep(1)

        Winner = game.find_winner()
        turn += 1
        if (not Winner and turn >= COLUMNS * ROWS):
            print("It is a tie game!")

            if (timers[0] != timers[1]):
                if (timers[0] < timers[1]):
                    Winner = players[0].letter
                else:
                    Winner = players[1].letter
            else:
                return

    winning_player = None
    for i in range(len(players)):
        print("Time elapsed by %s player %s : %d ns" %(players[i].letter, players[i].name, timers[i]))
        if (players[i].letter == Winner):
            winning_player = players[i]
    if (winning_player):
        print("The Winner is %s." % winning_player.name)

if __name__ == '__main__':
    x_player = RandomBotPlayer(PIECE_ONE)
#    o_player = HumanPlayer(PIECE_TWO, "Human")
    o_player = RandomBotPlayer(PIECE_TWO)
    g = Connect4()
    play(g, x_player, o_player, print_game=True)