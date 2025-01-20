import pygame
import copy

class WorkSpace:

    def __init__(self,m):
        
        self.zoom = 1
        self.offset = [0,0]
        self.last_offset = self.offset

    def main(self,m):

        m.screen.fill((40, 44, 52))

        WorkSpace.print_figure(self,m)

        return m

    def print_figure(self,m):

        for figure in m.WS.figures:

            if figure['type'] == "line":
                pos = copy.deepcopy(figure['pos'])
                for dot in range(len(pos)):
                    for i in range(len(pos[dot])):
                        pos[dot][i] = eval(str(pos[dot][i]))*self.zoom
                        if i == 1:
                            pos[dot][i] = -pos[dot][i]
                    if "settings" in figure:
                        if 'align' in figure['settings']:
                            if figure['settings']['align'] == 'center':
                                pos[dot][0] += m.width//2
                                pos[dot][1] += m.height//2
                pygame.draw.line(m.screen, figure['color'], pos[0] , pos[1], round(figure['size']*self.zoom))