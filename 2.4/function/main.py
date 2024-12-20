from function.endfunc import *

class Main:

    def __init__(self):

        pygame.init()
        
        self.clock = pygame.time.Clock()

        Main.setscreen(self)
        
    
    def main(self):
        
        while True:

            self.width, self.height = self.screen.get_size()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    #Main.click(x,y)
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F11:
                        Main.f11(self)

            pygame.display.flip()
            self.clock.tick(120)

    def f11(self):

        new_config = Config.read()

        if self.config['fullscreen'] == False:
            new_config['fullscreen'] = True

        else:
            new_config['fullscreen'] = False

        Config.write(new_config)
        Main.setscreen(self)
    
    def setscreen(self):

        self.config = Config.read()

        if self.config['fullscreen'] == "False":

            info = pygame.display.Info()

            self.width = info.current_w//1.5
            self.height = info.current_h//1.5
            self.screen = pygame.display.set_mode((self.width, self.height),pygame.RESIZABLE)
        
        else:

            self.screen = pygame.display.set_mode((0, 0),pygame.RESIZABLE)
            self.width, self.height = self.screen.get_size()