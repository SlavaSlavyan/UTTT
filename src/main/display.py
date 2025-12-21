import pygame

class Display:

    def __init__(self,mainself):

        self.colors = [
            (0,0,0), # 0 black
            (218, 192, 123) # 1 yellow
        ]

        self.screen = pygame.display.set_mode([800,800], pygame.RESIZABLE)

        self.Clock = pygame.time.Clock()

        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        # fps
        # speed
        # zoom

    def main(self,mainself):

        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.zoom = min(self.width,self.height)/800 * mainself.config['zoom']
        self.fps = self.Clock.get_fps()
        try: self.speed = 60/self.fps
        except: self.speed = 0

        mainself.Scenes.logo.Display.main(mainself)

        pygame.display.flip()