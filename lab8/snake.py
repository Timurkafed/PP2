import pygame
from color_palette import *
import random

pygame.init()

WIDTH = 600
HEIGHT = 600
CELL = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
FPS = 5

def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL))

def draw_text(surface, text, pos, color=colorWHITE):
    label = font.render(text, True, color)
    surface.blit(label, pos)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
        self.new_direction = (1, 0)

    def move(self):
        # Сохраняем последний сегмент, чтобы добавить его при еде
        tail = self.body[-1]

        # Передвигаем тело
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        # Обновляем голову
        self.dx, self.dy = self.new_direction
        self.body[0].x += self.dx
        self.body[0].y += self.dy

        '''# Телепортация по краям
        self.body[0].x %= WIDTH // CELL
        self.body[0].y %= HEIGHT // CELL'''
        
        # Проверка на выход за границы
        if (self.body[0].x < 0 or self.body[0].x >= WIDTH // CELL or
            self.body[0].y < 0 or self.body[0].y >= HEIGHT // CELL):
            return False
        return True

    def grow(self):
        # Добавляем новый сегмент в конец тела
        tail = self.body[-1]
        self.body.append(Point(tail.x, tail.y))

    def draw(self):
        pygame.draw.rect(screen, colorRED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            print("Got food!")
            self.grow()
            food.generate_random_pos(self.body)
            return True
        return False


    def check_self_collision(self):
        head = self.body[0]
        for segment in self.body[1:]:
            if head.x == segment.x and head.y == segment.y:
                return True
        return False

    def set_direction(self, dx, dy):
        # Защита от разворота назад
        if (dx, dy) == (-self.dx, -self.dy):
            return
        self.new_direction = (dx, dy)

class Food:
    def __init__(self):
        self.pos = Point(9, 9)

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self, snake_body):
        while True:
            new_x = random.randint(0, WIDTH // CELL - 1)
            new_y = random.randint(0, HEIGHT // CELL - 1)
            if all(part.x != new_x or part.y != new_y for part in snake_body):
                self.pos = Point(new_x, new_y)
                break

# === Game Setup ===

score = 0
level = 1
level_up_threshold = 3  # каждые 3 еды - новый уровень
FPS = 5
font = pygame.font.SysFont("Arial", 24)

snake = Snake()
food = Food()
running = True

# === Main Game Loop ===
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.set_direction(1, 0)
            elif event.key == pygame.K_LEFT:
                snake.set_direction(-1, 0)
            elif event.key == pygame.K_DOWN:
                snake.set_direction(0, 1)
            elif event.key == pygame.K_UP:
                snake.set_direction(0, -1)

    screen.fill(colorBLACK)
    draw_grid()

    if not snake.move():
        print("Game Over: Hit the wall!")
        running = False

    if snake.check_self_collision():
        print("Game Over: You collided with yourself!")
        running = False

    if snake.check_collision(food):
        score += 1
        if score % level_up_threshold == 0:
            level += 1
            FPS += 1  # Увеличиваем скорость

    snake.check_collision(food)

    if snake.check_self_collision():
        print("Game Over: You collided with yourself!")
        running = False

    snake.draw()
    food.draw()
    
    draw_text(screen, f"Score: {score}", (10, 10))
    draw_text(screen, f"Level: {level}", (10, 40))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
