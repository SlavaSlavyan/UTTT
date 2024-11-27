from data.func.endfunc import *

colors = []
lang = []
startscreen = []

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
    
    def main(self):

        global startscreen,colors,lang

        if self.anim == 1:
            colors = getThem(1)
            lang = getLang()
            startscreen = [self.height//100,gradient(colors[0],colors[1],120),0,[125,250,500]]
            self.anim = 1.1
        
        if startscreen[2] != len(startscreen[1]):
            self.screen.fill(startscreen[1][startscreen[2]])
            startscreen[2] += 1
        
        else:
            self.screen.fill(colors[1])
        
            for i in range(3):
                StartScreen.button(self,-25-55*i,startscreen[3][i]*startscreen[0],i)
            
            if self.anim == 1.1:
                startscreen[3] = [i / 1.05 for i in startscreen[3]]

        return self.anim
    
    def button(self,endpos,offset,text):

        x = self.width//2
        y = self.height//2-endpos+offset

        pos = [(x-200,y+25),(x+200,y+25),(x+200,y-25),(x-200,y-25)]

        pygame.draw.polygon(self.screen, colors[2], pos)