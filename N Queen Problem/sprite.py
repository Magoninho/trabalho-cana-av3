import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
    
        super().__init__()
    
        self.image = pygame.image.load("queen.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y