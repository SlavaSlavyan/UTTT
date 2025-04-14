import pygame

class Game:
    
    def __init__(self,m,d):
        
        self.colors = d.colors['game']
        self.colors['grad-cells'] = d.gradient(self.colors['grad-cells'][0],self.colors['grad-cells'][1],30)
        self.colors['grad-player'] = d.gradient(self.colors['grad-player'][0],self.colors['grad-player'][1],30)
        self.offset = []
        
        for i in range(12):
            self.offset.append(100*(i+1))
            
        self.select = {
            "size":1,
            "pos":[0,0],
            "offset":[0,0],
            "old_selected_cell":None,
            "grad":0
        }
        self.grad_cells = [0,0,0,0,0,0,0,0,0]
        
    def main(self,m):
        
        m.Disp.screen.fill(self.colors['bg'])
        
        if m.Disp.anim == 'game_start':
            
            self.bg(m)
            self.cells(m)
            self.small_cells(m)
            self.select_anim(m)
            
            self.offset = [i / (1 + 0.07*m.Disp.animSpeed) for i in self.offset]
            
            if round(self.offset[-1], 2) == 0:
                m.Disp.anim = 'game_main'
                m.status = 'game'
                
                if m.PI.Game.player == 0:
                    self.select['grad'] = 0
                else:
                    self.select['grad'] = 30
        
        elif m.Disp.anim == 'game_main':
            self.static(m)
            self.select_main(m)
        
    def bg(self,m):
        
        z = m.config['zoom'] + m.Disp.max_zoom
        x = m.Disp.width//2 + m.Disp.width*(self.offset[0]/100) - 300*z
        y = m.Disp.height//2 - 300*z
        
        pygame.draw.rect(m.Disp.screen, self.colors['bg2'], (x, y, 600*z, 600*z))
    
    def cells(self,m):
        
        z = m.config['zoom'] + m.Disp.max_zoom
        
        for i in range(-1,2,2):
                
            x = m.Disp.width//2 + m.Disp.width*(self.offset[1]*i/100)
            y = m.Disp.height//2
            pygame.draw.line(m.Disp.screen, self.colors['cells'], (x-300*z,y+100*i*z), (x+300*z,y+100*i*z), round(5*z))
            
            x = m.Disp.width//2 
            y = m.Disp.height//2 + m.Disp.height*(self.offset[1]*i/100)
            pygame.draw.line(m.Disp.screen, self.colors['cells'], (x+100*i*z,y+300*z), (x+100*i*z,y-300*z), round(5*z))
    
    def small_cells(self,m):
        
        for Y in range(3):
            for X in range(3):
                
                if 3*Y+X != 4:
                    
                    z = m.config['zoom'] + m.Disp.max_zoom
                
                    x = m.Disp.width//2 - m.Disp.width*(self.offset[2+3*Y+X]*(X-1)/100) - 200*z*(X-1)
                    y = m.Disp.height//2 - m.Disp.width*(self.offset[2+3*Y+X]*(Y-1)/100) - 200*z*(Y-1)
                
                else:
                    z = (m.config['zoom'] + m.Disp.max_zoom) * abs(self.offset[6]/700 - 1)
                    
                    x = m.Disp.width//2
                    y = m.Disp.height//2
                
                for i in range(-1,2,2):
                    pygame.draw.line(m.Disp.screen, self.colors['grad-cells'][0], (x-75*z,y+25*i*z), (x+75*z,y+25*i*z), round(3*z))
                    pygame.draw.line(m.Disp.screen, self.colors['grad-cells'][0], (x+25*i*z,y+75*z), (x+25*i*z,y-75*z), round(3*z))
    
    def select_anim(self,m):
        
        z = (m.config['zoom'] + m.Disp.max_zoom) * (self.offset[11] + 1)
        x = m.Disp.width//2
        y = m.Disp.height//2
        
        for X in range(-1,2,2):
            for Y in range(-1,2,2):

                pos = [[x-320*X*z,y+320*Y*z],[x-170*X*z,y+320*Y*z],[x-170*X*z,y+370*Y*z],[x-370*X*z,y+370*Y*z],[x-370*X*z,y+170*Y*z],[x-320*X*z,y+170*Y*z]]
                pygame.draw.polygon(m.Disp.screen, self.colors['grad-player'][-m.PI.Game.player], pos)
    
    def static(self,m):
        
        z = m.config['zoom'] + m.Disp.max_zoom
        x = m.Disp.width//2
        y = m.Disp.height//2
        
        pygame.draw.rect(m.Disp.screen, self.colors['bg2'], (x-300*z, y-300*z, 600*z, 600*z))

        for i in range(-1,2,2):
            pygame.draw.line(m.Disp.screen, self.colors['cells'], (x-300*z,y+100*i*z), (x+300*z,y+100*i*z), round(5*z))
            pygame.draw.line(m.Disp.screen, self.colors['cells'], (x+100*i*z,y+300*z), (x+100*i*z,y-300*z), round(5*z))
        
        for Y in range(3):
            for X in range(3):
                
                for i in range(-1,2,2):
                    pygame.draw.line(m.Disp.screen, self.colors['grad-cells'][round(self.grad_cells[3*Y+X])], (x+200*z*(X-1)-75*z,y+200*z*(Y-1)+25*i*z), (x+200*z*(X-1)+75*z,y+200*z*(Y-1)+25*i*z), round(3*z))
                    pygame.draw.line(m.Disp.screen, self.colors['grad-cells'][round(self.grad_cells[3*Y+X])], (x+200*z*(X-1)+25*i*z,y+200*z*(Y-1)+75*z), (x+200*z*(X-1)+25*i*z,y+200*z*(Y-1)-75*z), round(3*z))

                if m.PI.Game.selected_cell == 3*Y+X:
                    
                    self.grad_cells[3*Y+X] += 1*m.Disp.animSpeed
                    if self.grad_cells[3*Y+X] > 29:
                        self.grad_cells[3*Y+X] = 29
                
                else:
                    
                    self.grad_cells[3*Y+X] -= 1*m.Disp.animSpeed
                    if self.grad_cells[3*Y+X] < 0:
                        self.grad_cells[3*Y+X] = 0
        
    def select_main(self,m):
        
        if m.PI.Game.selected_cell != None:
            
            self.select['size'] -= 0.02*m.Disp.animSpeed
            if self.select['size'] < 0.25:
                self.select['size'] = 0.25
        
        else:
            
            self.select['size'] += 0.02*m.Disp.animSpeed
            if self.select['size'] > 1:
                self.select['size'] = 1
        
        z = (m.config['zoom'] + m.Disp.max_zoom)*self.select['size']
        
        x = m.Disp.width//2 + self.select['pos'][0]*(m.config['zoom'] + m.Disp.max_zoom) + self.select['offset'][0]*(m.config['zoom'] + m.Disp.max_zoom)
        y = m.Disp.height//2 + self.select['pos'][1]*(m.config['zoom'] + m.Disp.max_zoom) + self.select['offset'][1]*(m.config['zoom'] + m.Disp.max_zoom)
        
        if self.select['old_selected_cell'] != m.PI.Game.selected_cell:
            
            old_pos = self.select['pos']
            
            if m.PI.Game.selected_cell != None:
            
                for Y in range(3):
                    for X in range(3):
                        if m.PI.Game.selected_cell == 3*Y+X:
                            self.select['pos'] = [-200+200*X,-200+200*Y]
            
            else:
                self.select['pos'] = [0,0]

            for i in range(2):
                self.select['offset'][i] = self.select['offset'][i] + old_pos[i] - self.select['pos'][i]
            
            self.select['old_selected_cell'] = m.PI.Game.selected_cell
        
        for X in range(-1,2,2):
            for Y in range(-1,2,2):

                pos = [[x-320*X*z,y+320*Y*z],[x-170*X*z,y+320*Y*z],[x-170*X*z,y+370*Y*z],[x-370*X*z,y+370*Y*z],[x-370*X*z,y+170*Y*z],[x-320*X*z,y+170*Y*z]]
                pygame.draw.polygon(m.Disp.screen, self.colors['grad-player'][round(self.select['grad'])], pos)
        
        self.select['offset'] = [i / (1 + 0.1*m.Disp.animSpeed) for i in self.select['offset']]
        
        if m.PI.Game.player == 0:
            
            self.select['grad'] -= 1*m.Disp.animSpeed
            if self.select['grad'] < 0:
                self.select['grad'] = 0
        
        elif m.PI.Game.player == 1:
            
            self.select['grad'] += 1*m.Disp.animSpeed
            if self.select['grad'] > 30:
                self.select['grad'] = 30
        
        else:
            self.select['grad'] = 15