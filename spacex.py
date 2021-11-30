import pygame

class Spacex(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/spaceX.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(360, 360, 100, 100)

        self.speed = 0
        self.acceleration = 0.1
    
    def update(self, *args):
        #Logica
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
          self.speed -= self.acceleration
        elif keys[pygame.K_d]:
          self.speed += self.acceleration
        else:
            self.speed *= 0.95  

        self.rect.x += self.speed  
           


        if self.rect.x < 0:
            self.rect.x = 0
            self.speed = 0
        elif self.rect.x > 745:
            self.rect.x = 745 
            self.speed = 0    