import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройка экрана
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Размытый круг")

# Цвета
background_color = (255, 255, 255)  # Белый фон
circle_color = (255, 0, 0)           # Красный цвет для круга

# Параметры круга
circle_center = (400, 300)
circle_radius = 100
blur_radius = 50  # Радиус размытия

# Функция для рисования размытого круга
def draw_blurred_circle(surface, center, radius, blur_radius, color):
    # Создаем временную поверхность для рисования круга
    temp_surface = pygame.Surface((radius * 2 + blur_radius * 2, radius * 2 + blur_radius * 2), pygame.SRCALPHA)
    
    # Рисуем круг на временной поверхности
    pygame.draw.circle(temp_surface, color, (radius + blur_radius, radius + blur_radius), radius)

    # Создаем градиент размытия
    for r in range(radius + blur_radius, radius):
        alpha = int(255 * (1 - (r - radius) / blur_radius))  # Прозрачность
        pygame.draw.circle(temp_surface, (color[0], color[1], color[2], alpha), (radius + blur_radius, radius + blur_radius), r)

    # Накладываем временную поверхность на экран
    surface.blit(temp_surface, (center[0] - radius - blur_radius, center[1] - radius - blur_radius))

# Главный цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Заполнение фона
    screen.fill(background_color)

    # Рисуем размытый круг
    draw_blurred_circle(screen, circle_center, circle_radius, blur_radius, circle_color)

    # Обновление экрана
    pygame.display.flip()