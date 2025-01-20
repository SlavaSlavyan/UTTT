import pygame

from function.filereader import File

class WorkSpace:

    def __init__(self,m):
        
        self.figures = File.load("test")

    def main(self,m):

        WorkSpace.move_offset(self,m)

        return m
    
    def move_offset(self,m):

        if m.Disp.mouse_pressed == True:
            m.Disp.WS.offset = [m.Disp.WS.last_offset[0]-(m.Disp.mouse_pos_last[0]-m.Disp.mouse_pos[0]),m.Disp.WS.last_offset[1]+m.Disp.mouse_pos_last[1]-m.Disp.mouse_pos[1]]