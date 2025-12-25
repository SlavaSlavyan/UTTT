from scenes.game.display import Display
from scenes.game.logic import Logic

class Main:

    def __init__(self,mainself):

        self.Display = Display(mainself)
        self.Logic = Logic(mainself)