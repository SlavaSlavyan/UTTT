from data.func.read import *
from data.func.drawfunc.logo import *
from data.func.drawfunc.startscreen import *
from data.func.drawfunc.gamescreen import *

class Draw:

    def __init__(self,swh,anim,game):
            
        self.swh = swh
        self.anim = anim
        self.game = game
    
    def main(self):

        global anim

        if self.anim >= 0 and self.anim < 1:
            self.anim = Logo(self.swh,self.anim).main()  
        
        elif self.anim >= 1 and self.anim < 2:
            self.anim = StartScreen(self.swh,self.anim).main()
        
        elif self.anim >= 2 and self.anim < 3:
            self.anim = GameScreen(self.swh,self.anim,self.game).main()
        
        return self.anim