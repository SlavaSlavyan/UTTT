import pygame

class Game:

    def __init__(self,m,d):
        
        self.colors = d.colors[m.config['them']]['game']
        self.offset = []
        for i in range(12):
            self.offset.append(200*(i+1))
        self.selectsize = 1
        self.selectpos = [0,0]
        self.selectoffset = [0,0]
        self.selectcolor = m.Game.player * (len(self.colors["0toX"])-1)
        self.cellscolor = [0,0,0,0,0,0,0,0,0]
        self.smallfiguresizes = []
        for i in range(9):
            self.smallfiguresizes.append([])
            for j in range(9):
                self.smallfiguresizes[i].append(0)
        self.lastselectedcell = None

    def start(self,m):

        m.screen.fill(self.colors['bg'])
        self.cube(m)
        self.bigcells(m)
        self.smallcells(m)
        self.select(m)

        self.offset = [i/1.1 for i in self.offset]

        if round(self.offset[6],2) == 0 or m.status == 'game':
            m.Disp.anim = 'game'
            m.status = 'game'

    def main(self,m):

        self.start(m)
        self.smallfigures(m)
        self.offset = [i/1.3 for i in self.offset]

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
                
                if m.Game.selected_cell == 3*Y+X:
                    self.cellscolor[3*Y+X] += 1
                    if self.cellscolor[3*Y+X] == len(self.colors['active-passive']):
                        self.cellscolor[3*Y+X] = len(self.colors['active-passive'])-1
                else:
                    self.cellscolor[3*Y+X] -= 1
                    if self.cellscolor[3*Y+X] == -1:
                        self.cellscolor[3*Y+X] = 0

                pygame.draw.line(m.screen, self.colors['active-passive'][self.cellscolor[3*Y+X]], (x-75*z, y-25*z), (x+75*z, y-25*z), round(3*m.config['zoom']))
                pygame.draw.line(m.screen, self.colors['active-passive'][self.cellscolor[3*Y+X]], (x-75*z, y+25*z), (x+75*z, y+25*z), round(3*m.config['zoom']))
                pygame.draw.line(m.screen, self.colors['active-passive'][self.cellscolor[3*Y+X]], (x-25*z, y-75*z), (x-25*z, y+75*z), round(3*m.config['zoom']))
                pygame.draw.line(m.screen, self.colors['active-passive'][self.cellscolor[3*Y+X]], (x+25*z, y-75*z), (x+25*z, y+75*z), round(3*m.config['zoom']))
    
    def select(self,m):

        z = (self.offset[11]+self.selectsize)*m.config['zoom']
        x = m.width//2+m.Disp.offset[0] + self.selectpos[0]*m.config['zoom'] + self.selectoffset[0]*m.config['zoom']
        y = m.height//2-m.Disp.offset[1] - self.selectpos[1]*m.config['zoom'] - self.selectoffset[1]*m.config['zoom']

        if m.Game.player == 0:
            self.selectcolor -= 1
            if self.selectcolor == -1:
                self.selectcolor = 0

        elif m.Game.player == 1:
            self.selectcolor += 1
            if self.selectcolor == len(self.colors["0toX"]):
                self.selectcolor = len(self.colors["0toX"])-1
        
        for X in range(-1,2,2):

            for Y in range(-1,2,2):

                pos = [[x-320*X*z,y+320*Y*z],[x-170*X*z,y+320*Y*z],[x-170*X*z,y+370*Y*z],[x-370*X*z,y+370*Y*z],[x-370*X*z,y+170*Y*z],[x-320*X*z,y+170*Y*z]]
                pygame.draw.polygon(m.screen, self.colors["0toX"][self.selectcolor], pos)
        
        if m.Game.selected_cell != None:

            self.selectsize -= 0.03
            if self.selectsize < 0.25:
                self.selectsize = 0.25

        else:

            self.selectsize += 0.03
            if self.selectsize > 1:
                self.selectsize = 1
        
        if self.lastselectedcell != m.Game.selected_cell:

            self.lastselectedcell = m.Game.selected_cell
            now = []
            for i in range(2):
                now.append(self.selectoffset[i] + self.selectpos[i])

            if m.Game.selected_cell == None:
                self.selectpos = [0,0]
            else:
                for X in range(3):
                    for Y in range(3):
                        if 3*Y+X == m.Game.selected_cell:
                            self.selectpos = [200*(X-1),-200*(Y-1)]
            
            self.selectoffset[0] = now[0] - self.selectpos[0]
            self.selectoffset[1] = now[1] - self.selectpos[1]
        
        self.selectoffset = [i/1.1 for i in self.selectoffset]
    
    def smallfigures(self,m):

        z = m.config['zoom']
        x = m.width//2+m.Disp.offset[0]
        y = m.height//2-m.Disp.offset[1]
        
        for X in range(3):
            for Y in range(3):
                for xX in range(3):
                    for yY in range(3):
                        if m.Game.cells[3*Y+X][3*yY+xX] == 0:

                            pos = (x+200*z*(X-1)+50*z*(xX-1),y+200*z*(Y-1)+50*z*(yY-1))
                            pygame.draw.circle(m.screen, self.colors['player0'], pos, 20*z*self.smallfiguresizes[3*Y+X][3*yY+xX])
                            pygame.draw.circle(m.screen, self.colors['darkbg'], pos, 15*z*self.smallfiguresizes[3*Y+X][3*yY+xX])

                            if self.smallfiguresizes[3*Y+X][3*yY+xX] < 1:
                                self.smallfiguresizes[3*Y+X][3*yY+xX] += 0.05

                        elif m.Game.cells[3*Y+X][3*yY+xX] == 1:

                            offset = (x+200*z*(X-1)+50*z*(xX-1),y+200*z*(Y-1)+50*z*(yY-1))
                            pos = [[0,-37.5],[37.5,-75],[75,-37.5],
                                   [37.5,0],[75,37.5],[37.5,75],
                                   [0,37.5],[-37.5,75],[-75,37.5],
                                   [-37.5,0],[-75,-37.5],[-37.5,-75]]
                            for i in pos:
                                for j in range(2):
                                    i[j] = i[j]*z*0.25*self.smallfiguresizes[3*Y+X][3*yY+xX]+offset[j]
                            
                            pygame.draw.polygon(m.screen, self.colors['playerX'], pos)

                            if self.smallfiguresizes[3*Y+X][3*yY+xX] < 1:
                                self.smallfiguresizes[3*Y+X][3*yY+xX] += 0.05
                            