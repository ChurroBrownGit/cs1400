def makeboard():
    board = [[" "," "," "], [" ", " ", " "], [" ", " ", " "]]
    return board

def clearBoard(board):
    for i in range(3):
        for f in range(3):
            board[i][f] = [" "]
            return board

def whosTurn(b):
    countX = 1
    countO = 0
    if countX > countO:
        countO += 1
        xTurn = True
        oTurn = False
        return xTurn, oTurn
    if countO == countX:
        countX += 1
        oTurn = True
        xTurn = False
        return xTurn, oTurn

def play(oTurn, xTurn, board):
    if oTurn == True:
        print(board[0])
        print(board[1])
        print[board[2]]
    if xTurn == True:
        print(board[0])
        print(board[1])
        print[board[2]]
        col = int(input("Choose a num b"))
    

def isGameOver(board):
    hasEmpty = False
    for i in board:
        for f in board:
            if f == " ":
                hasEmpty = True
    if not hasEmpty:
        return True
    w = winner(board)
    if board != "":
        return True
    return False

def winner(board):
