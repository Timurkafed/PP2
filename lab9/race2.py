import pygame
import random
import time

pygame.init()

# Game constants
WIDTH = 400
HEIGHT = 600
FPS = 60
SPEED_INCREASE_INTERVAL = 5  # Increase speed every N coins
MAX_COINS = 3  # Maximum coins on screen at once

# Load images
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
background = pygame.image.load('resources/AnimatedStreet.png')

player_img = pygame.image.load('resources/player_car.png')
player_img = pygame.transform.scale(player_img, (40, 95))
enemy_img = pygame.image.load('resources/Enemy.png')
enemy_img2 = pygame.image.load('resources/Enemy2.png')
enemy_img2 = pygame.transform.scale(enemy_img2, (50, 70))
zebra_png = pygame.image.load('resources/Zebra2.png')
zebra_png = pygame.transform.scale(zebra_png, (500, 110))

# Load three different coin images
coin_img1 = pygame.image.load('resources/coin1.png')  # Basic coin (1 point)
coin_img1 = pygame.transform.scale(coin_img1, (30, 30))
coin_img2 = pygame.image.load('resources/coin2.png')  # Silver coin (2 points)
coin_img2 = pygame.transform.scale(coin_img2, (35, 35))
coin_img3 = pygame.image.load('resources/coin3.png')  # Gold coin (3 points)
coin_img3 = pygame.transform.scale(coin_img3, (40, 40))

# Load sounds
pygame.mixer.music.load('resources/background.wav')
crash_sound = pygame.mixer.Sound('resources/crash.wav')
coin_sound = pygame.mixer.Sound('resources/coin.wav')
pygame.mixer.music.play(-1)

# Fonts
font_big = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font_big.render("Game Over", True, "black")

# Initial speeds
PLAYER_SPEED = 5
INIT_ENEMY_SPEED = 10
INIT_DED_SPEED = 3
COIN_SPEED = 5

coins_collected = 0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2 - self.rect.w // 2
        self.rect.y = HEIGHT - self.rect.h

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-PLAYER_SPEED, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(PLAYER_SPEED, 0)
        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -PLAYER_SPEED)
        if keys[pygame.K_DOWN]:
            self.rect.move_ip(0, PLAYER_SPEED)

        # Screen boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, speed):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.speed = speed
        self.generate_random_rect()

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.generate_random_rect()

    def generate_random_rect(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.w)
        self.rect.y = -50

    def increase_speed(self, amount):
        self.speed += amount

class EnemyDed(Enemy):
    def __init__(self):
        super().__init__(enemy_img2, INIT_DED_SPEED)

class EnemyCar(Enemy):
    def __init__(self):
        super().__init__(enemy_img, INIT_ENEMY_SPEED)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.set_random_properties()
        self.reset_position()

    def set_random_properties(self):
        """Set random coin type with different weights and images"""
        coin_type = random.randint(1, 3)
        
        if coin_type == 1:  # Basic coin (1 point)
            self.weight = 1
            self.image = coin_img1
        elif coin_type == 2:  # Silver coin (2 points)
            self.weight = 2
            self.image = coin_img2
        else:  # Gold coin (3 points)
            self.weight = 3
            self.image = coin_img3
        
        self.rect = self.image.get_rect()

    def move(self):
        self.rect.move_ip(0, COIN_SPEED)
        if self.rect.top > HEIGHT:
            self.reset_position()

    def reset_position(self):
        """Place coin at random position above screen"""
        self.set_random_properties()
        self.rect.x = random.randint(30, WIDTH - self.rect.w)
        self.rect.y = random.randint(-500, -30)

# Create game objects
player = Player()
enemycar = EnemyCar()
enemyded = EnemyDed()

# Sprite groups
all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()

all_sprites.add([player, enemycar, enemyded])
enemy_sprites.add([enemycar, enemyded])

# Create initial coins
for _ in range(MAX_COINS):
    coin = Coin()
    coin_sprites.add(coin)
    all_sprites.add(coin)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background
    screen.blit(background, (0, 0))

    # Move all objects
    player.move()
    enemycar.move()
    enemyded.move()
    
    for coin in coin_sprites:
        coin.move()

    # Draw zebra crossing behind enemy car
    zebra_y = enemyded.rect.y - 20
    for i in range(0, WIDTH, 40):
        screen.blit(zebra_png, (10, zebra_y))

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    # Collision with enemy
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        crash_sound.play()
        time.sleep(1)

        screen.fill("red")
        center_rect = game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(game_over, center_rect)
        pygame.display.flip()
        time.sleep(2)
        running = False

    # Coin collection
    collected_coins = pygame.sprite.spritecollide(player, coin_sprites, True)
    if collected_coins:
        coin_sound.play()
        for coin in collected_coins:
            coins_collected += coin.weight
            # Increase enemy speed every SPEED_INCREASE_INTERVAL coins
            if coins_collected % SPEED_INCREASE_INTERVAL == 0:
                enemycar.increase_speed(1)
                enemyded.increase_speed(1)
            
            # Create new coin to replace collected one
            new_coin = Coin()
            coin_sprites.add(new_coin)
            all_sprites.add(new_coin)

    # Keep number of coins at MAX_COINS
    while len(coin_sprites) < MAX_COINS:
        new_coin = Coin()
        coin_sprites.add(new_coin)
        all_sprites.add(new_coin)

    # Display score and speed
    score_text = font_small.render(f"Coins: {coins_collected}", True, "black")
    speed_text = font_small.render(f"Speed: {enemycar.speed}", True, "black")
    screen.blit(score_text, (WIDTH - 120, 10))
    screen.blit(speed_text, (WIDTH - 120, 40))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()