# from youtu.be/8ext9G7xspg&t=2209
import math, random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    # we want all players to get their next move given a game
    def get_move(self, game):
        pass

# using inheritance
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            # we're gonna check that this is a correct value by trying to cast
            # it to an integer, and if it's not, then we say it's invalid.
            # If that spot is not available on the board, we also say it's invalid
            try:
                # if user enters a str (e.g.) it'll raise an error
                val = int(square)
                # if it's not available, raise an error
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if it passes both tests, then it's valid
            except ValueError:
                print('Invalid Square dingus')
        return val
