import pygame

class Display:

    def __init__(self,mainself):

        self.cells_gradient = mainself.Display.gradient(5,4,100)
        self.cells_colors = []
        
        for i in range(9):
            self.cells_colors.append(0)

        self.anim = 0

    def main(self,mainself):

        mainself.Display.screen.fill(mainself.Display.colors[2])

        if self.anim == 0:
            mainself.Scenes.game.Animation.main(mainself)

            if mainself.Scenes.game.Animation.counter < 0.001:

                self.anim = 1
                mainself.Scenes.game.Animation.counter = 0.001
                mainself.Scenes.game.Animation.speed = -0.1

        elif self.anim == 1: 

            mainself.Scenes.game.Animation.back_rect(mainself)
            mainself.Scenes.game.Animation.big_cells_grid(mainself)

            for y in range(-1,2):
                for x in range(-1,2):

                    size = mainself.Scenes.game.Figures.big_figures_sizes[3*(y+1)+(x+1)]/100

                    color = self.cells_gradient_logic(mainself,3*(y+1)+(x+1))
                    
                    mainself.Scenes.game.Animation.cells_grid(mainself,self.cells_gradient[color],(200*x,-200*y),size=0.25*-(abs(size)-1))
            
            mainself.Scenes.game.Figures.main(mainself)
            mainself.Scenes.game.Select.main(mainself)
    
    def cells_gradient_logic(self,mainself, id: int) -> int:

        if mainself.Scenes.game.Logic.selected_cell == id:

            if self.cells_colors[id] < 99:
                self.cells_colors[id] += 2*mainself.Display.speed

            if round(self.cells_colors[id]) > 99:
                self.cells_colors[id] = 99

        else:

            if self.cells_colors[id] > 0:
                self.cells_colors[id] -= 2*mainself.Display.speed

            if round(self.cells_colors[id]) < 0:
                self.cells_colors[id] = 0
        
        return round(self.cells_colors[id])