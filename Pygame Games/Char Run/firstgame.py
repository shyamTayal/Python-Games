import pygame
pygame.init()

screen_dim = (852,480)
win = pygame.display.set_mode(screen_dim)

pygame.display.set_caption('First Game')

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
stand = pygame.image.load('standing.png')

x = 50
y = screen_dim[1] - 100
vel = 5
isJump = False
jumpHeight = 10
left = False
right = False
walkCount = 0

def redrawGameWindow() :
        global walkCount
        win.blit(bg, (0, 0))

        if walkCount + 1 >= 27 :
            walkCount = 0

        if left :
            win.blit(walkLeft[walkCount//3], (x, y))
            walkCount += 1
        elif right :
            win.blit(walkRight[walkCount//3], (x, y))
            walkCount += 1
        else :
            win.blit(stand, (x, y))
            walkCount = 0

        pygame.display.update()


# main loop
run = True
while run :
    pygame.time.delay(30)

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT :
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x-=vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < screen_dim[0] - 40 - vel:
        x+=vel
        right = True
        left = False
    else :
        right = False
        left = False
        walkCount = 0

    if not (isJump) :
        if keys[pygame.K_SPACE] :
            isJump = True
    else :
        if jumpHeight >= -10 :
            left = False
            right = False
            # walkCount = 0
            neg = 1
            if jumpHeight < 0 :
                neg = -1
            y -= (jumpHeight**2) * 0.5 * neg
            jumpHeight -= 1
        else :
            isJump = False
            jumpHeight = 10

    redrawGameWindow()

pygame.quit()
