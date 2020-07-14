import pygame, sys, random

#calling the files
from image import *

pygame.init()

#display surface
# screen = pygame.display.set_mode((567,1024),pygame.RESIZABLE)
clock = pygame.time.Clock()

# background = pygame.image.load('assets/background.png').convert()


#game lopp
while True:

    #looking for events
    for event in pygame.event.get():
        #closing the window with X
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #creating a new surafce on the screen
    screen.blit(background,(0,0))
    screen.blit(ground,(0,0))

    pygame.display.update()
    clock.tick(120)