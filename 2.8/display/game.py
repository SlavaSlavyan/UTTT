import pygame

class Game:

    def __init__(self,m,d):
        
        self.colors = d.colors[m.config['them']]['game']
        self.offset = []
        for i in range(12):
            self.offset.append(200*(i+1))
        self.selectsize = 1
        self.selectpos = [0,0]

    def start(self,m):

        m.screen.fill(self.colors['bg'])
        self.cube(m)
        self.bigcells(m)
        self.smallcells(m)
        self.select(m)

        self.offset = [i/1.1 for i in self.offset]

    def main(self,m):

        pass

    def cube(self,m):

        z = m.config['zoom']
        x = m.width//2+m.Disp.offset[0]
        y = m.height//2-m.Disp.offset[1] + self.offset[0]*m.Disp.ratio[1]

        
        pos = [(x-300*z,y+300*z),(x+300*z,y+300*z),(x+300*z,y-300*z),(x-300*z,y-300*z)]

        pygame.draw.polygon(m.screen, self.colors['darkbg'], pos)
    
    def bigcells(self,m):

        z = m.config['zoom']
        x = m.width//2+m.Disp.offset[0]
        y = m.height//2-m.Disp.offset[1] - self.offset[1]*m.Disp.ratio[1]
        
        pygame.draw.line(m.screen, self.colors['activecell'], (x-300*z, y-100*z), (x+300*z, y-100*z), round(5*z))
        pygame.draw.line(m.screen, self.colors['activecell'], (x-300*z, y+100*z), (x+300*z, y+100*z), round(5*z))
        pygame.draw.line(m.screen, self.colors['activecell'], (x-100*z, y-300*z), (x-100*z, y+300*z), round(5*z))
        pygame.draw.line(m.screen, self.colors['activecell'], (x+100*z, y-300*z), (x+100*z, y+300*z), round(5*z))

    def smallcells(self,m):

        for X in range(3):
            
            for Y in range(3):
                
                if 3*Y+X != 4:

                    z = m.config['zoom']
                    x = m.width//2+m.Disp.offset[0] + 200*z*(X-1) + self.offset[3*Y+X+2]*m.Disp.ratio[0]*(X-1)
                    y = m.height//2-m.Disp.offset[1] + 200*z*(Y-1) + self.offset[3*Y+X+2]*m.Disp.ratio[1]*(Y-1)
                
                else:

                    z = abs(self.offset[6]/1400-1)*m.config['zoom']
                    self.offset[6] *= 1.05
                    x = m.width//2+m.Disp.offset[0]
                    y = m.height//2-m.Disp.offset[1]

                pygame.draw.line(m.screen, self.colors['passivecell'], (x-75*z, y-25*z), (x+75*z, y-25*z), round(3*m.config['zoom']))
                pygame.draw.line(m.screen, self.colors['passivecell'], (x-75*z, y+25*z), (x+75*z, y+25*z), round(3*m.config['zoom']))
                pygame.draw.line(m.screen, self.colors['passivecell'], (x-25*z, y-75*z), (x-25*z, y+75*z), round(3*m.config['zoom']))
                pygame.draw.line(m.screen, self.colors['passivecell'], (x+25*z, y-75*z), (x+25*z, y+75*z), round(3*m.config['zoom']))
    
    def select(self,m):

        z = (self.offset[11]+self.selectsize)*m.config['zoom']
        x = m.width//2+m.Disp.offset[0] + self.selectpos[0]*z
        y = m.height//2-m.Disp.offset[1] + self.selectpos[0]*z
        
        for X in range(-1,2,2):
            for Y in range(-1,2,2):

                pos = [[x-320*X*z,y+320*Y*z],[x-170*X*z,y+320*Y*z],[x-170*X*z,y+370*Y*z],[x-370*X*z,y+370*Y*z],[x-370*X*z,y+170*Y*z],[x-320*X*z,y+170*Y*z]]
                pygame.draw.polygon(m.screen, self.colors['player0'], pos)
        
        if m.Game.selected_cell != None:
            self.selectsize -= 0.03
            if self.selectsize < 0.25:
                self.selectsize = 0.25
        else:
            self.selectsize += 0.03
            if self.selectsize > 1:
                self.selectsize = 1