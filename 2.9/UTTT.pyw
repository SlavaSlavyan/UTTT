import pygame
import sys

from func.screen import Window
from func.playerinput import PlayerInput

class Main: # основной класс, который отвечат за начальные настройки всего кода

    def __init__(self):

        pygame.init()

        self.w = Window(self)
        self.PI = PlayerInput(self)

        self.status = "game" # Статус игры, отвечат за то, как будет интерпритироваться информация от игрока 
        #(например при статусе "loading" игра не будет использовтаь информацию которую вводит игрок, а при статусе "game" игрок сможет взаимодействовать с игрой)

        pygame.display.set_caption("Ultimate Tic Tac Toe 2.9.0 DEV") # Изменение названя окна
        pygame.mouse.set_visible(True) # Запрет на показ курсора системы внутри окна игры (необходимо для кастомного курсора)
        

    def start(self): # функция запуска программы

        while True:

            self.w.getsize(self) # получение высоты и ширины экрана
            self.PI.main(self) # получение информации от игрока
            
            self.w.fps = int(self.w.clock.get_fps()) # получение кадров в секунду

            pygame.display.flip()
            self.w.fpslimit(self)


UTTT = Main() # для запуска я создаю экземпляр класса

UTTT.start()