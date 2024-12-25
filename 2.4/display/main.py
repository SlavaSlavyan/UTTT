from function.endfunc import *
from display.game import DisplayGame

class Display:

    def __init__(self):
        
        self.display_game = DisplayGame()

    def main(arg,self):

        if self.anim == 'game_start':
            self = self.display_game.main(self)

        return self