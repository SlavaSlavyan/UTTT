from data.func.drawfunc import *

pygame.init()

fullscreen = config('fullscreen')
size = float(config('scale'))

if fullscreen == "False":
    width, height = 1000*size, 800*size
    screen = pygame.display.set_mode((width, height),pygame.RESIZABLE)

else:
    infoObject = pygame.display.Info()
    width, height = infoObject.current_w, infoObject.current_h
    screen = pygame.display.set_mode((width, height),pygame.FULLSCREEN)

pygame.display.set_caption("Ultimate Tic Tac Toe 2.2.1 DEV")

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

        global status,anim

        if status == 0:
            if anim >= 0 and anim < 1:
                anim = 1
            elif anim >= 1 and anim < 1.2:
                anim = 1.2
                status = 1
        elif status == 1:
            if anim == 1.2:
                arg = Main.startscreenclick(x,y)
                if arg != None:
                    status = 2+arg
                    anim = 1.3
        
    def startscreenclick(x,y):

        x = width//2-x
        y = height//2-y

        selected_button = 0

        for i in range(3):
            if x < 200 and x > -200 and y < 0+50*i and y > -50+50*i:
                return selected_button
            
            else:
                selected_button += 1
        
        return None
        