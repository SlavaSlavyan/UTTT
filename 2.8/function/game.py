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

    def main(self,m):

        z = m.config['zoom']
        self.x = round((m.Disp.mouse_pos[0] - m.width//2 - m.Disp.offset[0])/z)
        self.y = round((-m.Disp.mouse_pos[1] + m.height//2 - m.Disp.offset[1])/z)

        self.selected_cell = self.selectbigcell(m)

    def selectbigcell(self,m):

        for x in range(3):
            for y in range(3):
                if self.x < -100+200*x and self.x > -300+200*x and self.y < 300-200*y and self.y > 100-200*y:
                    return 3*y+x
        
        return None