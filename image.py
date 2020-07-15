<<<<<<< HEAD
import pygame, sys, random, time
=======
import pygame, sys

screen = pygame.display.set_mode((632,1024),pygame.RESIZABLE)

background = pygame.image.load('assets/background.png').convert()
#background = pygame.transform.scale2x(background)
>>>>>>> a6cb196adcd7282a4c7067f03a0d55b49745f6a1

background = pygame.image.load('assets/background.png')

background = pygame.transform.scale(background, (576, 1024))


bomb = pygame.image.load('assets/bomb.png')
bomb = pygame.transform.scale(bomb, (75, 75))

ground = pygame.image.load('assets/ground.png')

<<<<<<< HEAD

# ground = pygame.transform.scale(ground, )

fly_dino1 = pygame.image.load('assets/1FlyDino.png')
fly_dino1 = pygame.transform.scale(fly_dino1, (220, 220))
fly_dino1 = pygame.transform.flip(fly_dino1, True, False)

dinoMain = pygame.image.load('assets/dino1.png')
dinoMain = pygame.transform.scale(dinoMain, (300, 200))


# fly_dino2 = pygame.image.load('assets/2FlyDino.png').convert()

# fly_dino3 = pygame.image.load('assets/3FlyDino.png').convert()

# fly_dino4 = pygame.image.load('assets/4FlyDino.png').convert()
=======
fly_dino4 = pygame.image.load('assets/4FlyDino.png').convert()
>>>>>>> a6cb196adcd7282a4c7067f03a0d55b49745f6a1
