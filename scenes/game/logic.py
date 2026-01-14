from scenes.game.game_logic import Game
from scenes.game.buttons_logic import Buttons
from scenes.game.select_cells_logic import Select

class Logic:

    def __init__(self,mainself):

        self.Select = Select(mainself)
        self.Game = Game(mainself)
        self.Buttons = Buttons(mainself)
    
    def main(self,mainself):

        if mainself.Scenes.game.Display.anim == 1:

            if mainself.Event.Mouse.buttons[0]['press'] or mainself.Event.KeyBoard.keys['select']['press']:

                self.Buttons.main(mainself)
                self.Game.main(mainself)