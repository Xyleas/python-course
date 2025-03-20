from gameObject import GameObject

class Player(GameObject):

    def __init__(self, x, y, width, height, image_path, speed):
        super().__init__(x, y, width, height, image_path)
        
        self.speed = speed
        
    # Moving the player character on the screen
    def move(self, direction, max_height):
        # Checking both the boundaries and the direction of the player to prevent it from leaving the screen
        if (self.y >= max_height - self.height and direction > 0) or (self.y <= 0 and direction < 0):
            return
          
        self.y += (direction * self.speed)