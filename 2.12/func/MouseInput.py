import pygame

class MouseInput:
    
    def __init__(self,m):
        
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse = {"rt":False,"lt":False}
        self.clicked = {"rt":False,"lt":False}
        self.released = {"rt":False,"lt":False}
        
        self.zoom = 0
    
    def main(self,m,event):
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if event.button == 3:
                
                self.mouse['rt'] = True
                self.clicked['rt'] = True
            
            if event.button == 1:

                self.mouse['lt'] = True
                self.clicked['lt'] = True
        
        if event.type == pygame.MOUSEBUTTONUP:

            if event.button == 3:

                self.mouse['rt'] = False
                self.released['rt'] = True
            
            if event.button == 1:

                self.mouse['lt'] = False
                self.released['lt'] = True
        
        if event.type == pygame.MOUSEWHEEL:
            
            if event.y > 0:
                self.zoom = round(self.zoom + 0.10,2)
                
            elif event.y < 0:
                self.zoom = round(self.zoom - 0.10,2)
        
    def zooming(self,m):
        
        speed = round(0.01 + abs(self.zoom)/10,2)
        
        if self.zoom > 0:
            
            self.zoom = round(self.zoom - speed,2)
            m.config['zoom'] = round(m.config['zoom'] + speed,2)
        
        elif self.zoom < 0:
            
            self.zoom = round(self.zoom + speed,2)
            m.config['zoom'] = round(m.config['zoom'] - speed,2)