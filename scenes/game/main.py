from scenes.game.display import Display
from scenes.game.logic import Logic
from scenes.game.animation import Animation
from scenes.game.select import Select
from scenes.game.figures import Figures
from scenes.game.small_cells import SmallCells
from scenes.game.buttons import Buttons
from scenes.game.win import Win

class Main:

    def __init__(self,mainself):

        self.Display = Display(mainself)
        self.Logic = Logic(mainself)
        self.Animation = Animation(mainself)
        self.Select = Select(mainself)
        self.Figures = Figures(mainself)
        self.SmallCells = SmallCells(mainself)
        self.Buttons = Buttons(mainself)
        self.Win = Win(mainself)