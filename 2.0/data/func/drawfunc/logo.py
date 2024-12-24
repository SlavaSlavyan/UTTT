from data.func.read import *

logo = []

class Logo:

    def __init__(self,swh,anim):
            
        self.screen = swh[0]
        self.width = swh[1]
        self.height = swh[2]
        self.anim = anim

    def main(self):

        self.screen.fill(getcolor(0))

        global logo

        if self.anim == 0:
            logo = [0,self.width,3]
            self.anim = 0.1

        Logo.S(self,-200*((logo[1]/self.width)+1),logo[1],math.cos(logo[0])*50,math.sin(logo[0])*50,logo[1]/(self.width/4))
        Logo.L(self,0,logo[1],math.cos(logo[0])*50,math.sin(logo[0])*50,logo[1]/(self.width/4))
        Logo.L(self,200*((logo[1]/self.width)+1),logo[1],math.cos(logo[0])*50,math.sin(logo[0])*50,logo[1]/(self.width/4))
        
        if self.anim == 0.1:
            logo[1] /= 1.12
            if round(logo[1]) == 0:
                self.anim = 0.2

        elif self.anim == 0.2:
            logo[1] = 0
            logo[2] -= 0.015
            if logo[2] <= 0:
                self.anim = 0.3
                logo[1] = -0.2

        elif self.anim == 0.3:
            logo[1] *= 1.12
            if logo[1] < -self.width:
                self.anim = 1

        logo[0] += 0.04

        return self.anim

    def S(self,endpos,offset,offsetX,offsetY,size):

        size+=1
        if size < 1:
            size = 1

        x = self.width//2-75*size+endpos+offset
        y = self.height//2+125*size
        pos = [(x,y),(150*size+x,y),(150*size+x,-150*size+y),(50*size+x,-150*size+y),(50*size+x,-200*size+y),(150*size+x,-200*size+y),(150*size+x,-250*size+y),(x,-250*size+y),(x,-100*size+y),(100*size+x,-100*size+y),(100*size+x,-50*size+y),(x,-50*size+y),(x,y)]

        x += offsetX*size
        y -= offsetY*size
        pos2 = [(x,y),(150*size+x,y),(150*size+x,-150*size+y),(50*size+x,-150*size+y),(50*size+x,-200*size+y),(150*size+x,-200*size+y),(150*size+x,-250*size+y),(x,-250*size+y),(x,-100*size+y),(100*size+x,-100*size+y),(100*size+x,-50*size+y),(x,-50*size+y),(x,y)]
        
        for i in range(len(pos)-1):
            pygame.draw.polygon(self.screen, getcolor(1), [pos[i],pos[i+1],pos2[i+1],pos2[i]])
        
        pygame.draw.polygon(self.screen, getcolor(0), pos)

        for i in range(len(pos)-1):
            pygame.draw.line(self.screen, getcolor(1), pos[i], pos[i+1], 1)

    def L(self,endpos,offset,offsetX,offsetY,size):

        size+=1
        if size < 1:
            size = 1

        x = self.width//2-75*size+endpos+offset
        y = self.height//2+125*size
        pos = [(x,y),(150*size+x,y),(150*size+x,-50*size+y),(50*size+x,-50*size+y),(50*size+x,-250*size+y),(x,-250*size+y),(x,y)]

        x += offsetX*size
        y -= offsetY*size
        pos2 = [(x,y),(150*size+x,y),(150*size+x,-50*size+y),(50*size+x,-50*size+y),(50*size+x,-250*size+y),(x,-250*size+y),(x,y)]

        for i in range(len(pos)-1):
            pygame.draw.polygon(self.screen, getcolor(1), [pos[i],pos[i+1],pos2[i+1],pos2[i]])
        
        pygame.draw.polygon(self.screen, getcolor(0), pos)

        for i in range(len(pos)-1):
            pygame.draw.line(self.screen, getcolor(1), pos[i], pos[i+1], 1)