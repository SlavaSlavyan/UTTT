from data.func.draw import *

pygame.init()

width, height = 1000, 800
screen = pygame.display.set_mode((width, height),pygame.RESIZABLE)
pygame.display.set_caption("Ultimate Tic Tac Toe 2.0.2")

class StartScreen:

    def main():

        global width, height

        while True:

            screen.fill(getcolor(0))
            width, height = screen.get_size()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
            
            Draw.StartScreen([screen,width,height]).main()

            pygame.display.flip()
            pygame.time.Clock().tick(300)