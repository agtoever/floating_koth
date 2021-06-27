def strategy(is_new_game, store):
    if is_new_game:
        store['moves'] = []
    if store and store['moves']:
        return store['moves'][-1]
    return .1


def plan(opmove, store):
    if opmove > .5:
        if store and store['moves']:
            store['moves'].append(opmove / 2)
        else:
            store['moves'] = [opmove / 2]
    else:
        if store and store['moves']:
            store['moves'].append(opmove * 2)
        else:
            store['moves'] = [opmove * 2]
