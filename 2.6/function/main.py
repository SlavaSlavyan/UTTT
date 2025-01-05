import pygame
import sys

from display.main import Display
from function.load import Load

class Main:

    def __init__(self):
        
        pygame.init()

        self.config = Load.read('function\\config')
        self.fps = int
        self.F3 = True
        self.status = 'loading'
        Main.setScreen(self)
        self.Display = Display(self)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Ultimate Tic Tac Toe 2.6.0 DEV")
        pygame.mouse.set_visible(True)

    def main(self):

        while True:
            
            self.width, self.height = self.screen.get_size()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    Main.exitAndSave(self)
                
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_F11:
                        Main.F11(self)
                    
                    if event.key == pygame.K_F3:
                        Main.F3(self)
            
            self.Display.main()
            
            self.fps = int(self.clock.get_fps())

            pygame.display.flip()
            self.clock.tick(60)
            

    def setScreen(self):

        if self.config['fullscreen'] == False:

            self.width = 1200
            self.height = 800
            self.screen = pygame.display.set_mode((self.width, self.height),pygame.RESIZABLE)
        
        else:
            
            self.screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
            self.width, self.height = self.screen.get_size()

    def F11(self):

        if self.config['fullscreen'] == False:
            self.config['fullscreen'] = True

        else:
            self.config['fullscreen'] = False
        
        Load.write(self.config,'function\\config')
        Main.setScreen(self)
    
    def F3(self):

        if self.F3 == False:
            self.F3 = True

        else:
            self.F3 = False

    def exitAndSave(self):

        Load.write(self.config,'function\\config')
        pygame.quit()
        sys.exit()
