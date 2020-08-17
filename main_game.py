import pygame, sys, random, time

import images as imag
import methods as method

pygame.init()

#game variables
dinoMovement = 0
gravity = 1.0

#score

game_active = True
score = 0
high_score = 0

pygame.init()
def score_display(game_state):
    if game_state == 'main_game':
        score_surface = game_font.render(str(int(score)),True,(255,255,255))
        score_rect = score_surface.get_rect(center = (288,100))
        imag.screen.blit(score_surface,score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f'Score: {int(score)}', True,(255,255,255))
        score_rect = score_surface.get_rect(center = (288, 100))
        imag.screen.blit(score_surface,score_rect)

        high_score_surface = game_font.render(f'High score: {int(high_score)}', True,(255,255,255))
        high_score_rect = high_score_surface.get_rect(center = (288, 500))
        imag.screen.blit(high_score_surface,high_score_rect)

def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score

#bomb
bomb_list = []
SPAWNBOMB = pygame.USEREVENT
pygame.time.set_timer(SPAWNBOMB, random.randint(4000,9000))
# pygame.time.set_timer(SPAWNBOMB, 1800)

#flying Dino
fly_dino_list = []
FLYDINOWALK = pygame.USEREVENT+1
pygame.time.set_timer(FLYDINOWALK, 3200)

#player dino
DINOWALK = pygame.USEREVENT + 2
pygame.time.set_timer(DINOWALK, 200)

# game_theme = pygame.mixer.music.load('Sounds/Nishat.mp3')
# time.sleep(2)
# pygame.mixer.music.play()

# game_theme = pygame.mixer.music.load('Sounds/DinoTheme.mp3')
# time.sleep(2)
# pygame.mixer.music.play()

# screen = pygame.display.set_mode((576, 1024), pygame.RESIZABLE)
clock = pygame.time.Clock()

game_font = pygame.font.Font('assets/04B_19.ttf', 40)
#GAME LOOP
while True:
    #Event loop - NEEDED IN ANY GAME
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #Ends the game properly
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if method.dino_rect.centery == 850:
                if event.key == pygame.K_SPACE and game_active:
                    dinoMovement = 0
                    dinoMovement -= 16
                if event.key == pygame.K_SPACE and game_active == False:
                    game_active = True
                    bomb_list.clear()
                    dinoMovement = 0
                    score = 0


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
            pygame.time.set_timer(SPAWNBOMB, random.randint(4000,9000))

        if event.type == FLYDINOWALK:
            # fly_dino_list.append(method.create_fly_dino())

            # print(fly_dino_list)
            # method.draw_flydino(fly_dino_list)

            if method.fly_dino_index < 3:
                method.fly_dino_index += 1
            else:
                method.fly_dino_index = 0

    imag.screen.blit(imag.background, (0,0))
    method.ground_x_pos -= 2
    method.flyx -=5
    #screen.blit(imag.ground, (ground_x_pos, 720))


    method.draw_ground()
    method.draw_flydino()

    if method.ground_x_pos <= -615:
        method.ground_x_pos = 0

    if method.flyx <= -1200:
        method.flyx = 500

    # bomb_list = method.bomb_movment(bomb_list)
    # method.draw_bombs(bomb_list)
    if game_active:
        dinoMovement += gravity
        method.dino_rect.centery += dinoMovement
        game_active = method.check_collision(bomb_list)

        if method.dino_rect.centery > 850:
            method.dino_rect.centery = 850

        imag.screen.blit(method.dino_surface, method.dino_rect)
        bomb_list = method.bomb_movment(bomb_list)
        method.draw_bombs(bomb_list)

        score += 0.1
        score_display('main_game')
    else:
        imag.screen.blit(imag.game_over_surface,imag.game_over_rect)
        high_score = update_score(score,high_score)
        score_display('game_over')


    pygame.display.update()
    clock.tick(120)
