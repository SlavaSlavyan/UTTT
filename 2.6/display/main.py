import pygame

from display.game import Game
from function.load import Load

class Display:

    def __init__(self,var):
        
        self.colors = Load.read(f'theme\\{var.config['theme']}')
        self.anim = 'game_start'
        self.Game = Game(self)

    def main(self):

        if self.anim == 'game_start':
            self = self.Game.start()
        
        if self.F3 == True:
            Display.F3(self)
        
        Display.cursor(self,0)
    
    def F3(self):

        text = [
            'Made by SLL :3','',
            f'Screen: {self.width}x{self.height}',
            f'Fullscreen: {self.config['fullscreen']}',
            f'Zoom: {self.config['zoom']}',
            f'Theme: {self.config['theme']}',
            f'FPS: {self.fps}',
            f'Status: {self.status}'
            f'Scene (Anim): {self.Display.anim}'
        ]

        font = pygame.font.Font('assets\\fonts\\text.ttf', 10)

        for i in range(len(text)):
            self.screen.blit(font.render(text[i], True, (255,255,255)), (10, 10+10*i))

    def cursor(self,var):

        pass