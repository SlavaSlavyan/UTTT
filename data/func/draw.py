from data.func.read import *
from data.func.logo import *
from data.func.startscreen import *

anim = 1

class Draw:

    def __init__(self,swh):
            
        self.swh = swh
    
    def main(self):

        global anim

        if anim >= 0 and anim < 1:
            anim = Logo(self.swh,anim).main()
        
        elif anim >= 1 and anim < 2:
            anim = StartScreen(self.swh,anim).main()