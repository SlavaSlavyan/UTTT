import pygame

class Display:

    def __init__(self,mainself):

        self.counter = 1
        self.anim = 0

    def main(self,mainself):

        z = mainself.Display.zoom

        mainself.Display.screen.fill(mainself.Display.colors[2])

        if self.anim == 0:

            pygame.draw.rect(mainself.Display.screen,mainself.Display.colors[3],
                             (mainself.Display.width//2 -300*z*-(self.counter-1),
                              mainself.Display.height//2 -300*z*-(self.counter-1),
                              600*z*-(self.counter-1),600*z*-(self.counter-1)))
            
            self.counter /= (1 + 0.1*mainself.Display.speed)

            if round(self.counter,2) == 0:
                self.anim = 1
                self.counter = 1
        
        elif self.anim == 1:

            pygame.draw.rect(mainself.Display.screen,mainself.Display.colors[3],
                             (mainself.Display.width//2 -300*z,mainself.Display.height//2 -300*z,600*z,600*z))


            pygame.draw.line(mainself.Display.screen,mainself.Display.colors[4],
                            (mainself.Display.width//2 + 300*z - mainself.Display.width*self.counter,
                            mainself.Display.height//2 - 100*z),
                            (mainself.Display.width//2 - 300*z - mainself.Display.width*self.counter,
                            mainself.Display.height//2 - 100*z),
                            round(5*z))

            pygame.draw.line(mainself.Display.screen,mainself.Display.colors[4],
                            (mainself.Display.width//2 + 300*z + mainself.Display.width*self.counter,
                            mainself.Display.height//2 + 100*z),
                            (mainself.Display.width//2 - 300*z + mainself.Display.width*self.counter,
                            mainself.Display.height//2 + 100*z),
                            round(5*z))
            
            pygame.draw.line(mainself.Display.screen,mainself.Display.colors[4],
                            (mainself.Display.width//2 - 100*z,
                            mainself.Display.height//2 + 300*z + mainself.Display.height*self.counter),
                            (mainself.Display.width//2 - 100*z ,
                            mainself.Display.height//2 - 300*z + mainself.Display.height*self.counter),
                            round(5*z))
            
            pygame.draw.line(mainself.Display.screen,mainself.Display.colors[4],
                            (mainself.Display.width//2 + 100*z,
                            mainself.Display.height//2 + 300*z - mainself.Display.height*self.counter),
                            (mainself.Display.width//2 + 100*z,
                            mainself.Display.height//2 - 300*z - mainself.Display.height*self.counter),
                            round(5*z))
            
            self.counter /= (1 + 0.1*mainself.Display.speed)

            if round(self.counter,2) == 0:
                self.anim = 1
                self.counter = 1
        
        elif self.anim == 2:

            pygame.draw.rect(mainself.Display.screen,mainself.Display.colors[3],
                             (mainself.Display.width//2 -300*z,mainself.Display.height//2 -300*z,600*z,600*z))


            pygame.draw.line(mainself.Display.screen,mainself.Display.colors[2],
                            (mainself.Display.width//2 + 300*z,
                            mainself.Display.height//2 - 100*z),
                            (mainself.Display.width//2 - 300*z,
                            mainself.Display.height//2 - 100*z),
                            round(5*z))

            pygame.draw.line(mainself.Display.screen,mainself.Display.colors[2],
                            (mainself.Display.width//2 + 300*z,
                            mainself.Display.height//2 + 100*z),
                            (mainself.Display.width//2 - 300*z,
                            mainself.Display.height//2 + 100*z),
                            round(5*z))
            
            pygame.draw.line(mainself.Display.screen,mainself.Display.colors[2],
                            (mainself.Display.width//2 - 100*z,
                            mainself.Display.height//2 + 300*z),
                            (mainself.Display.width//2 - 100*z,
                            mainself.Display.height//2 - 300*z),
                            round(5*z))
            
            pygame.draw.line(mainself.Display.screen,mainself.Display.colors[2],
                            (mainself.Display.width//2 + 100*z,
                            mainself.Display.height//2 + 300*z),
                            (mainself.Display.width//2 + 100*z,
                            mainself.Display.height//2 - 300*z),
                            round(5*z))