import pygame
from board import *
from sprite import *

pygame.init()
TILESIZE = 64
n = 8
width = n*TILESIZE
height = n*TILESIZE
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("N queen problem")

queen_sprite = Sprite(TILESIZE - 10, TILESIZE - 10)
board = Board(n, queen_sprite)
board.solve(lambda: board.render(screen))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    
    board.update()


    pygame.display.update()
