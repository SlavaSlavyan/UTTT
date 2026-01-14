import pygame

class Buttons:

    def __init__(self,mainself):

        self.back_surface = pygame.Surface((50,50),pygame.SRCALPHA)
        self.back_transparency = 0

        # selected_button

    def main(self,mainself):

        self.selected_button = mainself.Scenes.game.Logic.Buttons.select_button(mainself)
        
        self.back(mainself)

    def back(self,mainself):

        self.back_surface.fill((0,0,0,0))

        self.back_surface.fill((*mainself.Display.colors[3],self.back_transparency))

        pygame.draw.polygon(self.back_surface,(*mainself.Display.colors[4],self.back_transparency),
                            [[35,10],[10,25],[35,40]])
        
        mainself.Display.screen.blit(self.back_surface,(10,70))

        self.back_logic(mainself)
    
    def back_logic(self,mainself):
        
        if mainself.Scenes.game.Logic.Buttons.select_button(mainself) == 1:
            
            if self.back_transparency < 255:

                self.back_transparency += 8*mainself.Display.speed

            if self.back_transparency > 255:
                self.back_transparency = 255

        else:

            if self.back_transparency > 63:

                self.back_transparency -= 8*mainself.Display.speed

                if self.back_transparency < 63:
                    self.back_transparency = 63
            
            if self.back_transparency < 63:

                self.back_transparency += 8*mainself.Display.speed

                if self.back_transparency > 63:
                    self.back_transparency = 63