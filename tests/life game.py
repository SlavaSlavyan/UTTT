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

cells[15][15] = 1
cells[15][16] = 1
cells[15][14] = 1

size = (len(cells)*20, len(cells[0])*20)

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

    def newlife():

        global cells

        for s in range(len(cells)):

            for i in range(len(cells[0])):
                
                cell = 0

                for ss in range(3):
                    for ii in range(3):
                        try:
                            if cells[s-1+ss][i-1+ii] == 1:
                                cell+=1
                        except:
                            pass
                
                if cell == 3:
                    cells[s][i] = 2

    def kill():

        global cells

        for s in range(len(cells)):

            for i in range(len(cells[0])):
                
                cell = 0

                for ss in range(3):
                    for ii in range(3):
                        try:
                            if cells[s-1+ss][i-1+ii] == 1:
                                cell+=1
                        except:
                            pass
                
                if cells[s][i] == 1:

                    if cell < 2 and cell > 3:
                        cells[s][i] = 0
    
    def clear():

        global cells

        for s in range(len(cells)):

            for i in range(len(cells[0])):

                if cells[s][i] == 2:
                    cells[s][i] = 1
                        


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
        clock.tick(100)

main()