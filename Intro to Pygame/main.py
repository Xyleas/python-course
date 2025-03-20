import pygame, sys, math

pygame.init()

clock = pygame.time.Clock()

# Note we're using custom values here for width and height
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("My Special Game")

background_color = "white"

circle_x = 50
circle_y = 50

# Game loop  
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Detect when any key was pressed down
        # if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_LEFT:
                # print("Left keydown")
        # Detect when any key was released
        # if event.type == pygame.KEYUP:
            # print("Keyup")
            
            
    # Get list of keys currently being pressed
    keys = pygame.key.get_pressed()
    
    # Each case returns true if that key is currently being pressed
    if keys[pygame.K_LEFT]:
        circle_x -= 1
    if keys[pygame.K_RIGHT]:
        circle_x += 1
    if keys[pygame.K_UP]:
        circle_y -= 1
    if keys[pygame.K_DOWN]:
        circle_y += 1


    # Set the screen color
    screen.fill(background_color)
    
    pygame.draw.circle(screen, "purple", (circle_x, circle_y), 25)
    
    # Redraw the entire display
    pygame.display.flip()
    
    clock.tick(60)
    

