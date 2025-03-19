import pygame

from display.Logo import Logo

class Display: # Класс отображения графической информации
    
    def __init__(self, m):
        
        m.log.w('[INIT] Инициализация класса Display.')
        
        # Создание полного/оконного экрана
        
        self.anim = 'logo_start'
        m.log.w(f'[INFO] Начальная сцена: {self.anim}.')
        self.colors = m.Reader.load(f"data\\them\\{m.config['them']}")
        for i in self.colors.values():
            for key, value in i.items():
                if key[:4] == "grad":
                    value = exec(value)
        
        self.reloadscreen(m)
        
        self.Logo = Logo(m,self)
        
        self.clock = pygame.time.Clock() # класс для последовательного отображения кадров без задержек или спешки (контроль FPS)
    
    def main(self, m): # основная функция класса которая отвечает за отрисовку каждого кадра. Определяет условия и порядок отображения информации
        
        m.config['screensize'] = self.screen.get_size()
        
        if self.anim[:4] == 'logo':
            self.Logo.main(m)
        
    def reloadscreen(self,m): # перезагрузка/создание переменной screen
        
        m.log.w('[FUNC] Перезагрузка информации об окне.')
        
        new = m.Reader.load("data\\config")
        new['screensize'] = m.config['screensize']
        m.Reader.save("data\\config",new)
        
        m.reloadconfig() # обновление кофига
        
        if m.config['fullscreen']:

            m.log.w('[INFO] Режим окна был изменён на полноэкранный.')
            self.screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
        
        else:
            
            m.log.w('[INFO] Режим окна был изменён на оконный.')
            self.screen = pygame.display.set_mode((m.config['screensize'][0], m.config['screensize'][1]),pygame.RESIZABLE)
    
    def gradient(self,color1: list, color2: list, steps: int) -> list:

        gradient = []
        
        for step in range(steps + 1):
            r = int(color1[0] + (color2[0] - color1[0]) * step / steps)
            g = int(color1[1] + (color2[1] - color1[1]) * step / steps)
            b = int(color1[2] + (color2[2] - color1[2]) * step / steps)
            gradient.append((r, g, b))
        
        return gradient