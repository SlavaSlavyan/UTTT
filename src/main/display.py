import pygame

from src.utils.cursor_display import Cursor

class Display:

    def __init__(self,mainself):

        self.colors = [
            (0,0,0), # 0 black
            (218, 192, 123), # 1 yellow
            (40, 44, 52), # 2 gray
            (33, 37, 43), # 3 dark gray
            (171, 178, 191), # 4 white
            (127, 134, 144), # 5 light_gray
            (229, 192, 123), # 6 yellow
            (89, 175, 239), # 7 blue
            (209, 154, 102), # 8 orange
            (224, 108, 117) # 9 red
        ]

        self.text = [
            ["ИГРОК 0","ИГРОК X","ПОБЕДИЛ"]
        ]

        self.screen = pygame.display.set_mode([800,800], pygame.RESIZABLE)

        self.Cursor = Cursor(mainself)
        self.Clock = pygame.time.Clock()

        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        # fps
        # speed
        # zoom

    def main(self,mainself):

        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        self.zoom = min(self.width,self.height)/800

        self.fps = self.Clock.get_fps()

        try: self.speed = 60/self.fps
        except: self.speed = 0

        exec(f"mainself.Scenes.{mainself.status}.Display.main(mainself)")

        self.Cursor.main(mainself)
        
        pygame.display.flip()

    def gradient(self, color1: int, color2: int, steps: int) -> list:

        color1 = self.colors[color1]
        color2 = self.colors[color2]

        gradient = []
        
        for step in range(steps + 1):
            r = int(color1[0] + (color2[0] - color1[0]) * step / steps)
            g = int(color1[1] + (color2[1] - color1[1]) * step / steps)
            b = int(color1[2] + (color2[2] - color1[2]) * step / steps)
            gradient.append((r, g, b))
        
        return gradient