import pygame
from spacex import Spacex
from asteroid import Asteroid
from shot import Shot
import random

#Inicializando o pygame e criando a janela
pygame.init()

display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("Elon Invader")


#Grupos
objectGroup = pygame.sprite.Group()

asteroidGroup = pygame.sprite.Group()

shotGroup = pygame.sprite.Group()


#Fundo
bg = pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load("data/background.png")
bg.image = pygame.transform.scale(bg.image, [840, 480])
bg.rect = bg.image.get_rect()

spacex1 = Spacex(objectGroup)





#Musica
pygame.mixer.music.load("data/music.ogg")
pygame.mixer.music.play(-1)

#Sons
shot = pygame.mixer.Sound("data/shot.mp3")
reload = pygame.mixer.Sound("data/reload.wav")



gameLoop = True
gameOver = False
timer = 20
clock = pygame.time.Clock()
isPressingW = False
if __name__ == "__main__":
  while gameLoop:
    clock.tick(60)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        gameLoop = False
      elif event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE and not gameOver:
          reload.play()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          shot.play()    
          newShot =Shot(objectGroup, shotGroup)
          newShot.rect.center = spacex1.rect.center
               

    #Logica de atualização:
    if not gameOver:
      objectGroup.update()

      timer += 1
      if timer > 30:
        timer = 0
        if random.random() < 0.3:
          newAsteroid = Asteroid(objectGroup, asteroidGroup)

        collisions = pygame.sprite.spritecollide(spacex1, asteroidGroup, False, pygame.sprite.collide_mask)

        if collisions:
          print("Game Over!") 
          gameOver = True 

          

                                       
        


      hits = pygame.sprite.groupcollide(shotGroup, asteroidGroup, True, True, pygame.sprite.collide_mask)

    #Atualização e desenho
    display.fill([35, 35, 45]) #cor do fundo
        
    objectGroup.draw(display) 

    pygame.display.update()