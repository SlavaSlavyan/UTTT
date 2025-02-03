import pygame

class Game:

    def __init__(self,m,d):
        
        self.colors = d.colors[m.config['them']]['game']
        self.offset = []
        for i in range(1):
            self.offset.append(200*(i+1))

    def start(self,m):

        m.screen.fill(self.colors['bg'])
        self.cube(m)

        self.offset = [i/1.1 for i in self.offset]

    def main(self,m):

        pass

    def cube(self,m):

        z = m.config['zoom']
        x = m.width//2+m.Disp.offset[0]
        y = m.height//2-m.Disp.offset[1] + self.offset[0]*m.Disp.ratio[1]

        
        pos = [(x-300*z,y+300*z),(x+300*z,y+300*z),(x+300*z,y-300*z),(x-300*z,y-300*z)]

        pygame.draw.polygon(m.screen, self.colors['darkbg'], pos)
    