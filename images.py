import pygame

screen = pygame.display.set_mode((576, 1024), pygame.RESIZABLE)

#background
background = pygame.image.load('assets/background.png')
background = pygame.transform.scale(background, (576, 1024))

#ground
ground = pygame.image.load('assets/ground.png')

rain = pygame.image.load('assets/Rain1.png')
#bomb
bomb_img = pygame.image.load('assets/bomb.png')
bomb_img = pygame.transform.scale(bomb_img, (50,50))

#player dino
dino1 = pygame.transform.scale(pygame.image.load('assets/ino1.png'),(180,300))
dino2 = pygame.transform.scale(pygame.image.load('assets/ino2.png'),(180,300))
dino3 = pygame.transform.scale(pygame.image.load('assets/ino3.png'),(180,300))
dino4 = pygame.transform.scale(pygame.image.load('assets/ino4.png'),(180,300))

#flying dinos
fly_dino1 = pygame.transform.scale(pygame.image.load('assets/1FlyDino.png'),(220, 220))
fly_dino1 = pygame.transform.flip(fly_dino1, True, False)

fly_dino2 = pygame.transform.scale(pygame.image.load('assets/2FlyDino.png'), (220, 220))
fly_dino2 = pygame.transform.flip(fly_dino2, True, False)

fly_dino3 = pygame.transform.scale(pygame.image.load('assets/3FlyDino.png'), (220, 220))
fly_dino3 = pygame.transform.flip(fly_dino3, True, False)

fly_dino4 = pygame.transform.scale(pygame.image.load('assets/4FlyDino.png'), (220, 220))
fly_dino4 = pygame.transform.flip(fly_dino4, True, False)
