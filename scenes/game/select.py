import pygame

class Select:

    def __init__(self,mainself):

        self.select_points = [[0,0],[3,0],[3,-1],[-1,-1],[-1,3],[0,3]]
        self.size = 1

        self.end_pos = [0,0]
        self.offset = [0,0]

        self.last_selected_cell = None

    def main(self,mainself):

        z = mainself.Display.zoom

        parts = []
        
        for Y in range(-1,2,2):
            for X in range(-1,2,2):

                parts.append([])

                for point in self.select_points:

                    x = mainself.Display.width//2 - 320*z*X*self.size + point[0]*X * 50*z*self.size + self.end_pos[0]*200*z + self.offset[0]*200*z
                    y = mainself.Display.height//2 - 320*z*Y*self.size + point[1]*Y * 50*z*self.size + self.end_pos[1]*200*z + self.offset[1]*200*z

                    parts[-1].append((x,y))

        for part in parts:
            pygame.draw.polygon(mainself.Display.screen,mainself.Display.colors[6],part)

        for i in range(2):
            self.offset[i] /= 1 + 0.1 * mainself.Display.speed
        
        self.logic(mainself)
    
    def logic(self,mainself):

        self.zoom(mainself)
        self.new_end_pos(mainself)
    
    def zoom(self,mainself):

        if mainself.Scenes.game.Logic.selected_cell == None:

            if self.size < 1:
                self.size += 0.025 * mainself.Display.speed
            if self.size > 1:
                self.size = 1
        
        else:

            if self.size > 0.25:
                self.size -= 0.025 * mainself.Display.speed
            if self.size < 0.25:
                self.size = 0.25
    
    def new_end_pos(self,mainself):

        if self.last_selected_cell != mainself.Scenes.game.Logic.selected_cell:

            pos = [0,0]
            
            for i in range(2):
                pos[i] = self.offset[i] + self.end_pos[i]

            if mainself.Scenes.game.Logic.selected_cell == None:
                self.end_pos = [0,0]

            else:

                for x in range(3):
                    for y in range(3):

                        if y*3+x == mainself.Scenes.game.Logic.selected_cell:
                            self.end_pos = [x-1,y-1]

            for i in range(2):
                self.offset[i] = pos[i] - self.end_pos[i]

            self.last_selected_cell = mainself.Scenes.game.Logic.selected_cell