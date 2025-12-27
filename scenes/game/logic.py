class Logic:

    def __init__(self,mainself):

        self.cells = []

        for i in range(9):

            self.cells.append([])

            for j in range(9):
                self.cells[-1].append(None)

        self.player = 0
        self.selected_cell = None

        self.history = []
    
    def main(self,mainself):

        if mainself.Event.Mouse.buttons[0]['press']:
            
            if self.selected_cell == None:
                self.check_selected_big_cell(mainself,self.select_big_cell(mainself))

            else:
                self.check_selected_small_cell(mainself,self.select_small_cell(mainself))

    def select_big_cell(self,mainself) -> int | None:
        
        x = (mainself.Event.Mouse.pos[0] - mainself.Display.width//2)/mainself.Display.zoom
        y = (mainself.Event.Mouse.pos[1] - mainself.Display.height//2)/-mainself.Display.zoom

        for X in range(3):
            for Y in range(3):

                if x > -300 + 200*X and x < -100 + 200*X and y > 100 - 200*Y and y < 300 - 200*Y:
                    return 3 * Y + X
    
    def check_selected_big_cell(self,mainself, selected_cell: int):

        if selected_cell != None:
            if None in self.cells[selected_cell]:
                self.selected_cell = selected_cell
    
    def select_small_cell(self,mainself) -> int | None:

        z = mainself.Display.zoom

        for X in range(3):
            for Y in range(3):
                if self.selected_cell == Y*3+X:
                    selected_cell_cords = [X-1,Y-1]
        
        x = (mainself.Event.Mouse.pos[0] - mainself.Display.width//2 - 200*selected_cell_cords[0]*z)/z
        y = (mainself.Event.Mouse.pos[1] - mainself.Display.height//2 - 200*selected_cell_cords[1]*z)/-z

        for X in range(3):
            for Y in range(3):

                if x > -75 + 50*X and x < -25 + 50*X and y > 25 - 50*Y and y < 75 - 50*Y:
                    return 3 * Y + X
    
    def check_selected_small_cell(self,mainself, selected_cell: int):

        if selected_cell != None:

            if self.cells[self.selected_cell][selected_cell] == None:

                self.cells[self.selected_cell][selected_cell] = self.player

                if self.player == 0:
                    self.player = 1
                else:
                    self.player = 0
                
                capture = self.capture_check(mainself,self.selected_cell)

                if capture != None:

                    self.cells[self.selected_cell] = []

                    for i in range(9):
                        self.cells[self.selected_cell].append(capture)

                if None in self.cells[selected_cell]:
                    self.selected_cell = selected_cell

                else:
                    self.selected_cell = None
    
    def capture_check(self,mainself, big_cell: int) -> None | int:

        for p in range(2):

            capture = False

            for i in range(3):

                if self.cells[big_cell][i*3] == p and self.cells[big_cell][1+i*3] == p and self.cells[big_cell][2+i*3] == p:
                    capture = True
                    break

                if self.cells[big_cell][i] == p and self.cells[big_cell][3+i] == p and self.cells[big_cell][6+i] == p:
                    capture = True
                    break
            
            for i in range(2):
            
                if self.cells[big_cell][0+2*i] == p and self.cells[big_cell][4] == p and self.cells[big_cell][8-2*i] == p:
                    capture = True
                    break
            
            if capture:
                return p
        
        return None