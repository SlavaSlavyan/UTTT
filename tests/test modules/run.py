from m1 import M1

class Main:

    def __init__(self):
        self.var = 1
        self.m_first = M1()
    
    def main(self):
        
        self.m_first.main(self)

start = Main()

start.main()