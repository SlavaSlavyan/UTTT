from data.func.read import *

logocheck = 0
logo = [0,None,3]

class Draw:

    class StartScreen:

        def __init__(self,swh):
            self.screen = swh[0]
            self.width = swh[1]
            self.height = swh[2]

        def main(self):

            global logo,logocheck

            if logocheck == False:
                logo[1] = self.width
                logocheck = 1

            Draw.StartScreen.S(self,-200*((logo[1]/self.width)+1),logo[1],math.cos(logo[0])*50,math.sin(logo[0])*50,logo[1]/(self.width/4))
            Draw.StartScreen.L(self,0,logo[1],math.cos(logo[0])*50,math.sin(logo[0])*50,logo[1]/(self.width/4))
            Draw.StartScreen.L(self,200*((logo[1]/self.width)+1),logo[1],math.cos(logo[0])*50,math.sin(logo[0])*50,logo[1]/(self.width/4))
            
            if logocheck == 1:
                logo[1] /= 1.05
                if round(logo[1]) == 0:
                    logocheck = 2
            elif logocheck == 2:
                logo[1] = 0
                logo[2] -= 0.015
                if logo[2] <= 0:
                    logocheck = 3
                    logo[1] = -0.1
            elif logocheck == 3:
                logo[1] *= 1.05
                if logo[1] < -self.width:
                    logocheck = 4
                    print('test')
            logo[0] += 0.02

        def S(self,endpos,offset,offsetX,offsetY,size):

            size+=1
            if size < 0:
                size = 0
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
            if size < 0:
                size = 0
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