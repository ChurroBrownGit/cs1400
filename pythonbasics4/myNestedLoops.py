#Goal 1
for i in range(10):
    for j in range(10):
        print("*", end = ' ')
    print(" ")

#Goal 2
def multTable(h,g):
    for h in range(1,13):
        for g in range(1,13):
            print(h*g, end = ' ')
        print(" ")

multTable(1,1)

#Goal 3
b = 1
for c in range(24):
    print(" " * int(24 - b), end="")  
    for a in range(1, b):
        print("*", end=" ")
    print()
    b += 1

#Challenge 1
def matrix_increment(lists):
    for i in lists:
        for f in range(len(i)):
            i[f] += 1
    return lists    

list = matrix_increment([[1,1,1,1], [1,1,1,1], [1,1,1,1],[1,1,1,1]])
print(list)

#Challenge 2
def print_ttt_board(board):
    for i in range(3):
        print(" " + (board[i][0] if board[i][0] else " ") + " | " +
        (board[i][1] if board[i][1] else " ") + " | " +
        (board[i][2] if board[i][2] else " "))
        if i < 2:
                print("-----------")

board = [
    ["X", "O", " "],
    ["O", "X", " "],
    ["O", "X", "O"]
]

print_ttt_board(board)