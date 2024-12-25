from function.endfunc import *
from display.main import Display
class Main:

    def __init__(self):

        pygame.init()
        
        self.status = 'loading'
        self.anim = 'game_start'
        self.zoom = 1
        self.keyF3 = False
        self.fps = int
        self.clock = pygame.time.Clock()
        self.colors = {"bg_gray":(40, 44, 52),
                       "bg_darkgray":(33, 37, 43),
                       "lightgray":(171,178,191),
                       "secondlightgray":(92, 99, 112),
                       "yellow":(229, 192, 123),
                       "green":(152, 195, 121),
                       "blue":(97, 175, 239),
                       "orange":(198, 107, 60),
                       "red":(194, 64, 52),
                       "black":(0,0,0)}

        Main.setscreen(self)

        self.display = Display(self)

        icon = pygame.image.load("3767084.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Ultimate Tic Tac Toe 2.5.0 DEV")

    
    def main(self):
        
        while True:

            self.width, self.height = self.screen.get_size()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        self.zoom += 0.1
                    elif event.button == 5:
                        self.zoom -= 0.1
                    elif event.button == 2:
                        self.zoom = 1
                    x, y = event.pos
                    #Main.click(x,y)
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F11:
                        Main.f11(self)
                    if event.key == pygame.K_F3:
                        if self.keyF3 == True:
                            self.keyF3 = False
                        else:
                            self.keyF3 = True

            self = self.display.main(self)

            if self.keyF3 == True:
                Main.f3(self)
            
            self.fps = int(self.clock.get_fps())

            pygame.display.flip()
            self.clock.tick(60)

    def f11(self):

        new_config = Config.read()

        if self.config['fullscreen'] == False:
            new_config['fullscreen'] = True

        else:
            new_config['fullscreen'] = False

        Config.write(new_config)
        Main.setscreen(self)
    
    def f3(self):

        font = pygame.font.Font('assets\\Title.ttf', 15)
        outputText = [f'Screen: {self.width}x{self.height}',
                      f'Status: {self.status}',
                      f'Anim: {self.anim}',
                      f'Zoom: {str(self.zoom)[:3]}',
                      f'FPS: {self.fps}',
                      f'Fullscreen: {self.config['fullscreen']}',]
        
        for i in range(len(outputText)):
            text_surface = font.render(outputText[i], True, (255,255,255))
            self.screen.blit(text_surface, (10, 10+15*i))
    
    def setscreen(self):

        self.config = Config.read()

        if self.config['fullscreen'] == False:

            info = pygame.display.Info()

            self.width = info.current_w//1.5
            self.height = info.current_h//1.25
            self.screen = pygame.display.set_mode((self.width, self.height),pygame.RESIZABLE)
        
        else:

            self.screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
            self.width, self.height = self.screen.get_size()