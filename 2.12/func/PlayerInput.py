import pygame

from func.MouseInput import MouseInput

from func.StartScreen import StartScreen

class PlayerInput:
    
    def __init__(self,m):
        
        self.MI = MouseInput(self)
        
        self.StartScreen = StartScreen(m)
        
    def main(self,m):

        self.MI.mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                m.end()
            
            self.MI.main(m,event)
            
            self.logic(m)
            
            self.MI.clicked = {"rt":False,"lt":False}
            self.MI.released = {"rt":False,"lt":False}
        
        self.MI.zooming(m)
    
    def logic(self,m):
        
        if True in self.MI.clicked.values():
            m.Sound.click(m)
        
        if m.status == 'logo':
            
            if True in self.MI.clicked.values():
                
                print("[INFO] Skip logo")
                
                m.status = 'startscreen_start'
                m.Disp.anim = 'startscreen_start'
                m.Time.removetimer(m,'logo')
        
        elif m.status == 'startscreen_start':
            if True in self.MI.mouse.values():
                m.Disp.animSpeed *= 2