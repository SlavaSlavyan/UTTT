import pygame
import sys
import time

pygame.init()

width, height = 1000, 800
screen = pygame.display.set_mode((width, height),pygame.RESIZABLE)
pygame.display.set_caption("main test")

colors = [(40,44,52),(33,37,43),(171,178,191),(120,127,138),(68,163,239),(209,154,102)]

big_selected_cell = None
last_big_selected_cell = None
player = 0
cells = [[],[],[],[],[],[],[],[],[]]
for n in range(9):
    for i in range(9):
        cells[n].append(None)
for i in range(len(cells)):
    print(cells[i])

select = [0,[0,0],[0,0]] #0 size #1 offset #2 pos

def main(x,y):

    global big_selected_cell

    x = x - width // 2
    y = -(y - height //2)

    if big_selected_cell == None:
        big_selected_cell = check_big_selected_cell(x,y,big_selected_cell)

    else:
        pass

def check_big_selected_cell(x,y,last):

    selected_cell = 0

    for n in range(3):
        for i in range(3):
            if x > -300+200*i and x < -100+200*i and y > 100-200*n and y < 300-200*n:
                selected_cell = i+3*n
                return selected_cell
    
    return last

def check_small_selected_cell(x,y):

    global big_selected_cell

    selected_cell = 0

    for n in range(3):
        for i in range(3):
            if x > -75+50*i and x < -25+50*i and y > 100-200*n and y < 300-200*n:
                selected_cell = i+3*n
                return selected_cell
    

class Draw:

    def main():

        Draw.bgcells()
        Draw.cells()
        Draw.circles()
    
    def bgcells():

        x = width//2
        y = height//2

        pygame.draw.polygon(screen, colors[1], [(x-300,y+300),(x+300,y+300),(x+300,y-300),(x-300,y-300)])

    def cells():

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

        pos = [(x-320*dx,y-320*dy),(x-170*dx,y-320*dy),(x-170*dx,y-370*dy),(x-370*dx,y-370*dy),(x-370*dx,y-170*dy),(x-320*dx,y-170*dy)]

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

        select[1][0] /= 1.03
        select[1][1] /= 1.03

        if big_selected_cell == None:
            select[0] += 0.006
            if select[0] > 1:
                select[0] = 1
        else:
            select[0] -= 0.006
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
    #Draw.circle(-50+50*x-200+200*bx,50-50*y+200-200*by,1)
    def circles():

        for by in range(3):
            for bx in range(3):
                for y in range(3):
                    for x in range(3):

                        if cells[bx+3*by][x+3*y] == 0:
                            Draw.circle(-50+50*x-200+200*bx,50-50*y+200-200*by,1)
    
    def circle(x,y,size):
        
        pygame.draw.circle(screen, colors[4], (x + width // 2, height // 2 - y), 20*size)
        pygame.draw.circle(screen, colors[1], (x + width // 2, height // 2 - y), 15*size)


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
            main(x_mouse,y_mouse)

    Draw.main()
    
    pygame.display.flip()
    pygame.time.Clock().tick(300)