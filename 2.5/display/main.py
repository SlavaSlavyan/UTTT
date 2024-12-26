from function.endfunc import *
from display.game import DisplayGame

class Display:

    def __init__(self,var):
        
        self.display_game = DisplayGame(var)

    def main(self,var):

        if var.anim == 'game_start':
            var = self.display_game.start(var)
        
        elif var.anim == 'game':
            var = self.display_game.main(var)

        return var