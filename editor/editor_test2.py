import pygame
import sys
import json

pygame.init()
width, height = 1200, 800
screen = pygame.display.set_mode((width, height),pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.display.set_caption("editor 1.2 dev")

selected_file = 'test2'
autoload = True
error = True
zoom = 1

def load(path):

    try:
        with open(f'{path}.json', 'r', encoding='utf-8') as file:

            data = json.load(file)
            return data,False

    except:
        return [],True
    
figures,error = load(selected_file)

def print_figure(figures_input):

    figures = figures_input.copy()

    try:

        for f in figures:

            if f['type'] == 'line':
                for pos_num in range(len(f['pos'])):
                    for cord in range(len(f['pos'][pos_num])):
                        if isinstance(f['pos'][pos_num][cord],str):
                            f['pos'][pos_num][cord] = eval(f['pos'][pos_num][cord])*zoom
                f['size'] *= zoom            

                if 'config' in f:

                    if 'zoomable' in f['config']:
                        if f['config']['zoomable'] == False:
                            for pos_num in range(len(f['pos'])):
                                for cord in range(len(f['pos'][pos_num])):
                                    f['pos'][pos_num][cord] /= zoom
                            f['size'] /= zoom

                    
                    if 'align' in f['config']:
                        if f['config']['align'] == 'center':
                            for pos_num in range(len(f['pos'])):
                                for cord in range(len(f['pos'][pos_num])):
                                    if cord == 0:
                                        f['pos'][pos_num][cord] += width//2
                                    else:
                                        f['pos'][pos_num][cord] = -f['pos'][pos_num][cord]
                                        f['pos'][pos_num][cord] += height//2

                pygame.draw.line(screen, (255,255,255), f['pos'][0] , f['pos'][1], round(f['size']))
    except:
        pass

while True:

    screen.fill((40, 44, 52))
    width, height = screen.get_size()

    if autoload == True:
        figures,error = load(selected_file)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
                
            if event.button == 4:
                zoom += 0.1

            elif event.button == 5:
                zoom -= 0.1

            elif event.button == 2:
                zoom = 1
    
    print_figure(figures)

    pygame.display.flip()

    clock.tick(3000)
    #print(int(clock.get_fps()))