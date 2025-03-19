import pygame
import sys

# исмпорт библиотек sll
from func.Logs import Log
from func.PlayerInput import PlayerInput
from func.Reader import Reader
from display.main import Display

class Main: # основной класс игры который является корнем игры. В него импортируются все остальные классы.
    
    def __init__(self):
        
        self.status = 'logo'
        
        self.Reader = Reader()
        
        self.config = self.Reader.load("data\\config")
        
        self.log = Log(self.config)
        
        self.log.w('[INIT] Инициализация основного класса. -->')
        self.log.w(f'[INFO] Конфигурация программы: {self.config}.')
        self.log.w(f'[INFO] Начальный статус: {self.status}.')
        
        try:
            
            self.Disp = Display(self)
            self.PI = PlayerInput(self)

            self.log.w('[INFO] Все библиотеки загружены успешно.')
            
        except Exception as err:
            
            self.log.w(f'[ERROR] Произошла ошибка при инициализации одной из библиотек: {err}.')
            self.SaveAndExit()
        
        pygame.init() # запуск pygame
        
        self.setConfigurations()
        
        self.log.w("[INIT] Конец инициализации. <--\n")
    
    def start(self): # функция для страта программы
        
        self.log.w("[FUNC] Запуск игры...\n")
        
        while True: # Основной цикл
            
            try:
                
                self.Disp.main(self) # отрисовка кадра
                
                self.PI.main(self) # Взаимодействие пользователя с игрой
                
                pygame.display.flip() # обновление кадра (вывод)
                self.Disp.clock.tick(self.config['maxfps']) # ограничение кадров в секунду соответствующее максимальному значению в cofig
                
            except Exception as err:
                
                self.log.w(f"[ERROR] {err}")
                self.SaveAndExit()
        
    def setConfigurations(self): # функция для выставления базовых настроек программы.
        
        self.log.w('[FUNC] Выставление настроек pygame.')
        pygame.display.set_caption("Ultimate Tic Tac Toe 2.10.1 DEV")
        pygame.mouse.set_visible(True)
    
    def reloadconfig(self): # перезагрузка конфига
        
        self.log.w('[FUNC] Перезагрузка информации о конфигурации программы.')
        self.config = self.Reader.load("data\\config")
    
    def saveconfig(self): # сохранение конфига
        
        self.log.w('[FUNC] Сохранение информации о конфигурации программы.')
        self.config = self.Reader.save("data\\config",self.config)
    
    def SaveAndExit(self): # выход из игры
        
        self.log.w('[WARNING] Запущена функция отключения программы!')
        self.saveconfig()
        self.log.w('/$end$')
        
        pygame.quit()
        sys.exit()
    
UTTT = Main() # Создание экземпляра основного класса

UTTT.start() # Запуск основной функции

#@SLL https://github.com/SlavaSlavyan