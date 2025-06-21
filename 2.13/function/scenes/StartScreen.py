import pygame

class StartScreen:

    def __init__(self,m):

        m.Log.write("Инициализация логики сцены StartScreen.","DEBUG")

    def main(self,m):
        
        for i in range(len(m.Disp.StartScreen.btns)):
            
            try:
                if m.PI.MI.is_point_in_polygon(m,m.Disp.StartScreen.btns[i].points,m.PI.MI.mouse_pos):
                    m.Disp.StartScreen.btns[i].grad_btn = 1
                    m.Disp.StartScreen.btns[i].size *= 1 + (0.2*m.Disp.anim_speed)
            except:
                pass
        
        self.onclick(m)
    
    def onclick(self,m):

        pass
