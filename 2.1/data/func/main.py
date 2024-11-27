from data.func.drawfunc import *

pygame.init()

width, height = 1000, 800
screen = pygame.display.set_mode((width, height),pygame.RESIZABLE)
pygame.display.set_caption("Ultimate Tic Tac Toe 2.1.4 DEV")

status = 0
anim = 0

class Main:

    def start():

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

            anim = Draw([screen,width,height,anim]).main()

            pygame.display.flip()
            pygame.time.Clock().tick(120)
    
    def click(x,y):

        pass