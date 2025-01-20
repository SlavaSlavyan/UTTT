import pygame

from display.workspace import WorkSpace

class Display:

    def __init__(self,m):

        self.WS = WorkSpace(m)
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_pos_last = self.mouse_pos
        self.mouse_pressed = False

    def main(self,m):

        self.mouse_pos = pygame.mouse.get_pos()

        m = self.WS.main(m)

        return m