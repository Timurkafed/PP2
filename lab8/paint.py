'''
Инструменты:
R - прямоугольник
C - круг
D - карандаш
E - ластик

'''

import pygame

pygame.init()

# Цвета
colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)
current_color = colorRED  # Текущий цвет по умолчанию

# Настройки экрана
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill(colorWHITE)  # Белый фон

# Инструменты
mode = 'draw'  # Режимы: draw, rect, circle, erase
LMBpressed = False
THICKNESS = 5

# Координаты для инструментов
prevX, prevY = 0, 0
currX, currY = 0, 0
start_pos = (0, 0)

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

running = True

while running:
    screen.blit(base_layer, (0, 0))  # Отображаем базовый слой

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обработка нажатий мыши
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            prevX, prevY = event.pos
            currX, currY = event.pos
            start_pos = event.pos

        elif event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                currX, currY = event.pos
                
                # Режим рисования линий
                if mode == 'draw':
                    pygame.draw.line(base_layer, current_color, (prevX, prevY), (currX, currY), THICKNESS)
                    prevX, prevY = currX, currY
                
                # Режим ластика
                elif mode == 'erase':
                    pygame.draw.line(base_layer, colorWHITE, (prevX, prevY), (currX, currY), THICKNESS)
                    prevX, prevY = currX, currY

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            
            # Фиксация фигур на базовом слое
            if mode == 'rect':
                pygame.draw.rect(base_layer, current_color, calculate_rect(start_pos[0], start_pos[1], currX, currY), THICKNESS)
            elif mode == 'circle':
                radius = int(((currX-start_pos[0])**2 + (currY-start_pos[1])**2)**0.5)
                pygame.draw.circle(base_layer, current_color, start_pos, radius, THICKNESS)

        # Обработка клавиш
        if event.type == pygame.KEYDOWN:
            # Выбор инструментов
            if event.key == pygame.K_r: mode = 'rect'
            elif event.key == pygame.K_c: mode = 'circle'
            elif event.key == pygame.K_d: mode = 'draw'
            elif event.key == pygame.K_e: mode = 'erase'
            
            # Выбор цвета
            if event.key == pygame.K_1: current_color = colorRED
            elif event.key == pygame.K_2: current_color = colorBLUE
            elif event.key == pygame.K_3: current_color = colorBLACK
            elif event.key == pygame.K_4: current_color = colorWHITE
            
            # Регулировка толщины
            if event.key == pygame.K_EQUALS: THICKNESS += 1
            elif event.key == pygame.K_MINUS and THICKNESS > 1: THICKNESS -= 1

    # Предварительный просмотр фигур
    if LMBpressed and mode == 'rect':
        pygame.draw.rect(screen, current_color, calculate_rect(start_pos[0], start_pos[1], currX, currY), THICKNESS)
    elif LMBpressed and mode == 'circle':
        radius = int(((currX-start_pos[0])**2 + (currY-start_pos[1])**2)**0.5)
        pygame.draw.circle(screen, current_color, start_pos, radius, THICKNESS)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()