from data.func.read import *

anim = 0
logo = []
startscreen = []

class Draw:

    def __init__(self,swh):
            
            self.swh = swh

    def main(self):

        global anim

        if anim >= 0 and anim < 1:
            Draw.Logo(self.swh).main()

        elif anim >= 1 and anim < 2:
            Draw.StartScreen(self.swh).main()

    class Logo:

        def __init__(self,swh):

            self.screen = swh[0]
            self.width = swh[1]
            self.height = swh[2]

        def main(self):

            self.screen.fill(getcolor(0))

            global logo,anim

            if anim == 0:
                logo = [0,self.width,3]
                anim = 0.1

            Draw.Logo.S(self,-200*((logo[1]/self.width)+1),logo[1],math.cos(logo[0])*50,math.sin(logo[0])*50,logo[1]/(self.width/4))
            Draw.Logo.L(self,0,logo[1],math.cos(logo[0])*50,math.sin(logo[0])*50,logo[1]/(self.width/4))
            Draw.Logo.L(self,200*((logo[1]/self.width)+1),logo[1],math.cos(logo[0])*50,math.sin(logo[0])*50,logo[1]/(self.width/4))
            
            if anim == 0.1:
                logo[1] /= 1.05
                if round(logo[1]) == 0:
                    anim = 0.2

            elif anim == 0.2:
                logo[1] = 0
                logo[2] -= 0.015
                if logo[2] <= 0:
                    anim = 0.3
                    logo[1] = -0.1

            elif anim == 0.3:
                logo[1] *= 1.05
                if logo[1] < -self.width:
                    anim = 1
                    print('test')

            logo[0] += 0.02

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

    class StartScreen:

        def __init__(self,swh):

            self.screen = swh[0]
            self.width = swh[1]
            self.height = swh[2]
        
        def main(self):

            global anim,startscreen

            if anim == 1:
                
                startscreen = [[gradient(getcolor(0),getcolor(2),300),gradient(getcolor(0),getcolor(3),300)],0,[self.height,self.height*2,self.height*4,self.height*8]]
                anim = 1.1

            if startscreen[1] < len(startscreen[0][0]):
                self.screen.fill(startscreen[0][0][startscreen[1]])
                startscreen[1] += 1

            else:
                self.screen.fill(getcolor(2))
            
            for i in range(3):
                Draw.StartScreen.button(self,-25-55*i,startscreen[2][i],i)
            
            startscreen[2] = [i / 1.02 for i in startscreen[2]]
        
        def button(self,endpos,offset,text):

            x = self.width//2
            y = self.height//2-endpos+offset
            pos = [(-200+x,-25+y),(200+x,-25+y),(200+x,25+y),(-200+x,25+y)]

            pygame.draw.polygon(self.screen, startscreen[0][1][startscreen[1]-1], pos)