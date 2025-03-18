import pygame

class Display: # Класс отображения графической информации
    
    def __init__(self, m):
        
        m.log.w('Инициализация класса Display.')
        
        # Создание полного/оконного экрана
        
        self.reloadscreen(m)
        self.clock = pygame.time.Clock() # класс для последовательного отображения кадров без задержек или спешки (контроль FPS)
    
    def main(self, m): # основная функция класса которая отвечает за отрисовку каждого кадра. Определяет условия и порядок отображения информации
        
        m.config['screensize'] = self.screen.get_size()
        self.screen.fill((0,0,0))
        
    def reloadscreen(self,m): # перезагрузка/создание переменной screen
        
        m.log.w('Перезагрузка информации об окне.')
        
        new = m.Reader.load("data\\config")
        new['screensize'] = m.config['screensize']
        m.Reader.save("data\\config",new)
        
        m.reloadconfig() # обновление кофига
        
        if m.config['fullscreen']:

            m.log.w('Режим окна был изменён на полноэкранный.')
            self.screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
        
        else:
            
            m.log.w('Режим окна был изменён на оконный.')
            self.screen = pygame.display.set_mode((m.config['screensize'][0], m.config['screensize'][1]),pygame.RESIZABLE)