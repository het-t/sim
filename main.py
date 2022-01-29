
import pygame
import math

pygame.init()

screenWidth = 1200
screenHeight = 600
screen = pygame.display.set_mode([screenWidth, screenHeight])

#fixing fps
clock = pygame.time.Clock()
fps = 60

Bx = 600
By = 30
vel = 0
acc = 0.1
move_up = False
move_down = True


def ball():
    global Bx
    global By
   
    
    ball_color = (255, 255, 255)
    pygame.draw.circle(screen, ball_color, [Bx, By], 30, 0)  # Raduis = 30
    

def base():
    base_color = (255, 255, 255)
    pygame.draw.rect(screen, base_color, pygame.Rect(0, 580, 1200, 20))  # base is 20 unit about bottom

def motion():
    global vel
    global By
    global move_down
    global move_up

    d = By - 30
    if d < 0.005:
        d = 1
    if move_up:
        vel = -math.sqrt(2*acc*d)
    if move_down:
        vel = math.sqrt(2*acc*d)
    if By < 30 :
        move_up = False
        move_down = True
    if By > 560 :
        move_up = True
        move_down = False
    By += vel
    print(d)
    print(By) 
    # d = By - 28  #distance from starting position of ball
    # if d < 1:
    #    d = 2
    # if move_up:
    #     vel= -math.sqrt(2*acc*d)      #velocity of ball
    # if move_down:
    #     vel= math.sqrt(2*acc*d)
    # By += vel
    # if By > 550:
    #      move_up = True
    #      move_down = False
    # print(d)
    # print(By)

        
    
    

runLoop = True
while runLoop:
    screen.fill((100, 0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            runLoop = False
            pygame.quit()
    
    base()
    ball()
    motion()
    

    clock.tick(fps)
    pygame.display.flip() 