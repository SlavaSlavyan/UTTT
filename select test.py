import pygame
import sys

# Инициализация Pygame
pygame.init()

width, height = 700, 700
X = width // 2
Y = height // 2

# Установка размеров окна
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Рисование сложных форм')

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
pos = [0,0]

def select(x,y):
    # Координаты вершин многоугольника
    points = [(X-300*x+pos[0],Y+300*y+pos[1]),(X-150*x+pos[0], Y+300*y+pos[1]),(X-150*x+pos[0], Y+350*y+pos[1]),
    (X-350*x+pos[0], Y+350*y+pos[1]),(X-350*x+pos[0], Y+150*y+pos[1]),(X-300*x+pos[0], Y+150*y+pos[1])]

    # Рисование многоугольника
    pygame.draw.polygon(screen, BLUE, points)

# Главный цикл
while True:
    # Заполнение фона
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         # Проверка на клик мыши
        #if event.type == pygame.MOUSEBUTTONDOWN:
        #    # Получаем координаты клика
        #    mouse_x, mouse_y = event.pos
        #    mouse_x = mouse_x - width//2
        #    mouse_y = mouse_y - height//2
        #    print(f'Клик в координатах: {mouse_x}, {-mouse_y}')

        #    # Пример: рисуем круг в месте клика
        #    pos = [mouse_x,mouse_y]
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    pos = [mouse_x-width//2,mouse_y-height//2]


    size = 0.25

    select(size,size)
    select(-size,size)
    select(size,-size)
    select(-size,-size)

    # Обновление экрана
    pygame.display.flip()