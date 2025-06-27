game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

def game_board(player=0, row=0, column=0):
    game[row][column] = player
    print('   0  1  2')
    for count, row in enumerate(game):
        print(count, row)
      
game_board(just_display = True)
game_board(player=2, row=0, column=0)


