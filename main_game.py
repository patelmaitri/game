
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
