import pkgutil
import importlib
import itertools
import contestants
import collections


NUM_GAMES = 100


def load(player: pkgutil.ModuleInfo) -> importlib.import_module:
    return importlib.import_module('contestants.' + player.name)


def iter_tournament():
    perm = itertools.permutations
    for p1, p2 in perm(pkgutil.iter_modules(contestants.__path__), 2):
        yield (load(p1), load(p2))


def main():
    win_score = collections.defaultdict(int)
    for p1, p2 in iter_tournament():
        stores = [{}, {}]
        scores = [0, 0]
        for game_iter in range(NUM_GAMES):
            a = p1.strategy(game_iter == 0, stores[0])
            b = p2.strategy(game_iter == 0, stores[1])
            scores[0] += a * b * 2 + (1 - a) * b * 3 + (1 - a) * (1 - b)
            scores[1] += a * b * 2 + a * (1 - b) * 3 + (1 - a) * (1 - b)
            p1.plan(b, stores[0])
            p2.plan(a, stores[1])

        win_score[p1] += (scores[0] == scores[1]) + 2 * (scores[0] > scores[1])
        win_score[p2] += (scores[0] == scores[1]) + 2 * (scores[1] > scores[0])

        print(f'Result of {p1.__name__} versus {p2.__name__}: {scores}')

    # Sort win_score dict by value
    win_score = dict(sorted(win_score.items(), key=lambda item: item[1]))

    print('\n*** Final scores ***')
    for player, score in win_score.items():
        print(f'{player.__name__}: {score}')

    print(f'\n{list(win_score.keys())[-1].__name__} is the winner!!!')


if __name__ == "__main__":
    main()
