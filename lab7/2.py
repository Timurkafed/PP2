import pygame
import os

pygame.init()
pygame.mixer.init()

music_folder = 'sources'
musics = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]

music_index = 0

def play():
    pygame.mixer.music.load(f"{music_folder}/{musics[music_index]}")
    pygame.mixer.music.play()

def next():
    global music_index
    music_index = (music_index + 1) % len(musics)
    play()
    
def previous():
    global music_index
    music_index = (music_index + 1) % len(musics)
    play()

WIDTH, HEIGHT = 1920//1.5, 1080//1.5

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True

f1 = pygame.font.Font(None, 36)
text = f1.render('NEXT', 1, (180, 0, 0))
text2 = f1.render('BACK', 1, (180, 0, 0))
text3 = f1.render('PAUSE', 1, (180, 0, 0))


play()

while running:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    screen.blit(text3, (WIDTH//2, HEIGHT//2))
                    pygame.mixer.music.pause()                    
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                screen.blit(text, (WIDTH//2, HEIGHT//2))
                next()
            elif event.key == pygame.K_LEFT:
                screen.blit(text2, (WIDTH//2, HEIGHT//2))
                previous()
    pygame.display.flip()
    clock.tick(30)

pygame.quit()