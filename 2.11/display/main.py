import pygame

from display.Text import Text
from display.logo import Logo

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
            
        self.clock = pygame.time.Clock() # класс для последовательного отображения кадров без задержек или спешки (контроль FPS)
        self.fps = self.clock.get_fps()
    
    # Основная функция класса, которая даёт условия для вывода инофрмации
    def main(self,m):
        
        self.width, self.height = self.screen.get_size()
        
        if self.anim[:4] == 'logo':
            self.Logo.main(m)
            
        self.Text.F3(m)
    
    def setscreen(self,m): # Обновление информации экрана
        
        m.log.write('[DEBUG] Изменение режима окна.')
        
        if m.config['fullscreen']:

            m.log.write('[INFO] Режим окна был изменён на полноэкранный.')
            self.screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN | pygame.DOUBLEBUF)
        
        else:
            
            m.log.write('[INFO] Режим окна был изменён на оконный.')
            self.screen = pygame.display.set_mode((self.width,self.height),pygame.RESIZABLE | pygame.DOUBLEBUF)

        m.saveconfig(False)