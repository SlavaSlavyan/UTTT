import pygame
import sys

from function.Reader import File
from display.main import Display

class Main:
    
    def __init__(self):
        
        pygame.init()

        Main.setscreen(self)

        self.fps = int
        self.maxfps = 60
        self.status = "game"
        self.F3 = True
        self.clock = pygame.time.Clock()

        self.Disp = Display(self)

        pygame.display.set_caption("Ultimate Tic Tac Toe 2.8.0 DEV")
        pygame.mouse.set_visible(True)

    def main(self):

        while True:

            self.width, self.height = self.screen.get_size()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_F3:
                        Main.F3(self)
                    
                    if event.key == pygame.K_F11:
                        Main.F11(self)
            
            self.Disp.main(self)
                    
            self.fps = int(self.clock.get_fps())

            pygame.display.flip()
            self.clock.tick(self.maxfps)
    
    def F11(self):

        if self.config['fullscreen'] == False:
            self.config['fullscreen'] = True

        else:
            self.config['fullscreen'] = False
        
        File.save('function\\config',self.config)
        Main.setscreen(self)
    
    def F3(self):

        if self.F3 == True:
            self.F3 = False

        else:
            self.F3 = True
    
    def setscreen(self):

        self.config = File.load('function\\config')

        if self.config['fullscreen'] == False:

            self.width = 1200
            self.height = 800
            self.screen = pygame.display.set_mode((self.width, self.height),pygame.RESIZABLE)
        
        else:

            self.screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
            self.width, self.height = self.screen.get_size()

Start = Main()

Start.main()