game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def game_board(current_game, player=0, row=0, column=0, just_display=False):
    print("   0  1  2")
    if not just_display:
        game[row][column] = player
    for count, row in enumerate(current_game):
        print(count, row)
    return current_game


game_board(game)
game_board(game, player=2, row=0, column=0)

print(game)
print(id(game))
