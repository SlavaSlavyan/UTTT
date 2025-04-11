import pygame
import math

class Logo:
    
    def __init__(self,m,d):
        
        self.colors = d.colors['logo']
        
        self.offset = [100,200,400]
        self.rotate = 0
    
    def main(self,m):
        
        m.Disp.screen.fill(self.colors['bg']) 

        self.letter(m,"S",-200,self.offset[0])
        self.letter(m,"L",0,self.offset[1])
        self.letter(m,"L",200,self.offset[2])

        self.rotate += 0.03*m.Disp.animSpeed
        
        if m.Disp.anim == 'logo_start':
            self.offset = [i / (1 + 0.05*m.Disp.animSpeed) for i in self.offset]

            if round(self.offset[-1], 1) == 0:

                m.Disp.anim = 'logo_wait'
                self.offset = [i * -1 for i in self.offset]
                self.offset.reverse()
                m.Time.addtimer(m,"logo",-1,(0,1,0))
        
        elif m.Disp.anim == 'logo_wait':

            if m.Time.timers['logo']['min'] <= -1:
                m.Time.removetimer(m,'logo')
                m.Disp.anim = 'logo_end'
            
        if m.Disp.anim == 'logo_end':

            self.offset = [i * (1 + 0.05*m.Disp.animSpeed) for i in self.offset]

            if self.offset[-1]/100*m.Disp.width < -m.Disp.width:

                m.Disp.anim = 'startscreen_start'
                m.status = 'startscreen_start'
        

    def letter(self,m,letter: str, pos: float, offset: float):
        
        z = m.config['zoom'] + m.Disp.max_zoom
        x = m.Disp.width//2 + pos*z + m.Disp.width*(offset/100) -75*z 
        y = m.Disp.height//2 + 125*z
        
        if letter == "S":
            pos = [[x,y],[x+150*z,y],[x+150*z,y-150*z],[x+50*z,y-150*z],[x+50*z,y-200*z],[x+150*z,y-200*z],[x+150*z,y-250*z],[x,y-250*z],[x,y-100*z],[x+100*z,y-100*z],[x+100*z,y-50*z],[x,y-50*z]]
        else:
            pos = [[x,y],[x+150*z,y],[x+150*z,y-50*z],[x+50*z,y-50*z],[x+50*z,y-250*z],[x,y-250*z]]
        
        pos2 = []
        
        for dot in pos:
            pos2.append([dot[0]+50*z*math.cos(self.rotate),dot[1]+50*z*math.sin(self.rotate)])
    
        for i in range(len(pos)):
            pygame.draw.polygon(m.Disp.screen, self.colors['text'], [pos[i-1],pos[i],pos2[i],pos2[i-1]])
        
        pygame.draw.polygon(m.Disp.screen, self.colors['bg'], pos)
        
        for i in range(len(pos)):    
            pygame.draw.line(m.Disp.screen, self.colors['text'], pos[i-1], pos[i], 1)
    
    def resetmodule(self,m):
        
        self.colors = m.Disp.colors['logo']
        
        self.offset = [100,200,400]
        self.rotate = 0