from data.func.endfunc import *

colors = []
lang = []
startscreen = []
size = float(config("scale"))

#0 - соотношение высоты и множителя
#1 - градиент фона
#2 - выбранный цвет градиента
#3 - смещение объектов

class StartScreen:

    def __init__(self,args):
        
        self.screen = args[0]
        self.width = args[1]
        self.height = args[2]
        self.anim = args[3]
        self.status = args[4]
    
    def startscreenclick(self,x,y):

        x = self.width//2-x
        y = self.height//2-y

        selected_button = 0

        for i in range(3):
            if x < 200 and x > -200 and y < 0-55*i and y > -50-55*i:
                return selected_button
            
            else:
                selected_button += 1
        
        return None
    
    def main(self):

        global startscreen,colors,lang

        if self.anim == 1:
            colors = getThem()
            lang = getLang(0)
            startscreen = [self.height//100,gradient(colors['black'],colors['gray'],120),0,[125,250,500,1000]]
            self.anim = 1.1
        
        if startscreen[2] != len(startscreen[1]) and self.anim == 1.1:
            self.screen.fill(startscreen[1][startscreen[2]])
            startscreen[2] += 1
        
        else:

            self.screen.fill(colors['gray'])

            mouse_x, mouse_y = pygame.mouse.get_pos()
            arg = StartScreen.startscreenclick(self,mouse_x,mouse_y)

            for i in range(3):
                StartScreen.button(self,-25-55*i,startscreen[3][i]*startscreen[0],i,arg)
            StartScreen.title(self,130,startscreen[3][3]*startscreen[0])
            
            if self.anim == 1.1:
                startscreen[3] = [i / 1.05 for i in startscreen[3]]
                if startscreen[3][3] < 0.2:
                    self.anim = 1.2

            elif self.anim == 1.2:
                startscreen[3] = [i*0 for i in startscreen[3]]
                self.status = 1
            
            elif self.anim == 1.3 or self.anim == 1.4:
                if self.anim == 1.3:
                    startscreen[3] = [0.0625,0.125,0.25,0.5]
                    self.anim = 1.4
                startscreen[3] = [i * 1.1 for i in startscreen[3]]

                if startscreen[3][0]*startscreen[0] >= self.height:
                    from data.func.main import status
                    if status == 4:
                        pygame.quit()
                        sys.exit()

        return self.anim,self.status
    
    def button(self,endpos,offset,text,arg):

        endpos*=size
        offset*=size
        x = self.width//2
        y = self.height//2-endpos+offset

        pos = [(x-200*size,y+25*size),(x+200*size,y+25*size),(x+200*size,y-25*size),(x-200*size,y-25*size)]

        pygame.draw.polygon(self.screen, colors['darkgray'], pos)
        
        if text != arg:
            textcolor = colors['lightgray']

        else:
            textcolor = colors['yellow']
    
        text = pygame.font.Font('data\\font\\text.ttf', int(40*size)).render(lang[text+2], True, textcolor)
        self.screen.blit(text, text.get_rect(center=(self.width // 2, self.height//2-endpos+offset-3*size)))
    
    def title(self,endpos,offset):

        endpos*=size
        offset*=size
        x = self.width//2
        y = self.height//2+offset+endpos

        for i in range(2):

            text = pygame.font.Font('data\\font\\Title.ttf', int((100-50*i)*size)).render(lang[i], True, colors['green'])
            self.screen.blit(text, text.get_rect(center=(self.width // 2, self.height // 2-offset-endpos+70*size*i)))