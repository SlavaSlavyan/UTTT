import pygame


class Game:

    def __init__(self,m):
        
        self.player = 0
        self.selected_cell = None
        self.x = int
        self.y = int
        self.cells = []
        for i in range(9):
            self.cells.append([])
            for j in range(9):
                self.cells[i].append(None)
        self.memory = []
        self.timer = {'tick':0,'seconds':0,'minutes':0}
        self.win = None

    def main(self,m):

        z = m.config['zoom']
        self.x = round((m.Disp.mouse_pos[0] - m.width//2 - m.Disp.offset[0])/z)
        self.y = round((-m.Disp.mouse_pos[1] + m.height//2 - m.Disp.offset[1])/z)

        if self.selected_cell == None:
            self.checkselectedbigcell(m,self.selectbigcell(m))
        
        else:
            self.checkselectedsmallcell(m,self.selectsmallcell(m))

    def selectbigcell(self,m):

        for x in range(3):
            for y in range(3):
                if self.x < -100+200*x and self.x > -300+200*x and self.y < 300-200*y and self.y > 100-200*y:
                    return 3*y+x
        
        return None

    def checkselectedbigcell(self,m,cell):

        if cell != None and None in self.cells[cell]:
            self.memory.append([f'self.selected_cell = {self.selected_cell}'])
            self.selected_cell = cell
    
    def selectsmallcell(self,m):

        for X in range(3):
            for Y in range(3):
                if 3*Y+X == self.selected_cell:
                    offset = [X-1,Y-1]
        X,Y = offset

        for x in range(3):
            for y in range(3):
                if self.x < -25+50*x+200*X and self.x > -75+50*x+200*X and self.y < 75-50*y-200*Y and self.y > 25-50*y-200*Y:
                    return 3*y+x
        
        return None
    
    def checkselectedsmallcell(self,m,cell):

        if cell != None and self.cells[self.selected_cell][cell] == None:
            self.memory.append([f'self.cells[{self.selected_cell}] = {self.cells[self.selected_cell]}',
                                f'self.selected_cell = {self.selected_cell}',
                                f'self.player = {self.player}'])
            self.cells[self.selected_cell][cell] = self.player
            self.capture(m)
            self.nextcell(m,cell)

            if self.player == 0:
                self.player = 1
            else:
                self.player = 0
    
    def nextcell(self,m,cell):

        if None in self.cells[cell]:
            self.selected_cell = cell
        else:
            self.selected_cell = None
    
    def capture(self,m):

        capture = False

        for p in range(2):

            for i in range(3):

                if self.cells[self.selected_cell][0+3*i] == p and self.cells[self.selected_cell][1+3*i] == p and self.cells[self.selected_cell][2+3*i] == p:
                    self.cells[self.selected_cell] = [p,p,p,p,p,p,p,p,p]
                    capture = True
                    break

                if self.cells[self.selected_cell][0+i] == p and self.cells[self.selected_cell][3+i] == p and self.cells[self.selected_cell][6+i] == p:
                    self.cells[self.selected_cell] = [p,p,p,p,p,p,p,p,p]
                    capture = True
                    break

            if self.cells[self.selected_cell][0] == p and self.cells[self.selected_cell][4] == p and self.cells[self.selected_cell][8] == p:
                self.cells[self.selected_cell] = [p,p,p,p,p,p,p,p,p]
                capture = True

            elif self.cells[self.selected_cell][2] == p and self.cells[self.selected_cell][4] == p and self.cells[self.selected_cell][6] == p:
                self.cells[self.selected_cell] = [p,p,p,p,p,p,p,p,p]
                capture = True
    
        if capture:
            if self.wincheck(m) != None:
                self.win = self.wincheck(m)
                m.Disp.anim = 'game_end'
                m.status = 'loading'

    def loadsave(self,m):

        try:
            for i in self.memory[-1]:
                exec(i)
            self.memory = self.memory[:-1]
        except:
            pass

    def wincheck(self,m):

        win = None

        for p in range(2):

            for i in range(3):

                if self.cells[0+3*i] == [p,p,p,p,p,p,p,p,p] and self.cells[1+3*i] == [p,p,p,p,p,p,p,p,p] and self.cells[2+3*i] == [p,p,p,p,p,p,p,p,p]:
                    win = p
                    break

                if self.cells[0+i] == [p,p,p,p,p,p,p,p,p] and self.cells[3+i] == [p,p,p,p,p,p,p,p,p] and self.cells[6+i] == [p,p,p,p,p,p,p,p,p]:
                    win = p
                    break

            if self.cells[0] == [p,p,p,p,p,p,p,p,p] and self.cells[4] == [p,p,p,p,p,p,p,p,p] and self.cells[8] == [p,p,p,p,p,p,p,p,p]:
                win = p

            elif self.cells[2] == [p,p,p,p,p,p,p,p,p] and self.cells[4] == [p,p,p,p,p,p,p,p,p] and self.cells[6] == [p,p,p,p,p,p,p,p,p]:
                win = p
        
        return win
