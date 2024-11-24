import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, width, height):
    
        pygame.sprite.Sprite.__init__(self)
    
        self.image = pygame.image.load("queen.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))

        self.rect = self.image.get_rect()
    
    def draw(self, screen, x, y):
        self.rect.x = x
        self.rect.y = y
        screen.blit(self.image, self.rect)
