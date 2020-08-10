import random

import images as imag

# fly_dino_list = []
# SPAWNFLYDINO = pygame.USEREVENT
# pygame.time.set_timer(SPAWNFLYDINO, 10000)
fly_dino_height = [700, 800]
fly_dino_x_list = [400, 600, 700, 752]
fly_dino_frames = [imag.fly_dino1,imag.fly_dino2,imag.fly_dino3,imag.fly_dino4]
fly_dino_index = 0
fly_dino_surface = fly_dino_frames[fly_dino_index]
flyx = 500

def create_fly_dino():
    fly_dino_random = random.choice(fly_dino_x_list)
    # new_fly_dino = fly_dino_animation().get_rect(midtop = (700, 700))
    return fly_dino_random

def draw_flydino():
    # random_fly_dion_pos = random.choice(fly_dino_height)
    # for fdino in fdinos:
        # imag.screen.blit(imag.fly_dino1, fdino)
        # imag.screen.blit(fly_dino_surface, (400, 600))
    imag.screen.blit(fly_dino_animation(), (flyx, 750))
    imag.screen.blit(fly_dino_animation(), (flyx+900, 750))
    # imag.screen.blit(fly_dino_animation(), (flyx + create_fly_dino(), 200))

def fly_dino_animation():
    fly_new_dino = fly_dino_frames[dino_index]
    # fly_new_dino_rect = fly_new_dino.get_rect(center= (400, fly_dino_rect.centery))
    return fly_new_dino

def create_bomb():
    new_bomb = imag.bomb_img.get_rect(midbottom = (585, 1030))
    return new_bomb

def bomb_movment(bombs):
    for bomb in bombs:
        bomb.centerx -= 10
    return bombs

def draw_bombs(bombs):
    for bomb in bombs:
        imag.screen.blit(imag.bomb_img, bomb)

def check_collision(bombs):
    for bomb in bombs:
        if dino_rect.colliderect(bomb):
            print("Collided")
            #return False
        else:
            print("Not Collided")

    return True

#ground
ground_x_pos = 0

def draw_ground():
    #-50,720
    imag.screen.blit(imag.ground, (ground_x_pos, 760))
    imag.screen.blit(imag.ground, (ground_x_pos + 615, 760))

dino_frames = [imag.dino1,imag.dino2,imag.dino3,imag.dino4]
dino_index = 0
dino_surface = dino_frames[dino_index]
dino_rect = dino_surface.get_rect(center = (95,900))

#pygame.Rect(width,height,x,y) (30:30) video flappy

def dino_animation():
    new_dino = dino_frames[dino_index]
    new_dino_rect = new_dino.get_rect(center= (10, dino_rect.centery))
    return new_dino,new_dino_rect
