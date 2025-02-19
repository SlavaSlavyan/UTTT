import pygame

from display.game import Game

class Display: # Этот клас отвечает за условия выведения экранов игры (anim) по типу "startscreen" или "game"

    def __init__(self,m):
        
        self.anim = 'game_start' # Отвечает за пока определённой "анимации" или экрана.

        self.Game = Game(m)
        

    def main(self,m):

        if self.anim[:4] == 'game':
            self.Game.main(m)