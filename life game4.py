import pygame
import sys
import random

count_of_cells = [120,120]
zoom = 1
start_delay = 0

pygame.init()

width, height = 1000, 800
screen = pygame.display.set_mode((width, height),pygame.RESIZABLE)
pygame.display.set_caption("Life game")
clock = pygame.time.Clock()
pygame.mouse.set_visible(True)

shift = False
showInProcessCells = True
colors = [(10,10,10),(255,255,255),(119,221,119),(196,30,58)]
life = False
fullscreen = False
fps = 60
delay = start_delay
cells = []

for y in range(count_of_cells[1]+2):
    cells.append([])

    for x in range(count_of_cells[0]+2):
        cells[y].append(0)

for y in range(len(cells)):
    for x in range(len(cells[0])):
        if x == 0 or x == len(cells[0])-1 or y == 0 or y == len(cells)-1:
            pass
        else:
            cells[y][x] = random.randint(0,1)

class Draw:

    def main():

        screen.fill((0,0,0))
        Draw.cells()
    
    def cells():

        size = (20*zoom*len(cells)//2, 20*zoom*len(cells[0])//2)

        for y in range(len(cells)):
            for x in range(len(cells[0])):

                X = width//2 + 20*zoom*x - size[1]
                Y = height//2 + 20*zoom*y - size[0]

                pos = [(X-10*zoom,Y-10*zoom),(X+10*zoom,Y-10*zoom),(X+10*zoom,Y+10*zoom),(X-10*zoom,Y+10*zoom)]

                pygame.draw.polygon(screen, colors[cells[y][x]], pos)

class Life:

    def main():

        if showInProcessCells == True:
            arg = Life.check()
            if arg == False:
                Life.newlife()
                Life.kill()
            else:
                Life.clear()
        else:
            Life.newlife()
            Life.kill()
            Life.clear()
        
    
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
                        if alive == 3:
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
                        if alive != 3 and alive != 2:
                            cells[y][x] = 3
    
    def clear():

        global cells

        for y in range(len(cells)):
            for x in range(len(cells[0])):
                if cells[y][x] == 2:
                    cells[y][x] = 1
                elif cells[y][x] == 3:
                    cells[y][x] = 0
    
    def check():

        for y in range(len(cells)):
            for x in range(len(cells[0])):
                if cells[y][x] == 2 or cells[y][x] == 3:
                    return True
        return False

class User:

    def zoom():

        global zoom
        key = pygame.key.get_pressed()
        arg = 0.01
        if key[pygame.K_LSHIFT]:
            arg = 0.1

        if event.button == 4:  # Прокрутка вверх
            zoom -= arg
        elif event.button == 5:  # Прокрутка вниз
            zoom += arg

    def click(mouse_x,mouse_y):

        global cells

        size = (20*zoom*len(cells)//2, 20*zoom*len(cells[0])//2)

        for y in range(len(cells)):
            for x in range(len(cells[0])):

                X = width//2 + 20*zoom*x - size[1]
                Y = height//2 + 20*zoom*y - size[0]

                pos = [(X-10*zoom,Y-10*zoom),(X+10*zoom,Y+10*zoom)]

                if mouse_x > pos[0][0] and mouse_x < pos[1][0] and mouse_y > pos[0][1] and mouse_y < pos[1][1]:

                    if cells[y][x] == 0:
                        cells[y][x] = 1
                    
                    else:
                        cells[y][x] = 0
                    
                    return

    def keyboard():

        global shift

        if event.key == pygame.K_F11:
            User.Keyboard.f11fullscreen()
        
        if event.key == pygame.K_SPACE:
            User.Keyboard.stop()
        
        if event.key == pygame.K_LSHIFT:
            shift = True
        
        if event.key == pygame.K_q:
            User.Keyboard.reset()
        
        if event.key == pygame.K_r:
            User.Keyboard.random()

    class Keyboard:

        def f11fullscreen():

            global fullscreen,screen, width, height

            if fullscreen == False:
                fullscreen = True
                screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

            else:
                fullscreen = False
                screen = pygame.display.set_mode((width, height),pygame.RESIZABLE)
        
        def reset():

            global cells

            for y in range(len(cells)):
                for x in range(len(cells[0])):
                    cells[y][x] = 0
        
        def random():

            global cells

            for y in range(len(cells)):
                for x in range(len(cells[0])):
                    if x == 0 or x == len(cells[0])-1 or y == 0 or y == len(cells)-1:
                        pass
                    else:
                        cells[y][x] = random.randint(0,1)

        
        def stop():

            global life

            if life == True:
                life = False
            else:
                life = True


while True:

    width, height = screen.get_size()
    fps = clock.get_fps()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            User.keyboard()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            User.zoom()
            if event.button == 1:
                x, y = event.pos
                User.click(x,y)

    Draw.main()

    if life == True:

        if delay <= 0:

            Life.main()
            delay = start_delay
        
        else:
            if fps == 0:
                fps = 60
            delay -= 1/fps
            
    pygame.display.flip()
    clock.tick(60)

    shift = False