import pygame
import sys

from functions.load import File
from display.main import Display

class Main:

    def __init__(self):

        pygame.init()
        Main.setscreen(self)
        self.clock = pygame.time.Clock()
        self.fps = int
        self.F3 = True
        self.status = 'loading'

        self.Disp = Display(self)

        pygame.display.set_caption("Ultimate Tic Tac Toe 2.7.0 DEV")
        pygame.mouse.set_visible(True)

    def main(self):

        while True:

            self.width, self.height = self.screen.get_size()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    Main.saveAndExit(self)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Main.zoom(self,event.button)

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_F3:
                        Main.F3(self)
                    
                    if event.key == pygame.K_F11:
                        Main.F11(self)

            self = self.Disp.main(self)
                    
            self.fps = int(self.clock.get_fps())

            pygame.display.flip()
            self.clock.tick(60)
    
    def zoom(self,btn):

        if btn == 4:
            self.config['zoom'] += 0.1
        elif btn == 5:
            self.config['zoom'] -= 0.1
        elif btn == 2:
            self.config['zoom'] = 1
    
    def F11(self):

        if self.config['fullscreen'] == False:
            self.config['fullscreen'] = True

        else:
            self.config['fullscreen'] = False
        
        File.save('functions\\config',self.config)
        Main.setscreen(self)
    
    def F3(self):

        if self.F3 == True:
            self.F3 = False

        else:
            self.F3 = True
    
    def saveAndExit(self):

        File.save('functions\\config',self.config)
        pygame.quit()
        sys.exit()

    def setscreen(self):

        self.config = File.load('functions\\config')

        if self.config['fullscreen'] == False:

            self.width = 1200
            self.height = 800
            self.screen = pygame.display.set_mode((self.width, self.height),pygame.RESIZABLE)
        
        else:

            self.screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
            self.width, self.height = self.screen.get_size()
