import pygame

from display.game import Game

class Display:

    def __init__(self,m):
        
        self.anim = 'game_start'
        self.colors = {
            "dark":{
                "background":(40, 44, 52)
            }
        }
        self.Game = Game
    
    def main(self,m):

        if self.anim == 'game_start':

            self.Game.start(m)