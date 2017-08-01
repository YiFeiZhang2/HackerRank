[r, c, n] = list(map(int, input().strip().split(' ')))

def nextToBomb(board, i, j):
    if i+1 < r and board[i+1][j] == 1:
        return True
    elif i-1 >= 0 and board[i-1][j] == 1:
        return True
    elif j+1 < c and board[i][j+1] == 1:
        return True
    elif j-1 >= 0 and board[i][j-1] == 1:
        return True
    else:
        return False

def tick(board):
    n_board = []
    for i in range(len(board)):
        r = []
        for j in range(len(board[i])):
            if board[i][j] != 1 and nextToBomb(board, i, j):
                r.append(-1)
            else:
                r.append(board[i][j])
        n_board.append(r)
        
    for i in range(len(n_board)):
        for j in range(len(n_board[i])):
            if n_board[i][j] == -1:
                n_board[i][j] = 0
            elif n_board[i][j] != 0:
                n_board[i][j] = n_board[i][j] - 1
    #print('NB IS')
    #print(n_board)
    return n_board

def fill(board):
    n_board = []
    for row in board:
        r = []
        for e in row:
            if e != 0:
                r.append(e-1)
            else:
                r.append(3)
        n_board.append(r)
    return n_board
    
def printBoard(board):
    for r in board:
        for e in r:
            if e == 0:
                print('.', end = '')
            else:
                print('O', end='')
        print()

boardstates = []
board = []
for i in range(r):
    row = input().strip()
    board.append([3 if x == 'O' else 0 for x in row])
    
boardstates.append(board)
for i in range(0, 5):
    if i%2 == 0:
        boardstates.append(tick(boardstates[i]))
    else:
        boardstates.append(fill(boardstates[i]))
        
if n > 5 and n%4 > 1:        
    printBoard(boardstates[n%4])
elif n> 5 and n%4 < 2:
    printBoard(boardstates[n%4 + 4])
else:
    printBoard(boardstates[n])
                
    