import pygame

# Pet class
class Pet:

    def __init__(self, x, y, health, max_health, happiness, max_happiness):
        self.x = x
        self.y = y
        # Health = radius
        self.health = health
        self.max_health = max_health
        # Happiness = green color saturation
        self.happiness = happiness
        self.max_happiness = max_happiness
        self.colour = pygame.Color(0, happiness, 0)

    # Returns the x and y positions (center of circle) as a 2D vector
    def get_pos(self):
        return pygame.Vector2(self.x, self.y)
  
    # Returns a rectangle surrounding the circle where the x and y positions are center-radius and the width and height are radius*2
    def get_rect(self):
        return pygame.Rect(self.x - self.health, self.y - self.health, self.health * 2, self.health * 2)
        
    # Increases/decreases x and/or y
    def move(self, x_amount, y_amount):
        self.x += x_amount
        self.y += y_amount
    
    # Updates health and happiness by consuming item
    def consume_item(self, item):
        self.update_health(item.health)
        self.update_happiness(item.happiness)
    
    # Updates health
    def update_health(self, d_h):
        self.health += d_h
        if self.health > self.max_health:
            self.health = self.max_health
        elif self.health < 0:
            self.health = 0

    # Updates happiness
    def update_happiness(self, d_h):
        self.happiness += d_h
        if self.happiness > self.max_happiness:
            self.happiness = self.max_happiness
        elif self.happiness < 0:
             self.happiness = 0
        self.colour = pygame.Color(0, self.happiness, 0)
    
    # Checks end game conditions
    def check_if_dead(self):
        return self.health <= 0 or self.happiness <= 0
    
    
class Item:

    def __init__(self, x, y, health, happiness, image_name):
        # Setting up basic fields
        self.x = x
        self.y = y
        self.health = health
        self.happiness = happiness
        
        # Loads and stores image based on its filepath
        self.image = pygame.image.load(image_name)
        # Shifts the image rect so that the x and y are at the center of the image (rather than top left)
        rect = self.image.get_rect()
        self.image_rect = pygame.Rect(x - rect.width / 2, y - rect.height / 2, rect.width, rect.height)
        
  
class Game:
  
    def __init__(self):
        # Setting up a few display variables
        self.width = 500
        self.height = 500
        self.background_colour = "white"
        self.buttons_bar_height = 100
        self.buttons_bar_colour = "orange"
        
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pygame Pet")
        
        self.clock_tick = 60
        self.clock = pygame.time.Clock()
      
        # Item variables
        self.image_names = ["apple.png", "icecream.png", "toy.png"]
        self.item_mode_index = 0
        self.item = None
        
        # Button variables
        self.apple_button = Item(self.width / 4, self.buttons_bar_height / 2, 0, 0, self.image_names[0])
        self.ice_cream_button = Item(self.width / 2, self.buttons_bar_height / 2, 0, 0, self.image_names[1])
        self.toy_button = Item(self.width * (3 / 4), self.buttons_bar_height / 2, 0, 0, self.image_names[2])
        
        # Pet variables
        self.pet = Pet(self.width / 2, self.height / 2, 50, 100, 180, 255)
        self.speed = 2
        self.d_x = 0
        self.d_y = 0
        self.decay_rate = -1
        self.current_tick = 0
        self.size_update_rate = self.clock_tick / 3
        self.colour_update_rate = self.clock_tick / 10
    
    
    # Selects an item from the buttons bar or places an item for the pet
    def handle_mouse_click(self):
        pos = pygame.mouse.get_pos()
        # Sets index based on item clicked
        if self.apple_button.image_rect.collidepoint(pos):
            self.item_mode_index = 0
        elif self.ice_cream_button.image_rect.collidepoint(pos):
            self.item_mode_index = 1
        elif self.toy_button.image_rect.collidepoint(pos):
            self.item_mode_index = 2
        # Does nothing if user clicks button bar outside of item buttons
        elif pos[1] < self.buttons_bar_height:
            return
        # Creates an item at the mouse position
        else:
            self.create_item(pos)
      
    
    # Spawns an item at the given position
    def create_item(self, pos):
        # Gets current image name
        image_name = self.image_names[self.item_mode_index]
        # Creates an item at the position
        if self.item_mode_index == 0:
            self.item = Item(pos[0], pos[1], 20, 0, image_name)
        elif self.item_mode_index == 1:
            self.item = Item(pos[0], pos[1], -10, 60, image_name)
        elif self.item_mode_index == 2:
            self.item = Item(pos[0], pos[1], 0, 40, image_name)
        self.set_speed()

    
    # Sets the speed and direction of the pet's movement
    def set_speed(self):
        # Gets differences in x and y positions of pet and item
        d_x = abs(self.pet.x - self.item.x)
        d_y = abs(self.pet.y - self.item.y)
        
        # Checks whether x difference is greater than y difference
        if d_x >= d_y:
            self.d_x = self.speed
            # Slows down the y movement
            self.d_y = self.speed * (d_y / d_x)
        else:
            # Slows down the x movement instead
            self.d_x = self.speed * (d_x / d_y)
            self.d_y = self.speed
            
        # Sets x speed to negative if item is further left than pet
        if self.pet.x > self.item.x:
            self.d_x = -self.d_x
        # Sets y speed to negative if item is further up than pet
        if self.pet.y > self.item.y:
            self.d_y = -self.d_y
    
    
    # Checks for collisions between pet and item
    def handle_item_collision(self):
        # If item exists and item.rect and pet.rect overlap, collision occurred
        if self.item != None and self.item.image_rect.colliderect(self.pet.get_rect()):
            # Consumes then deletes item
            self.pet.consume_item(self.item)
            self.item = None
            
            # Stops pet movement by setting its speed to 0
            self.d_x = 0
            self.d_y = 0
    
    
    # Updates pet position
    def update_pet(self):
        self.pet.move(self.d_x, self.d_y)
        
        # Updates health and happiness
        self.current_tick += 1
        # Decays health 3x per second
        if self.current_tick % self.size_update_rate == 0:
            self.pet.update_health(self.decay_rate)
    
        # Decays happiness 10x per second
        if self.current_tick % self.colour_update_rate == 0:
            self.pet.update_happiness(self.decay_rate)
            
        # Resets current tick to prevent it from becoming too large
        if self.current_tick == 60:
            self.current_tick = 0
    
    
    def draw_everything(self):
        # Screen
        self.screen.fill(self.background_colour)
      
        # Item
        if self.item != None:
            self.screen.blit(self.item.image, self.item.image_rect)
      
        # Pet
        pygame.draw.circle(self.screen, self.pet.colour, self.pet.get_pos(), self.pet.health)
        
        # Buttons bar
        pygame.draw.rect(self.screen, self.buttons_bar_colour, pygame.Rect(0, 0, self.width, self.buttons_bar_height))
    
        # Buttons
        self.screen.blit(self.apple_button.image, self.apple_button.image_rect)
        self.screen.blit(self.ice_cream_button.image, self.ice_cream_button.image_rect)
        self.screen.blit(self.toy_button.image, self.toy_button.image_rect)
    
        # Update
        pygame.display.update()
      
      
    # Runs the game loop
    def run(self):
        while True:
            # Handles incoming events
            for event in pygame.event.get():
                # Quit event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    # Breaks out of the loop
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_click()

            # Detects pet-item collision
            self.handle_item_collision()
            
            # Checks if pet is dead
            if self.pet.check_if_dead():
                pygame.quit()
                return
      
            # Updates pet
            self.update_pet()
                  
            # Draws to the game screen
            self.draw_everything()
      
            # Ticks clock
            self.clock.tick(self.clock_tick)


# Initializes Pygame so that we have access to the display, events, etc
pygame.init()

# Creates an instance of our Game class      
game= Game()
game.run()