import pygame

class Buttons:

    def __init__(self,mainself):

        self.back_surface = pygame.Surface((50,50),pygame.SRCALPHA)
        self.back_transparency = 50

    def main(self,mainself):
        
        self.back(mainself)

    def back(self,mainself):

        self.back_surface.fill((0,0,0,0))

        self.back_surface.fill((*mainself.Display.colors[3],self.back_transparency))

        pygame.draw.polygon(self.back_surface,(*mainself.Display.colors[4],self.back_transparency),
                            [[35,10],[10,25],[35,40]])
        
        mainself.Display.screen.blit(self.back_surface,(mainself.Display.width-60,10))
    
    def back_logic(self,mainself):
        pass