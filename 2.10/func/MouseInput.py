import pygame

class MouseInput: # этот класс отвечает за отслеживание ввода с мыши
    
    def __init__(self,m):
        
        m.log.w('[INIT] Инициализация класса MouseInput.')
        
        self.mouse_pos = pygame.mouse.get_pos() # позиция мыши на экране
        self.mouse = {"LT":False,"RT":False} # зажатые мыши
        self.clicked = [False,False] # переменная для проверки единичного нажатия
    
    def main(self,m,event):
        
        self.mouse_pos = pygame.mouse.get_pos()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if event.button == 3:
                
                self.mouse['RT'] = True
                self.clicked[1] = True
                m.log.w(f'[MOUSE/RT] Правая кнопка мыши была нажата на координатах {self.mouse_pos}')
            
            if event.button == 1:
                
                self.mouse['LT'] = True
                self.clicked[0] = True
                m.log.w(f'[MOUSE/LT] Левая кнопка мыши была нажата на координатах {self.mouse_pos}')
        
        if event.type == pygame.MOUSEBUTTONUP:
            
            if event.button == 3:
                
                self.mouse['RT'] = False
                self.clicked[1] = False
                m.log.w(f'[MOUSE/RT] Правая кнопка мыши была отжата на координатах {self.mouse_pos}')
            
            if event.button == 1:
                
                self.mouse['LT'] = False
                self.clicked[0] = False
                m.log.w(f'[MOUSE/LT] Левая кнопка мыши была отжата на координатах {self.mouse_pos}')
        
        self.logic(m)
        
        self.clicked = [False,False]

    def logic(self,m):
        
        if True in self.clicked:
            
            pass