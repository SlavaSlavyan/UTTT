import pygame

class Mouse: # Функции мыши

    def __init__(self,m):
        
        pass

    def getpos(self,m): # Позиция курсора на экране

        self.pos = pygame.mouse.get_pos()