import pygame

from func.MouseInput import MouseInput
from func.KeyInput import KeyInput

from func.StartScreen import StartScreen

class PlayerInput:
    
    def __init__(self,m):
        
        self.MI = MouseInput(m)
        self.KI = KeyInput(m)
        
        self.StartScreen = StartScreen(m)
        
    def main(self,m):

        self.MI.mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                m.end()
            
            self.MI.main(m,event)
            self.KI.main(m,event)
            
            self.logicOn(m)
            
            self.MI.clicked = {"rt":False,"lt":False}
            self.MI.released = {"rt":False,"lt":False}
        
        self.MI.zooming(m)
    
    def logicOn(self,m):
        
        if m.status == 'logo':
            
            if True in self.MI.clicked.values() or True in self.KI.keys.values():

                m.Sound.play(m,'skip')
                
                print("[INFO] Skip logo")
                
                m.status = 'startscreen_start'
                m.Disp.anim = 'startscreen_start'
                m.Time.removetimer(m,'logo')
        
        if m.status == 'startscreen':
            
            if self.MI.released['lt']:
                self.StartScreen.onclick(m)