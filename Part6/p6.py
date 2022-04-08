# Duran Ramlall
# Part 6 of NerdParadise PyGame: Getting Started walkthrough
# Friday April 8 2022
# TEJ4M1 P2 Gr 12

# Import Statements
import pygame 
import random

# Initialize
pygame.init()
screen = pygame.display.set_mode((400, 300))

# Misc
r = 90
g = 180
b = 25
color = (r,g,b)
points = [
    (90, 180),
    (180, 90),
    (60, 125)
]


# Declarations
clock = pygame.time.Clock()
done = False

while not done:
    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Reset to Black
            screen.fill((0,0,0))

            # Rand Color
            r = random.randrange(0,255)
            g = random.randrange(0,255)
            b = random.randrange(0,255)

            color = (r,g,b)

            # X1, Y1
            x1 = random.randrange(0,400)
            y1 = random.randrange(0, 300)
            points[0] = (x1,y1)
            
            # X2, Y2
            x2 = random.randrange(0,400)
            y2 = random.randrange(0,300)
            points[1] = (x2,y2)
            
            #X3, Y3
            x3 = random.randrange(0,400)
            y3 = random.randrange(0,300)
            points[2] = (x3,y3)

            pygame.draw.polygon(screen,color, points)
        if event.type == pygame.QUIT:
            done = True

    # Update Screen
    pygame.display.flip()
    clock.tick(60)
    
