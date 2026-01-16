import pygame

class Win:

    def __init__(self,mainself):
        
        self.counter = 1.001
        self.counter_bool = True
        self.speed = 0.1
        self.timer = 0

    def main(self,mainself):
        
        counter = self.counter-0.001

        self.rect(mainself,counter)

        if self.counter_bool:

            if self.speed > 0:
                self.counter /= (1 + self.speed*mainself.Display.speed)
            if self.speed < 0:
                self.counter *= (1 - self.speed*mainself.Display.speed)

    def rect(self,mainself, counter: float):

        z = mainself.Display.zoom

        rect = (mainself.Display.width//2 -250*z*-(counter-1),
                mainself.Display.height//2 -150*z*-(counter-1),
                500*z*-(counter-1),300*z*-(counter-1))

        pygame.draw.rect(mainself.Display.screen,mainself.Display.colors[2],
                        rect)
        
        pygame.draw.rect(mainself.Display.screen,mainself.Display.colors[7+mainself.Scenes.game.Logic.Game.win],
                        rect,round(10*z))
        
        self.text(mainself,counter,-50,mainself.Scenes.game.Logic.Game.win,7+mainself.Scenes.game.Logic.Game.win)
        self.text(mainself,counter,50,2,6)

    def text(self,mainself, counter:float, offset:float, text_id:int, color_id:int):

        z = mainself.Display.zoom

        if round(74*z*-(counter-1)) >= 0:

            font = pygame.font.Font("data\\fonts\\base.ttf", round(74*z*-(counter-1)))
            text_surface = font.render(mainself.Display.text[0][text_id], True, mainself.Display.colors[color_id])
            text_rect = text_surface.get_rect()
            text_rect.center = (mainself.Display.width // 2, mainself.Display.height // 2 + offset*z)

            mainself.Display.screen.blit(text_surface, text_rect)