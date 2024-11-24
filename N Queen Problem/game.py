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
# queen = Sprite(5, 5, TILESIZE - 10, TILESIZE - 10)
queen_sprite = Sprite(TILESIZE - 10, TILESIZE - 10)

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

    board.update()
    board.render(screen)

    pygame.display.update()
