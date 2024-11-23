board = [
    [1, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

def has_queen(row, col):
    return board[row][col] == 1

def is_safe(row, col):
    # 1. check if there is queen in row
    # 2. check if there is queen in col
    # 3. check if there is queen in diagonal
    # 4. check if there is queen in second diagonal

    # ROW CHECK
    # 1. check left positions
    for c in range(col - 1, -1, -1):
        if has_queen(row, c):
            return False
    # 2. check right positions
    for c in range(col + 1, len(board[0])):
        if has_queen(row, c):
            return False
    
    # COLUMN CHECK
    # check top positions
    for r in range(row - 1, -1, -1):
        if has_queen(r, col):
            return False

    # check bottom positions
    for r in range(row + 1, len(board)):
        if has_queen(r, col):
            return False

    # FIRST DIAGONAL
    # check left upwards
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if has_queen(i, j):
            return False
        i -= 1
        j -= 1

    # check right downwards
    i = row + 1
    j = col + 1
    while i < len(board) and j < len(board):
        if has_queen(i, j):
            return False
        i += 1
        j += 1    

    # SECOND DIAGONAL
    # check right upwards
    i = row - 1
    j = col + 1
    while i >= 0 and j < len(board):
        if has_queen(i, j):
            return False
        i -= 1
        j += 1
    
    # check left downwards
    i = row + 1
    j = col - 1
    while j >= 0 and i < len(board):
        if has_queen(i, j):
            return False
        i += 1
        j -= 1

    return True

