import pygame
import sys
import math

# Инициализация Pygame
pygame.init()

# Задаем размеры окна
width, height = 1000, 700
screen = pygame.display.set_mode((width, height))
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Круг с Pygame")

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Заполнение фона

# Рисуем круг
circle_radius = 25
circle_x = width // 2
circle_y = height // 2

font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

pos = [0,100]
move = 1
speed = 1

# Основной цикл
while True:
    pygame.event.pump() 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
    screen.fill(white)

    #pygame.draw.line(screen, black, (width // 2, 0), (width // 2, height), 2)  # Вертикальная ось
    #pygame.draw.line(screen, black, (0, height // 2), (width, height // 2), 2)  # Горизонтальная ось

    circle_x = width // 2 + pos[0]
    circle_y = height // 2 - pos[1]

    pygame.draw.circle(screen, red, (circle_x, circle_y), circle_radius)

    if pos[1] > height // 2 - circle_radius:
        if move == 0:
            move = 1
            speed += 0.1
        elif move == 2:
            move = 3
            speed += 0.1
    if pos[1] < -height // 2 + circle_radius:
        if move == 1:
            move = 0
            speed += 0.1
        elif move == 3:
            move = 2
            speed += 0.1
    if pos[0] > width // 2 - circle_radius:
        if move == 0:
            move = 2
            speed += 0.1
        elif move == 1:
            move = 3
            speed += 0.1
    if pos[0] < -width // 2 + circle_radius:
        if move == 2:
            move = 0
            speed += 0.1
        elif move == 3:
            move = 1
            speed += 0.1


    if move == 0: # x+ y+
        pos[0] += speed
        pos[1] += speed
    elif move == 1: # x+ y-
        pos[0] += speed
        pos[1] -= speed
    elif move == 2: # x- y+
        pos[0] -= speed
        pos[1] += speed
    elif move == 3: # x- y-
        pos[0] -= speed
        pos[1] -= speed



    coordinates_text = f"Координаты: ({int(circle_x-width// 2)}, {int(-(circle_y-height//2))})"
    text_surface = font.render(coordinates_text, True, black)
    screen.blit(text_surface, (10, 10))

    width, height = screen.get_size()

    # Обновляем экран
    pygame.display.flip()
    clock.tick(120)