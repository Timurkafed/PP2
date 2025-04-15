import pygame
import psycopg2
from color_palette import *
import random
import time

# Настройки базы данных

# Инициализация Pygame
pygame.init()
WIDTH = 600
HEIGHT = 600
CELL = 30
FPS = 5

# Подключение к базе данных
def create_connection():
    try:
        return psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="Timur260607",
            port="2280"
        )
    except psycopg2.Error as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None

# Создание таблиц
def setup_database():
    conn = create_connection()
    if not conn:
        return
    
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS players (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) UNIQUE
            )
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS scores (
                id SERIAL PRIMARY KEY,
                player_id INTEGER REFERENCES players(id),
                score INTEGER,
                level INTEGER,
                game_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
    except psycopg2.Error as e:
        print(f"Ошибка при создании таблиц: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

# Регистрация игрока
def get_player_id(name):
    conn = create_connection()
    if not conn:
        return None
    
    try:
        cur = conn.cursor()
        cur.execute("SELECT id FROM players WHERE name = %s", (name,))
        player = cur.fetchone()
        
        if not player:
            cur.execute("INSERT INTO players (name) VALUES (%s) RETURNING id", (name,))
            player = cur.fetchone()
        
        conn.commit()
        return player[0]
    except psycopg2.Error as e:
        print(f"Ошибка работы с игроком: {e}")
        return None
    finally:
        if conn:
            cur.close()
            conn.close()

# Сохранение результата
def save_game_result(player_id, score, level):
    conn = create_connection()
    if not conn:
        return
    
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO scores (player_id, score, level) VALUES (%s, %s, %s)",
            (player_id, score, level)
        )
        conn.commit()
    except psycopg2.Error as e:
        print(f"Ошибка сохранения результата: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

# Классы игры
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
        
    def move(self, max_x, max_y):
        self.dx, self.dy = self.new_direction
        
        for i in range(len(self.body)-1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

        if (self.body[0].x < 0 or self.body[0].x >= max_x or
            self.body[0].y < 0 or self.body[0].y >= max_y):
            return False
        return True

    def check_self_collision(self):
        head = self.body[0]
        for segment in self.body[1:]:
            if head.x == segment.x and head.y == segment.y:
                return True
        return False

    def set_direction(self, dx, dy):
        if (dx, dy) != (-self.dx, -self.dy):
            self.new_direction = (dx, dy)

    def grow(self, amount=1):
        for _ in range(amount):
            self.body.append(Point(self.body[-1].x, self.body[-1].y))

    def draw(self, screen):
        pygame.draw.rect(screen, colorRED, (self.body[0].x*CELL, self.body[0].y*CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x*CELL, segment.y*CELL, CELL, CELL))

class Food:
    def __init__(self, food_type=None):
        self.pos = Point(0, 0)
        self.food_types = [
            {"weight": 1, "color": colorGREEN, "lifetime": 10},
            {"weight": 2, "color": colorBLUE, "lifetime": 8},
            {"weight": 3, "color": colorPURPLE, "lifetime": 6}
        ]
        
        # Принудительно задаем тип при создании
        self.type = food_type if food_type is not None else random.randint(0, 2)
        self.apply_properties()
        
        self.spawn_time = time.time()

    def apply_properties(self):
        """Устанавливаем свойства выбранного типа"""
        props = self.food_types[self.type]
        self.weight = props["weight"]
        self.color = props["color"]
        self.lifetime = props["lifetime"]

    def generate_random_pos(self, snake_body):
        while True:
            self.pos.x = random.randint(0, WIDTH//CELL-1)
            self.pos.y = random.randint(0, HEIGHT//CELL-1)
            if not any(segment.x == self.pos.x and segment.y == self.pos.y for segment in snake_body):
                break

    def is_expired(self):
        return time.time() - self.spawn_time > self.lifetime
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.pos.x*CELL, self.pos.y*CELL, CELL, CELL))


class Game:
    def __init__(self, player_name):
        setup_database()
        self.player_id = get_player_id(player_name)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.reset_game()

    def reset_game(self):
        self.snake = Snake()
        
        # Создаем гарантированно по одному экземпляру каждого типа
        self.foods = [
            Food(food_type=0),
            Food(food_type=1),
            Food(food_type=2)
        ]
        
        for food in self.foods:
            food.generate_random_pos(self.snake.body)
            
        self.score = 0
        self.level = 1
        self.game_over = False
        self.current_fps = FPS
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_RIGHT:
                    self.snake.set_direction(1, 0)
                elif event.key == pygame.K_LEFT:
                    self.snake.set_direction(-1, 0)
                elif event.key == pygame.K_DOWN:
                    self.snake.set_direction(0, 1)
                elif event.key == pygame.K_UP:
                    self.snake.set_direction(0, -1)
                elif event.key == pygame.K_r and self.game_over:
                    self.reset_game()
        return True

    def update(self):
        if self.game_over:
            return

        max_x = WIDTH // CELL
        max_y = HEIGHT // CELL
        
        if not self.snake.move(max_x, max_y) or self.snake.check_self_collision():
            self.game_over = True
            save_game_result(self.player_id, self.score, self.level)
            return

        for food in self.foods:
            if self.snake.body[0].x == food.pos.x and self.snake.body[0].y == food.pos.y:
                self.score += food.weight
                self.snake.grow(food.weight)
                food.generate_random_pos(self.snake.body)
                if self.score % 3 == 0:
                    self.level += 1
                    self.current_fps += 1

    def draw(self):
        self.screen.fill(colorBLACK)
        self.snake.draw(self.screen)
        for food in self.foods:
            food.draw(self.screen)
        
        font = pygame.font.SysFont("Arial", 24)
        self.screen.blit(font.render(f"Score: {self.score}", True, colorWHITE), (10, 10))
        self.screen.blit(font.render(f"Level: {self.level}", True, colorWHITE), (10, 40))
        
        if self.game_over:
            self.screen.blit(font.render("GAME OVER", True, colorRED), (WIDTH//2-70, HEIGHT//2-20))
            self.screen.blit(font.render("Press R to restart", True, colorWHITE), (WIDTH//2-90, HEIGHT//2+10))
        
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.current_fps)
        pygame.quit()

# Меню
def main_menu():
    setup_database()
    while True:
        print("\nГлавное меню:")
        print("1. Начать игру")
        print("2. Выход")
        choice = input("Выберите действие: ")
        
        if choice == "1":
            player_name = input("Введите ваше имя: ")
            game = Game(player_name)
            game.run()
            break
        elif choice == "2":
            break

if __name__ == "__main__":
    main_menu()