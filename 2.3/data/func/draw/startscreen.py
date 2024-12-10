from data.func.endfunc import *

size = float(config("size"))
colors = getThem()
startscreen = {
    "ratio":None,
    "offset":None
}

class StartScreen:

    def __init__(self,args):
        
        self.args = args
    
    def main(self):

        self.args['screen'].fill((0,0,0))

        if self.args['anim'] == 1:


            self.args['anim'] = 1.1

        return self.args['anim'], self.args['status']