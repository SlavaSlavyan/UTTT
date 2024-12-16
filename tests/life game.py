import pygame
import sys

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

cells[15][15] = 1
cells[15][16] = 1
cells[15][14] = 1


pygame.display.set_caption("Life game")

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
                else:
                    color = (255,255,255)

                pygame.draw.polygon(screen, color, pos)

class Game:

    def main():

        Game.newlife()
        Game.kill()
        Game.clear()
        #Game.test()
    
    def test():

        global cells

        alive = -1

        for xx in range(3):
            for yy in range(3):
                
                if cells[15+yy-1][15+xx-1] == 1:
                    alive += 1
        
        print(alive)
    
    def newlife():

        global cells

        for x in range(len(cells[0])):
            for y in range(len(cells)):
                
                if x == 0 or x == len(cells[0])-1 or y == 0 or y == len(cells)-1:

                    pass

                else:
                        
                    alive = 0

                    for xx in range(3):
                        for yy in range(3):
                            
                            if cells[x+yy-1][y+xx-1] == 1:
                                alive += 1

                    if alive == 3:
                        cells[y][x] = 2



    def kill():

        global cells

        for x in range(len(cells[0])):
            for y in range(len(cells)):
                
                if x == 0 or x == len(cells[0]) or y == 0 or y == len(cells):

                    pass

                else:
                    
                    if cells[y][x] == 1:
                        
                        alive = -1

                        for xx in range(3):
                            for yy in range(3):
                                
                                if cells[x+yy-1][y+xx-1] == 1:
                                    alive += 1

                        if alive == 3 or alive == 2:
                            cells[y][x] = 1
                        else:
                            cells[y][x] = 0
    
    def clear():

        for x in range(len(cells[0])):
            for y in range(len(cells)):
                if cells[y][x] == 2:
                    cells[y][x] = 1
                        


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