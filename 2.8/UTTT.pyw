import pygame
import sys

from function.Reader import File
from display.main import Display
from function.game import Game

class Main:
    
    def __init__(self):
        
        pygame.init()

        Main.setscreen(self)

        self.fps = int
        self.maxfps = 60
        self.status = "loading"
        self.F3 = True
        self.keys = {
            "ctrl":False
        }
        self.mouse = {
            "lt":False,
            "rt":False
        }
        self.lastmousepos = [int,int]
        self.lastoffset = [int,int]
        self.clock = pygame.time.Clock()

        self.Game = Game(self)
        self.Disp = Display(self)

        pygame.display.set_caption("Ultimate Tic Tac Toe 2.8.9 DEV")
        pygame.mouse.set_visible(False)

    def main(self):

        while True:

            self.width, self.height = self.screen.get_size()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    File.save('function\\config',self.config)
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if self.keys['ctrl'] == True:
                        if event.button == 4:
                            self.config['zoom'] -= 0.1

                        if event.button == 5:
                            self.config['zoom'] += 0.1

                        if event.button == 2: 
                            self.Disp.offset = [0,0]
                            self.config['zoom'] = 1
                    
                    if event.button == 3:
                        
                        self.lastmousepos = self.Disp.mouse_pos
                        self.lastoffset = self.Disp.offset
                        self.mouse['rt'] = True
                    
                    if event.button == 1:

                        self.mouse['lt'] = True
                        self.mouseinput()
                
                if event.type == pygame.MOUSEBUTTONUP:

                    if event.button == 3:

                        self.mouse['rt'] = False
                    
                    if event.button == 1:

                        self.mouse['lt'] = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                        self.keys['ctrl'] = True
                    
                    if event.key == pygame.K_F2:
                        if self.maxfps == 60:
                            self.maxfps = 1200
                        else:
                            self.maxfps = 60

                    if event.key == pygame.K_F3:
                        Main.F3(self)
                    
                    if event.key == pygame.K_F11:
                        Main.F11(self)
                    
                    if event.key == pygame.K_z and self.keys['ctrl']:
                        self.Game.loadsave(self)
                
                if event.type == pygame.KEYUP:

                    if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                        self.keys['ctrl'] = False
            
            self.Disp.main(self)
            self.offset()
                    
            self.fps = int(self.clock.get_fps())
            self.timer()

            pygame.display.flip()
            self.clock.tick(self.maxfps)
    
    def offset(self):
        
        if self.mouse['rt'] == True:
            self.Disp.offset = [self.lastoffset[0]-self.lastmousepos[0]+self.Disp.mouse_pos[0],self.lastoffset[1]+self.lastmousepos[1]-self.Disp.mouse_pos[1]]
    
    def mouseinput(self):

        if self.Disp.anim == "game_start":
            self.Disp.anim = 'game'
            self.status = "game"
        elif self.status == 'game':
            self.Game.main(self)
    
    def F11(self):

        if self.config['fullscreen'] == False:
            self.config['fullscreen'] = True

        else:
            self.config['fullscreen'] = False
        
        File.save('function\\config',self.config)
        Main.setscreen(self)
    
    def F3(self):

        if self.F3 == True:
            self.F3 = False

        else:
            self.F3 = True
    
    def setscreen(self):

        self.config = File.load('function\\config')

        if self.config['fullscreen'] == False:

            self.width = 1200
            self.height = 800
            self.screen = pygame.display.set_mode((self.width, self.height),pygame.RESIZABLE)
        
        else:

            self.screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
            self.width, self.height = self.screen.get_size()
    
    def timer(self):

        if self.status == 'game':
            
            try:
                tick = 100/self.fps
            except:
                tick = 0
            self.Game.timer['tick'] += tick

            if self.Game.timer['tick'] >= 100:
                self.Game.timer['tick'] -= 100
                self.Game.timer['seconds'] += 1
            
            if self.Game.timer['seconds'] >= 60:
                self.Game.timer['seconds'] = 0
                self.Game.timer['minutes'] += 1

Start = Main()

Start.main()