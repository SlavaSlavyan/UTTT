class Game:
    
    def __init__(self,m):
        
        self.player = 0
        
        self.cells = []
        
        for i in range(9):
            self.cells.append([])
            for j in range(9):
                self.cells[i].append(None)
        
        self.selected_cell = None
    
    def onclick(self,m):
        
        if self.selected_cell == None:
            self.check_selected_big_cell(m,self.select_big_cell(m))
        
        else:
            self.check_selected_small_cell(m,self.select_small_cell(m))
    
    def select_big_cell(self,m) -> int:
        
        z = m.config['zoom'] + m.Disp.max_zoom
        x = m.PI.MI.mouse_pos[0] - m.Disp.width//2
        y = -m.PI.MI.mouse_pos[1] + m.Disp.height//2
        
        selected_cell = None
        
        for Y in range(3):
            for X in range(3):
                
                if x > -300*z+200*z*X and x < -100*z+200*z*X and y < 300*z-200*z*Y and y > 100*z-200*z*Y :
                    selected_cell = 3*Y+X
        
        if selected_cell != None:
            return selected_cell
    
    def check_selected_big_cell(self,m,cell:int):
        
        if cell != None:
            if None in self.cells[cell]:
                self.selected_cell = cell
            else:
                self.selected_cell = None

    def select_small_cell(self,m) -> int:
        
        z = m.config['zoom'] + m.Disp.max_zoom
        
        for X in range(3):
            for Y in range(3):
                if 3*Y+X == self.selected_cell:
                    x = m.PI.MI.mouse_pos[0] - m.Disp.width//2 +200*z -200*z*X
                    y = -m.PI.MI.mouse_pos[1] + m.Disp.height//2 -200*z +200*z*Y
        
        selected_cell = None
        
        for Y in range(3):
            for X in range(3):
                
                if x > -75*z+50*z*X and x < -25*z+50*z*X and y < 75*z-50*z*Y and y > 25*z-50*z*Y :
                    selected_cell = 3*Y+X
        
        if selected_cell != None:
            return selected_cell
    
    def check_selected_small_cell(self,m,cell:int):
        
        if cell != None and self.cells[self.selected_cell][cell] == None:
            self.cells[self.selected_cell][cell] = self.player
            
            self.check_selected_big_cell(m,cell)
            
            if self.player == 0:
                self.player = 1
            else:
                self.player = 0
    
    def captupeCheck(self,m):
        
        pass