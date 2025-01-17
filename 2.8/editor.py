import pygame
import sys
import json

pygame.init()
width, height = 1200, 800
screen = pygame.display.set_mode((width, height),pygame.RESIZABLE)
pygame.display.set_caption("DEV")
zoom = 1
offset = [0,0]
selected_file = "test"
autoload = True

def load(path):
    with open(f'{path}.json', 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
            return data
        except:
            pass
    

def display(pos):

    if autoload:
        global MainPOS
        MainPOS = load(selected_file)

    try:
        for vizual_object in pos:
            try:
                if vizual_object['type'] == 'line':
                    newpos = [[int,int],[int,int]]
                    for i in range(2):
                        newpos[i][0] = vizual_object['pos'][i][0]*zoom + offset[0]
                        newpos[i][1] = -vizual_object['pos'][i][1]*zoom - offset[1]
                        if vizual_object['cord_system'] == 'center':
                            newpos[i][0] += width//2
                            newpos[i][1] += height//2
                    pygame.draw.line(screen, vizual_object['color'], newpos[0] , newpos[1], round(vizual_object['size']*zoom))
            except:
                pass
    except:
        pass
MainPOS = load(selected_file)

while True:

    screen.fill((40, 44, 52))
    width, height = screen.get_size()

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
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F6:
                MainPOS = load(selected_file)


    display(MainPOS)
    
    pygame.display.flip()