from data.func.endfunc import *

size = float(config("size"))

class StartScreenGame:
    
    def __init__(self,args,x,y):
        
        self.args = args
        self.x = x
        self.y = y

    def main(self):
        
        arg = StartScreenGame.startscreenclick(self)

        if arg != None:
            self.args['status'] = arg+2
            self.args['anim'] = 1.3

        return self.args['anim'], self.args['status']
    
    def startscreenclick(self):
        
        x = self.x - self.args['width']//2
        y = self.y - self.args['height']//2

        print(f"Pos: {x,y}")
        
        for i in range(3):

            if x > -200*size and x < 200*size and y < 50*size+55*size*i and y > 55*size*i:
                return i
        
        return None