# Duran Ramlall
# Part 2 of NerdParadise PyGame: Getting Started walkthrough
# Friday April 1 2022
# TEJ4M1 P2 Gr 12

# Import Statements
import pygame

plrImage = pygame.image.load('./Part2/assets/ball.png')

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
    screen.fill((255, 255, 255))
    screen.blit(plrImage, (20, 20))

    # Update Screen
    pygame.display.flip()
    clock.tick(60)
    
