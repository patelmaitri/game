def draw_ground():

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
