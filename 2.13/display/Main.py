import pygame

from display.scenes.Logo import Logo

class Display:
    
    def __init__(self,m):

        m.Log.write("Инициализация класса отображения.","DEBUG")

        self.colors = m.JsonManager.load(m,f"data\\theme\\{m.config['theme']}",True)

        self.reload_screen(m)

        self.anim = "Logo_0"
        m.Log.write(f"Начальная сцена = {self.anim}.","DEBUG")

        self.clock = pygame.time.Clock()

        self.Logo = Logo(m)
    
    def main(self,m):

        self.width, self.height = self.screen.get_size()
        
        self.fps = self.clock.get_fps()

        if self.fps == 0: self.anim_speed = 0
        else: self.anim_speed = 60/self.fps

        self.zoom = round(m.config['zoom'] + min(self.width/m.config['start-screensize'][0],self.height/m.config['start-screensize'][1]) -1,1)

        if self.anim[:4] == "Logo":
            self.Logo.main(m)

    def reload_screen(self,m):

        m.Log.write("Перезагрузка переменной Disp.screen.","DEBUG")
        
        if m.config['fullscreen']:
            self.screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN | pygame.DOUBLEBUF)

        else:
            self.screen = pygame.display.set_mode(m.config['start-screensize'],pygame.DOUBLEBUF | pygame.RESIZABLE)