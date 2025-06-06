import pygame
import sys

from display.Main import Display

class Main:
    
    def __init__(self, game_version:str):
        
        pygame.init()
        
        self.Disp = Display(self)
        
    def main(self):
        
        pass
        
    def stop(self):
        
        pygame.quit()
        sys.exit()