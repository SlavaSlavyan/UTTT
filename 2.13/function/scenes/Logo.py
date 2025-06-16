class Logo:
    
    def __init__(self,m):
        m.Log.write("Инициализация логики сцены Logo.","DEBUG")
    
    def main(self,m):
        
        self.onclick(m)
    
    def onclick(self,m):
        
        m.Disp.Logo.speed = 1
        
        if m.Disp.anim != "Logo_2":
            
            for button in m.PI.MI.mouse.values():
                
                if button['hold']:
                    m.Disp.Logo.speed = 3
        
        else:
            
            for button in m.PI.MI.mouse.values():
                
                if button['press']:
                    m.Disp.anim = "Logo_3"