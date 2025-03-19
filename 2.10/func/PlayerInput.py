import pygame

from func.MouseInput import MouseInput

class PlayerInput: # этот класс отвечает за все заимодействия пользователя с игрой
    
    def __init__(self,m):
        
        m.log.w('[INIT] Инициализация класса PlayerInput.')
        
        self.MI = MouseInput(m) # класс для взаимодействия с мышью
     
    def main(self,m): # проверка ввода от игрока
        
        for event in pygame.event.get(): # Проверка всех ивентов в pygame

            if event.type == pygame.QUIT: # Операция выхода из игры

                m.SaveAndExit() # Вызов функции выхода из игры с сохранением информации
            
            self.MI.main(m,event) # Проверка нажаний мышью