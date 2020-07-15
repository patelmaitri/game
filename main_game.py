import pygame, sys, random, time
import image as imag


pygame.init()


def draw_ground():
    screen.blit(imag.ground, (ground_x_pos, 720))
    screen.blit(imag.ground, (ground_x_pos + 576, 720))


def create_bomb():
    new_bomb = imag.bomb.get_rect(midbottom = (585, 1000))
    return new_bomb

def bomb_movment(bombs):
    for bomb in bombs:
        bomb.centerx -= 5
    return bombs

def draw_bombs(bombs):
    for bomb in bombs:
        screen.blit(imag.bomb, bomb)





screen = pygame.display.set_mode((576, 1024), pygame.RESIZABLE)
clock = pygame.time.Clock()

#Game variables
dinoMovement = 0
gravity = 0.75

score = 0
highScore = 0

ground_x_pos = -50

bomb_list = []
SPAWNBOMB = pygame.USEREVENT
pygame.time.set_timer(SPAWNBOMB, 4500)

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
        if event.type == SPAWNBOMB:
            bomb_list.append(create_bomb())

    


    
    screen.blit(imag.background, (0,0))
    ground_x_pos -= 2
    draw_ground()
    if ground_x_pos <= -576:
        ground_x_pos = 0

    bomb_list = bomb_movment(bomb_list)
    draw_bombs(bomb_list)
    
    # screen.blit(imag.bomb, (400, 900))
    # screen.blit(imag.fly_dino1, (350, 450))
    # screen.blit(imag.dinoMain, (10, 800))

    pygame.display.update()
    clock.tick(120)
