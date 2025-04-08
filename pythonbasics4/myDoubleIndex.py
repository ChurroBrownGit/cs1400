#Goal 1
tictactoetest = [
    'x', 'o', 'x', 
    'o', ' ', 'x', 
    'x', 'o', ' '
]

#Goal 2
zeros = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

#Challenge 1
def centerX(board):
    for i in range(len(board)):
        for f in range(len(board[i])):
            board[1][1] = "X"
            return board

new_board = centerX([['x', 'o', 'x'], ['o', ' ', 'x'], ['x', 'o', ' ']])
print(new_board)

#Challenge 2
def moveX(boards, i, f):
    boards[i][f] = "X"
    return boards

moved_board = moveX([['x', 'o', 'x'], ['o', ' ', 'x'], ['x', 'o', ' ']], 1, 2)
print(moved_board)