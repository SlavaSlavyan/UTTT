from data.func.logo import *

startscreen = []

class StartScreen:

    def __init__(self,swh,anim):
            
        self.screen = swh[0]
        self.width = swh[1]
        self.height = swh[2]
        self.anim = anim
    
    def main(self):

        global startscreen

        if self.anim == 1:
            startscreen = [[0,gradient(getcolor(0),getcolor(2),600),gradient(getcolor(0),getcolor(3),601)],[self.width,self.width*2,self.width*4,self.width*8]]
            self.anim = 1.1

        if startscreen[0][0] != 600:
            self.screen.fill(startscreen[0][1][startscreen[0][0]])
            startscreen[0][0] += 1
        
        else:
            self.screen.fill(getcolor(2))
        
        for i in range(3):
            StartScreen.button(self,25+55*i,startscreen[1][i],0)

        startscreen[1] = [i / 1.02 for i in startscreen[1]]

        return self.anim

    def button(self,endpos,offset,text):

        x = self.width//2
        y = self.height//2+offset+endpos

        pos = [(x-200,y+25),(x+200,y+25),(x+200,y-25),(x-200,y-25)]
        pygame.draw.polygon(self.screen, startscreen[0][2][startscreen[0][0]], pos)