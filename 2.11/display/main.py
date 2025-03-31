import pygame

from display.Text import Text
from display.Logo import Logo
from display.StartScreen import StartScreen

# Класс отвечающий за визуальный вывод
class Display:
    
    def __init__(self,m):
        
        m.log.write('[DEBUG] Инициализация класса Display.Main')
        
        self.colors = m.Manager.load(m,f'data\\them\\{m.config['them']}')
        
        if self.colors[1]:
            self.colors = self.colors[0]
        else:
            m.log.write('[FATAL] Не удалось импортировать палитру!')
            m.end()
        
        # Эта переменная очень похожа на status, но отвечает не за ввод информации, а за вывод.
        self.anim = 'logo_start'
        
        self.width, self.height = m.config['start-screen-size']
        self.setscreen(m)
        
        self.Text = Text(m)
        self.Logo = Logo(m,self)
        self.StartScreen = StartScreen(m,self)
            
        self.clock = pygame.time.Clock() # класс для последовательного отображения кадров без задержек или спешки (контроль FPS)
        self.fps = self.clock.get_fps()
    
    # Основная функция класса, которая даёт условия для вывода инофрмации
    def main(self,m):
        
        self.width, self.height = self.screen.get_size()
        
        if self.anim[:4] == 'logo':
            self.Logo.main(m)
        
        elif self.anim[:11] == "startscreen":
            self.StartScreen.main(m)
        
        else:
            self.screen.fill(self.colors['main']['bg'])
            self.Text.title(m,self.Text.text['main'][0],70,(0,0),self.colors['main']['title-text'])
            
        self.Text.F3(m)
    
    def setscreen(self,m): # Обновление информации экрана
        
        m.log.write('[DEBUG] Изменение режима окна.')
        
        if m.config['fullscreen']:

            m.log.write('[INFO] Режим окна был изменён на полноэкранный.')
            self.screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN | pygame.DOUBLEBUF)
        
        else:
            
            m.log.write('[INFO] Режим окна был изменён на оконный.')
            self.screen = pygame.display.set_mode((self.width,self.height),pygame.DOUBLEBUF | pygame.RESIZABLE)

        m.saveconfig(False)

    def gradient(self,m,color1: tuple, color2: tuple, steps: int):
        
        m.log.write(f'[INFO] Был создан градиент из цветов {color1} и {color2}.')

        gradient = []
        
        for step in range(steps + 1):
            r = int(color1[0] + (color2[0] - color1[0]) * step / steps)
            g = int(color1[1] + (color2[1] - color1[1]) * step / steps)
            b = int(color1[2] + (color2[2] - color1[2]) * step / steps)
            gradient.append((r, g, b))
        
        return gradient