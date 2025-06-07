import pygame
import sys

from function.managers.LogManager import LogManager
from function.managers.JsonManager import JsonManager
from function.inputs.PlayerInput import PlayerInput
from display.Main import Display

class Main:
    
    def __init__(self, game_version:str):

        self.Log = LogManager()
        self.Log.write([f"[==========[VERS:{game_version}]==========]\n","@SLL Привет всем, кто читает этот лог! ツ","Инициализация всех библиотек..."],"DEBUG")

        self.JsonManager = JsonManager(self)
        
        pygame.init()

        self.PI = PlayerInput(self)
        self.Disp = Display(self)

        self.status = "Logo"
        self.Log.write(f"Начальный статус = {self.status}.","DEBUG")

        pygame.display.set_caption(f"Ultimate Tic Tac Toe {game_version}")
        #pygame.display.set_icon(pygame.image.load('data\\assets\\small_ico.png'))
        pygame.mouse.set_visible(True)

        self.Log.write("Инициализация всех библиотек окончена!","DEBUG")
        
    def main(self):
        
        self.PI.main(self)

        self.Disp.main(self)

        pygame.display.flip()
        self.Disp.clock.tick(self.config['max-fps'])

    def stop(self):

        self.Log.write("Запущена функция отключения!\n","WARNING")
        self.Log.save()
        
        pygame.quit()
        sys.exit()