from data.func.endfunc import *

class StartScreenGame:
    
    def __init__(self,args,x,y):
        
        self.args = args
        self.x = x
        self.y = y

    def main(self):
        
        StartScreenGame.startscreenclick(self)

        return self.args['anim'], self.args['status']
    
    def startscreenclick(self):
        
        x = self.x - self.args['width']//2
        y = self.y - self.args['height']//2

        print(f"Pos: {x,y}")