class Logic:

    def __init__(self,mainself):

        self.cells = []

        for i in range(9):

            self.cells.append([])

            for j in range(9):
                self.cells[-1].append(None)

        self.player = 0
        self.selected_cell = None
    
    def main(self,mainself):

        if mainself.Event.Mouse.buttons[0]['press']:
            
            if self.selected_cell == None:
                self.selected_cell = self.select_big_cell(mainself)
            else:
                print(self.select_small_cell(mainself))

    def select_big_cell(self,mainself) -> int | None:
        
        x = (mainself.Event.Mouse.pos[0] - mainself.Display.width//2)/mainself.Display.zoom
        y = (mainself.Event.Mouse.pos[1] - mainself.Display.height//2)/-mainself.Display.zoom

        for X in range(3):
            for Y in range(3):

                if x > -300 + 200*X and x < -100 + 200*X and y > 100 - 200*Y and y < 300 - 200*Y:
                    return 3 * Y + X
    
    def select_small_cell(self,mainself) -> int | None:

        for X in range(3):
            for Y in range(3):
                if self.selected_cell == Y*3+X:
                    selected_cell_cords = [X-1,Y-1]
        
        x = (mainself.Event.Mouse.pos[0] - mainself.Display.width//2 - 200*selected_cell_cords[0]*mainself.Display.zoom)/mainself.Display.zoom
        y = (mainself.Event.Mouse.pos[1] - mainself.Display.height//2 - 200*selected_cell_cords[1]*mainself.Display.zoom)/-mainself.Display.zoom

        for X in range(3):
            for Y in range(3):

                if x > -75 + 50*X and x < -15 + 50*X and y > 15 - 50*Y and y < 75 - 50*Y:
                    return 3 * Y + X