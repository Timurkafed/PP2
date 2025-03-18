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
    
def stop():
    pygame.mixer.stop()
    
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

play()

while running:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                next()
            elif event.key == pygame.K_LEFT:
                previous()
            elif event.key == pygame.K_ESCAPE:
                stop()

pygame.quit()