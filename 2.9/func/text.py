import pygame

from func.filereader import File

class Text:

    def __init__(self,m):
        
        self.letters = File.load('assets\\letters')
    
    def symbol(self,m,symbol,pos,size):

        symbol_load = self.letters[symbol]
        symbol_map = symbol_load['map']
        symbol_size = symbol_load['size']

        z = round(size/2,1)
        x = pos[0]
        y = pos[1] - symbol_size[1]*size

        for Y in range(len(symbol_map)):

            for X in range(len(symbol_map[0])):

                if symbol_map[Y][X] == 1:

                    pos = [[x+0+2*z*X,y+0+2*z*Y],[x+(z*2-1)+2*z*X,y+0+2*z*Y],[x+(z*2-1)+2*z*X,y+(z*2-1)+2*z*Y],[x+0+2*z*X,y+(z*2-1)+2*z*Y]]
                    pygame.draw.polygon(m.w.screen, (255,255,255), pos)
        
        return symbol_size[0]*size


    def F3(self,m,text):

        size = 2
        y = 6*size

        if isinstance(text,list):

            for line in text:

                x = 1*size
                for s in line:

                    if s == '"':
                        s = "''"

                    offset = self.symbol(m,s.upper(),[x,y],size)
                    x = x + 1*size + offset

                y += 7*size

    def test(self,m):

        m.w.screen.fill((0,0,0))

        f = File.load("test")

        letter_map = f['A']

        z = 0.5
        x = m.w.width//2 - len(letter_map[0])*z*2//2
        y = m.w.height//2 - len(letter_map)*z*2//2

        for Y in range(len(letter_map)):
            for X in range(len(letter_map[0])):
                if letter_map[Y][X] == 1:
                    pos = [[x+0+2*z*X,y+0+2*z*Y],[x+(z*2-1)+2*z*X,y+0+2*z*Y],[x+(z*2-1)+2*z*X,y+(z*2-1)+2*z*Y],[x+0+2*z*X,y+(z*2-1)+2*z*Y]]
                    pygame.draw.polygon(m.w.screen, (255,255,255), pos)
        
        pygame.draw.line(m.w.screen, (125,125,125), (m.w.width//2,0), (m.w.width//2, m.w.height), 1)
        pygame.draw.line(m.w.screen, (125,125,125), (0,m.w.height//2), (m.w.width, m.w.height//2), 1)