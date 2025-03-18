''' Game components:
1) Game window
2) Game loop
3) Event loop
'''

import pygame

pygame.init() # initializes all the pygame sub-modules

screen = pygame.display.set_mode((800, 480)) # creating a game windiw
# set_mode() takes a tuple as an argument

running = True

while running: # game loop
    for event in pygame.event.get(): #event loop
        if event.type == pygame.QUIT:
            running = False
    # or -> pygame.quit()

