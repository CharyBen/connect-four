class Game:

    def __init__(self):
        self.board = {0: 0, 1: 0, 2: 0}
        self.moves = [i for i in range(7)]
        self.turn = 0

    def play(self, column):
        b = get_column(self.board[2], column)
        b = (b << 1) | 1

        if not b & 0b1000000:
            if b == 0b111111:
                self.moves.remove(column)
            self.board[2] = self.board[2] | b << column * 7
            next_turn = self.turn ^ 1
            self.board[self.turn] = self.board[next_turn] ^ self.board[2]
            self.turn = next_turn
            if self.find_win() in [0, 1]:
                self.moves = []

    def undo(self, column):
        b = get_column(self.board[2], column)
        b = b ^ (b >> 1)
        self.board[2] = self.board[2] ^ (b << 7 * column)
        previous_turn = self.turn ^ 1
        self.board[previous_turn] = self.board[self.turn] ^ self.board[2]
        self.turn = previous_turn

    def find_win(self):
        for i in range(2):
            b = self.board[i] & self.board[i] << 7
            if b & b << 7 * 2:
                return i

            b = self.board[i] & self.board[i] << 1
            if b & b << 1 * 2:
                return i

            b = self.board[i] & self.board[i] << 8
            if b & b << 8 * 2:
                return i

            b = self.board[i] & self.board[i] << 6
            if b & b << 6 * 2:
                return i

        if bin(self.board[2]).count('1') >= 6 * 7:
            return 2


def get_column(board, column):
    return (board >> column * 7) & 0b1111111


def print_board(bitboard):
    print('+---+---+---+---+---+---+---+')
    for i in range(6):
        for j in range(7):
            print('+ ' + ('x' if bitboard & 1 << j * 7 + 5 - i else ' ') + ' ', end='')
        print('+\n+---+---+---+---+---+---+---+')
    print()


if __name__ == '__main__':
    game = Game()
    game.play(0)
    game.play(0)
    game.play(0)
    game.play(0)
    game.play(0)
    game.play(0)
    print_board(game.board[0])
    print_board(game.board[1])
    game.undo(0)
    print_board(game.board[0])
    print_board(game.board[1])


'''bitboard = 0b1111110110111
print('{:064b}'.format(bitboard))
print('{:64b}'.format((bitboard >> 1 * 7) & 0b1111111))
print_board(bitboard)'''