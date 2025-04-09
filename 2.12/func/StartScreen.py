class StartScreen:
    
    def __init__(self,m):

        self.grad_buttons = [0,0,0,0]
        self.inbtn = [False,False,False,False]
        self.btn_sound = {"in":[False,False,False,False],"out":[False,False,False,False]}
    
    def onclick(self,m):
        pass

    def main(self,m):

        z = m.config['zoom']
        x = m.PI.MI.mouse_pos[0] - m.Disp.width//2
        y = -m.PI.MI.mouse_pos[1] + m.Disp.height//2

        for i in range(4):

            if x > -200*z and x < 200*z and y < -10*z - 55*z*i and y > -60*z - 55*z*i:
                self.inbtn[i] = True
                self.grad_buttons[i] += 1+m.Disp.animSpeed
            
            else:
                self.inbtn[i] = False
                self.grad_buttons[i] -= 1+m.Disp.animSpeed
            
            if self.inbtn[i]:
                if not self.btn_sound['in'][i]:
                    self.btn_sound['in'][i] = True
                    m.Sound.play(m,"startscreen_select")
            else:
                self.btn_sound['in'][i] = False
            
            if self.grad_buttons[i] < 0:
                self.grad_buttons[i] = 0
            
            elif self.grad_buttons[i] >= 30:
                self.grad_buttons[i] = 29