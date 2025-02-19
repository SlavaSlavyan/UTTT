import pygame

from func.mouse import Mouse
from func.keyboard import Keyboard

class PlayerInput: # Класс отвечающий за ввод информации от игрока

    def __init__(self,m):
        
        self.Mouse = Mouse(m) 
        self.Keyboard = Keyboard(m) 

    def main(self,m): # Основная фуункция класса

        self.Mouse.getpos(m)

        for event in pygame.event.get(): # проверка всех ивентов в pygame (клавиатура/мышь)

            pass
