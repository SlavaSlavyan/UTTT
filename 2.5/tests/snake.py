import pygame
import time
import random
import numpy as np

# Инициализация Pygame
pygame.init()

# Определение цветов
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Установка размеров окна
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Змейка')

# Настройки игры
snake_block = 10
snake_speed = 15
speed_up_factor = 10  # Увеличение скорости при ускорении
normal_speed = snake_speed

# Шрифт для отображения счета
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Q-Learning параметры
alpha = 0.1  # Скорость обучения
gamma = 0.9  # Дисконтирование
epsilon = 0.1  # Вероятность случайного действия
q_table = {}  # Q-таблица

def get_state(snake_head, food_pos):
    return (snake_head[0] // snake_block, snake_head[1] // snake_block, food_pos[0] // snake_block, food_pos[1] // snake_block)

def get_action(state):
    if state not in q_table:
        q_table[state] = [0, 0, 0, 0]  # [UP, DOWN, LEFT, RIGHT]
    
    if random.uniform(0, 1) < epsilon:
        return random.randint(0, 3)  # Случайное действие
    else:
        return np.argmax(q_table[state])  # Лучшая акция

def update_q_table(state, action, reward, next_state):
    if next_state not in q_table:
        q_table[next_state] = [0, 0, 0, 0]
    
    q_table[state][action] += alpha * (reward + gamma * max(q_table[next_state]) - q_table[state][action])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

def your_score(score):
    value = score_font.render("Счет: " + str(score), True, white)
    screen.blit(value, [0, 0])

def gameLoop():  # Основной игровой цикл
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # Начальное направление
    direction = None

    # Счет
    score = 0

    while not game_over:

        while game_close == True:
            screen.fill(blue )
            message("Ты проиграл! Нажми C, чтобы играть снова или Q, чтобы выйти", red)
            your_score(score)  # Отображение счета
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Получение состояния и выбор действия
        state = get_state((x1, y1), (foodx, foody))
        action = get_action(state)

        if action == 0 and direction != 'DOWN':  # UP
            x1_change = 0
            y1_change = -snake_block
            direction = 'UP'
        elif action == 1 and direction != 'UP':  # DOWN
            x1_change = 0
            y1_change = snake_block
            direction = 'DOWN'
        elif action == 2 and direction != 'RIGHT':  # LEFT
            x1_change = -snake_block
            y1_change = 0
            direction = 'LEFT'
        elif action == 3 and direction != 'LEFT':  # RIGHT
            x1_change = snake_block
            y1_change = 0
            direction = 'RIGHT'

        # Проверка выхода за границы и перенаправление
        if x1 >= width:
            x1 = 0
        elif x1 < 0:
            x1 = width - snake_block
        if y1 >= height:
            y1 = 0
        elif y1 < 0:
            y1 = height - snake_block

        # Обновление позиции змейки
        x1 += x1_change
        y1 += y1_change
        screen.fill(blue)
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        your_score(score)  # Отображение счета

        pygame.display.update()

        # Проверка на поедание еды
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            score += 1  # Увеличение счета
            reward = 1  # Положительная награда
        else:
            reward = -0.1  # Негативная награда за каждый шаг

        # Обновление Q-таблицы
        next_state = get_state((x1, y1), (foodx, foody))
        update_q_table(state, action, reward, next_state)

        try:
            pygame.time.Clock().tick(snake_speed)
        except:
            pygame.time.Clock().tick(15)

    pygame.quit()
    quit()

gameLoop()