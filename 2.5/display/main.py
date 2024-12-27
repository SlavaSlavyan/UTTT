from function.endfunc import *
from display.game import DisplayGame

class Display:

    def __init__(self,var):
        
        self.display_game = DisplayGame(var)
        self.mouseX = int
        self.mouseY = int
        self.mouseSize = 0

    def main(self,var):

        if var.anim == 'game_start':
            var = self.display_game.start(var)
        
        elif var.anim == 'game':
            var = self.display_game.main(var)
        
        Display.cursor(self,var)

        return var

    def cursor(self,var):

        z = var.zoom
        self.mouseX, self.mouseY = pygame.mouse.get_pos()
        x = self.mouseX
        y = self.mouseY

        pos = [(x,y),(x+(10+self.mouseSize)*z,y),(x,y+(10+self.mouseSize)*z)]
        pygame.draw.polygon(var.screen, var.colors['yellow'], pos)
        self.mouseSize /= 1.2