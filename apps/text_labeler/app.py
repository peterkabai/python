import pygame.locals
pygame.init()

# Create window, set the title and the app icon
screen = pygame.display.set_mode((500, 500))
icon = pygame.image.load("resources/icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Text Labeler")

# This is needed for the refresh rate
clock = pygame.time.Clock()

loop = True
while loop:
    for event in pygame.event.get():
        
        # Quit event to break the loop
        if event.type == pygame.QUIT:
            loop = False
            
        # Gets an array of keys that are pressed
        key_pressed = pygame.key.get_pressed()
        
        # Quits if esc is pressed
        if key_pressed[pygame.K_ESCAPE]:
            loop = False
        
        # Delay for screen refresh
        clock.tick(60)
    
    # Refresh the screen
    pygame.display.flip()

# Quit when the loop stops
pygame.quit()
