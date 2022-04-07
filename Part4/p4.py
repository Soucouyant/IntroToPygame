# Duran Ramlall
# Part x of NerdParadise PyGame: Getting Started walkthrough
# Thursday April 7 2022
# TEJ4M1 P2 Gr 12

# Import Statements
import pygame 

# Initialize
pygame.init()
screen = pygame.display.set_mode((400, 300))

# Declarations
clock = pygame.time.Clock()
done = False

while not done:
    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Update Screen
    pygame.display.flip()
    clock.tick(60)
    
