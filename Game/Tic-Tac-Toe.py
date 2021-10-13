global board
board = [[" "," "," "],[" "," "," "],[" ", " ", " "]]
player = "X"
'''
Print the board visually
'''
def printBoard(board):
    for line in board:
        print(line)

'''
Take input and replace the appropriate space
'''
def makeMove():
    global player
    x = int(input("What is the X co-ordinate: "))
    y = int(input("What is the Y co-ordinate: "))
    if player == "X":
        board[y][x] = "X"
        player = "0"
    else:
        board[y][x] = "0"
        player = "X"

def tictac():
    printBoard(board)
    makeMove()
    printBoard()


def main():
    gamewon = False
    while gamewon == False:
        tictac
    print("GAMEOVER")



main()