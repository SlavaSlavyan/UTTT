from data.func.endfunc import *
from data.func.draw.logo import Logo
from data.func.draw.startscreen import StartScreen

class Draw:

    def __init__(self,args):
        
        self.args = args
        self.anim = args[3]
    
    def main(self):

        if self.anim >= 0 and self.anim < 1:
            self.anim = Logo(self.args).main()

        elif self.anim >= 1 and self.anim < 2:
            self.anim = StartScreen(self.args).main()

        return self.anim