class StartScreen:
    
    def __init__(self,m):

        m.log.write('[DEBUG] Инициализация класса PlayerInput.StartScreen')

        self.gradselectbtn = [0,0,0,0]
    
    def main(self,m):
        pass

    def gradbtn(self,m):

        z = m.config['zoom']
        x = m.PI.MI.mouse_pos[0] - m.Disp.width//2
        y = -m.PI.MI.mouse_pos[1] + m.Disp.height//2

        for i in range(4):
            
            if m.Disp.fps != 0:

                if x > -200*z and x < 200*z and y < -10*z - 55*z*i and y > -60*z - 55*z*i:
                    self.gradselectbtn[i] += 1+60/m.Disp.fps
                
                else:
                    self.gradselectbtn[i] -= 1+60/m.Disp.fps
                
                if self.gradselectbtn[i] < 0:
                    self.gradselectbtn[i] = 0
                
                elif self.gradselectbtn[i] >= 30:
                    self.gradselectbtn[i] = 29