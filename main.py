import pygame
import sys
import math
import random

pygame.init
pygame.display.set_caption("The adventures of Tom Greenyberry")
clock = pygame.time.Clock()

WIDTH = 1200
HEIGHT = 800
GRAVITY = 1

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the screen
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Create classes
class Sprite():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.width = width
        self.height = height
        self.color = WHITE
        self.friction = 0.8
        self.rect = pygame.Rect(int(self.x - self.width / 2.0), int(self.y - self.height / 2.0), self.width, self.height)

    def goto(self, x, y):
        self.x = x
        self.y = y

    def render(self):
        # create a rectangle object
        self.rect = pygame.Rect(int(self.x - self.width / 2.0), int(self.y - self.height / 2.0), self.width, self.height)
        pygame.draw.rect(SCREEN, self.color, self.rect)

    def is_aabb_collision(self, other):
        #  do I collide with other?
        #return self.rect.colliderect(other)

        # Axis Aligned Bounding Box
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collision and y_collision)

class Player(Sprite):
    def __init__(self, x, y, width, height):
        Sprite.__init__(self, x, y, width, height)
        self.color = GREEN
    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.dy += GRAVITY
        
    def jump(self):
        self.dy -= 24   
        
    def left(self):
        self.dx -= 6
        
    def right(self):
        self.dx += 6
        
# Create font

# Create Sounds

# Create game objects
player = Player(600, 0, 20, 40)
blocks = []
blocks.append(Sprite(600, 200, 400, 20)) 

# Main game loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        # Keyboard Events
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_UP or event.type == pygame.K_SPACE:
                player.jump()
            elif event.type == pygame.K_LEFT:
                player.left()
            elif event.type == pygame.K_RIGHT:
                player.right()
        
    # Move/Update objects
    player.move()
    # Check for collisions
    for block in blocks:
         if player.is_aabb_collision(block):
              player.dy = 0
    # Border check the player
    if player.y > 600:
      player.goto(600, 0)
      player.dy = 0
    # Render (draw)
    # Fill the background
    SCREEN.fill(BLACK)
    
    # render objects
    player.render()
    for block in blocks:
        block.render()
    # flip the display
    pygame.display.flip()
    
    # Set the FPS
    clock.tick(30)
    
    
    