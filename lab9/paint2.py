'''
Инструменты:
R - прямоугольник
C - круг
D - карандаш
E - ластик
T - прямоугольный треугольник
Y - равносторонний треугольник
H - ромб

Цвета:
1 - красный
2 - синий
3 - черный
4 - белый

Толщина:
"+" - увеличить
"-" - уменьшить

'''

import pygame
import math

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
mode = 'draw'  # Режимы: draw, rect, circle, erase, right_triangle, equilateral_triangle, rhombus
LMBpressed = False
THICKNESS = 5

# Координаты для инструментов
prevX, prevY = 0, 0
currX, currY = 0, 0
start_pos = (0, 0)

def calculate_rect(x1, y1, x2, y2):
    """Вычисляет прямоугольник по двум точкам"""
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def draw_right_triangle(surface, color, start, end, thickness):
    """Рисует прямоугольный треугольник"""
    x1, y1 = start
    x2, y2 = end
    points = [(x1, y1), (x1, y2), (x2, y2)]
    pygame.draw.polygon(surface, color, points, thickness)

def draw_equilateral_triangle(surface, color, start, end, thickness):
    """Рисует равносторонний треугольник"""
    x1, y1 = start
    x2, y2 = end
    side_length = max(abs(x2 - x1), abs(y2 - y1))
    height = side_length * math.sqrt(3) / 2
    
    # Определяем направление рисования
    if x2 < x1:
        side_length = -side_length
    if y2 < y1:
        height = -height
    
    points = [
        (x1, y1),
        (x1 + side_length, y1),
        (x1 + side_length / 2, y1 - height)
    ]
    pygame.draw.polygon(surface, color, points, thickness)

def draw_rhombus(surface, color, start, end, thickness):
    """Рисует ромб"""
    x1, y1 = start
    x2, y2 = end
    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    
    points = [
        (center_x, y1),          # Верхняя точка
        (x2, center_y),          # Правая точка
        (center_x, y2),          # Нижняя точка
        (x1, center_y)           # Левая точка
    ]
    pygame.draw.polygon(surface, color, points, thickness)

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
            elif mode == 'right_triangle':
                draw_right_triangle(base_layer, current_color, start_pos, (currX, currY), THICKNESS)
            elif mode == 'equilateral_triangle':
                draw_equilateral_triangle(base_layer, current_color, start_pos, (currX, currY), THICKNESS)
            elif mode == 'rhombus':
                draw_rhombus(base_layer, current_color, start_pos, (currX, currY), THICKNESS)

        # Обработка клавиш
        if event.type == pygame.KEYDOWN:
            # Выбор инструментов
            if event.key == pygame.K_r: mode = 'rect'
            elif event.key == pygame.K_c: mode = 'circle'
            elif event.key == pygame.K_d: mode = 'draw'
            elif event.key == pygame.K_e: mode = 'erase'
            elif event.key == pygame.K_t: mode = 'right_triangle'       # T - right Triangle
            elif event.key == pygame.K_y: mode = 'equilateral_triangle' # Y - equilYateral triangle
            elif event.key == pygame.K_h: mode = 'rhombus'              # H - rombH
            
            # Выбор цвета
            if event.key == pygame.K_1: current_color = colorRED
            elif event.key == pygame.K_2: current_color = colorBLUE
            elif event.key == pygame.K_3: current_color = colorBLACK
            elif event.key == pygame.K_4: current_color = colorWHITE
            
            # Регулировка толщины
            if event.key == pygame.K_EQUALS: THICKNESS += 1
            elif event.key == pygame.K_MINUS and THICKNESS > 1: THICKNESS -= 1

    # Предварительный просмотр фигур
    if LMBpressed:
        if mode == 'rect':
            pygame.draw.rect(screen, current_color, calculate_rect(start_pos[0], start_pos[1], currX, currY), THICKNESS)
        elif mode == 'circle':
            radius = int(((currX-start_pos[0])**2 + (currY-start_pos[1])**2)**0.5)
            pygame.draw.circle(screen, current_color, start_pos, radius, THICKNESS)
        elif mode == 'right_triangle':
            draw_right_triangle(screen, current_color, start_pos, (currX, currY), THICKNESS)
        elif mode == 'equilateral_triangle':
            draw_equilateral_triangle(screen, current_color, start_pos, (currX, currY), THICKNESS)
        elif mode == 'rhombus':
            draw_rhombus(screen, current_color, start_pos, (currX, currY), THICKNESS)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()