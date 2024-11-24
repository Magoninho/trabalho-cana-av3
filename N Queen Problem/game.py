import pygame
from board import *
from sprite import *
from settings import *

pygame.init()
width = N*TILESIZE
height = N*TILESIZE
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("N queen problem")

queen_sprite = Sprite(TILESIZE - 10, TILESIZE - 10)
board = Board(N, queen_sprite)
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
