import pygame

class Display:
    
    def __init__(self,m):

        m.Log.write("Инициализация класса отображения.","DEBUG")

        self.reload_screen(m)
        self.width, self.height = m.config['start-screensize']

        self.anim = "Logo"
        m.Log.write(f"Начальная сцена = {self.anim}.","DEBUG")

        self.clock = pygame.time.Clock()
        self.fps = self.clock.get_fps()

        self.zoom = m.config['zoom']
    
    def main(self,m):
        
        self.fps = self.clock.get_fps()

        self.zoom = m.config['zoom']


    def reload_screen(self,m):

        m.Log.write("Перезагрузка переменной Disp.screen.","DEBUG")
        
        if m.config['fullscreen']:
            self.screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN | pygame.DOUBLEBUF)

        else:
            self.screen = pygame.display.set_mode(m.config['start-screensize'],pygame.DOUBLEBUF | pygame.RESIZABLE)