import pygame
import random
import time

pygame.init()

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load('resources/AnimatedStreet.png')

running = True
clock = pygame.time.Clock()
FPS = 60

player_img = pygame.image.load('resources/player_car.png')
player_img = pygame.transform.scale(player_img, (40, 95))
enemy_img = pygame.image.load('resources/Enemy.png')
enemy_img2 = pygame.image.load('resources/Enemy2.png')
enemy_img2 = pygame.transform.scale(enemy_img2, (50, 70))
zebra_png = pygame.image.load('resources/Zebra2.png')
zebra_png = pygame.transform.scale(zebra_png, (500, 110))
coin_img = pygame.image.load('resources/coin.png')  # добавь изображение монетки
coin_img = pygame.transform.scale(coin_img, (30, 30))

pygame.mixer.music.load('resources/background.wav')
crash_sound = pygame.mixer.Sound('resources/crash.wav')

pygame.mixer.music.play(-1)

font_big = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font_big.render("Game Over", True, "black")

PLAYER_SPEED = 5
ENEMY_SPEED = 10
DED_SPEED = 3
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

        # границы экрана
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

class EnemyDed(Enemy):
    def __init__(self):
        super().__init__(enemy_img2, DED_SPEED)

class EnemyCar(Enemy):
    def __init__(self):
        super().__init__(enemy_img, ENEMY_SPEED)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.reset_position()

    def move(self):
        self.rect.move_ip(0, COIN_SPEED)
        if self.rect.top > HEIGHT:
            self.reset_position()

    def reset_position(self):
        self.rect.x = random.randint(30, WIDTH - 30)
        self.rect.y = random.randint(-500, -30)


# создание объектов
player = Player()
enemycar = EnemyCar()
enemyded = EnemyDed()
coin = Coin()

all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()

all_sprites.add([player, enemycar, enemyded, coin])
enemy_sprites.add([enemycar, enemyded])
coin_sprites.add(coin)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    player.move()
    enemycar.move()
    enemyded.move()
    coin.move()

    zebra_y = enemyded.rect.y - 20
    for i in range(0, WIDTH, 40):
        screen.blit(zebra_png, (10, zebra_y))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    # столкновение с врагом
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        crash_sound.play()
        time.sleep(1)

        screen.fill("red")
        center_rect = game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(game_over, center_rect)
        pygame.display.flip()
        time.sleep(2)
        running = False

    # сбор монет
    if pygame.sprite.spritecollideany(player, coin_sprites):
        coins_collected += 1
        coin.reset_position()

    # отображение счёта
    score_text = font_small.render(f"Coins: {coins_collected}", True, "black")
    screen.blit(score_text, (WIDTH - 120, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
