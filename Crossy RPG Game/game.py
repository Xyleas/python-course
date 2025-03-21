import pygame
from gameObject import GameObject
from player import Player
from enemy import Enemy

class Game:
  
    def __init__(self):
        self.width = 600
        self.height = 600
        self.white_colour = (255, 255, 255)
        
        self.game_window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        
        # Loading the game assets
        # NOTE: We're using different values and image paths here specifically for the Trinket application
        self.background = GameObject(0, 0, self.width, self.height, 'background.png')
        self.treasure = GameObject(280, 35, 40, 40, 'treasure.png')

        # Adding levels to the game
        self.level = 1.0
        self.reset_map()
        
        
    def reset_map(self):
      # NOTE: We're using different values and image paths here specifically for the Trinket application
        self.player = Player(280, 530, 40, 40, 'player.png', 3)
        
        # Increases the speed of enemies as the level goes up
        speed = 1 + (self.level * 0.5)
        
        # Increases the number of enemies as the game level goes up
        if self.level >= 4.0:
            self.enemies = [
                Enemy(0, 450, 40, 40, 'enemy.png', speed),
                Enemy(250, 300, 40, 40, 'enemy.png', speed),
                Enemy(0, 150, 40, 40, 'enemy.png', speed),
            ]
        elif self.level >= 2.0:
            self.enemies = [
                Enemy(0, 450, 40, 40, 'enemy.png', speed),
                Enemy(250, 300, 40, 40, 'enemy.png', speed),
            ]
        else:
            self.enemies = [
                Enemy(0, 450, 40, 40, 'enemy.png', speed),
            ]
        
        
    def draw_objects(self):
        self.game_window.fill(self.white_colour)
        
        # Blitting assets to the screen
        self.game_window.blit(self.background.image, (self.background.x, self.background.y))
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))
        
        for enemy in self.enemies:
            self.game_window.blit(enemy.image, (enemy.x, enemy.y))
        
        pygame.display.update()
        
        
    def move_objects(self, player_direction):
        self.player.move(player_direction, self.height)
        for enemy in self.enemies:
            enemy.move(self.width)
            
    
    def check_if_collided(self):
        # Checks for collisions between the player and the enemies
        for enemy in self.enemies:
            if self.detect_collision(self.player, enemy):
                self.level = 1.0
                return True
        # Checks for collisions between the player and the treasure
        if self.detect_collision(self.player, self.treasure):
            self.level += 0.5
            return True
        return False
            
            
    # Collision detection    
    def detect_collision(self, object_1, object_2):
        if object_1.y > (object_2.y + object_2.height):
            return False
        elif (object_1.y + object_1.height) < object_2.y:
            return False
        if object_1.x > (object_2.x + object_2.width):
            return False
        elif (object_1.x + object_1.width) < object_2.x:
            return False
        return True    
        
        
    def run_game_loop(self):
        player_direction = 0
      
        while True:
            # Handle events
            events = pygame.event.get()
            for event in events:
                # If there's a QUIT event, we break the loop and exit the method
                if event.type == pygame.QUIT:
                    return
                  
                # Listening for when a key is pressed down on the keyboard
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player_direction = -1
                    elif event.key == pygame.K_DOWN:
                        player_direction = 1
                        
                # Stopping the player when arrow keys are released
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_direction = 0
                  
            # Execute logic
            self.move_objects(player_direction)
            
            # Update display
            self.draw_objects()
            
            if self.check_if_collided():
                # Increases difficulty or resets game
                self.reset_map()
            
            # NOTE: We've altered this value so that the codes run more smoothly
            self.clock.tick(120)
            