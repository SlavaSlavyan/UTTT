from function.endfunc import *

class DisplayGame:

    def __init__(self,var):
        
        self.ratio = [var.width//100,var.height//100]
        self.offset = []
        for i in range(11):
            self.offset.append(100*(i+1))
    
    def main(self,var):

        var.screen.fill(var.colors['bg_gray'])

        DisplayGame.bg_cells(self,var)
        DisplayGame.big_cells(self,var)
        DisplayGame.small_cells(self,var)

        return var

    def start(self,var):

        var.screen.fill(var.colors['bg_gray'])

        DisplayGame.bg_cells(self,var)
        DisplayGame.big_cells(self,var)
        DisplayGame.small_cells(self,var)

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