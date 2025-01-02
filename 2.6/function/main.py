import pygame
import sys

from function.load import Config
from display.main import Display

class Main:

    def __init__(self):
        
        pygame.init()

        self.config = Config.read()

        self.zoom = self.config['zoom']
        Main.setscreen(self)

        self.Display = Display

        
    def main(self):

        while True:

            self.width, self.height = self.screen.get_size()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    
                    save_config = Config.read()
                    save_config['zoom'] = self.zoom
                    Config.write(save_config)

                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:

                    if event.button == 2 or event.button == 4 or event.button == 5:
                        Main.zoom(self,event.button)

                    if event.button == 1:
                        Main.click(self)
                
                if event.type == pygame.KEYDOWN:
                    pass

            self = self.display.main(self)

            if self.keyF3 == True:
                Main.f3(self)
            
            self.fps = int(self.clock.get_fps())

            pygame.display.flip()
            self.clock.tick(60)
    
    def zoom(self,btn):

        pass
    
    def setscreen(self):

        self.config = Config.read()

        if self.config['fullscreen'] == False:

            info = pygame.display.Info()

            self.width = info.current_w//1.5
            self.height = info.current_h//1.25
            self.screen = pygame.display.set_mode((self.width, self.height),pygame.RESIZABLE)
        
        else:

            self.screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
            self.width, self.height = self.screen.get_size()