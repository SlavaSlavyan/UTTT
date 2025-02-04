import pygame
import sys
import time

pygame.init()

width, height = 1000, 800
screen = pygame.display.set_mode((width, height),pygame.RESIZABLE)
pygame.display.set_caption("main test 2")

colors = [(40,44,52),(33,37,43),(171,178,191),(120,127,138),(68,163,239),(209,154,102)]

big_selected_cell = None
last_big_selected_cell = None
player = 0
cells = [[],[],[],[],[],[],[],[],[]]
figuresizes = [[],[],[],[],[],[],[],[],[]]
bigfiguresizes = []
for n in range(9):
    for i in range(9):
        cells[n].append(None)
        figuresizes[n].append(-1)
    bigfiguresizes.append(-1)

select = [0,[0,0],[0,0]] #0 size #1 offset #2 pos

class Main:

    def click(x,y):

        global big_selected_cell,player

        x = x - width // 2
        y = -(y - height //2)

        if big_selected_cell == None:
            big_selected_cell = Main.checkselectedbigcell(Main.selectbigcell(x,y))
        
        else:
            check = Main.checkselectedsmallcell(Main.selectsmallcell(x,y))
            if check[0] == 1:
                big_selected_cell = Main.nextcell(check[1])
                if player == 0:
                    player = 1
                else:
                    player = 0
            Main.capturecheck()

            

    def selectbigcell(x,y):

        selected_cell = 0

        for n in range(3):
            for i in range(3):

                if x > -300+200*i and x < -100+200*i and y > 100-200*n and y < 300-200*n:
                    selected_cell = i+3*n
                    return selected_cell
                
        return None

    def checkselectedbigcell(cell):

        global big_selected_cell

        if cell != None:

            if None not in cells[cell]:
                return big_selected_cell
            
            else:
                return cell
        else:
            return big_selected_cell
    
    def selectsmallcell(x,y):

        global big_selected_cell
        selected_cell = 0

        for i in range(3):
            if big_selected_cell >= 0+3*i and big_selected_cell <= 2+3*i:
                y -= 200-200*i
        for i in range(3):
            if big_selected_cell == 0+i or big_selected_cell == 3+i or big_selected_cell == 6+i:
                x -= -200+200*i

        for n in range(3):
            for i in range(3):

                if x > -75+50*i and x < -25+50*i and y > 25-50*n and y < 75-50*n:
                    selected_cell = i+3*n
                    return selected_cell
                
        return None

    def checkselectedsmallcell(cell):

        global big_selected_cell, cells

        if cell != None:

            if cells[big_selected_cell][cell] == None:

                cells[big_selected_cell][cell] = player
                return [1,cell]
            
            else:
                return [0,0]
        else:
            return [0,0]
    
    def nextcell(cell):
        
        global big_selected_cell

        Main.capturecheck()

        if cell != None:

            print(cells[cell])

            if None not in cells[cell]:
                return None
            
            else:
                return cell
        else:
            return None
    
    def capturecheck():

        for p in range(2):
            for bc in range(9):
                for i in range(3):
                    if cells[bc][0+3*i] == p and cells[bc][1+3*i] == p and cells[bc][2+3*i] == p:
                        cells[bc] = [p,p,p,p,p,p,p,p,p]
                    if cells[bc][0+i] == p and cells[bc][3+i] == p and cells[bc][6+i] == p:
                        cells[bc] = [p,p,p,p,p,p,p,p,p]
                for i in range(2):
                    if cells[bc][0+2*i] == p and cells[bc][4] == p and cells[bc][8-2*i] == p:
                        cells[bc] = [p,p,p,p,p,p,p,p,p]


class Draw:

    def main():

        Draw.cells()
        Draw.figures()
        Draw.select()
    
    def bgcells():

        x = width//2
        y = height//2

        pygame.draw.polygon(screen, colors[1], [(x-300,y+300),(x+300,y+300),(x+300,y-300),(x-300,y-300)])

    def cells():

        Draw.bgcells()

        x = width//2
        y = height//2
        
        pygame.draw.line(screen, colors[2], (x-300, y-100), (x+300, y-100), 5)
        pygame.draw.line(screen, colors[2], (x-300, y+100), (x+300, y+100), 5)
        pygame.draw.line(screen, colors[2], (x-100, y-300), (x-100, y+300), 5)
        pygame.draw.line(screen, colors[2], (x+100, y-300), (x+100, y+300), 5)

        for n in range(3):
            for i in range(3):
                Draw.minicell(-200+200*i,200-200*n,i+3*n)
            
        Draw.select()
        

    def minicell(offsetX,offsetY,i):
        
        x = width//2 
        y = height//2 
        if big_selected_cell == i:
            color = colors[2]
        else:
            color = colors[3]

        pygame.draw.line(screen, color, (x-75+offsetX, y-25-offsetY), (x+75+offsetX, y-25-offsetY), 3)
        pygame.draw.line(screen, color, (x-75+offsetX, y+25-offsetY), (x+75+offsetX, y+25-offsetY), 3)
        pygame.draw.line(screen, color, (x-25+offsetX, y-75-offsetY), (x-25+offsetX, y+75-offsetY), 3)
        pygame.draw.line(screen, color, (x+25+offsetX, y-75-offsetY), (x+25+offsetX, y+75-offsetY), 3)
    
    def quarter_select(dx,dy):

        x = width//2 + select[2][0] + select[1][0]
        y = height//2 - select[2][1] - select[1][1]
        if player == 0:
            color = colors[4]
        else:
            color = colors[5]

        pos = [(x-320*dx,y-320*dy),
               (x-170*dx,y-320*dy),
               (x-170*dx,y-370*dy),
               (x-370*dx,y-370*dy),
               (x-370*dx,y-170*dy),
               (x-320*dx,y-170*dy)]

        pygame.draw.polygon(screen, color, pos)

        return [x,y]
    
    def select():

        global select,last_big_selected_cell

        Draw.quarter_select(select[0],select[0])
        Draw.quarter_select(-select[0],select[0])
        Draw.quarter_select(select[0],-select[0])
        pos = Draw.quarter_select(-select[0],-select[0])

        pos[0] -= width // 2
        pos[1] -= height // 2

        select[1][0] /= 1.02
        select[1][1] /= 1.02

        if big_selected_cell == None:
            select[0] += 0.004
            if select[0] > 1:
                select[0] = 1
        else:
            select[0] -= 0.004
            if select[0] < 0.25:
                select[0] = 0.25
        
        if last_big_selected_cell != big_selected_cell:
            if big_selected_cell != None:
                for i in range(3):
                    if big_selected_cell >= 0+3*i and big_selected_cell <= 2+3*i:
                        select[2][1] = 200-200*i
                for i in range(3):
                    if big_selected_cell == 0+i or big_selected_cell == 3+i or big_selected_cell == 6+i:
                        select[2][0] = -200+200*i
            else:
                select[2][0] = 0
                select[2][1] = 0

            select[1][0] = pos[0] - select[2][0]
            select[1][1] = -pos[1] - select[2][1]

            last_big_selected_cell = big_selected_cell

    def circle(x,y,size):

        pygame.draw.circle(screen, colors[4], (x + width // 2,-y + height // 2), 20*(size+1))
        pygame.draw.circle(screen, colors[1], (x + width // 2,-y + height // 2), 15*(size+1))
    
    def cross(x,y,size):

        pygame.draw.line(screen, colors[5], (x + width // 2-13*(size+1), -y + height // 2-15*(size+1)), (x + width // 2+13*(size+1), -y + height // 2+15*(size+1)), 10)
        pygame.draw.line(screen, colors[5], (x + width // 2+13*(size+1), -y + height // 2-15*(size+1)), (x + width // 2-13*(size+1), -y + height // 2+15*(size+1)), 10)
    
    def bigcircle(x,y,size):

        pygame.draw.polygon(screen, colors[1], [((x-75+ width // 2),(-y-75+ height // 2)),
                                                ((x+75+ width // 2),(-y-75+ height // 2)),
                                                ((x+75+ width // 2),(-y+75+ height // 2)),
                                                ((x-75+ width // 2),(-y+75+ height // 2))])
        pygame.draw.circle(screen, colors[4], (x + width // 2,-y + height // 2), 75*(size+1))
        pygame.draw.circle(screen, colors[1], (x + width // 2,-y + height // 2), 56*(size+1))
    
    def bigcross(x,y,size):

        pygame.draw.polygon(screen, colors[1], [((x-75+ width // 2),(-y-75+ height // 2)),
                                                ((x+75+ width // 2),(-y-75+ height // 2)),
                                                ((x+75+ width // 2),(-y+75+ height // 2)),
                                                ((x-75+ width // 2),(-y+75+ height // 2))])
        pygame.draw.line(screen, colors[5], (x + width // 2-60*(size+1), -y + height // 2-75*(size+1)), (x + width // 2+60*(size+1), -y + height // 2+75*(size+1)), 40)
        pygame.draw.line(screen, colors[5], (x + width // 2+60*(size+1), -y + height // 2-75*(size+1)), (x + width // 2-60*(size+1), -y + height // 2+75*(size+1)), 40)
    
    def figures():

        global figuresizes

        for by in range(3):
            for bx in range(3):
                for y in range(3):
                    for x in range(3):
                        
                        if cells[bx+3*by][x+3*y] != None:
                            if cells[bx+3*by][x+3*y] == 0:
                                Draw.circle(-50+50*x-200+200*bx,50-50*y+200-200*by,figuresizes[bx+3*by][x+3*y])
                            if cells[bx+3*by][x+3*y] == 1:
                                Draw.cross(-50+50*x-200+200*bx,50-50*y+200-200*by,figuresizes[bx+3*by][x+3*y])
                            figuresizes[bx+3*by][x+3*y] /= 1.02
                            if figuresizes[bx+3*by][x+3*y] > 0:
                                figuresizes[bx+3*by][x+3*y] = 0
        Draw.bigfigures()
    
    def bigfigures():

        global bigfiguresizes

        for p in range(2):
            for y in range(3):
                for x in range(3):
                    if cells[x+3*y] == [p,p,p,p,p,p,p,p,p]:
                        if p == 0:
                            Draw.bigcircle(-200+200*x,200-200*y,bigfiguresizes[x+3*y])
                        if p == 1:
                            Draw.bigcross(-200+200*x,200-200*y,bigfiguresizes[x+3*y])
                        bigfiguresizes[x+3*y] /= 1.02
                        if bigfiguresizes[x+3*y] > 0:
                            bigfiguresizes[x+3*y] = 0

while True:

    screen.fill(colors[0])
    width, height = screen.get_size()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Получаем координаты нажатия
            x_mouse, y_mouse = event.pos
            Main.click(x_mouse,y_mouse)

    Draw.main()
    
    pygame.display.flip()
    pygame.time.Clock().tick(300)