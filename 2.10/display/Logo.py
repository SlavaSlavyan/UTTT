import pygame
import math

class Logo: # класс отображения начального лога
    
    def __init__(self,m,d):
        
        m.log.w('[INIT] Инициализация класса Logo <-- Display.')
        
        self.colors = d.colors['logo']
        
        self.offset = [100,200,400]
        self.rotate = 0
    
    def main(self,m):
        
        m.Disp.screen.fill(self.colors['bg'])
        
        self.letter(m,"S",-200,self.offset[0])
        self.letter(m,"L",0,self.offset[1])
        self.letter(m,"L",200,self.offset[2])
        
        self.offset = [i / 1.05 for i in self.offset]
        self.rotate += 0.03
        
        text = pygame.font.Font("data\\font\\text.ttf", 30).render("Центрированный текст", True, (255,255,255))
        m.Disp.screen.blit(text, text.get_rect(center=(m.config['screensize'][0]//2, m.config['screensize'][1]//2)))
    
    def letter(self,m,letter: str,pos: float,offset: float):
        
        z = m.config['zoom']
        x = m.config['screensize'][0]//2 + pos*z + m.config['screensize'][0]*(offset/100) -75*z
        y = m.config['screensize'][1]//2 + 125*z
        
        if letter == "S":
            pos = [[x,y],[x+150*z,y],[x+150*z,y-150*z],[x+50*z,y-150*z],[x+50*z,y-200*z],[x+150*z,y-200*z],[x+150*z,y-250*z],[x,y-250*z],[x,y-100*z],[x+100*z,y-100*z],[x+100*z,y-50*z],[x,y-50*z]]
        else:
            pos = [[x,y],[x+150,y],[x+150,y-50],[x+50,y-50],[x+50,y-250],[x,y-250]]
        
        #pygame.draw.polygon(m.Disp.screen, self.colors['logo'], pos)
        #pygame.draw.line(m.screen, self.colors['activecell'], (x-300*z, y-100*z), (x+300*z, y-100*z), round(5*z))
        
        pos2 = []
        
        for dot in pos:
            pos2.append([dot[0]+50*z*math.cos(self.rotate),dot[1]+50*z*math.sin(self.rotate)])
        
        
        for i in range(len(pos)):    
            pygame.draw.polygon(m.Disp.screen, self.colors['logo'], [pos[i-1],pos[i],pos2[i],pos2[i-1]])
        
        pygame.draw.polygon(m.Disp.screen, self.colors['bg'], pos)
        
        for i in range(len(pos)):    
            pygame.draw.line(m.Disp.screen, self.colors['logo'], pos[i-1], pos[i], 1)
        