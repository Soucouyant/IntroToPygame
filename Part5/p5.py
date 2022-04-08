# Duran Ramlall
# Part 5 of NerdParadise PyGame: Getting Started walkthrough
# Thursday April 7th
# TEJ4M1 P2 Gr 12

# Import Statements
import pygame 

# Initialize
pygame.init()
screen = pygame.display.set_mode((400, 300))

# Font 
font = pygame.font.Font('./Part5/assets/fonts/NEONLEDLight.otf', 30)
text = font.render("Hello, World", True, (66, 182, 245))

# Declarations
clock = pygame.time.Clock()
done = False

while not done:
    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    # Create
    screen.blit(text, (200 - text.get_width() // 2, 150 - text.get_height() // 2 ))

    # Update Screen
    pygame.display.flip()
    clock.tick(60)
    
