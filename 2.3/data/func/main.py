from data.func.endfunc import *
from data.func.drawfunc import Draw
from data.func.draw.logo import size
from data.func.game.startscreen import StartScreenGame

pygame.init()

main = {"screen":pygame.display.set_mode((1000, 750),pygame.RESIZABLE),"width":1000,"height":750,"status":0,"anim":0}

pygame.display.set_caption("Ultimate Tic Tac Toe 2.3.2 DEV")

clock = pygame.time.Clock()
fps = 0

class Main:

    def start():

        global main,fps

        while True:

            main['width'], main['height'] = main["screen"].get_size()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    Main.click(x,y)

            main['anim'], main['status'] = Draw(main).main()
            output([f"FPS: {int(fps)}",
                    f"Status: {main['status']}",
                    f"Anim: {main['anim']}",
                    f"Width: {main['width']}",
                    f"Height: {main['height']}",
                    f"Global size: {size}"],
                    main['screen'])

            fps = clock.get_fps()

            pygame.display.flip()
            clock.tick(120)
    
    def click(x,y):

        if main['anim'] >= 0 and main["anim"] < 1:
            main["anim"] = 1

        elif main['anim'] == 1.1 or main['anim'] == 1:
            main['anim'] = 1.2
            main['status'] = 1
        
        elif main['status'] == 1:
            
            if main['anim'] == 1.2:
                StartScreenGame(main,x,y).main()
        
