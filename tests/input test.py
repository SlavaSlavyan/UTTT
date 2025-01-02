import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров окна
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ввод букв с клавиатуры")

# Установка шрифта
font = pygame.font.Font(None, 74)

# Переменная для хранения введенного текста
input_text = ""

# Главный игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Обработка нажатия клавиш
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Если нажата клавиша Enter
                print("Введенный текст:", input_text)
                input_text = ""  # Сбросить текст после нажатия Enter
            elif event.key == pygame.K_BACKSPACE:  # Если нажата клавиша Backspace
                input_text = input_text[:-1]  # Удалить последний символ
            else:
                # Добавляем символ к введенному тексту
                input_text += event.unicode

    # Получаем состояние всех клавиш
    keys = pygame.key.get_pressed()
    print(keys)

    # Заполнение фона
    screen.fill((255, 255, 255))

    # Отображение введенного текста
    text_surface = font.render(input_text, True, (0, 0, 0))
    screen.blit(text_surface, (50, 50))

    # Обновление экрана
    pygame.display.flip()

    # Ограничение частоты кадров
    pygame.time.delay(100)  # Задержка для предотвращения слишком быстрого ввода