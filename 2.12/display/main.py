import pygame

from display.Text import Text
from display.Logo import Logo
from display.StartScreen import StartScreen

class Display:

    def __init__(self,m):

        self.colors = m.JsonManager.load(f'data\\them\\{m.config['them']}')

        self.anim = "logo_start"
        print(f'Start-anim={self.anim}')
        self.old_anim = self.anim

        self.width, self.height = m.config['start-screensize']
        
        self.setscreen(m)

        self.Text = Text(m)
        self.Logo = Logo(m,self)
        self.StartScreen = StartScreen(m,self)

        self.clock = pygame.time.Clock()
        self.fps = self.clock.get_fps()

        self.animSpeed = 1
        self.max_zoom = 0

    def main(self,m):

        self.fps = self.clock.get_fps()

        if self.fps != 0:
            self.animSpeed = 60/self.fps
        else:
            self.animSpeed = 0

        self.width, self.height = self.screen.get_size()
        self.max_zoom = round(min([self.width/1200 - 1,self.height/800 - 1]),1)

        if self.anim[:4] == 'logo':
            self.Logo.main(m)
        
        elif self.anim[:11] == 'startscreen':
            self.StartScreen.main(m)
        
        else:
            
            z = m.config['zoom'] + m.Disp.max_zoom

            self.screen.fill(self.colors['main']['error'])

            m.Disp.Text.title(m,m.Disp.Text.text['main'][0],100*z,(0,50*z),self.colors['main']['f3-text'])
            m.Disp.Text.title(m,self.anim,50*z,(0,-20*z),self.colors['main']['f3-text'])
        
        self.Text.F3(m)

    def setscreen(self,m):
        
        if m.config['fullscreen']:
            self.screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN | pygame.DOUBLEBUF)
        else:
            self.screen = pygame.display.set_mode((m.config['start-screensize'][0],m.config['start-screensize'][1]),pygame.DOUBLEBUF | pygame.RESIZABLE)

    def gradient(self,color1: tuple, color2: tuple, steps: int):
        
        gradient = []
        
        for step in range(steps + 1):
            r = int(color1[0] + (color2[0] - color1[0]) * step / steps)
            g = int(color1[1] + (color2[1] - color1[1]) * step / steps)
            b = int(color1[2] + (color2[2] - color1[2]) * step / steps)
            gradient.append((r, g, b))
        
        return gradient
