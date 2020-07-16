import random

import images as imag

# fly_dino_list = []
# SPAWNFLYDINO = pygame.USEREVENT
# pygame.time.set_timer(SPAWNFLYDINO, 10000)
fly_dino_height = [200, 700, 800]

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
        imag.screen.blit(imag.fly_dino1, fdino)


# bomb_list = []
# SPAWNBOMB = pygame.USEREVENT
# pygame.time.set_timer(SPAWNBOMB, 300)

def create_bomb():
    new_bomb = imag.bomb_img.get_rect(midbottom = (585, 500))
    return new_bomb

def bomb_movment(bombs):
    for bomb in bombs:
        bomb.centerx -= 5
    return bombs

def draw_bombs(bombs):
    for bomb in bombs:
        imag.screen.blit(imag.bomb_img, bomb)


#ground
ground_x_pos = -50

def draw_ground():
    #-50,720
    imag.screen.blit(imag.ground, (ground_x_pos, 720))
    imag.screen.blit(imag.ground, (ground_x_pos + 679, 720))

dino_frames = [imag.dino1,imag.dino2,imag.dino3,imag.dino4]
dino_index = 2
dino_surface = dino_frames[dino_index]
dino_rect = dino_surface.get_rect(center = (125,900))

def dino_animation():
    new_dino = dino_frames[dino_index]
    new_dino_rect = new_dino.get_rect(center= (125, dino_rect.centery))
    return new_dino,new_dino_rect