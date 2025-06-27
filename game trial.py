game = 'i want to play a game'
print(id(game))

def game_board():
    game = "A game"
    print(id(game))
    return game

game = game_board()
print(game)
print(id(game))