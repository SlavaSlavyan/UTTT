class StartScreen:
    
    def __init__(self,m):

        self.grad_buttons = [0,0,0,0]
        self.btn_sound = [False,False,False,False]
        self.selected_button = None
        self.selecting_button = None
        self.keypress = [False,False]
    
    def onclick(self,m) -> int:
        
        z = m.config['zoom'] + m.Disp.max_zoom
        x = m.PI.MI.mouse_pos[0] - m.Disp.width//2
        y = -m.PI.MI.mouse_pos[1] + m.Disp.height//2
        
        for i in range(4):

            if x > -200*z and x < 200*z and y < -10*z - 55*z*i and y > -60*z - 55*z*i:
                self.selected_button = i
                break
            else:
                self.selected_button = None
        
        return self.selected_button

    def onkey(self,m):
        
        if m.status == 'startscreen':
        
            if m.PI.KI.keys['up'] or m.PI.KI.keys['w']:
                
                if not self.keypress[0]:
                    
                    self.keypress[0] = True
                    
                    if self.selecting_button == None or self.selecting_button == 0:
                        self.selecting_button = 3
                        m.Sound.play(m,"select")
                    
                    else:
                        self.selecting_button -= 1
                        m.Sound.play(m,"select")
            
            else:
                self.keypress[0] = False
                    
            
            if m.PI.KI.keys['down'] or m.PI.KI.keys['s']:
                
                if not self.keypress[1]:
                    self.keypress[1] = True
                    
                    if self.selecting_button == None or self.selecting_button == 3:
                        self.selecting_button = 0
                        m.Sound.play(m,"select")
                    
                    else:
                        self.selecting_button += 1
                        m.Sound.play(m,"select")
            
            else:
                self.keypress[1] = False
            
            if m.PI.KI.keys['esc']:
                self.selecting_button = None
            
            if m.PI.KI.keys['space'] or m.PI.KI.keys['enter']:
                
                self.selected_button = self.selecting_button
                
    def main(self,m):

        z = m.config['zoom'] + m.Disp.max_zoom
        x = m.PI.MI.mouse_pos[0] - m.Disp.width//2
        y = -m.PI.MI.mouse_pos[1] + m.Disp.height//2
        
        key = True

        for i in range(4):

            if x > -200*z and x < 200*z and y < -10*z - 55*z*i and y > -60*z - 55*z*i:
                
                self.selecting_button = None
                self.grad_buttons[i] = 30

                if not self.btn_sound[i]:
                    self.btn_sound[i] = True
                    m.Sound.play(m,"select")
                
                key = False
            
            else:
                
                self.grad_buttons[i] -= 1+m.Disp.animSpeed
                self.btn_sound[i] = False
                
                if self.selecting_button == i:
                    self.grad_buttons[i] = 30
            
            if self.grad_buttons[i] < 0:
                self.grad_buttons[i] = 0
        
        if key:
            self.onkey(m)
        
        if self.selected_button != None:
            m.Disp.anim = 'startscreen_end'
            m.status = 'startscreen_end'
    
    def nextanim(self,m):
        
        if self.selected_button == 0:
            m.Disp.anim = 'game_start'
            m.status = 'game_start'
        elif self.selected_button == 3:
            m.end()
        else:
            m.Disp.anim = 'startscreen_start'
            m.status = 'startscreen_start'
            self.resetmodule(m)
            m.PI.StartScreen.resetmodule(m)
    
    def resetmodule(self,m):
        
        self.grad_buttons = [0,0,0,0]
        self.btn_sound = [False,False,False,False]
        self.selected_button = None
        self.selecting_button = None
        self.keypress = [False,False]