class SmallCells:

    def __init__(self,mainself):
        
        self.cells_gradient = mainself.Display.gradient(5,4,100)
        self.cells_colors = []
        
        for i in range(9):
            self.cells_colors.append(0)

    def main(self,mainself):
        
        for y in range(-1,2):
            for x in range(-1,2):

                size = mainself.Scenes.game.Figures.big_figures_sizes[3*(y+1)+(x+1)]/100

                color = self.cells_gradient_logic(mainself,3*(y+1)+(x+1))
                
                mainself.Scenes.game.Animation.cells_grid(mainself,self.cells_gradient[color],(200*x,-200*y),size=0.25*-(abs(size)-1))
    
    def cells_gradient_logic(self,mainself, id: int) -> int:

        if mainself.Scenes.game.Logic.Game.selected_cell == id:

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