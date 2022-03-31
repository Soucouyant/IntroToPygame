#Single Line Comments are so lame
#Just have multi line
#lame language
#Required Comments ^

# what?
import pygame 

# Initialize
pygame.init()
screen = pygame.display.set_mode((400, 300))

#Do things

isBlue = True

if isBlue: color = (0, 128, 255)
else: color = (255, 100, 0)

# draw
pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))

# Event Handler
done = False

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            isBlue = not isBlue
        if event.type == pygame.QUIT:
            done = True
    
    # Update Screen
    pygame.display.flip()
    
    
