from function.endfunc import *

class Game:

    def __init__(self,var):
        
        self.big_celected_cell = None
        self.player = 0

    def main(self,var):

        x = var.display.mouseX - var.width//2
        y = -(var.display.mouseY - var.height//2)

        if self.big_celected_cell == None:
            self.big_celected_cell = Game.selectBigCell(self,var,x,y)

        return var

    def selectBigCell(self,var,x,y):

        selected_cell = 0

        for Y in range(3):
            for X in range(3):
                if x > -300+200*X and x < -100+200*X and y < 300-200*Y and y > 100-200*Y:
                    print(selected_cell)
                    return selected_cell
                else:
                    selected_cell += 1
        
        return None