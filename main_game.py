import pygame, sys, random, time
import image as imag


pygame.init()


def draw_ground():
    screen.blit(imag.ground, (ground_x_pos, 720))
    screen.blit(imag.ground, (ground_x_pos + 576, 720))



screen = pygame.display.set_mode((576, 1024), pygame.RESIZABLE)
clock = pygame.time.Clock()

#Game variables
dinoMovement = 0
gravity = 0.75

score = 0
highScore = 0

ground_x_pos = -50

#GAME LOOP
while True:
    #Event loop - NEEDED IN ANY GAME
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #Ends the game properly
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dinoMovement = 0
                dinoMovement = -12

    


    
    screen.blit(imag.background, (0,0))
    ground_x_pos -= 5
    draw_ground()
    
    # screen.blit(imag.bomb, (400, 900))
    # screen.blit(imag.fly_dino1, (350, 450))
    # screen.blit(imag.dinoMain, (10, 800))

    pygame.display.update()
    clock.tick(120)
