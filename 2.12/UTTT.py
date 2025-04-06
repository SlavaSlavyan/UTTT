UTTT_version = "2.12.0 DEV"
print(f"VERS={UTTT_version}")

import pygame
import sys

from func.JsonManager import JsonManager
from func.PlayerInput import PlayerInput
from display.main import Display
from func.Timer import Timer

class Main:

    def __init__(self):

        self.vers = UTTT_version
        
        self.JsonManager = JsonManager(self)
        
        pygame.init()

        self.status = 'logo'
        print(f'Start-status={self.status}')

        self.Disp = Display(self)
        self.PI = PlayerInput(self)
        self.Time = Timer(self)

        pygame.display.set_caption(f"Ultimate Tic Tac Toe {UTTT_version}")
        pygame.display.set_icon(pygame.image.load('data\\assets\\UTTT.png'))
        pygame.mouse.set_visible(True)

    def start(self):

        print('Start main while...')

        while True:

            self.Disp.main(self)
            
            self.PI.main(self)

            pygame.display.flip()
            self.Disp.clock.tick(self.config['max-fps'])

            self.Time.main(self)
    
    def loadconfig(self):

        self.config = self.JsonManager.load('data\\config')

    def saveconfig(self):

        self.JsonManager.save('data\\config',self.config)

    def end(self):

        self.saveconfig()

        pygame.quit()
        sys.exit()

UTTT = Main()
UTTT.start()