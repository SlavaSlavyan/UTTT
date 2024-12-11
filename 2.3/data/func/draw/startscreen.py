from data.func.endfunc import *

size = float(config("size"))
colors = getThem()
lang = getLang('startscreen')
startscreen = {
    "ratio":None,
    "offset":None,
    "bgcolors":None,
    "bgnum":0
}

class StartScreen:

    def __init__(self,args):
        
        self.args = args
    
    def main(self):

        if self.args['anim'] == 1:

            startscreen['ratio'] = self.args['height']//100
            startscreen['offset'] = [100,200,400,-1600,-800]
            startscreen['bgcolors'] = gradient(colors['black'],colors['gray'], 120)
            startscreen['bgnum'] = 0
            self.args['anim'] = 1.1
        
        if startscreen['bgnum'] != len(startscreen['bgcolors']):

            self.args['screen'].fill(startscreen['bgcolors'][startscreen['bgnum']])
            startscreen['bgnum'] += 1
        
        else:

            self.args['screen'].fill(colors['gray'])

            for i in range(3):
                StartScreen.button(self,25+55*i,startscreen['offset'][i],i)
            
            for i in range(2):
                StartScreen.title(self,-150+80*i,startscreen['offset'][i+3],i)
            
            if self.args['anim'] == 1.1:

                startscreen['offset'] = [i / 1.05 for i in startscreen['offset']]

                if startscreen['offset'][3] >= -0.1:
                    self.args['anim'] = 1.2
            
            if self.args['anim'] == 1.2:
                startscreen['offset'] = [i * 0 for i in startscreen['offset']]

        return self.args['anim'], self.args['status']
    
    def button(self,endpos,offset,textnum):

        x = self.args['width']//2 
        y = self.args['height']//2 + endpos*size + offset*startscreen['ratio']*size

        pos = [(x-200*size,y+25*size),(x+200*size,y+25*size),(x+200*size,y-25*size),(x-200*size,y-25*size)]

        pygame.draw.polygon(self.args['screen'], colors['darkgray'], pos)

        text = pygame.font.Font('data\\font\\text.ttf', int(40*size)).render(lang[textnum+2], True, colors['lightgray'])
        self.args['screen'].blit(text, text.get_rect(center=(x, y - 3*size)))
    
    def title(self,endpos,offset,titlenum):

        x = self.args['width']//2 
        y = self.args['height']//2 + endpos*size + offset*startscreen['ratio']*size

        text = pygame.font.Font('data\\font\\title.ttf', int((150-75*titlenum)*size)).render(lang[titlenum], True, colors['green'])
        self.args['screen'].blit(text, text.get_rect(center=(x, y)))