import pygame
from color_palette import *
import random
import time

pygame.init()

# Game constants
WIDTH = 600
HEIGHT = 600
FPS = 5
BASE_FOOD_WEIGHT = 1  # Standard food value
MAX_FOOD_TYPES = 3     # Different types of food

class Point:
    """Class to represent x,y coordinates on game grid"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:
    """Class representing the snake player"""
    def __init__(self):
        # Initialize snake with 3 body segments
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1  # Initial movement direction (right)
        self.dy = 0
        self.new_direction = (1, 0)  # Buffer for smooth direction changes
        
    def move(self, max_x, max_y):
        """Move the snake based on current direction"""
        # Update direction from buffer
        self.dx, self.dy = self.new_direction
        
        # Move body segments (from tail to head)
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        # Move head
        self.body[0].x += self.dx
        self.body[0].y += self.dy

        # Check wall collision
        if (self.body[0].x < 0 or self.body[0].x >= max_x or
            self.body[0].y < 0 or self.body[0].y >= max_y):
            return False
        return True

    def grow(self, amount=1):
        """Add new segments to the snake"""
        for _ in range(amount):
            tail = self.body[-1]
            self.body.append(Point(tail.x, tail.y))

    def draw(self, screen, CELL):
        """Draw snake on screen"""
        # Draw head (red)
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        # Draw body (yellow)
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        """Check if snake head collides with food"""
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.grow(food.weight)  # Grow based on food weight
            return True
        return False

    def check_self_collision(self):
        """Check if snake hits itself"""
        head = self.body[0]
        for segment in self.body[1:]:
            if head.x == segment.x and head.y == segment.y:
                return True
        return False

    def set_direction(self, dx, dy):
        """Change movement direction (with 180° turn protection)"""
        if (dx, dy) != (-self.dx, -self.dy):
            self.new_direction = (dx, dy)

class Food:
    """Class representing food items with different properties"""
    def __init__(self):
        self.pos = Point(0, 0)
        self.weight = BASE_FOOD_WEIGHT
        self.color = colorGREEN
        self.spawn_time = time.time()
        self.lifetime = random.randint(5, 15)  # Random lifetime 5-15 seconds
        self.generate_random_properties()
        
    def generate_random_properties(self):
        """Assign random type/weight to food"""
        food_type = random.randint(1, MAX_FOOD_TYPES)
        
        if food_type == 1:  # Standard food
            self.weight = 1
            self.color = colorGREEN
        elif food_type == 2:  # Premium food
            self.weight = 2
            self.color = colorBLUE
            self.lifetime = 8  # Shorter lifetime for better food
        else:  # Special food
            self.weight = 3
            self.color = colorPURPLE
            self.lifetime = 5  # Shortest lifetime
            
    def is_expired(self):
        """Check if food should disappear"""
        return time.time() - self.spawn_time > self.lifetime
        
    def generate_random_pos(self, snake_body, CELL):
        """Find valid random position not occupied by snake"""
        while True:
            self.pos.x = random.randint(0, WIDTH // CELL - 1)
            self.pos.y = random.randint(0, HEIGHT // CELL - 1)
            if not any(segment.x == self.pos.x and segment.y == self.pos.y for segment in snake_body):
                self.spawn_time = time.time()  # Reset timer for new food
                self.generate_random_properties()  # Randomize new food properties
                break

    def draw(self, screen, CELL):
        """Draw food on screen with colored border indicating remaining time"""
        # Calculate remaining lifetime percentage
        life_left = 1 - (time.time() - self.spawn_time) / self.lifetime
        border_width = max(1, int(3 * life_left))  # Thinner border as time runs out
        
        # Draw main food body
        pygame.draw.rect(screen, self.color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))
        
        # Draw time indicator border
        border_color = (min(255, int(255 * (1 - life_left))),  # More red as time runs out
                        min(255, int(255 * life_left)),       # Less green
                        0)
        pygame.draw.rect(screen, border_color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL), border_width)

class GameScene:
    """Main game scene handling gameplay"""
    def __init__(self):
        self.CELL = 30
        self.foods = [Food() for _ in range(3)]  # Multiple food items
        self.snake = Snake()
        self.score = 0
        self.level = 1
        self.level_up_threshold = 3
        self.font = pygame.font.SysFont("Arial", 24)
        self.game_over = False
        
        # Initialize food positions
        for food in self.foods:
            food.generate_random_pos(self.snake.body, self.CELL)

    def draw_grid(self, screen):
        """Draw game grid lines"""
        for i in range(HEIGHT // self.CELL):
            for j in range(WIDTH // self.CELL):
                pygame.draw.rect(screen, colorGRAY, (i * self.CELL, j * self.CELL, self.CELL, self.CELL), 1)

    def draw_text(self, surface, text, pos, color=colorWHITE):
        """Helper method to draw text"""
        label = self.font.render(text, True, color)
        surface.blit(label, pos)

    def ProcessInput(self, events):
        """Handle user input"""
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.snake.set_direction(1, 0)
                elif event.key == pygame.K_LEFT:
                    self.snake.set_direction(-1, 0)
                elif event.key == pygame.K_DOWN:
                    self.snake.set_direction(0, 1)
                elif event.key == pygame.K_UP:
                    self.snake.set_direction(0, -1)

    def Update(self):
        """Update game state"""
        if self.game_over:
            return "game_over"
            
        max_x = WIDTH // self.CELL
        max_y = HEIGHT // self.CELL
        
        # Move snake and check collisions
        if not self.snake.move(max_x, max_y) or self.snake.check_self_collision():
            self.game_over = True
            return "game_over"
        
        # Check food collisions
        for food in self.foods:
            if self.snake.check_collision(food):
                self.score += food.weight
                food.generate_random_pos(self.snake.body, self.CELL)
                if self.score % self.level_up_threshold == 0:
                    self.level += 1
                    return "level_up"
        
        # Check for expired food
        for i, food in enumerate(self.foods):
            if food.is_expired():
                self.foods[i] = Food()
                self.foods[i].generate_random_pos(self.snake.body, self.CELL)
        
        return "playing"

    def Render(self, screen):
        """Render game objects"""
        screen.fill(colorBLACK)
        self.draw_grid(screen)
        
        # Draw all foods
        for food in self.foods:
            food.draw(screen, self.CELL)
        
        self.snake.draw(screen, self.CELL)
        
        # Draw UI text
        self.draw_text(screen, f"Score: {self.score}", (10, 10))
        self.draw_text(screen, f"Level: {self.level}", (10, 40))
        
        # Game over message
        if self.game_over:
            self.draw_text(screen, "GAME OVER", (WIDTH//2 - 70, HEIGHT//2 - 20), colorRED)
            self.draw_text(screen, "Press R to restart", (WIDTH//2 - 90, HEIGHT//2 + 10))

def run_game():
    """Main game loop"""
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    scene = GameScene()
    current_fps = FPS
    running = True

    while running:
        events = pygame.event.get()
        
        # Handle events
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r and scene.game_over:
                # Restart game
                scene = GameScene()
                current_fps = FPS
        
        # Process input and update
        scene.ProcessInput(events)
        result = scene.Update()
        
        # Increase speed on level up
        if result == "level_up":
            current_fps += 1
        
        # Render everything
        scene.Render(screen)
        pygame.display.flip()
        clock.tick(current_fps)

    pygame.quit()

run_game()