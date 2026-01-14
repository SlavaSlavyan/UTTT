class Buttons:

    def __init__(self,mainself):
        self.visual_selecting_cell = None

    def main(self,mainself):
        
        selected_button = self.select_button(mainself)

        if selected_button == 1:
            mainself.Scenes.game.Logic.Game.history_back(mainself)

    def select_button(self,mainself) -> int | None:

        x = mainself.Event.Mouse.pos[0]
        y = mainself.Event.Mouse.pos[1]

        for i in range(2):

            if x > 10 and x < 60 and y > 10+60*i and y < 60+60*i:
                return i