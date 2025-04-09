class StartScreen:
    
    def __init__(self,m):

        self.grad_buttons = [0,0,0,0]
        self.btn_sound = [False,False,False,False]
    
    def onclick(self,m):
        pass

    def main(self,m):

        z = m.config['zoom'] + m.Disp.max_zoom
        x = m.PI.MI.mouse_pos[0] - m.Disp.width//2
        y = -m.PI.MI.mouse_pos[1] + m.Disp.height//2

        for i in range(4):

            if x > -200*z and x < 200*z and y < -10*z - 55*z*i and y > -60*z - 55*z*i:

                self.grad_buttons[i] = 30

                if not self.btn_sound[i]:
                    self.btn_sound[i] = True
                    m.Sound.play(m,"select")
            
            else:
                
                self.grad_buttons[i] -= 1+m.Disp.animSpeed
                self.btn_sound[i] = False
                
            
            if self.grad_buttons[i] < 0:
                self.grad_buttons[i] = 0