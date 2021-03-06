import pygame
# -- Global Constants
# -- Start
# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

# -- Initialise pygame and clock
pygame.init()

# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("Pong")
# -- Variables
done = False
x_val = 150
y_val = 200
x_direction = 1
y_direction = 1
x_padd = 0
y_padd = 20
ball_width = 20
score = 0

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

### -- Game Loop
while not done:
    # -- User inputs here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # - EndIf
        
    ## - the up or down key has been pressed
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP] and not y_padd <= 0:
        y_padd = y_padd - 5
    if keys[pygame.K_DOWN] and not y_padd >= 420:
        y_padd = y_padd + 5
            
    # -- Game logic goes after this comment
    if x_val <= 15 and y_val >= y_padd and y_val <= y_padd + 60:
        x_direction = x_direction * -1
        x_val = x_val + x_direction
    
    if x_val < 0:
        x_val = 300
        y_val = 220
        score = score - 1
        x_direction = x_direction * -1
        x_val = x_val + x_direction
    else:
        x_val = x_val + x_direction

    if x_val > 660:
        x_val = 300
        y_val = 220
        score = score + 1
        x_direction = x_direction * -1
        x_val = x_val + x_direction
    else:
        x_val = x_val + x_direction

    if y_val == 460 or y_val == 0:
        y_direction = y_direction * -1
        y_val = y_val + y_direction
    else:
        y_val = y_val + y_direction

    # Screen background is BLACK
    screen.fill(BLACK)
    # -- Draw here
    pygame.draw.rect(screen,BLUE,(x_val,y_val,ball_width,ball_width))
    pygame.draw.rect(screen,WHITE,(x_padd,y_padd,15,60))
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    clock.tick(240)

### -- End of game loop
pygame.quit()
