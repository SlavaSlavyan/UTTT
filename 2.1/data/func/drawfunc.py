from data.func.draw.logo import *

class Draw:

    def __init__(self,args):
        
        self.args = args
    
    def main(self):

        anim = Logo(self.args).main()

        return anim