class Select:

    def __init__(self,mainself):

        self.control = "MOUSE"
        self.selecting_cell = None

    def select_big_cell(self,mainself) -> int | None:
        
        x = (mainself.Event.Mouse.pos[0] - mainself.Display.width//2)/mainself.Display.zoom
        y = (mainself.Event.Mouse.pos[1] - mainself.Display.height//2)/-mainself.Display.zoom

        for X in range(3):
            for Y in range(3):

                if x > -300 + 200*X and x < -100 + 200*X and y > 100 - 200*Y and y < 300 - 200*Y:
                    return 3 * Y + X
                
    def select_small_cell(self,mainself) -> int | None:

        z = mainself.Display.zoom

        for X in range(3):
            for Y in range(3):
                if mainself.Scenes.game.Logic.Game.selected_cell == Y*3+X:
                    selected_cell_cords = [X-1,Y-1]
        
        x = (mainself.Event.Mouse.pos[0] - mainself.Display.width//2 - 200*selected_cell_cords[0]*z)/z
        y = (mainself.Event.Mouse.pos[1] - mainself.Display.height//2 - 200*selected_cell_cords[1]*z)/-z

        for X in range(3):
            for Y in range(3):

                if x > -75 + 50*X and x < -25 + 50*X and y > 25 - 50*Y and y < 75 - 50*Y:
                    return 3 * Y + X