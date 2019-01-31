import sys, pygame, time
pygame.init()

# set sizes
size = width, height = 500,700 
paddleH, paddleW = 10, 100

# create window, set the title and the app icon
screen = pygame.display.set_mode(size)
icon = pygame.image.load("resources/ball.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("pyPong")

# create various arrays for positions and colors
ballPos = [20,20]
white = [255,255,255]
red = [255,0,0]
playerX = width/2-paddleW/2
computerX = width/2-paddleW/2

clock = pygame.time.Clock()
pygame.key.set_repeat(1, 5)

# set images
background = pygame.image.load("resources/background.png")
ball = pygame.image.load("resources/ball.png")
paddle = pygame.image.load("resources/paddle.png")

loop = True
while loop:
    for event in pygame.event.get():
        
        # quit event to break the loop
        if event.type == pygame.QUIT:
            loop = False
            
        # gets an array of keys that are pressed
        key_pressed = pygame.key.get_pressed()
        
        # moves the paddle
        if key_pressed[pygame.K_LEFT]:
            playerX-=4
        if key_pressed[pygame.K_RIGHT]:
            playerX+=4
        
        # quits the game
        if key_pressed[pygame.K_ESCAPE]:
            loop = False
        
        clock.tick(60)
    
    # paint the background image, ball and paddles
    screen.blit(background, (0,0))
    screen.blit(ball, ballPos)
    screen.blit(paddle, (computerX,0))
    screen.blit(paddle, (playerX,height-paddleH))
    
    # refresh the screen
    pygame.display.flip()

pygame.quit()

# other stuff that may be useful later

# set the window position
# import os
# os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)

# paint the screen white
# screen.fill(white)

# hide the window frame
# screen = pygame.display.set_mode(size, pygame.NOFRAME)

# draw a circle
# pygame.draw.circle(screen,color,position,diameter,border)
