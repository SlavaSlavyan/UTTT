import pygame

from display.game import Game
from func.filereader import File
from func.text import Text

class Display: # Этот клас отвечает за условия выведения экранов игры (anim) по типу "startscreen" или "game"

    def __init__(self,m):
        
        self.anim = 'game_start' # Отвечает за пока определённой "анимации" или экрана.

        self.Text = Text(m)
        self.Game = Game(m)
        

    def main(self,m): # Основная функция, которая определяет условия вывода информации на экран

        m.w.screen.fill((0,0,0))

        if self.anim[:4] == 'game':
            self.Game.main(m)

        self.Text.F3(m,[f"FPS: {m.w.fps}"])