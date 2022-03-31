#Single Line Comments are so lame
#Just have multi line
#lame language
#Required Comments ^

import pygame 

# Initialize
pygame.init()
screen = pygame.display.set_mode((400, 300))

#Do things

isBlue = True
color = (0, 0, 0)

if isBlue == True: 
    color = (0, 128, 255)
elif isBlue == False: 
    color = (255, 100, 0)

# draw
pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))

# Event Handler
done = False

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            print(color)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print(color)
        if event.type == pygame.QUIT:
            done = True
    
    # Update Screen
    pygame.display.flip()
    
    
