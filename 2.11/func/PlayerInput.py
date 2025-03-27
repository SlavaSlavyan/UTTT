import pygame

# Класс обработки ввода от игрока
class PlayerInput:
    
    def __init__(self,m):
        
        m.log.write('[DEBUG] Инициализация класса Func.PlayerInput')
        
    def main(self,m):
        
        for event in pygame.event.get(): # проверка всех эвентов в pygame
            
            if event.type == pygame.QUIT: # выход из игры
                
                m.log.write('[DEBUG] Запуск инструкций для отключения программы')
                
                m.end() # запуск функции для выхода из игры