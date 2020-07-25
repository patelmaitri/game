import pygame, sys, random, time

import images as imag
import new_methods as new_method

pygame.init()

#game variables
dinoMovement = 0
gravity = 0.75

#score
score = 0
highScore = 0

#bomb
bomb_list = []
SPAWNBOMB = pygame.USEREVENT
pygame.time.set_timer(SPAWNBOMB, 2000)


#player dino
DINOWALK = pygame.USEREVENT + 3
pygame.time.set_timer(DINOWALK, 200)

fly_dino_list = []
FLYDINOWALK = pygame.USEREVENT + 4
pygame.time.set_timer(FLYDINOWALK, 200)

clock = pygame.time.Clock()


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
                dinoMovement = -6

        if event.type == DINOWALK:
            if new_method.dino_index < 3:
                new_method.dino_index += 1
            else:
                new_method.dino_index = 0

            new_method.dino_surface, new_method.dino_rect = new_method.dino_animation()

        if event.type == FLYDINOWALK:
            # fly_dino_list.append(new_method.create_fly_dino())
            
            # print(fly_dino_list)
            # new_method.draw_flydino(fly_dino_list)

            if new_method.fly_dino_index < 3:
                new_method.fly_dino_index += 1
            else:
                new_method.fly_dino_index = 0

            # new_method.fly_dino_surface = new_method.fly_dino_animation()


        if event.type == SPAWNBOMB:
            bomb_list.append(new_method.create_bomb())


    imag.screen.blit(imag.background, (0,0))
    new_method.ground_x_pos -= 2
    new_method.flyx -= 2
    # imag.screen.blit(imag.ground, (new_method.ground_x_pos, 720))

    new_method.draw_ground()
    new_method.draw_flydino()
    
    if new_method.flyx <= -1200:
        new_method.flyx = 500


    if new_method.ground_x_pos <= -615:
        new_method.ground_x_pos = -0

    imag.screen.blit(new_method.dino_surface, new_method.dino_rect)
    # imag.screen.blit(new_method.fly_dino_surface, (0,0))
    # imag.screen.blit(new_method.fly_dino_surface, new_method.fly_dino_rect)
    
    bomb_list = new_method.bomb_movment(bomb_list)
    new_method.draw_bombs(bomb_list)


    pygame.display.update()
    clock.tick(120)