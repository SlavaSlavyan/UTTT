import pygame

# Импорт отдельных модулей для мышки и клавиатуры
from func.MouseInput import MouseInput

# Импорт инструкций для использованния ввода
from func.StartScreen import StartScreen


# Класс обработки ввода от игрока
class PlayerInput:
    
    def __init__(self,m):
        
        m.log.write('[DEBUG] Инициализация класса Func.PlayerInput')
        
        self.MI = MouseInput(m)
        
        self.StartScreen = StartScreen(m)
        
    def main(self,m):
        
        self.MI.mouse_pos = pygame.mouse.get_pos() 
        
        for event in pygame.event.get(): # проверка всех эвентов в pygame
            
            if event.type == pygame.QUIT: # выход из игры
                
                m.log.write('[DEBUG] Запуск инструкций для отключения программы')
                
                m.end() # запуск функции для выхода из игры
            
            self.MI.main(m,event) # проверка мыши
            
            self.logic(m) # Запуск логики
            
            self.MI.clicked = {"rt":False,"lt":False} # Обновление клика
        
        self.MI.zooming(m)
    
    def logic(self,m):
        
        if m.status == 'logo':
            if any(self.MI.clicked.values()):
                m.log.write('[INFO] Пропуск анимации лого')
                
                m.Disp.anim = 'startscreen_start'
                m.status = 'loading'
                m.Time.removetimer(m,'logo')
                
        if m.status == 'startscreen':
            self.StartScreen.main(m)