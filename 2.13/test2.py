import pygame
#import pygame.locals as pl

pygame.init()

# Настройки окна
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("UTF-8 Text Input")
font = pygame.font.Font("data\\font\\GNF.ttf", 32)  # Используйте свой шрифт, поддерживающий UTF-8

# Переменные для текста
input_text = ""
cursor_visible = True
cursor_timer = 0

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# Активируем ввод текста
input_rect = pygame.Rect(50, 50, 700, 40)
active = True

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if active:
                # Обработка специальных клавиш
                if event.key == pygame.K_RETURN:
                    print("Entered text:", input_text)
                    input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_ESCAPE:
                    running = False
                # Добавление юникод-символа
                elif event.unicode:
                    input_text += event.unicode
    
    # Мигание курсора
    cursor_timer += 1
    if cursor_timer >= 30:  # Частота мигания
        cursor_visible = not cursor_visible
        cursor_timer = 0
    
    # Отрисовка
    screen.fill(WHITE)
    
    # Поле ввода
    pygame.draw.rect(screen, GRAY, input_rect, 2)
    
    # Текст
    text_surface = font.render(input_text, True, BLACK)
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    
    # Курсор
    if active and cursor_visible:
        cursor_x = input_rect.x + 5 + text_surface.get_width()
        pygame.draw.line(screen, BLACK, (cursor_x, input_rect.y + 5), 
                         (cursor_x, input_rect.y + 35), 2)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()