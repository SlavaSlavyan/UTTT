class Select:

    def __init__(self,mainself):

        self.control = "MOUSE"
        self.selecting_cell = None

    def select_big_cell(self,mainself) -> int | None:
        
        if self.control == "MOUSE":
        
            x = (mainself.Event.Mouse.pos[0] - mainself.Display.width//2)/mainself.Display.zoom
            y = (mainself.Event.Mouse.pos[1] - mainself.Display.height//2)/-mainself.Display.zoom

            for X in range(3):
                for Y in range(3):

                    if x > -300 + 200*X and x < -100 + 200*X and y > 100 - 200*Y and y < 300 - 200*Y:
                        self.selecting_cell = 3 * Y + X
                        return 3 * Y + X
        
        else:
            return self.selecting_cell
                
    def select_small_cell(self,mainself) -> int | None:
        
        if self.control == "MOUSE":

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
                        self.selecting_cell = 3 * Y + X
                        return 3 * Y + X
        
        else:
            return self.selecting_cell
    
    def select_keyboard_update(self,mainself):
        
        if mainself.Event.KeyBoard.keys['up']['press']:
            if self.selecting_cell == None:
                self.selecting_cell = 4
            elif self.selecting_cell > 2: 
                self.selecting_cell -= 3
        
        elif mainself.Event.KeyBoard.keys['down']['press']:
            if self.selecting_cell == None:
                self.selecting_cell = 4
            elif self.selecting_cell < 6: 
                self.selecting_cell += 3
        
        elif mainself.Event.KeyBoard.keys['left']['press']:
            if self.selecting_cell == None:
                self.selecting_cell = 4
            elif int(self.selecting_cell%3) > 0:
                self.selecting_cell -= 1
        
        elif mainself.Event.KeyBoard.keys['right']['press']:
            if self.selecting_cell == None:
                self.selecting_cell = 4
            elif int(self.selecting_cell%3) < 2:
                self.selecting_cell += 1
    
    def control_switch(self,mainself):
        
        if self.control == "MOUSE":
        
            keys = [
                mainself.Event.KeyBoard.keys['up']['press'],
                mainself.Event.KeyBoard.keys['down']['press'],
                mainself.Event.KeyBoard.keys['right']['press'],
                mainself.Event.KeyBoard.keys['left']['press'],
                mainself.Event.KeyBoard.keys['select']['press']
            ]
            
            if True in keys:
                self.control = "KEYBOARD"
                mainself.Display.Cursor.display = False

        else:
            
            if mainself.Event.Mouse.buttons[0]['press']:
                self.control = "MOUSE"
                mainself.Display.Cursor.display = True