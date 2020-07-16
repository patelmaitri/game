import pygame, sys, random, time

import images as imag
import methods as method

pygame.mixer.pre_init(frequency = 44100, size = 16, channels = 1, buffer = 256)

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

#flying Dino
fly_dino_list = []
SPAWNFLYDINO = pygame.USEREVENT
pygame.time.set_timer(SPAWNFLYDINO, 32000)

#player dino
DINOWALK = pygame.USEREVENT + 1
pygame.time.set_timer(DINOWALK, 200)

game_theme = pygame.mixer.music.load('nishat.mp3')
time.sleep(2)
pygame.mixer.music.play()

# game_theme = pygame.mixer.music.load('Sounds/DinoTheme.mp3')
# time.sleep(2)
# pygame.mixer.music.play()



pygame.init()

# screen = pygame.display.set_mode((576, 1024), pygame.RESIZABLE)
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
            if method.dino_index < 3:
                method.dino_index += 1
            else:
                method.dino_index = 0

            method.dino_surface, dino_rect = method.dino_animation()

        if event.type == SPAWNBOMB:
            bomb_list.append(method.create_bomb())

        #spawing dino
        if event.type == SPAWNFLYDINO:
            fly_dino_list.append(method.create_fly_dino())

    imag.screen.blit(imag.background, (0,0))
    method.ground_x_pos -= 2
    #screen.blit(imag.ground, (ground_x_pos, 720))

    method.draw_ground()

    if method.ground_x_pos <= -679:
        method.ground_x_pos = -50

    imag.screen.blit(method.dino_surface, method.dino_rect)
    bomb_list = method.bomb_movment(bomb_list)
    method.draw_bombs(bomb_list)

    fly_dino_list = method.move_fly_dino(fly_dino_list)
    method.draw_fly_dino(fly_dino_list)

    pygame.display.update()
    clock.tick(120)