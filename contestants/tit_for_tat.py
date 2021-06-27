def strategy(is_new_game, store):
    if is_new_game:
        return 1
    return store["opmove"]


def plan(opmove, store):
    store["opmove"] = opmove
