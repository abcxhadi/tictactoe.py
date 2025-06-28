game = "this is a game"
print(game,id(game))

def game_board():
    global game
    game = ("A game")

game_board()
print(game)
print(id(game))