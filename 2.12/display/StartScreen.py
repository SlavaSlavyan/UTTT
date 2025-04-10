import pygame

class StartScreen:
    
    def __init__(self,m,d):
        
        self.colors = d.colors['startscreen']
        self.colors['grad-bg'] = d.gradient(self.colors['grad-bg'][0],self.colors['grad-bg'][1],120)
        self.colors['grad-button-text'] = d.gradient(self.colors['grad-button-text'][0],self.colors['grad-button-text'][1],30)
        
        self.bg = 0
        self.offset = [100,200,400,800,1600,3200]
    
    def main(self,m):
        
        if True in m.PI.MI.mouse.values() or True in m.PI.KI.keys.values():
            m.Disp.animSpeed *= 2
        
        if m.Disp.anim == 'startscreen_start':
            
            try:
                m.Disp.screen.fill(self.colors['grad-bg'][round(self.bg)])
            
            except:
                m.Disp.screen.fill(self.colors['bg'])
            
            if self.bg < 120:
                self.bg += m.Disp.animSpeed
            
            else:
                m.Disp.anim = 'startscreen_start2'
                
        else:
            
            m.Disp.screen.fill(self.colors['bg'])
            
            self.title(m)
            for i in range(4):
                self.buttons(m,i)
                    
            if m.Disp.anim == 'startscreen_start2':
                self.offset = [i / (1 + 0.06*m.Disp.animSpeed) for i in self.offset]
                
                if round(self.offset[-1], 1) == 0:
                    m.Disp.anim = 'startscreen_main'
                    m.status = 'startscreen'
            
            if m.Disp.anim == 'startscreen_main':
                m.PI.StartScreen.main(m)
            
            if m.Disp.anim == 'startscreen_end':
                self.offset = [i * (1 + 0.06*m.Disp.animSpeed) for i in self.offset]
                
                if self.offset[0] >= 200:
                    m.Disp.anim = 'idk'
                    m.status = 'iddk'
            
    def title(self,m):
        
        z = m.config['zoom'] + m.Disp.max_zoom
        
        m.Disp.Text.title(m,m.Disp.Text.text['startscreen'][0],170*z,(0,220*z + m.Disp.height*(self.offset[1]/100)),self.colors['title'])
        m.Disp.Text.title(m,m.Disp.Text.text['startscreen'][1],100*z,(0,120*z + m.Disp.height*(self.offset[0]/100)),self.colors['title'])
    
    def buttons(self,m,i: int):
        
        z = m.config['zoom'] + m.Disp.max_zoom
        x = m.Disp.width//2 - 200*z
        y = m.Disp.height//2 + m.Disp.height*(self.offset[i+2]/100) + 55*z*(i+2) - 100*z
        
        pos = [[x,y],[x+400*z,y],[x+400*z,y+50*z],[x,y+50*z]]
        
        pygame.draw.polygon(m.Disp.screen, self.colors['button'], pos)
        
        m.Disp.Text.title(m,m.Disp.Text.text['startscreen'][i+2],30*z,(0,-m.Disp.height*(self.offset[i+2]/100)-55*z*i-33*z),self.colors['grad-button-text'][round(m.PI.StartScreen.grad_buttons[i])])