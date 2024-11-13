import pygame

class Agent:
   
    def __init__(self, x, y, speed, environment):
        self.x = x
        self.y = y
        self.speed = speed
        self.environment = environment
   
    def move(self, dx, dy):
        #Move the agent in the specified direction.
        if dx != 0 or dy != 0: #only increment speed if there is a movement 
            self.speed +=1 # increment speed by a amount
        # Get the keys pressed
        keys = pygame.key.get_pressed()  
       
        if keys[pygame.K_LEFT]:
            dx = -1
        elif keys[pygame.K_RIGHT]:
            dx = 1
        if keys[pygame.K_UP]:
            dy = -1
        elif keys[pygame.K_DOWN]:
             dy = 1
        
      # Calculate new position based on direction and new speed
        new_x = self.x + dx * self.speed
        new_y = self.y + dy * self.speed
# Make sure the agent stays within the environment boundaries
        self.x = max(0, min(new_x, self.environment.width - 20))
        self.y = max(0, min(new_y, self.environment.height - 20))
    def get_position(self):
        return int(self.x), int(self.y)