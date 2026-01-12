import pygame

class Display:

    def __init__(self,mainself):

        self.anim = 0

    def main(self,mainself):

        mainself.Display.screen.fill(mainself.Display.colors[2])

        if self.anim == 0:
            mainself.Scenes.game.Animation.main(mainself)

            if mainself.Scenes.game.Animation.counter < 0.001:

                self.anim = 1
                mainself.Scenes.game.Animation.counter = 0.001
                mainself.Scenes.game.Animation.speed = -0.05

        elif self.anim == 1: 

            mainself.Scenes.game.Animation.back_rect(mainself)
            mainself.Scenes.game.Animation.big_cells_grid(mainself)

            mainself.Scenes.game.SmallCells.main(mainself)          
            mainself.Scenes.game.Figures.main(mainself)
            mainself.Scenes.game.Select.main(mainself)
            mainself.Scenes.game.Buttons.main(mainself)

            if mainself.Scenes.game.Logic.win != None:
                mainself.Scenes.game.Win.main(mainself)

                if mainself.Scenes.game.Win.counter < 0.001:

                    mainself.Scenes.game.Win.counter_bool = False
                    mainself.Scenes.game.Win.timer += 1/120*mainself.Display.speed

                    if mainself.Scenes.game.Win.timer >= 1:

                        self.anim = 2
                        mainself.Scenes.game.Win.counter_bool = True
                        mainself.Scenes.game.Win.counter = 0.001
                        mainself.Scenes.game.Win.speed = -0.1

                        for small_cell in mainself.Scenes.game.Logic.cells:
                            small_cell.clear()
                            
                            for i in range(9):
                                small_cell.append(None)
        
        elif self.anim == 2:

            mainself.Scenes.game.Animation.main(mainself)
            mainself.Scenes.game.Figures.main(mainself)
            mainself.Scenes.game.Win.main(mainself)

            if mainself.Scenes.game.Animation.counter > 1.001:

                mainself.stop()




