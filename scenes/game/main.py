from scenes.game.display import Display
from scenes.game.logic import Logic
from scenes.game.animation import Animation
from scenes.game.select import Select
from scenes.game.figures import Figures

class Main:

    def __init__(self,mainself):

        self.Display = Display(mainself)
        self.Logic = Logic(mainself)
        self.Animation = Animation(mainself)
        self.Select = Select(mainself)
        self.Figures = Figures(mainself)