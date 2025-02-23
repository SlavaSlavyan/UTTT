import pygame

from func.filereader import File

class Text:

    def __init__(self,m):
        
        self.letters = File.load('assets\\letters')

    def letter(self,m,pos,letter):

        pass

    def string(self,m,string,args):

        z = round(args['size']/2,1)
        x = args['pos'][0]
        y = args['pos'][1]

        for letter in string:
            
            self.letter(m,(x,y),letter)
            x += len(self.letters[letter][0])



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