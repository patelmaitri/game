<<<<<<< HEAD
import pygame, sys, random, time
import image as imag

pygame.init()

screen = pygame.display.set_mode((576, 1024), pygame.RESIZABLE)


#GAME LOOP
while True:
    #Event loop - NEEDED IN ANY GAME
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #Ends the game properly
            pygame.quit()
            sys.exit()
    


    
    screen.blit(imag.background, (0,0))
    screen.blit(imag.ground, (-50, 720))
    screen.blit(imag.bomb, (400, 900))
    screen.blit(imag.fly_dino1, (350, 450))
    screen.blit(imag.dinoMain, (10, 800))

    pygame.display.update()

=======
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
    screen.blit(background,(0,0)) #background
    screen.blit(ground,(-50,400)) #ground

    pygame.display.update()
    clock.tick(120)
>>>>>>> a6cb196adcd7282a4c7067f03a0d55b49745f6a1
