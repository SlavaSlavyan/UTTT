import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Полупрозрачный объект в Pygame")

# Создание полупрозрачного объекта
# Создаем поверхность с альфа-каналом
transparent_surface = pygame.Surface((200, 200), pygame.SRCALPHA)
# Заливаем поверхность красным цветом с альфа-каналом (128 - полупрозрачный)
transparent_surface.fill((255, 255, 255, 50))

def square():
    x = width//2
    y = height//2

    pos = [(x-300,y+300),(x+300,y+300),(x+300,y-300),(x-300,y-300)]
        
    pygame.draw.polygon(screen, (33, 37, 43), pos)
    

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Заполнение экрана белым цветом
    screen.fill((0,0,0))

    # Отрисовка полупрозрачного объекта

    square()


    screen.blit(transparent_surface, (300, 200))

    # Обновление экрана
    pygame.display.flip()