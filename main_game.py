import pygame, sys, random, time
import image as imag

def dino_animation():
    new_dino = dino_frames[dino_index]
    new_dino_rect = new_dino.get_rect(center= (125, dino_rect.centery))
    return new_dino,new_dino_rect

pygame.init()

screen = pygame.display.set_mode((576, 1024), pygame.RESIZABLE)
clock = pygame.time.Clock()

#Game variables
dinoMovement = 0
gravity = 0.75

score = 0
highScore = 0

ground_x_pos = -50

dino1 = pygame.transform.scale((pygame.image.load('assets/dino1.png').convert_alpha()),(250,150))
dino2 = pygame.transform.scale((pygame.image.load('assets/dino2.png').convert_alpha()),(250,150))
dino3 = pygame.transform.scale((pygame.image.load('assets/dino3.png').convert_alpha()),(250,150))
dino4 = pygame.transform.scale((pygame.image.load('assets/dino4.png').convert_alpha()),(250,150))

dino_frames = [dino1,dino2,dino3,dino4]
dino_index = 2
dino_surface = dino_frames[dino_index]
dino_rect = dino_surface.get_rect(center = (125,900))

DINOWALK = pygame.USEREVENT + 1
pygame.time.set_timer(DINOWALK, 200)


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

        if event.type == DINOWALK:
            if dino_index < 3:
                dino_index += 1
            else:
                dino_index = 0

            dino_surface, dino_rect = dino_animation()


    screen.blit(imag.background, (0,0))
    ground_x_pos -= 2
    screen.blit(imag.ground, (ground_x_pos, 720))
    screen.blit(dino_surface, dino_rect)
    # screen.blit(imag.bomb, (400, 900))
    # screen.blit(imag.fly_dino1, (350, 450))
    # screen.blit(imag.dinoMain, (10, 800))

    pygame.display.update()
    clock.tick(120)
