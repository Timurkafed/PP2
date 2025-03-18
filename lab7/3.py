import pygame

pygame.init()
'''
class Ball():
    def __init__(self, x, y, radius, color, move_step):
        self.x = x
        self.y = y
'''

WIDTH, HEIGHT = 1920//1.5, 1080//1.5

RED = (122,0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

x, y = WIDTH//2, HEIGHT//2
statusR = "STOP"
statusL = "STOP"
statusU = "STOP"
statusD = "STOP"

running = True

while running:
    
    screen.fill((255,255,255))
    ball = pygame.draw.circle(screen, RED, (x,y), 25)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                statusR = "RIGHT"
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                statusL = "LEFT"
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                statusD = "DOWN"
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                statusU = "UP"
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.KEYUP :            
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                statusU = "STOP"
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                statusD = "STOP"
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                statusR = "STOP"
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                statusL = "STOP" 
    if statusR == "RIGHT" and x+25 <= WIDTH:
        x += 10
    if statusL == "LEFT" and x-25 >= 0:
        x -= 10
    if statusD == "DOWN" and y+25 <= HEIGHT:
        y += 10
    if statusU == "UP" and y-25 >= 0:
        y -= 10
            
    pygame.display.flip()
    clock.tick(60)
        
pygame.quit()