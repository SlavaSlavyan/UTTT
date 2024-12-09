import pygame
import sys
import math

p = 3.1415926

# Инициализация Pygame
pygame.init()

# Задаем размеры окна
width, height = 1000, 700
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("sincos test")

clock = pygame.time.Clock()

pos = []
s = 1
for i in range(4*s):
    pos.append(p*(0.5/s*i))

o = p
r = 100

while True:

    pygame.event.pump()
    width, height = screen.get_size()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = []
            s += 1
            for i in range(4*s):
                pos.append(p*(0.5/s*i))
            r /= 1.125
            print(s)

    screen.fill((255,255,255))
    #pygame.draw.circle(screen, (0,0,0), (width//2, height//2), 202)
    #pygame.draw.circle(screen, (255,255,255), (width//2, height//2), 198)

    for i in range(len(pos)):
        pygame.draw.circle(screen, (0,0,0), (width//2+math.sin(pos[i])*(200+math.sin(o)*100), height//2+math.cos(pos[i])*(200+math.cos(o)*100)), round(r))
    
    pos = [i+0.01 for i in pos]
    o += 0.1

    # Обновляем экран
    pygame.display.flip()
    clock.tick(120)