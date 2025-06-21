import pygame

from function.inputs.MouseInput import MouseInput
from function.inputs.KeyInput import KeyInput

from function.scenes.Logo import Logo
from function.scenes.StartScreen import StartScreen

class PlayerInput:

    def __init__(self,m):
        
        m.Log.write("Инициализация класса ввода от пользователя.","DEBUG")
        
        self.MI = MouseInput(m)
        self.KI = KeyInput(m)
        
        self.Logo = Logo(m)
        self.StartScreen = StartScreen(m)

    def main(self,m):
        
        self.MI.mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                m.Log.write("Пользователь запустил эвент выхода.","WARNING")
                m.stop()
            
            self.MI.main(m,event)
            self.KI.main(m,event)
        
        self.logic(m)
        
        self.MI.reload_mouse(m)
        self.KI.reload_keyboard(m)
    
    def logic(self,m):
        
        self.KI.logic_main(m)
        
        if m.Disp.anim[:4] == "Logo":
            self.Logo.main(m)
        
        elif m.Disp.anim[:11] == "StartScreen":
            self.StartScreen.main(m)