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

pygame.init()

screen = pygame.display.set_mode((576, 1024), pygame.RESIZABLE)
clock = pygame.time.Clock()

#Game variables
dinoMovement = 0
gravity = 0.75
score = 0
highScore = 0
ground_x_pos =-50 

#Flying Dino
fly_dino_list = []
SPAWNFLYDINO = pygame.USEREVENT
pygame.time.set_timer(SPAWNFLYDINO, 2000)
fly_dino_height = [200, 700, 800]

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
        #spawing dino
        if event.type == SPAWNFLYDINO:
            fly_dino_list.append(create_fly_dino())
    
    #background
    screen.blit(imag.background, (0,0))
    
    #flying dino 
    fly_dino_list = move_fly_dino(fly_dino_list)
    draw_fly_dino(fly_dino_list)
   
    #ground
    ground_x_pos -= 2
    screen.blit(imag.ground, (ground_x_pos, 500))

    pygame.display.update()
    clock.tick(120)
