import pygame
import math

class Logo:

    def __init__(self,m):

        m.Log.write("Инициализация отображения сцены Logo.","DEBUG")

        self.rotate = 0
        self.offset = [100,150,200]
        self.speed = 1
        self.bg = 0
        self.end = False

    def main(self,m):
        
        if self.end:
            m.Disp.screen.fill(m.Disp.colors['Logo']['grad-bg'][round(self.bg*100)])
        else:
            m.Disp.screen.fill(m.Disp.colors['Logo']['bg'])

            self.letter(m,"s",(-200,0),(self.offset[0],0))
            self.letter(m,"l",(0,0),(self.offset[1],0))
            self.letter(m,"l",(200,0),(self.offset[2],0))

        if m.Disp.anim == "Logo_0":
            
            if m.Disp.anim_speed != 0:
                self.offset = [i / (1 + (0.03*self.speed*m.Disp.anim_speed)) for i in self.offset]
            
            if self.offset[-1] <= 0.1:
                
                m.Disp.anim = "Logo_1"
                self.offset = [i*-1 for i in self.offset]
                self.offset.reverse()
                m.TimeManager.stop(m,"logo_1")
                m.TimeManager.start(m,"logo_1",(0,2,0),-1)
        
        elif m.Disp.anim == "Logo_1":
            
            if 'logo_1' in m.TimeManager.timers:
                
                m.TimeManager.timers['logo_1']['mod'] = -self.speed
                
                if m.TimeManager.timers['logo_1']['sec'] <= 0:
                    
                    m.Disp.anim = "Logo_2"
                    m.TimeManager.stop(m,"logo_1")
                    self.press_blink = 0
        
        elif m.Disp.anim == 'Logo_2':
            
            self.press_blink += 0.06*m.Disp.anim_speed*self.speed
            
            if math.cos(self.press_blink) > 0:
                m.Disp.Text.title(m,m.Disp.Text.text['Logo'][0],(0,-200),27,m.Disp.colors['Logo']['press'])
        
        elif m.Disp.anim == 'Logo_3':
            
            self.offset = [i * (1 + (0.03*self.speed*m.Disp.anim_speed)) for i in self.offset]
            
            if self.offset[-1] < -m.Disp.width//2:
                m.Disp.anim = 'Logo_4'
                self.end = True
        
        elif m.Disp.anim == 'Logo_4':

            self.bg += 1/60*m.Disp.anim_speed*self.speed

            if self.bg > 1:

                m.Disp.anim = 'StartScreen_0'
                m.status = 'StartScreen'
                self.bg = 1
        
        self.rotate += 0.03*m.Disp.anim_speed*self.speed

    def letter(self, m, symbol:str, pos:tuple, offset:tuple):

        z = m.Disp.zoom

        if symbol == "s":
            points = [[0,0],[3,0],[3,3],[1,3],[1,4],[3,4],[3,5],[0,5],[0,2],[2,2],[2,1],[0,1]]
        if symbol == "l":
            points = [[0,0],[3,0],[3,1],[1,1],[1,5],[0,5]]
        
        for point in points:

            for cord in range(2):
                point[cord] *= 50*z

            point[0] = m.Disp.width//2 + point[0] - 75*z + pos[0]*z + m.Disp.width*(offset[0]/100)
            point[1] = m.Disp.height//2 - point[1] + 125*z - pos[1]*z - m.Disp.height*(offset[1]/100)
        
        points2 = []

        for point in points:
            points2.append((point[0] + math.cos(self.rotate)*50*z,point[1] - math.sin(self.rotate)*50*z))
        
        for i in range(len(points)):
            pygame.draw.polygon(m.Disp.screen,m.Disp.colors['Logo']['text'],(points[i-1],points2[i-1],points2[i],points[i]))

        pygame.draw.polygon(m.Disp.screen,m.Disp.colors['Logo']['bg'],points)
        pygame.draw.polygon(m.Disp.screen,m.Disp.colors['Logo']['text'],points,1)