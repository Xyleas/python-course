import pygame, sys

# Set up everything Pygame related
pygame.init()

clock = pygame.time.Clock()
#Testing clock.tick()

screen = pygame.display.set_mode()
pygame.display.set_caption("My Special Game")

# Background color
background_color = pygame.Color(255, 255, 255, 1)
    #Example red = pygame.Color(255, 0, 0 ,1)
    #Example purple - pygame.Color(128, 0, 128, 1)
    #Example rect = pygame.Rect(50,10,200,100)
    #Exmample triangle_coordinates = [(100, 50),(125,100),(75,100)]

apple = pygame.image.load("placeHolder.png")
apple_rect = apple.get_rect()
apple_rect.x = 50
apple_rect.y = 100

# Start our run loop
while True:
    # Listen for all events currently occuring
    for event in pygame.event.get():
        # Check if there is a quit event (triggerid by pressing the close button)
        if event.type == pygame.QUIT:
            # Shut down Pygame
            pygame.quit()
            # Exit the system
            sys.exit()
        
    # Set the screen color
    screen.fill(background_color)
        #Example pygame.draw.rect(screen, "red", rect, 5, 20)
        #Example pygame.draw.circle(screen, "blue", (100,100), 50)
        #Example pygame.draw.polygon(screen, "yellow", triangle_coordinates)
        #Example pygame.draw.rect(screen, "black", apple_rect, 1)
        #Example screen.blit(apple, apple_rect)
        #Example pygame.draw.line(screen, "red", (50,50), (200, 100), 5)
        #Example pygame.draw.line(screen, "blue", False, [(50,250), (50,50), (250, 250), (250,50)], 5)
        pygame.draw.ellipse(screen, "green", pygame.Rect(50, 50, 100, 200))

    # Redraw the entire display
    pygame.display.flip()
    #Example pygame.display.update()

    # Tick the clock according to the framerate (60)
    clock.tick(60)g print(fps)
    previous_time = clock.get_time()
    fps = clock.get_fps()
    #Testing print(previous_time)
    #Testing