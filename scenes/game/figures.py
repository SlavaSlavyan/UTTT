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

        self.cross_points = [[0,0],[1,0],[2,1],[1,2],[0,1],
                             [0,0],[-1,0],[-2,1],[-1,2],[0,1],
                             [0,0],[-1,0],[-2,-1],[-1,-2],[0,-1],
                             [0,0],[1,0],[2,-1],[1,-2],[0,-1]]

        self.counter = 0

    def main(self,mainself):

        self.fantom_logic(mainself)

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

    def fantom_logic(self,mainself):

        z = mainself.Display.zoom
        
        if mainself.Scenes.game.Logic.selected_cell == None:
            pass

        else:
            small_selected_cell = mainself.Scenes.game.Logic.select_small_cell(mainself)

            if small_selected_cell != None:

                for X in range(3):
                    for Y in range(3):
                        
                        if mainself.Scenes.game.Logic.selected_cell == Y*3+X:
                            big_selected_cell_cords = [X-1,Y-1]
                        
                        if small_selected_cell == Y*3+X:
                            small_selected_cell_cords = [X-1,Y-1]
                
                x = big_selected_cell_cords[0]*200 + small_selected_cell_cords[0]*50
                y = big_selected_cell_cords[1]*200 + small_selected_cell_cords[1]*50

                color = round((math.sin(self.counter)/4+0.75)*100)

                if mainself.Scenes.game.Logic.player == 0:
                    self.circle(mainself,(x,-y),color)
                else:
                    self.cross(mainself,(x,-y),color)