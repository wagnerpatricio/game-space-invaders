import pygame
import math
import random


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/asteroid.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(200, 50, 100, 100)

        self.rect.y = 0 + random.randint(1,2)
        self.rect.x = random.randint(1, 800)

        

        self.speed = 1 + random.random() * 2


    def update(self, *args):
        self.rect.y += self.speed

        if self.rect.top > 480:
            self.kill()
            
