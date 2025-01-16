import pygame
import json
import sys

class Main:

    def __init__(self):
        
        pygame.init()
        
        self.width = 1200
        self.height = 800
        self.screen = pygame.display.set_mode((self.width, self.height),pygame.RESIZABLE)

        self.Disp = Display(self)

        pygame.display.set_caption("SLL EDITOR SLL 0.2")

    def main(self):

        while True:

            self.width, self.height = self.screen.get_size()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self = self.Disp.main(self)

            pygame.display.flip()
    
    class Editor:

        def __init__(self,m):

            pass

        def main(m):

            return m

class Display:

    def __init__(self,m):
        
        self.colors = {"gray":(40, 44, 52),
                       "dark_gray":(33, 37, 43),
                       "light_gray":(171,178,191),
                       "second_light_gray":(92, 99, 112),
                       "yellow":(229, 192, 123),
                       "green":(152, 195, 121),
                       "blue":(97, 175, 239),
                       "orange":(198, 107, 60),
                       "red":(194, 64, 52),
                       "black":(0,0,0),
                       "white":(255,255,255)}
        
        self.Edit = Display.Editor(m)

    def main(self,m):

        m = m.Disp.Edit.main(m)

        return m

    class Editor:

        def __init__(self,m):

            pass

        def main(self,m):

            m.screen.fill(m.Disp.colors['gray'])

            pos = (((0,0),(0,50),(50,50),(50,0)),((0,100),(50,100),(50,300),(0,300)),((m.width,0),(m.width,m.height),(m.width-300,m.height),(m.width-300,0)))

            for i in range(len(pos)):
                pygame.draw.polygon(m.screen, m.Disp.colors['dark_gray'], pos[i])
            return m

Start = Main()

Start.main()