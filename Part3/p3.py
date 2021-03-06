# Duran Ramlall
# Part 3 of NerdParadise PyGame: Getting Started walkthrough
# Wednesday April 6 2022
# TEJ4M1 P2 Gr 12

# Import Statements
import pygame 

# Initialize
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((400, 300))

# Set & Play Music
pygame.mixer.music.load('./Part3/assets/sound/Ambient_Wind_01.ogg')
pygame.mixer.music.play(-1)


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
    
