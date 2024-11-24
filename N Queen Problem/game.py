import pygame
from board import *
from sprite import *

TILESIZE = 64
n = 4
width = n*TILESIZE
height = n*TILESIZE
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("N queen problem")

board = Board(n)
queen = Sprite(5, 5, TILESIZE - 10, TILESIZE - 10)

queen_list = pygame.sprite.Group()
queen_list.add(queen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    
    screen.fill((0, 0, 0))

    board.draw_board(screen)
    queen_list.draw(screen)

    pygame.display.update()
        
