import pygame
import math

class Figures:

    def __init__(self,mainself):
        
        self.figures_sizes = []

        for i in range(9):
            self.figures_sizes.append([])
            
            for j in range(9):
                self.figures_sizes[-1].append(0)
        
        self.big_figures_sizes = []

        for i in range(9): 
            self.big_figures_sizes.append(0)

        self.circle_gradient = mainself.Display.gradient(7,3,100)
        self.cross_gradient = mainself.Display.gradient(8,3,100)
        self.select_gradient = mainself.Display.gradient(5,3,100)

        self.cross_points = [[0,0],[1,0],[2,1],[1,2],[0,1],
                             [0,0],[-1,0],[-2,1],[-1,2],[0,1],
                             [0,0],[-1,0],[-2,-1],[-1,-2],[0,-1],
                             [0,0],[1,0],[2,-1],[1,-2],[0,-1]]

        self.counter = 0

    def main(self,mainself):

        self.fantom_logic(mainself)
        self.small_figures(mainself)

        self.counter += 0.1*mainself.Display.speed

    def circle(self,mainself, pos: tuple, color: int = 0, size: float = 0.25):

        z = mainself.Display.zoom
        
        x = pos[0]*z + mainself.Display.width//2
        y = -pos[1]*z + mainself.Display.height//2
        
        pygame.draw.circle(mainself.Display.screen,self.circle_gradient[color],(x,y),75*z*size)
        pygame.draw.circle(mainself.Display.screen,mainself.Display.colors[3],(x,y),55*z*size)
    
    def cross(self,mainself, pos: tuple, color: int = 0, size: float = 0.25):
        
        z = mainself.Display.zoom

        points = []

        for point in self.cross_points:

            x = mainself.Display.width//2 + point[0]*37*z*size + pos[0]*z
            y = mainself.Display.height//2 + point[1]*37*z*size - pos[1]*z

            points.append((x,y))

        pygame.draw.polygon(mainself.Display.screen,self.cross_gradient[color],points)

    def small_figures(self,mainself):

        z = mainself.Display.zoom

        for Y in range(3):
            for X in range(3):

                for y in range(3):
                    for x in range(3):

                        size = self.small_figures_logic(mainself,Y*3+X,y*3+x)/100

                        if self.figures_sizes[Y*3+X][y*3+x] != 0:
                            x_pos = 200*(X-1) + 50*(x-1)
                            y_pos = -200*(Y-1) - 50*(y-1)

                        if self.figures_sizes[Y*3+X][y*3+x] > 0:
                            self.circle(mainself,(x_pos,y_pos),size=0.25*size)
                        
                        if self.figures_sizes[Y*3+X][y*3+x] < 0:
                            self.cross(mainself,(x_pos,y_pos),size=0.25*size)
                
                #########################################################################

                size = self.big_figures_logic(mainself,Y*3+X)/100

                if self.big_figures_sizes[Y*3+X] != 0:
                    x_pos = 200*(X-1)
                    y_pos = -200*(Y-1)

                if self.big_figures_sizes[Y*3+X] > 0:
                    self.circle(mainself,(x_pos,y_pos),size=1*size)
                        
                if self.big_figures_sizes[Y*3+X] < 0:
                    self.cross(mainself,(x_pos,y_pos),size=1*size)

    def small_figures_logic(self,mainself, big_cell: int, small_cell: int) -> int:

        if mainself.Scenes.game.Logic.Game.cells[big_cell][small_cell] == None or None not in mainself.Scenes.game.Logic.Game.cells[big_cell] and 0 not in mainself.Scenes.game.Logic.Game.cells[big_cell] or None not in mainself.Scenes.game.Logic.Game.cells[big_cell] and 1 not in mainself.Scenes.game.Logic.Game.cells[big_cell]:
                            
            if self.figures_sizes[big_cell][small_cell] > 0:

                self.figures_sizes[big_cell][small_cell] -= 4*mainself.Display.speed

                if self.figures_sizes[big_cell][small_cell] < 0:
                    self.figures_sizes[big_cell][small_cell] = 0
            
            if self.figures_sizes[big_cell][small_cell] < 0:

                self.figures_sizes[big_cell][small_cell] += 4*mainself.Display.speed

                if self.figures_sizes[big_cell][small_cell] > 0:
                    self.figures_sizes[big_cell][small_cell] = 0

        else:

            if mainself.Scenes.game.Logic.Game.cells[big_cell][small_cell] == 0:

                if self.figures_sizes[big_cell][small_cell] < 99:
                    self.figures_sizes[big_cell][small_cell] += 4*mainself.Display.speed
                
                if self.figures_sizes[big_cell][small_cell] > 99:
                    self.figures_sizes[big_cell][small_cell] = 99
            
            if mainself.Scenes.game.Logic.Game.cells[big_cell][small_cell] == 1:

                if self.figures_sizes[big_cell][small_cell] > -99:
                    self.figures_sizes[big_cell][small_cell] -= 4*mainself.Display.speed
                
                if self.figures_sizes[big_cell][small_cell] < -99:
                    self.figures_sizes[big_cell][small_cell] = -99
        
        return round(self.figures_sizes[big_cell][small_cell])
    
    def big_figures_logic(self,mainself, cell: int) -> int:

        if mainself.Scenes.game.Logic.Game.cells[cell] == [0,0,0,0,0,0,0,0,0]:

            if self.big_figures_sizes[cell] < 99:
                self.big_figures_sizes[cell] += 2*mainself.Display.speed
            
            if self.big_figures_sizes[cell] > 99:
                self.big_figures_sizes[cell] = 99
        
        elif mainself.Scenes.game.Logic.Game.cells[cell] == [1,1,1,1,1,1,1,1,1]:

            if self.big_figures_sizes[cell] > -99:
                self.big_figures_sizes[cell] -= 2*mainself.Display.speed
            
            if self.big_figures_sizes[cell] < -99:
                self.big_figures_sizes[cell] = -99
        
        else:

            if self.big_figures_sizes[cell] > 0:

                self.big_figures_sizes[cell] -= 2*mainself.Display.speed

                if self.big_figures_sizes[cell] < 0:
                    self.big_figures_sizes[cell] = 0
            
            if self.big_figures_sizes[cell] < 0:

                self.big_figures_sizes[cell] += 2*mainself.Display.speed

                if self.big_figures_sizes[cell] > 0:
                    self.big_figures_sizes[cell] = 0
        
        return round(self.big_figures_sizes[cell])

    def fantom_logic(self,mainself):

        z = mainself.Display.zoom
        
        if mainself.Scenes.game.Logic.Game.selected_cell == None:

            selected_cell = mainself.Scenes.game.Logic.Select.select_big_cell(mainself)

            if selected_cell != None and None in mainself.Scenes.game.Logic.Game.cells[selected_cell]:

                color = round((math.sin(self.counter)/4+0.75)*100)
                self.select(mainself,mainself.Scenes.game.Select.select_points,selected_cell,color)

        else:
            small_selected_cell = mainself.Scenes.game.Logic.Select.select_small_cell(mainself)

            if small_selected_cell != None and mainself.Scenes.game.Logic.Game.cells[mainself.Scenes.game.Logic.Game.selected_cell][small_selected_cell] == None:

                for X in range(3):
                    for Y in range(3):
                        
                        if mainself.Scenes.game.Logic.Game.selected_cell == Y*3+X:
                            big_selected_cell_cords = [X-1,Y-1]
                        
                        if small_selected_cell == Y*3+X:
                            small_selected_cell_cords = [X-1,Y-1]
                
                x = big_selected_cell_cords[0]*200 + small_selected_cell_cords[0]*50
                y = big_selected_cell_cords[1]*200 + small_selected_cell_cords[1]*50

                color = round((math.sin(self.counter)/4+0.75)*100)

                if mainself.Scenes.game.Logic.Game.player == 0:
                    self.circle(mainself,(x,-y),color)
                else:
                    self.cross(mainself,(x,-y),color)

    def select(self,mainself,points: list,selected_cell:int,color:int):

        for X in range(3):
            for Y in range(3):
                
                if selected_cell == Y*3+X:
                    cords = [X-1,Y-1]

        z = mainself.Display.zoom

        parts = []
        
        for Y in range(-1,2,2):
            for X in range(-1,2,2):

                parts.append([])

                for point in points:

                    x = mainself.Display.width//2 - 320*z*X/4 + point[0]*X * 50*z/4 + 200*z*cords[0]
                    y = mainself.Display.height//2 - 320*z*Y/4 + point[1]*Y * 50*z/4 + 200*z*cords[1]

                    parts[-1].append((x,y))
        
        if mainself.Scenes.game.Logic.Game.player == 0:
            color = self.circle_gradient[color]
        else:
            color = self.cross_gradient[color]

        for part in parts:
            pygame.draw.polygon(mainself.Display.screen,color,part)