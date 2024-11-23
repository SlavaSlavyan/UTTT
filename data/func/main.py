from data.func.draw import *

pygame.init()

width, height = 1000, 800
screen = pygame.display.set_mode((width, height),pygame.RESIZABLE)
pygame.display.set_caption("Ultimate Tic Tac Toe 2.0.6")

status = 0
anim = 0

class Main:

    def main():

        global width, height, anim

        while True:

            width, height = screen.get_size()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    Main.click(x,y)
            
            anim = Draw([screen,width,height],anim).main()

            pygame.display.flip()
            pygame.time.Clock().tick(300)
    
    def click(x,y):

        global anim, width, height,status

        x = width//2 - x
        y = height//2 - y

        if status == 0:

            if anim >= 0 and anim < 1:
                anim = 1
        
            elif anim == 1.1:
                anim = 1.2
            
            elif anim == 1.2:
                status = Main.startscreen(x,y)
        
        elif status == 1:
            print('gameshit')
        
        elif status == 2:
            print('яицо')
        
        if status == 3:
            pygame.quit()
            sys.exit()
    
    def startscreen(x,y):

        for i in range(3):

            if x > -200 and x < 200 and y > -50-55*i and y < -55*i:
                print(f'yea >_> {i+1}')
                return i+1
        
        print('nah >:(')
        return 0