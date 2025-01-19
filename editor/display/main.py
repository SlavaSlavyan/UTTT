import pygame

from display.workspace import WorkSpace

class Display:

    def __init__(self,m):
        
        self.WS = WorkSpace(m)

    def main(self,m):

        m = self.WS.main(m)

        return m