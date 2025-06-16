import pygame
import math

from display.Text import Text
from display.scenes.Logo import Logo
from display.scenes.StartScreen import StartScreen

class Display:
    
    def __init__(self,m):

        m.Log.write("Инициализация класса отображения.","DEBUG")

        self.reload_palette(m)

        self.reload_screen(m)

        self.anim = "Logo_0"
        m.Log.write(f"Начальная сцена = {self.anim}.","DEBUG")

        self.clock = pygame.time.Clock()
        
        self.Text = Text(m)

        self.Logo = Logo(m)
        self.StartScreen = StartScreen(m)

        self.error_bg = 0
    
    def main(self,m):

        self.width, self.height = self.screen.get_size()
        
        self.fps = self.clock.get_fps()

        if self.fps == 0: self.anim_speed = 0
        else: self.anim_speed = 60/self.fps

        self.zoom = round(m.config['zoom'] + min(self.width/m.config['start-screensize'][0],self.height/m.config['start-screensize'][1]) -1,1)

        if self.anim[:4] == "Logo":
            self.Logo.main(m)
        
        if self.anim[:11] == "StartScreen":
            self.StartScreen.main(m)
        
        else:
            self.error(m)
        
        if m.config['debug']:
            self.F3(m)
    
    def F3(self,m):
        
        text = [
            f"Ultimate Tic Tac Toe {m.game_version}",
            "Created by SLL","",
            "[CONFIGURATION]","",m.config,"",
            "[MAIN]","",[
            f"Status: {m.status}",
            f"Anim: {self.anim}",
            f"Screen: [{self.width}x{self.height}]",
            f"FPS: {round(self.fps)}",
            f"Animation speed: {round(self.anim_speed,2)}",
            f"Zoom: {self.zoom}",""],
            "[MOUSE]","",[
            f"Pos: {m.PI.MI.mouse_pos}, [{self.width//2 - m.PI.MI.mouse_pos[0]}, {self.height//2 - m.PI.MI.mouse_pos[1]}]",
            "Mouse btn:",[
            f"RT: {m.PI.MI.mouse['RT']['hold']}",
            f"MID: {m.PI.MI.mouse['MID']['hold']}",
            f"LT: {m.PI.MI.mouse['LT']['hold']}"]],"",
            "[COLORS]","",[
            {scene: {k: v for k, v in colors.items() if not k.startswith("grad-")} for scene, colors in self.colors.items()}]
        ]

        self.Text.F3(m,text)
    
    def error(self,m):

        self.screen.fill(self.colors['Main']['grad-error'][round(math.sin(self.error_bg)*50 + 50)])

        #self.Text.title(m,"CANNOT FOUND SCENE!",(0,0),100,self.colors['Main']['f3-text'])

        points = []
        points2 = []

        for i in range(1,10):
            points.append((math.cos(self.error_bg/20*(math.pi*i))*min(self.width//2,self.height//2),math.sin(self.error_bg/20*(math.pi*i))*min(self.width//2,self.height//2)))
            points2.append((math.cos(-self.error_bg/20*(math.pi*i))*min(self.width//2,self.height//2),math.sin(-self.error_bg/20*(math.pi*i))*min(self.width//2,self.height//2)))
        
        for i in range(len(points)-1):
            
            for i in range(len(points)):
                
                pygame.draw.line(self.screen,self.colors['Main']['f3-text'],(self.width//2 + points[i][0],self.height//2 + points[i][1]),(self.width//2 + points[-1][0],self.height//2 + points[-1][1]),5)
                pygame.draw.line(self.screen,self.colors['Main']['grad-error'][round(math.cos(self.error_bg)*50 + 50)],(self.width//2 + points[i][0],self.height//2 + points[i][1]),(self.width//2 + points[-1][0],self.height//2 + points[-1][1]),3)
            
            points.pop(-1)
        
        for i in range(len(points2)-1):
            
            for i in range(len(points2)):

                pygame.draw.line(self.screen,self.colors['Main']['f3-text'],(self.width//2 -points2[i][0],self.height//2 + points2[i][1]),(self.width//2 -points2[-1][0],self.height//2 + points2[-1][1]),5)
                pygame.draw.line(self.screen,self.colors['Main']['grad-error'][round(math.cos(self.error_bg)*50 + 50)],(self.width//2 -points2[i][0],self.height//2 + points2[i][1]),(self.width//2 -points2[-1][0],self.height//2 + points2[-1][1]),3)
            
            points2.pop(-1)

        self.error_bg += 0.02*self.anim_speed

    def reload_screen(self,m):

        m.Log.write("Перезагрузка переменной Disp.screen.","DEBUG")
        
        if m.config['fullscreen']:
            self.screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN | pygame.DOUBLEBUF)

        else:
            self.screen = pygame.display.set_mode(m.config['start-screensize'],pygame.DOUBLEBUF | pygame.RESIZABLE)
    
    def reload_palette(self,m):

        m.Log.write("Перезагрузка переменной Disp.colors.","DEBUG")

        self.colors = m.JsonManager.load(m,f"data\\theme\\{m.config['theme']}",True)

        for scene_key, scene_value in self.colors.items():
            for color_key,color_value in scene_value.items():
                if color_key[:5] == "grad-":
                    self.colors[scene_key][color_key] = self.gradient(m,color_value[0],color_value[1],100)
    
    def gradient(self, m, color1: tuple, color2: tuple, steps: int) -> list:

        m.Log.write(f"Создан новый градиент от {color1} до {color2}.","DEBUG")
        
        gradient = []
        
        for step in range(steps + 1):
            r = int(color1[0] + (color2[0] - color1[0]) * step / steps)
            g = int(color1[1] + (color2[1] - color1[1]) * step / steps)
            b = int(color1[2] + (color2[2] - color1[2]) * step / steps)
            gradient.append((r, g, b))
        
        return gradient
