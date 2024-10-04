ROUNDS = 3

def play_game(game_function):
    for _ in range(ROUNDS):
        game_function()
