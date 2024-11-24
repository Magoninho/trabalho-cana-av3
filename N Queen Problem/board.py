import pygame
import time
from sprite import *
from settings import *


class Board:
    def __init__(self, n, queen_sprite):
        self.n = n
        self.board = self.generate_board()
        self.queen_sprite = queen_sprite
        self.enter_pressed = False

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
    
    def solve(self, callback):
        self.solveUntilN(self.board, 0, callback)
        
    
    def solveUntilN(self, board, col, callback):

        if col >= self.n:
            return True
        
        # looping trough rows and placing queens
        for i in range(self.n):
            # if its safe
            if self.is_safe(i, col):
                self.board[i][col] = 1
                callback()
                pygame.display.update()
                time.sleep(2**(-N)*16)
                if self.solveUntilN(self.board, col + 1, callback) == True:
                    return True
                # remove the queen
                self.board[i][col] = 0
        
        return False   

    def user_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN] and not self.enter_pressed:
            print('apertou enter')
            self.enter_pressed = True
        
        if not keys[pygame.K_RETURN] and self.enter_pressed:
            self.enter_pressed = False
        
                    
    def update(self):
        pass


    def render(self, screen):

        self.draw_board(screen)

        
    def draw_queen_on_spot(self, screen, i, j):
        self.queen_sprite.draw(screen, i * TILESIZE + 5, j * TILESIZE + 5)
    
    # draws the current board state
    def draw_board(self, screen):
        self.draw_tiles(screen)

        for row in range(self.n):
            for col in range(self.n):
                if self.has_queen(row, col):
                    self.draw_queen_on_spot(screen, row, col)

    def draw_tiles(self, screen):
        for i in range(self.n):
            for j in range(self.n):
                color = (240, 217, 181) if (i + j) % 2 == 0 else (181, 136, 99)
                pygame.draw.rect(screen, color, (i * TILESIZE, j * TILESIZE, TILESIZE, TILESIZE))
            