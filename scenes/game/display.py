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
                mainself.Scenes.game.Animation.speed = -0.1

        elif self.anim == 1: 

            mainself.Scenes.game.Animation.back_rect(mainself)
            mainself.Scenes.game.Animation.big_cells_grid(mainself)

            mainself.Scenes.game.SmallCells.main(mainself)          
            mainself.Scenes.game.Figures.main(mainself)
            mainself.Scenes.game.Select.main(mainself)
            mainself.Scenes.game.Buttons.main(mainself)