from data.func.endfunc import *

colors = []
logo = []

class Logo:

    def __init__(self,args):
        
        self.screen = args[0]
        self.width = args[1]
        self.height = args[2]
        self.anim = args[3]

    def main(self):

        global colors

        if self.anim == 0:
            
            colors = getThem()
            logo = [self.width//100,[100,100,100]]
            self.anim = 0.1
        
        self.screen.fill(colors[0][0])

        Logo.S(self,0,logo[1][0]*logo[0])

        return self.anim
        
    def S(self,endpos,offset):

        x = self.width//2+offset+endpos
        y = self.height//2

        pos = [(x+50,y+50),(x-50,y+50),(x-50,y-50),(x+50,y-50)]

        pygame.draw.polygon(self.screen, colors[0][1], pos)
        
        