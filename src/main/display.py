import pygame
import traceback

class Display:

    def __init__(self,mainself):

        self.colors = [
            (0,0,0), # 0 black
            (218, 192, 123), # 1 yellow
            (40, 44, 52), # 2 gray
            (33, 37, 43)
        ]

        self.screen = pygame.display.set_mode([800,800], pygame.RESIZABLE)

        self.Clock = pygame.time.Clock()

        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        self.anim = 'logo'

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
        
        try:
            exec(f"mainself.Scenes.{self.anim}.Display.main(mainself)")
        except Exception:
            self.error(traceback.format_exc().split('\n'))

        pygame.display.flip()

    def error(self,error:str):
        self.screen.fill((0,0,255))
        font = pygame.font.Font(None,16)
        for i in range(len(error)):
            text = font.render(error[i], 1,(255,255,255))
            self.screen.blit(text,(10,10+16*i))
    
    def gradient(self, color1: tuple, color2: tuple, steps: int) -> list:
        
        gradient = []
        
        for step in range(steps + 1):
            r = int(color1[0] + (color2[0] - color1[0]) * step / steps)
            g = int(color1[1] + (color2[1] - color1[1]) * step / steps)
            b = int(color1[2] + (color2[2] - color1[2]) * step / steps)
            gradient.append((r, g, b))
        
        return gradient