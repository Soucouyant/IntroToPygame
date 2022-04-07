# Duran Ramlall
# Part 4 of NerdParadise PyGame: Getting Started walkthrough
# Thursday April 7 2022
# TEJ4M1 P2 Gr 12

# Import Statements
import pygame 
import random

# Initialize
pygame.init()
screen = pygame.display.set_mode((400, 300))

# Declarations
clock = pygame.time.Clock()
done = False

# Shape Function
color = (34, 199, 171)

    # Random Points
x1 = random.randrange(0,400)
x2 = random.randrange(0,400) 
y1 = random.randrange(0,300)
y2 = random.randrange(0,300)
x3 = random.randrange(0,400)
y3 = random.randrange(0,400)

point_list = [
    (x1, y1),
    (x2, y2),
    (x3, y3)
]

while not done:
    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pygame.draw.polygon(screen,color, point_list)
    # Update Screen
    pygame.display.flip()
    clock.tick(60)
    