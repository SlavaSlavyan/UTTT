import pygame
import sys

from function.filereader import File
from display.main import Display
from function.workspace import WorkSpace

class Main:

    def __init__(self):
        
        pygame.init()

        self.width, self.height = 1200, 800
        self.screen = pygame.display.set_mode((self.width, self.height),pygame.RESIZABLE)

        self.WS = WorkSpace(self)

        self.Disp = Display(self)

        pygame.display.set_caption("SLL EDITOR 1.1")

    def main(self):

        while True:

            self.width, self.height = self.screen.get_size()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F5:
                        self.WS.figures = File.load('test')
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        self.Disp.WS.zoom += 0.1
                    elif event.button == 5:
                        self.Disp.WS.zoom -= 0.1
                    elif event.button == 2:
                        self.Disp.WS.zoom = 1
                    if event.button == 3:
                        self.Disp.WS.last_offset = self.Disp.WS.offset
                        self.Disp.mouse_pos_last = self.Disp.mouse_pos
                        self.Disp.mouse_pressed = True
                
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 3:
                        self.Disp.mouse_pressed = False

            self = self.Disp.main(self)
            self = self.WS.main(self)
            
            pygame.display.flip()