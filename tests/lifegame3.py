import pygame
import sys
import random

pygame.init()

width, height = 1000, 800
screen = pygame.display.set_mode((width, height),pygame.RESIZABLE)

cells = []

for i in range(30):
    cells.append([])

for s in range(30):
    for i in range(30):
        cells[s].append(0)

size = (len(cells)*20, len(cells[0])*20)

a = 1

if a == 1:
    for y in range(len(cells)):
        for x in range(len(cells[0])):
            if x == 0 or x == len(cells[0])-1 or y == 0 or y == len(cells)-1:
                pass
            else:
                cells[y][x] = random.randint(0,1)

pygame.display.set_caption("Life game 3")

clock = pygame.time.Clock()

class Draw:

    def main():

        screen.fill((0,0,0))
        Draw.cells()

    def cells():
        
        for s in range(len(cells)):

            for i in range(len(cells[0])):

                x = width//2 + 20*i - size[0]//2
                y = height//2 + 20*s - size[1]//2
                
                pos = [(x-10,y-10),(x+10,y-10),(x+10,y+10),(x-10,y+10)]

                if cells[s][i] == 0:
                    color = (10,10,10)
                elif cells[s][i] == 2:
                    color = (119,221,119)
                elif cells[s][i] == 3:
                    color = (196,30,58)
                else:
                    color = (255,255,255)

                pygame.draw.polygon(screen, color, pos)

def check():

    for y in range(len(cells)):
        for x in range(len(cells[0])):
            if cells[y][x] == 2 or cells[y][x] == 3:
                return True
    return False
            

class Game:

    def main():

        arg = check()
        if arg == False:
            Game.newlife()
            Game.kill()
        else:
            Game.clear()
        
    
    def newlife():

        global cells

        for y in range(len(cells)):
            for x in range(len(cells[0])):
                if x == 0 or x == len(cells[0])-1 or y == 0 or y == len(cells)-1:
                    pass
                else:
                    if cells[y][x] == 0:
                        alive = 0
                        for yy in range(3):
                            for xx in range(3):
                                if cells[y+yy-1][x+xx-1] == 1:
                                    alive+=1
                        if alive == 4:
                            cells[y][x] = 2

    def kill():

        global cells

        for y in range(len(cells)):
            for x in range(len(cells[0])):
                if x == 0 or x == len(cells[0])-1 or y == 0 or y == len(cells)-1:
                    pass
                else:
                    if cells[y][x] == 1:
                        alive = -1
                        for yy in range(3):
                            for xx in range(3):
                                if cells[y+yy-1][x+xx-1] == 1 or cells[y+yy-1][x+xx-1] == 3:
                                    alive+=1
                        if alive != 4 and alive != 3:
                            cells[y][x] = 3
    
    def clear():

        global cells

        for y in range(len(cells)):
            for x in range(len(cells[0])):
                if cells[y][x] == 2:
                    cells[y][x] = 1
                elif cells[y][x] == 3:
                    cells[y][x] = 0

def main():

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
            
        Draw.main()
        Game.main()
                
        pygame.display.flip()
        clock.tick(1)

main()