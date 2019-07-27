import time


class Computer:

    def __init__(self):
        self.nodes = 0

    def search(self, game, max_depth):
        self.nodes = 0
        t0 = time.time()

        best_value = -999
        moves = game.moves.copy()
        best_move = moves[0]

        for move in moves:
            game.play(move)
            value = -self.alpha_beta(game, -999, 999, max_depth)
            game.undo(move)
            game.moves = moves.copy()
            if value > best_value:
                best_value = value
                best_move = move

        try:
            print('{:.0f} NPS'.format(self.nodes / (time.time() - t0)))
        except ZeroDivisionError:
            print('Infinity NPS')
        return best_move

    def alpha_beta(self, game, alpha, beta, depth):
        self.nodes += 1

        if depth <= 0:
            return self.evaluate(game)

        value = -999

        moves = game.moves.copy()
        for move in moves:
            game.play(move)
            value = max(value, -self.alpha_beta(game, -beta, -alpha, depth - 1))
            game.undo(move)
            game.moves = moves.copy()
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value

    def evaluate(self, game):
        return 0


'''def ai_move(game, max_depth):
    best_value = -999

    moves = game.moves
    best_move = moves[0]

    for move in moves:
        copy = deepcopy(game)
        copy.play(move)
        value = -alpha_beta(copy, -999, 999, max_depth)
        if value > best_value:
            best_value = value
            best_move = move

    return best_move


def alpha_beta(game, alpha, beta, depth):
    if depth <= 0:
        return evaluate(game)

    value = -999
    for move in game.moves:
        copy = deepcopy(game)
        copy.play(move)
        value = max(value, -alpha_beta(copy, -beta, -alpha, depth-1))
        alpha = max(alpha, value)
        if alpha >= beta:
            break
    return value'''






