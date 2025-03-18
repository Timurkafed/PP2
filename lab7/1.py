import pygame
from datetime import datetime

pygame.init()

WIDTH, HEIGHT = 1920//1.5, 1080//1.5

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True

min_img = pygame.image.load("sources/min_hand.png")
rot_min = pygame.transform.rotate(min_img, -45)

sec_img = pygame.image.load("sources/sec_hand.png")
rot_sec = pygame.transform.rotate(sec_img, 60)

clock_img = pygame.image.load("sources/clock.png")

while running:
    screen.fill((255,255,255))
    
    now = datetime.now()
    minutes = now.minute
    seconds = now.second
    
    screen.blit(clock_img, ((WIDTH//2)-(clock_img.get_size()[0]//2), (HEIGHT//2)-(clock_img.get_size()[1]//2)))
    
    rotated_min = pygame.transform.rotate(rot_min, -minutes*6)
    rotated_sec = pygame.transform.rotate(rot_sec, -seconds*6)
    screen.blit(rotated_min, ((WIDTH//2)-(rotated_min.get_size()[0]//2), (HEIGHT//2)-(rotated_min.get_size()[1]//2)))
    screen.blit(rotated_sec, ((WIDTH//2)-(rotated_sec.get_size()[0]//2), (HEIGHT//2)-(rotated_sec.get_size()[1]//2)))

    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(2)
    
pygame.quit()