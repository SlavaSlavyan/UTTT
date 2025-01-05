from two import Addition

class Main:

    def __init__(self):
        
        self.var = 'Hi'
        self.Addition = Addition(self)
    
    def main(self):
        
        while True:
            
            action = input('> ')

            if action == '1':
                self.Addition.main(self)
                

Start = Main()

Start.main()