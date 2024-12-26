from data.func.endfunc import *
from data.func.draw.logo import Logo
from data.func.draw.startscreen import StartScreen

class Draw:

    def __init__(self,args):
        
        self.args = args
    
    def main(self):

        if self.args['anim'] >= 0 and self.args["anim"] < 1:
            self.args['anim'] = Logo(self.args).main()
        
        elif self.args['anim'] >= 1 and self.args["anim"] < 2:
            self.args['anim'], self.args['status'] = StartScreen(self.args).main()

        return self.args['anim'], self.args['status']