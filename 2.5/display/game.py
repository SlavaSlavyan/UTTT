from function.endfunc import *

class DisplayGame:

    def __init__(self,var):
        
        self.ratio = [var.width//100,var.height//100]
        self.offset = []
        for i in range(11):
            self.offset.append(100*(i+1))
        self.select_size = 10
        self.last_selected_big_cell = var.game.big_celected_cell
        self.select_pos = [0,0]
        self.select_offset = [0,0]
    
    def main(self,var):

        var.screen.fill(var.colors['bg_gray'])

        DisplayGame.bg_cells(self,var)
        DisplayGame.big_cells(self,var)
        DisplayGame.small_cells(self,var)

        DisplayGame.select(self,var)

        return var

    def start(self,var):

        var.screen.fill(var.colors['bg_gray'])

        DisplayGame.bg_cells(self,var)
        DisplayGame.big_cells(self,var)
        DisplayGame.small_cells(self,var)
        DisplayGame.select(self,var)

        self.offset = [i/1.09 for i in self.offset]

        if self.offset[-1] <= 0.1:
            var.anim = 'game'
            var.status = 'game'
            self.offset = [i*0 for i in self.offset]

        return var
    
    def bg_cells(self,var):

        z = var.zoom
        x = var.width//2
        y = var.height//2 + self.offset[0]*z*self.ratio[1]

        pos = [(x-300*z,y+300*z),(x+300*z,y+300*z),(x+300*z,y-300*z),(x-300*z,y-300*z)]
        
        pygame.draw.polygon(var.screen, var.colors['bg_darkgray'], pos)
    
    def big_cells(self,var):

        z = var.zoom
        x = var.width//2 
        y = var.height//2 - self.offset[1]*z*self.ratio[1]

        pygame.draw.line(var.screen, var.colors['lightgray'], (x-300*z, y-100*z), (x+300*z, y-100*z), round(5*z))
        pygame.draw.line(var.screen, var.colors['lightgray'], (x-300*z, y+100*z), (x+300*z, y+100*z), round(5*z))
        pygame.draw.line(var.screen, var.colors['lightgray'], (x-100*z, y-300*z), (x-100*z, y+300*z), round(5*z))
        pygame.draw.line(var.screen, var.colors['lightgray'], (x+100*z, y-300*z), (x+100*z, y+300*z), round(5*z))
    
    def small_cells(self,var):

        for y in range(3):
            for x in range(3):
                DisplayGame.small_cell(self,var,-200+200*x,-200+200*y,x,y)
        
    def small_cell(self,var,endposX,endposY,offsetX,offsetY):

        z = var.zoom
        if offsetX == 1 and offsetY == 1:
            offsetY = 0
        x = var.width//2 + self.offset[3*offsetY+offsetX+2]*z*self.ratio[0]*(offsetX-1) + endposX*z
        y = var.height//2 + self.offset[3*offsetY+offsetX+2]*z*self.ratio[1]*(offsetY-1) + endposY*z

        pygame.draw.line(var.screen, var.colors['lightgray'], (x-75*z, y-25*z), (x+75*z, y-25*z), round(3*z))
        pygame.draw.line(var.screen, var.colors['lightgray'], (x-75*z, y+25*z), (x+75*z, y+25*z), round(3*z))
        pygame.draw.line(var.screen, var.colors['lightgray'], (x-25*z, y-75*z), (x-25*z, y+75*z), round(3*z))
        pygame.draw.line(var.screen, var.colors['lightgray'], (x+25*z, y-75*z), (x+25*z, y+75*z), round(3*z))
    
    def select(self,var):
            
        z = self.select_size*var.zoom

        if var.anim == 'game':
            if var.game.big_celected_cell == None:
                self.select_size += 0.02
                if self.select_size > 1:
                    self.select_size = 1
            else:
                self.select_size -= 0.02
                if self.select_size < 0.25:
                    self.select_size = 0.25
        else:
            self.select_size = ((self.select_size-1)/1.1)+1

        x = var.width//2 + self.select_pos[0]*var.zoom + self.select_offset[0]*var.zoom
        y = var.height//2 - self.select_pos[1]*var.zoom - self.select_offset[1]*var.zoom

        if var.game.big_celected_cell != self.last_selected_big_cell:
            self.last_selected_big_cell = var.game.big_celected_cell
            last_selected_pos = self.select_pos
            if var.game.big_celected_cell != None:
                for Y in range(3):
                    for X in range(3):
                        if var.game.big_celected_cell == 3*Y+X: 
                            self.select_pos = [-200+200*X,200-200*Y]
            else:
                self.select_pos = [0,0]
            self.select_offset = [self.select_offset[0]+last_selected_pos[0]-self.select_pos[0],self.select_offset[1]+last_selected_pos[1]-self.select_pos[1]]


        if var.game.player == 0:
            color = var.colors['blue']
        elif var.game.player == 1:
            color = var.colors['orange']
        else:
            color = var.colors['yellow']
        
        X = (-1,1)
        Y = (-1,1)

        pos = []

        for Yy in range(2):
            for Xx in range(2):
                pos.append([(x-320*z*X[Xx],y-320*z*Y[Yy]),(x-170*z*X[Xx],y-320*z*Y[Yy]),(x-170*z*X[Xx],y-370*z*Y[Yy]),(x-370*z*X[Xx],y-370*z*Y[Yy]),(x-370*z*X[Xx],y-170*z*Y[Yy]),(x-320*z*X[Xx],y-170*z*Y[Yy])])

        for i in range(4):
            pygame.draw.polygon(var.screen, color, pos[i])
        
        self.select_offset = [i / 1.1 for i in self.select_offset]