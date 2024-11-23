from data.func.read import *

gamescreen = []

class GameScreen:

    def __init__(self,swh,anim):
            
        self.screen = swh[0]
        self.width = swh[1]
        self.height = swh[2]
        self.anim = anim
    
    def main(self):

        global gamescreen