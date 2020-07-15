import pygame, sys, random, time

#background
background = pygame.image.load('assets/background.png')
background = pygame.transform.scale(background, (576, 1024))

#ground
ground = pygame.image.load('assets/ground.png')

#bomb
bomb = pygame.image.load('assets/bomb.png')
bomb = pygame.transform.scale(bomb, (75, 75))

#player dino
dinoMain = pygame.image.load('assets/dino1.png')
dinoMain = pygame.transform.scale(dinoMain, (300, 200))

#dinos
fly_dino1 = pygame.image.load('assets/1FlyDino.png')
fly_dino1 = pygame.transform.scale(fly_dino1, (220, 220))
fly_dino1 = pygame.transform.flip(fly_dino1, True, False)
# fly_dino2 = pygame.image.load('assets/2FlyDino.png')

# fly_dino3 = pygame.image.load('assets/3FlyDino.png')

# fly_dino4 = pygame.image.load('assets/4FlyDino.png')