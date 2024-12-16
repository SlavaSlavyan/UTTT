import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 10
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# Цвета
BACKGROUND_COLOR = (255, 255, 255)
CELL_COLOR = (0, 0, 0)
GRID_COLOR = (200, 200, 200)

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра в жизнь")

# Генерация случайного состояния клеток
def generate_grid():
    return [[random.choice([0, 1]) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Отображение сетки
def draw_grid(grid):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if grid[y][x] == 1:
                pygame.draw.rect(screen, CELL_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, GRID_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

# Подсчет соседей для клетки
def count_neighbors(grid, x, y):
    neighbors = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            nx, ny = (x + dx) % GRID_WIDTH, (y + dy) % GRID_HEIGHT
            if dx == 0 and dy == 0:
                continue
            neighbors += grid[ny][nx]
    return neighbors

# Обновление состояния клеток
def update_grid(grid):
    new_grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            neighbors = count_neighbors(grid, x, y)
            if grid[y][x] == 1 and neighbors in [2, 3]:
                new_grid[y][x] = 1
            elif grid[y][x] == 0 and neighbors == 3:
                new_grid[y][x] = 1
    return new_grid

# Главный игровой цикл
def main():
    clock = pygame.time.Clock()
    grid = generate_grid()

    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Отображение сетки
        draw_grid(grid)

        # Обновление состояния клеток
        grid = update_grid(grid)

        pygame.display.flip()
        clock.tick(10)  # Обновление экрана 10 раз в секунду

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()