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
                    "darkbg":(33, 37, 43),
                    "activecell":(171,178,191),
                    "passivecell":(92, 99, 112),
                    "player0":(97, 175, 239),
                    "playerX":(198, 107, 60),
                    "active-passive":self.gradient((171,178,191),(92, 99, 112),120),
                    "0toX":self.gradient((97, 175, 239),(198, 107, 60),120)
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
    
    def gradient(self,color1, color2, steps):

        gradient = []
        
        for step in range(steps + 1):
            r = int(color1[0] + (color2[0] - color1[0]) * step / steps)
            g = int(color1[1] + (color2[1] - color1[1]) * step / steps)
            b = int(color1[2] + (color2[2] - color1[2]) * step / steps)
            gradient.append((r, g, b))
        
        return gradient