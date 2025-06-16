import pygame

pygame.init()

# Создаем окно
screen = pygame.display.set_mode((800, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_MINUS:
                print("-")

            if event.key == pygame.K_LSHIFT:
                print("shift")

            if event.key == pygame.K_PLUS:
                print("+")
            #if event.key == pygame.K_MINUS:
            #    print("Дефис (-) был нажат")
            #if event.key == pygame.K_EQUALS:
            #    print("Равно (=) было нажат")

pygame.quit()
