import pygame

class Cursor:

    def __init__(self,mainself):

        self.size = 1
        self.display = True
    
    def main(self,mainself):

        if self.display:

            z = self.size
            
            x,y = mainself.Event.Mouse.pos

            points = [[x,y],[x,y+17*z],[x+17*z,y]]
            points2 = [[x+2*z,y+2*z],[x+2*z,y+12*z],[x+12*z,y+2*z]]

            pygame.draw.polygon(mainself.Display.screen,mainself.Display.colors[1],points)
            pygame.draw.polygon(mainself.Display.screen,mainself.Display.colors[2],points2)