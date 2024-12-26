from data.func.endfunc import *

size = float(config("size"))
colors = getThem()
logo = {
    "ratio":None,
    "offset":None,
    "rotation":0,
    "timer":120
}

class Logo:

    def __init__(self,args):
        
        self.args = args

    def main(self):

        global logo

        self.args['screen'].fill(colors['black'])

        if self.args['anim'] == 0:

            logo["ratio"] = self.args['width']//100
            logo["offset"] = [100,200,400]
            self.args['anim'] = 0.1
        
        Logo.letter(self,"s",-200,logo['offset'][0],logo['rotation'])
        Logo.letter(self,"l",0,logo['offset'][1],logo['rotation'])
        Logo.letter(self,"l",200,logo['offset'][2],logo['rotation'])

        logo['rotation'] += 0.02

        if self.args['anim'] == 0.1:

            logo['offset'] = [i / 1.03 for i in logo['offset']]

            if logo['offset'][-1] <= 0.1:

                self.args['anim'] = 0.2
            
        elif self.args['anim'] == 0.2:

            logo['timer'] -= 1.2
            
            if logo['timer'] <= 0:

                logo["offset"] = [-0.04,-0.02,-0.01]
                self.args['anim'] = 0.3
        
        elif self.args['anim'] == 0.3:

            logo['offset'] = [i * 1.03 for i in logo['offset']]

            if logo['offset'][-1] <= -self.args['width']//2:

                self.args['anim'] = 1

        return self.args['anim']
    
    def letter(self,letter,endpos,offset,rotation):
        
        x = self.args['width']//2 + endpos*size + offset*logo['ratio']*size - 75*size
        y = self.args['height']//2 + 125*size

        if letter.lower() == 's':

            pos = [(x,y),(150*size+x,y),(150*size+x,-150*size+y),(50*size+x,-150*size+y),(50*size+x,-200*size+y),(150*size+x,-200*size+y),
               (150*size+x,-250*size+y),(x,-250*size+y),(x,-100*size+y),(100*size+x,-100*size+y),(100*size+x,-50*size+y),(x,-50*size+y),(x,y)]
            
            x += math.sin(rotation)*(50*size)
            y += math.cos(rotation)*(50*size)
            
            pos2 = [(x,y),(150*size+x,y),(150*size+x,-150*size+y),(50*size+x,-150*size+y),(50*size+x,-200*size+y),(150*size+x,-200*size+y),
               (150*size+x,-250*size+y),(x,-250*size+y),(x,-100*size+y),(100*size+x,-100*size+y),(100*size+x,-50*size+y),(x,-50*size+y),(x,y)]
        
        elif letter.lower() == "l":

            pos = [(x,y),(150*size+x,y),(150*size+x,-50*size+y),(50*size+x,-50*size+y),(50*size+x,-250*size+y),(x,-250*size+y),(x,y)]

            x += math.sin(rotation)*(50*size)
            y += math.cos(rotation)*(50*size)

            pos2 = [(x,y),(150*size+x,y),(150*size+x,-50*size+y),(50*size+x,-50*size+y),(50*size+x,-250*size+y),(x,-250*size+y),(x,y)]

        for i in range(len(pos)-1):
            pygame.draw.polygon(self.args['screen'], colors['yellow'], [pos[i],pos[i+1],pos2[i+1],pos2[i]])

        pygame.draw.polygon(self.args['screen'], colors['black'], pos)

        for i in range(len(pos)-1):
            pygame.draw.line(self.args['screen'], colors['yellow'], pos[i], pos[i+1], 1)