# Duran Ramlall
# Part 3 of NerdParadise PyGame: Getting Started walkthrough
# Friday April 1 2022
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
is_blue = True
x = 30
y = 30

while not done:
    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
        if event.type == pygame.QUIT:
            done = True

    # Pressed Events
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x+= 3

    screen.fill((0, 0, 0))
    # Color Switch
    if is_blue: color = (0, 128, 255)
    else: color = (255, 100, 0)

    # Draw
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60)) 

    # Update Screen
    pygame.display.flip()
    clock.tick(60)
    
