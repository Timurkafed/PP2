import pygame

pygame.init()
'''
class Ball():
    def __init__(self, x, y, radius, color, move_step):
        self.x = x
        self.y = y
'''

WIDTH, HEIGHT = 1920//1.5, 1080//1.5

RED = (255,0, 122)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

x, y = WIDTH//2, HEIGHT//2
status1 = "STOP"
status2 = "STOP"

running = True

while running:
    
    screen.fill((255,255,255))
    ball = pygame.draw.circle(screen, RED, (x,y), 25)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                status1 = "RIGHT"
            elif event.key == pygame.K_LEFT:
                status1 = "LEFT"
            elif event.key == pygame.K_DOWN:
                status2 = "DOWN"
            elif event.key == pygame.K_UP:
                status2 = "UP"
        elif event.type == pygame.KEYUP :            
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                status2 = "STOP"
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                status1 = "STOP"
    if status1 == "RIGHT" and x+25 <= WIDTH:
        x += 20
    elif status1 == "LEFT" and x-25 >= 0:
        x -= 20
    if status2 == "DOWN" and y+25 <= HEIGHT:
        y += 20
    elif status2 == "UP" and y-25 >= 0:
        y -= 20
            
    pygame.display.flip()
    clock.tick(60)
        
pygame.quit()