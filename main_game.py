import pygame, sys, random, time

import images as imag
import methods as method

pygame.init()

#game variables
dinoMovement = 0
gravity = 0.75


#score
score = 0
high_score = 0

def score_display(game_state):
    if game_state == 'main_game'
        score_surface = game_font.render(str(int(score)),True,(255,255,255))
        score_rect = score_surface.get_rect(center = (288,100))
        imag.screen.blit(score_surface,score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f'Score: {int(score)}', True,(255,255,255))
        score_rect = score_surface.get_rect(center = (288, 100))
        screen.blit(score_surface,score_rect) 

        high_score_surface = game_font.render(f'High score: {int(high_score)}', True,(255,255,255))
        high_score_rect = high_score_surface.get_rect(center = (288, 500))
        screen.blit(high_score_surface,high_score_rect)

def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score

#bomb
bomb_list = []
SPAWNBOMB = pygame.USEREVENT
pygame.time.set_timer(SPAWNBOMB, random.randint(2300, 15000))


#player dino
DINOWALK = pygame.USEREVENT + 1
pygame.time.set_timer(DINOWALK, 200)

fly_dino_list = []
FLYDINOWALK = pygame.USEREVENT + 2
pygame.time.set_timer(FLYDINOWALK, 200)

clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19.ttf', 40)


#GAME LOOP
while True:
    #Event loop - NEEDED IN ANY GAME
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #Ends the game properly
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if method.dino_rect.centery == 900:
                if event.key == pygame.K_SPACE:
                    dinoMovement = 0
                    dinoMovement -= 14

        if event.type == DINOWALK:
            if method.dino_index < 3:
                method.dino_index += 1
            else:
                method.dino_index = 0

            method.dino_surface, method.dino_rect = method.dino_animation()

        if event.type == FLYDINOWALK:
            # fly_dino_list.append(method.create_fly_dino())
            
            # print(fly_dino_list)
            # method.draw_flydino(fly_dino_list)

            if method.fly_dino_index < 3:
                method.fly_dino_index += 1
            else:
                method.fly_dino_index = 0

            # method.fly_dino_surface = method.fly_dino_animation()


        if event.type == SPAWNBOMB:
            bomb_list.append(method.create_bomb())
            pygame.time.set_timer(SPAWNBOMB, random.randint(2300, 15000))

    imag.screen.blit(imag.background, (0,0))
    method.ground_x_pos -= 2
    method.flyx -= 2
    # imag.screen.blit(imag.ground, (method.ground_x_pos, 720))
 
    method.draw_ground()
    method.draw_flydino()

    score += 0.01
    score_display('main_game')
    #else:
    #high_score = update_score(score, high_score)
    #score_diplay('game_over')
    # print(method.ranchoice)
    
    if method.flyx <= -1200:
        method.flyx = 500


    if method.ground_x_pos <= -615:
        method.ground_x_pos = -0

    imag.screen.blit(method.dino_surface, method.dino_rect)
    bomb_list = method.bomb_movment(bomb_list)
    method.draw_bombs(bomb_list)
    # imag.screen.blit(method.fly_dino_surface, (0,0))
    # imag.screen.blit(method.fly_dino_surface, method.fly_dino_rect)
    
    dinoMovement += gravity
    method.dino_rect.centery += dinoMovement

    if method.dino_rect.centery > 700:
        method.dino_rect.centery = 700

    method.check_collision(bomb_list)

    pygame.display.update()
    clock.tick(120)