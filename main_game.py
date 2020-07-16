import pygame, sys, random, time
import image as imag

def create_fly_dino():
    random_fly_dion_pos = random.choice(fly_dino_height)
    new_fly_dino = imag.fly_dino1.get_rect(midtop = (700, random_fly_dion_pos))
    return new_fly_dino

def move_fly_dino(fdinos):
    for fdino in fdinos:
        fdino.centerx -= 5
    return fdinos

def draw_fly_dino(fdinos):
    for fdino in fdinos:
        screen.blit(imag.fly_dino1, fdino)

def draw_ground():
    #-50,720
    526
    screen.blit(imag.ground, (ground_x_pos, 720))
    screen.blit(imag.ground, (ground_x_pos + 679, 720))

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

bomb_list = []
SPAWNBOMB = pygame.USEREVENT
pygame.time.set_timer(SPAWNBOMB, 300)

#Flying Dino
fly_dino_list = []
SPAWNFLYDINO = pygame.USEREVENT
pygame.time.set_timer(SPAWNFLYDINO, 10000)
fly_dino_height = [200, 700, 800]

dino1 = pygame.transform.scale((pygame.image.load('assets/dino1.png').convert_alpha()),(250,150))
dino2 = pygame.transform.scale((pygame.image.load('assets/dino2.png').convert_alpha()),(250,150))
dino3 = pygame.transform.scale((pygame.image.load('assets/dino3.png').convert_alpha()),(250,150))
dino4 = pygame.transform.scale((pygame.image.load('assets/dino4.png').convert_alpha()),(250,150))

dino_frames = [dino1,dino2,dino3,dino4]
dino_index = 2
dino_surface = dino_frames[dino_index]
dino_rect = dino_surface.get_rect(center = (125,900))

game_theme = pygame.mixer.music.load('Sounds/nishat.mp3')
pygame.mixer.music.play()

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
                dinoMovement = -6

        if event.type == DINOWALK:
            if dino_index < 3:
                dino_index += 1
            else:
                dino_index = 0

            dino_surface, dino_rect = dino_animation()

        if event.type == SPAWNBOMB:
            bomb_list.append(create_bomb())

        #spawing dino
        if event.type == SPAWNFLYDINO:
            fly_dino_list.append(create_fly_dino())

    screen.blit(imag.background, (0,0))
    ground_x_pos -= 2
    #screen.blit(imag.ground, (ground_x_pos, 720))

    draw_ground()

    if ground_x_pos <= -679:
        ground_x_pos = -50
    screen.blit(dino_surface, dino_rect)
    bomb_list = bomb_movment(bomb_list)
    draw_bombs(bomb_list)

    fly_dino_list = move_fly_dino(fly_dino_list)
    draw_fly_dino(fly_dino_list)
    # screen.blit(imag.bomb, (400, 900))
    # screen.blit(imag.fly_dino1, (350, 450))
    # screen.blit(imag.dinoMain, (10, 800))

    pygame.display.update()
    clock.tick(120)
