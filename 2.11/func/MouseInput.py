import pygame

class MouseInput:
    
    def __init__(self,m):
        m.log.write('[DEBUG] Инициализация класса PlayerInput.MouseInput')
        
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse = {"rt":False,"lt":False}
        self.clicked = {"rt":False,"lt":False}
    
    def main(self,m,event):
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if event.button == 3:
                
                self.mouse['rt'] = True
                self.clicked['rt'] = True
                
                m.log.write(f'[INFO] Зажата правая клавиша мыши {self.mouse_pos}.')
            
            if event.button == 1:

                self.mouse['lt'] = True
                self.clicked['lt'] = True
                
                m.log.write(f'[INFO] Зажата левая клавиша мыши {self.mouse_pos}.')
        
        if event.type == pygame.MOUSEBUTTONUP:

            if event.button == 3:

                self.mouse['rt'] = False
                
                m.log.write(f'[INFO] Разжата правая клавиша мыши {self.mouse_pos}.')
            
            if event.button == 1:

                self.mouse['lt'] = False
                
                m.log.write(f'[INFO] Разжата левая клавиша мыши {self.mouse_pos}.')