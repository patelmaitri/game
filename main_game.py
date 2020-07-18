import pygame, sys, random, time

import images as imag
import methods as method

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
for x in range(10):
    numb = random.randint(1000,1500)
    print(numb)

print("FINAL RAND")   
print(numb)
pygame.time.set_timer(SPAWNBOMB, numb)
# pygame.time.set_timer(SPAWNBOMB, 1800)

#flying Dino
fly_dino_list = []
SPAWNFLYDINO = pygame.USEREVENT
pygame.time.set_timer(SPAWNFLYDINO, 3200)

#player dino
DINOWALK = pygame.USEREVENT + 1
pygame.time.set_timer(DINOWALK, 200)

# game_theme = pygame.mixer.music.load('Sounds/Nishat.mp3')
# time.sleep(2)
# pygame.mixer.music.play()

game_theme = pygame.mixer.music.load('Sounds/DinoTheme.mp3')
time.sleep(2)
pygame.mixer.music.play()




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
            if method.dino_rect.centery == 900:
                if event.key == pygame.K_SPACE:
                    dinoMovement = 0
                    dinoMovement -= 14

        if event.type == DINOWALK:
            if method.dino_index < 3:
                method.dino_index += 1
            else:
                method.dino_index = 0

            method.dino_surface, dino_rect = method.dino_animation()
        
    # numb = random.randint(1000,1500)
    # pygame.time.set_timer(SPAWNBOMB, numb)
        if event.type == SPAWNBOMB:
            bomb_list.append(method.create_bomb())

        #spawing dino
        if event.type == SPAWNFLYDINO:
            fly_dino_list.append(method.create_fly_dino())

    
    imag.screen.blit(imag.background, (0,0))
    method.ground_x_pos -= 2
    
    #screen.blit(imag.ground, (ground_x_pos, 720))

    method.draw_ground()


    if method.ground_x_pos <= -615:
        method.ground_x_pos = 0

   

    imag.screen.blit(method.dino_surface, method.dino_rect)
    bomb_list = method.bomb_movment(bomb_list)
    method.draw_bombs(bomb_list)
    
    dinoMovement += gravity
    method.dino_rect.centery += dinoMovement
    
    if method.dino_rect.centery > 900:
        method.dino_rect.centery = 900
    
    # bomb_list = method.bomb_movment(bomb_list)
    # method.draw_bombs(bomb_list)

    fly_dino_list = method.move_fly_dino(fly_dino_list)
    method.draw_fly_dino(fly_dino_list)
    method.check_collision(bomb_list)
    pygame.display.update()
    clock.tick(120)