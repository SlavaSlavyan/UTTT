import pygame

class Event:

    def __init__(self,mainself):
        pass
    
    def main(self,mainself):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                mainself.stop()
        
        self.logic(mainself)
    
    def logic(self,mainself):

        exec(f"mainself.Scenes.{mainself.status}.Logic.main(mainself)")