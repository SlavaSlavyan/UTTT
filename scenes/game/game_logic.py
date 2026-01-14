class Game:

    def __init__(self,mainself):

        self.cells = []

        for i in range(9):

            self.cells.append([])

            for j in range(9):
                self.cells[-1].append(None)

        self.player = 0
        self.selected_cell = None
        self.win = None

        self.history = []

    def main(self,mainself):
            
        if self.selected_cell == None:
            self.check_selected_big_cell(mainself,mainself.Scenes.game.Logic.Select.select_big_cell(mainself))

        else:
            self.check_selected_small_cell(mainself,mainself.Scenes.game.Logic.Select.select_small_cell(mainself))
    
    def check_selected_big_cell(self,mainself, selected_cell: int):

        if selected_cell != None:
            if None in self.cells[selected_cell]:

                self.selected_cell = selected_cell

                self.history.append({
                    "player": self.player,
                    "big_cell": selected_cell,
                    "small_cell": None,
                    "capture": None
                })
    
    def check_selected_small_cell(self,mainself, selected_cell: int):

        if selected_cell != None:

            if self.cells[self.selected_cell][selected_cell] == None:

                self.cells[self.selected_cell][selected_cell] = self.player

                self.history.append({
                    "player": self.player,
                    "big_cell": self.selected_cell,
                    "small_cell": selected_cell,
                    "capture": None
                })

                if self.player == 0:
                    self.player = 1
                else:
                    self.player = 0
                
                capture = self.capture_check(mainself,self.selected_cell)

                if capture != None:

                    self.history[-1]['capture'] = self.cells[self.selected_cell]

                    self.cells[self.selected_cell] = []

                    for i in range(9):
                        self.cells[self.selected_cell].append(capture)

                    self.win = self.win_check(mainself)

                if None in self.cells[selected_cell]:
                    self.selected_cell = selected_cell

                else:
                    self.selected_cell = None
                
                if self.win != None:
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

    def win_check(self,mainself):

        win_patterns = [[0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1]]

        for p in win_patterns:

            win = False

            for i in range(3):

                if self.cells[i*3] == p and self.cells[1+i*3] == p and self.cells[2+i*3] == p:
                    win = True
                    break

                if self.cells[i] == p and self.cells[3+i] == p and self.cells[6+i] == p:
                    win = True
                    break
            
            for i in range(2):
            
                if self.cells[0+2*i] == p and self.cells[4] == p and self.cells[8-2*i] == p:
                    win = True
                    break
            
            if win:
                return p[0]
        
        return None
    
    def history_back(self,mainself):
        
        for line in self.history:
            print(line)

        if len(self.history) != 0:
            
            if self.history[-1]["small_cell"] == None:
                self.selected_cell = None
            
            else:

                if self.history[-1]["capture"] != None:
                    self.cells[self.history[-1]["big_cell"]] = self.history[-1]["capture"]
                
                self.cells[self.history[-1]["big_cell"]][self.history[-1]["small_cell"]] = None

                self.selected_cell = self.history[-1]["big_cell"]

                self.player = self.history[-1]["player"]
            
            self.history.pop(-1)