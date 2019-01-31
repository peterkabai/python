import sys, pygame, time
pygame.init()

# set sizes
size = width, height = 500,700 
paddle_h, paddle_w = 10, 100
ball_diam = 20

# create window, set the title and the app icon
screen = pygame.display.set_mode(size)
icon = pygame.image.load("resources/ball.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("pyPong")

# create various positions
ball_pos = [20,20]
player_x = width/2-paddle_w/2
ai_x = width/2-paddle_w/2

# game settings
player_speed = 4
ball_speed_x = 4
ball_speed_y = 4
ai_speed = 4
ai_diff = 50

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
            if player_x > 0:
                player_x-=player_speed
        if key_pressed[pygame.K_RIGHT]:
            if player_x+paddle_w < width:
                player_x+=player_speed
        
        # quits the game
        if key_pressed[pygame.K_ESCAPE]:
            loop = False
        
        clock.tick(60)
    
    # moves the ai
    if ball_pos[1]+ball_diam/2 < height/100*ai_diff:
        if ai_x > 0 and ball_pos[0]+ball_diam/2 < ai_x+paddle_w/2:
            ai_x -= ai_speed
        if ai_x+paddle_w < width and ball_pos[0]+ball_diam/2 > ai_x+paddle_w/2:
            ai_x += ai_speed
            
    # move the ball
    if ball_pos[0]+ball_diam >= width or ball_pos[0] <= 0:
        ball_speed_x = (-ball_speed_x)
    if ball_pos[1]+ball_diam >= height or ball_pos[1] <= 0:
        ball_speed_y = (-ball_speed_y)
    ball_pos[0]+=ball_speed_x
    ball_pos[1]+=ball_speed_y
    
    # paint the background image, ball and paddles
    screen.blit(background, (0,0))
    screen.blit(paddle, (ai_x,0))
    screen.blit(paddle, (player_x,height-paddle_h))
    screen.blit(ball, ball_pos)
    
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
