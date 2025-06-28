game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        print("   0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except:
        print("nah you cant do that")
        return False

game_board(game)
print(id(game))
game_board(game, player=2, row=10, column=0)
print(id(game))

