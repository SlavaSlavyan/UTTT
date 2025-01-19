import pygame
import sys

from display.main import Display
from function.filereader import File

class Main:

    def __init__(self):
        
        pygame.init()

        self.width, self.height = 1200, 800
        self.screen = pygame.display.set_mode((self.width, self.height),pygame.RESIZABLE)

        self.Disp = Display(self)

        pygame.display.set_caption("SLL EDITOR 1.0")

    def main(self):

        while True:

            self.width, self.height = self.screen.get_size()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self = self.Disp.main(self)
            
            pygame.display.flip()