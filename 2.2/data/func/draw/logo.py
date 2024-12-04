from data.func.endfunc import *

colors = []
logo = []
size = float(config("scale"))

#0 - соотношение ширины и множителю
#1 - смещение букв
#2 - вращение тени
#3 - таймер

class Logo:

    def __init__(self,args):
        
        self.screen = args[0]
        self.width = args[1]
        self.height = args[2]
        self.anim = args[3]

    def main(self):

        global colors,logo

        if self.anim == 0:
            
            colors = getThem()
            logo = [self.width//100,[100,250,500],0,240]
            self.anim = 0.1
        
        self.screen.fill(colors['black'])

        Logo.S(self,-200*size,logo[1][0]*logo[0]*size,logo[2])
        Logo.L(self,0,logo[1][1]*logo[0]*size,logo[2])
        Logo.L(self,200*size,logo[1][2]*logo[0]*size,logo[2])

        logo[2] += 0.02

        if self.anim == 0.1:
            logo[1] = [i / 1.05 for i in logo[1]]

            if logo[1][2] < 0.3:
                self.anim = 0.2
        
        elif self.anim == 0.2:
            logo[1] = [i * 0 for i in logo[1]]
            logo[3] -= 1

            if logo[3] == 0:
                logo[1] = [-0.25,-0.125,-0.0625]
                self.anim = 0.3
        
        elif self.anim == 0.3:
            logo[1] = [i * 1.05 for i in logo[1]]
            if logo[1][2] < -self.width:
                self.anim = 1

        return self.anim
        
    def S(self,endpos,offset,shadow):

        x = self.width//2+offset+endpos-75*size
        y = self.height//2+125*size
        shadowX = math.sin(shadow)*50*size
        shadowY = math.cos(shadow)*50*size

        pos = [(x,y),(150*size+x,y),(150*size+x,-150*size+y),(50*size+x,-150*size+y),(50*size+x,-200*size+y),(150*size+x,-200*size+y),
               (150*size+x,-250*size+y),(x,-250*size+y),(x,-100*size+y),(100*size+x,-100*size+y),(100*size+x,-50*size+y),(x,-50*size+y),(x,y)]

        x += shadowX
        y -= shadowY

        pos2 = [(x,y),(150*size+x,y),(150*size+x,-150*size+y),(50*size+x,-150*size+y),(50*size+x,-200*size+y),(150*size+x,-200*size+y),
               (150*size+x,-250*size+y),(x,-250*size+y),(x,-100*size+y),(100*size+x,-100*size+y),(100*size+x,-50*size+y),(x,-50*size+y),(x,y)]
        
        for i in range(len(pos)-1):
            pygame.draw.polygon(self.screen, colors['yellow'], [pos[i],pos[i+1],pos2[i+1],pos2[i]])

        pygame.draw.polygon(self.screen, colors['black'], pos)

        for i in range(len(pos)-1):
            pygame.draw.line(self.screen, colors['yellow'], pos[i], pos[i+1], 1)
    
    def L(self,endpos,offset,shadow):

        x = self.width//2+offset+endpos-75*size
        y = self.height//2+125*size
        shadowX = math.sin(shadow)*50*size
        shadowY = math.cos(shadow)*50*size

        pos = [(x,y),(150*size+x,y),(150*size+x,-50*size+y),(50*size+x,-50*size+y),(50*size+x,-250*size+y),(x,-250*size+y),(x,y)]

        x += shadowX
        y -= shadowY

        pos2 = [(x,y),(150*size+x,y),(150*size+x,-50*size+y),(50*size+x,-50*size+y),(50*size+x,-250*size+y),(x,-250*size+y),(x,y)]

        for i in range(len(pos)-1):
            pygame.draw.polygon(self.screen, colors['yellow'], [pos[i],pos[i+1],pos2[i+1],pos2[i]])

        pygame.draw.polygon(self.screen, colors['black'], pos)

        for i in range(len(pos)-1):
            pygame.draw.line(self.screen, colors['yellow'], pos[i], pos[i+1], 1)
        
        