from function.endfunc import *

class Game:

    def __init__(self,var):
        
        self.big_celected_cell = None
        self.player = 0

    def main(self,var):

        x = var.display.mouseX - var.width//2
        y = -(var.display.mouseY - var.height//2)

        self.big_celected_cell = Game.selectBigCell(self,var,x,y)

        return var

    def selectBigCell(self,var,x,y):

        z = var.zoom
        selected_cell = 0

        for Y in range(3):
            for X in range(3):
                if x > -300*z+200*z*X and x < -100*z+200*z*X and y < 300*z-200*z*Y and y > 100*z-200*z*Y:
                    print(selected_cell)
                    return selected_cell
                else:
                    selected_cell += 1
        
        return None