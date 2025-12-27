import pygame

from src.input.mouse import Mouse

class Event:

    def __init__(self,mainself):
        self.Mouse = Mouse(mainself)
    
    def main(self,mainself):

        self.Mouse.pos = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                mainself.stop()
            
            self.Mouse.main(mainself,event)
        
        self.logic(mainself)

        self.Mouse.reset(mainself)
    
    def logic(self,mainself):
        exec(f"mainself.Scenes.{mainself.status}.Logic.main(mainself)")