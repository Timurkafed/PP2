import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
screen.fill((255,255,255))

object1 = pygame.Rect((20, 50), (50, 100))
object2 = pygame.Rect((10, 10), (100, 100))

draw = pygame.draw.rect

draw(screen, (255, 0, 0), object1)
draw(screen, (0,0,255), object2, 3)

pygame.display.flip()

print(object1.colliderect(object2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False            
pygame.quit()
        