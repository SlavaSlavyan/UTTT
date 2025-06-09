import pygame

from function.inputs.MouseInput import MouseInput

from function.scenes.Logo import Logo

class PlayerInput:

    def __init__(self,m):
        
        m.Log.write("Инициализация класса ввода от пользователя.","DEBUG")
        
        self.MI = MouseInput(m)
        
        self.Logo = Logo(m)

    def main(self,m):
        
        self.MI.mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                m.Log.write("Пользователь запустил эвент выхода.","WARNING")
                m.stop()
            
            self.MI.main(m,event)
        
        self.logic(m)
    
    def logic(self,m):
        pass