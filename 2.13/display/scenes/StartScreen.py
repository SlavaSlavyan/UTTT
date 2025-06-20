class StartScreen:

    def __init__(self,m):
        
        self.offset = [100]
        
        for i in range(5):
            self.offset.append(self.offset[-1]*2)

    def main(self,m):

        m.Disp.screen.fill(m.Disp.colors['StartScreen']['bg'])