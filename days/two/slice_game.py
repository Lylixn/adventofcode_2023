def slice_game(game: str):
    game_id = ''
    for i in range(0, len(game)):
        if game[i].isdigit():
            game_id += game[i]
    return int(game_id)
