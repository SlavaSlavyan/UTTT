import pygame

from display.game import Game

class Display:

    def __init__(self,m):
        
        self.mouse_pos = pygame.mouse.get_pos()
        self.anim = 'game_start'
        self.colors = {
            "dark":{
                "game":{
                    "bg":(40, 44, 52),
                    "darkbg":(33, 37, 43)
                }
            }
        }
        self.offset = [0,0]
        self.ratio = [m.width/100,m.height/100]
        self.Game = Game(m,self)
    
    def main(self,m):

        self.ratio = [m.width/100,m.height/100]

        if self.anim == 'game_start':

            self.Game.start(m)
        
        self.cursor(m)
    
    def cursor(self,m):

        self.mouse_pos = pygame.mouse.get_pos()