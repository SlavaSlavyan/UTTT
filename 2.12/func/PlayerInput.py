import pygame

from func.MouseInput import MouseInput

class PlayerInput:
    
    def __init__(self,m):
        
        self.MI = MouseInput(self)
        
    def main(self,m):

        self.MI.mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                m.end()
            
            self.MI.main(m,event)
            self.MI.clicked = {"rt":False,"lt":False}
        
        self.MI.zooming(m)