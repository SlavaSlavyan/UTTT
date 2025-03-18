import pygame
import sys

# исмпорт библиотек sll
from func.Logs import Log
from func.PlayerInput import PlayerInput
from func.Reader import Reader
from display.main import Display

class Main: # основной класс игры который является корнем игры. В него импортируются все остальные классы.
    
    def __init__(self):
        
        self.Reader = Reader()
        
        self.config = self.Reader.load("data\\config")
        
        self.log = Log(self.config)
        
        self.log.w('Инициализация основного класса. -->')
        self.log.w(f'Конфигурация программы: {self.config}.')
        
        self.Disp = Display(self)
        self.PI = PlayerInput(self)
        
        pygame.init() # запуск pygame
        
        self.log.w("Конец инициализации. <--")
    
    def start(self): # функция для страта программы
        
        self.log.w("Запуск игры...")
        
        while True: # Основной цикл
            
            self.Disp.main(self) # отрисовка кадра
            
            self.PI.main(self) # Взаимодействие пользователя с игрой
            
            pygame.display.flip() # обновление кадра (вывод)
            self.Disp.clock.tick(self.config['maxfps']) # ограничение кадров в секунду соответствующее максимальному значению в cofig
    
    def setConfigurations(self): # функция для выставления базовых настроек программы.
        
        pygame.display.set_caption("Ultimate Tic Tac Toe 2.10.0 DEV")
        pygame.mouse.set_visible(True)
    
    def reloadconfig(self): # перезагрузка конфига
        
        self.log.w('Перезагрузка информации о конфигурации программы.')
        self.config = self.Reader.load("data\\config")
    
    def saveconfig(self): # сохранение конфига
        
        self.log.w('Сохранение информации о конфигурации программы.')
        self.config = self.Reader.save("data\\config",self.config)
    
    def SaveAndExit(self): # выход из игры
        
        self.saveconfig()
        self.log.w('/$end$')
        
        pygame.quit()
        sys.exit()
    
UTTT = Main() # Создание экземпляра основного класса

UTTT.start() # Запуск основной функции

#@SLL https://github.com/SlavaSlavyan