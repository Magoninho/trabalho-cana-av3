import pygame
import sprite

TILESIZE=64

class Board:
    def __init__(self, n):
        self.n = n
        self.board = self.generate_board()

    def generate_board(self):
        board = []
        for i in range(self.n):
            board.append([])
            for j in range(self.n):
                board[i].append(0)
        
        return board

    def has_queen(self, row, col):
        return self.board[row][col] == 1

    def print_board(self):
        for line in self.board:
            print(line)

    def is_safe(self, row, col):
        # 1. check if there is queen in row
        # 2. check if there is queen in col
        # 3. check if there is queen in diagonal
        # 4. check if there is queen in second diagonal

        # ROW CHECK
        # 1. check left positions
        for c in range(col - 1, -1, -1):
            if self.has_queen(row, c):
                return False
        # 2. check right positions
        for c in range(col + 1, len(self.board[0])):
            if self.has_queen(row, c):
                return False
        
        # COLUMN CHECK
        # check top positions
        for r in range(row - 1, -1, -1):
            if self.has_queen(r, col):
                return False

        # check bottom positions
        for r in range(row + 1, len(self.board)):
            if self.has_queen(r, col):
                return False

        # FIRST DIAGONAL
        # check left upwards
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if self.has_queen(i, j):
                return False
            i -= 1
            j -= 1

        # check right downwards
        i = row + 1
        j = col + 1
        while i < len(self.board) and j < len(self.board):
            if self.has_queen(i, j):
                return False
            i += 1
            j += 1    

        # SECOND DIAGONAL
        # check right upwards
        i = row - 1
        j = col + 1
        while i >= 0 and j < len(self.board):
            if self.has_queen(i, j):
                return False
            i -= 1
            j += 1
        
        # check left downwards
        i = row + 1
        j = col - 1
        while j >= 0 and i < len(self.board):
            if self.has_queen(i, j):
                return False
            i += 1
            j -= 1

        return True
    
    def solve(self):
        self.solveUntilN(self.board, 0)
        
    
    def solveUntilN(self, board, col):

        if col >= self.n:
            return True
        
        # looping trough rows and placing queens
        for i in range(self.n):
            # if its safe
            if self.is_safe(i, col):
                self.board[i][col] = 1
                self.print_board()
                print()
                if self.solveUntilN(self.board, col + 1) == True:
                    return True
                # remove the queen
                self.board[i][col] = 0
        
        return False   
    
    def draw_queens(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.has_queen(i, j):
                    sprite.queen_list.add(sprite.Sprite(j * TILESIZE + 5, i * TILESIZE + 5, TILESIZE - 10, TILESIZE - 10))

                    


    def draw_board(self, screen):
        for i in range(self.n):
            for j in range(self.n):
                color = (240, 217, 181) if (i + j) % 2 == 0 else (181, 136, 99)
                pygame.draw.rect(screen, color, (i * TILESIZE, j * TILESIZE, TILESIZE, TILESIZE))
            