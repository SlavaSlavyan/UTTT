class Logo:
    
    def __init__(self,m):
        m.Log.write("Инициализация логики сцены Logo.","DEBUG")
    
    def main(self,m):
        
        self.onclick(m)
    
    def onclick(self,m):
        
        #if m.Disp.anim == 'Logo_0' or m.Disp.anim == 'Logo_1':
            
            m.Disp.Logo.speed = 1
            
            for button in m.PI.MI.mouse.values():
                
                if button['hold']:
                    m.Disp.Logo.speed = 2