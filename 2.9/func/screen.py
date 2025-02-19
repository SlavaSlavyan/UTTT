import pygame

from func.filereader import File

class Window: # класс создания, настройки и поддержки основого вывода на экран.

    def __init__(self,m):
        
        self.colors = { # Все цвета в игре
            "dark":{
                "global":{
                    "text":(255,255,255),
                    "mouse":(229, 192, 123)
                },
                "game":{
                    "bg":(40, 44, 52),
                    "darkbg":(33, 37, 43),
                    "activecell":(171,178,191),
                    "passivecell":(92, 99, 112),
                    "player0":(97, 175, 239),
                    "playerX":(198, 107, 60),
                    "timertext":(255,255,255),
                    "active-passive":self.gradient((92, 99, 112),(171,178,191),30),
                    "0toX":self.gradient((97, 175, 239),(198, 107, 60),30)
                }
            }
        }

        self.setscreen(m)

        self.clock = pygame.time.Clock()
        self.fps = int

        self.offset = [0,0]


    def setscreen(self,m): # Настройка экрана (ширина/высота)

        m.config = File.load('config') # Получение настроек и запись их в класс Main

        if m.config['fullscreen']:

            self.screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
            self.width, self.height = self.screen.get_size()

        else:

            self.width = 1200
            self.height = 800
            self.screen = pygame.display.set_mode((self.width, self.height),pygame.RESIZABLE)
    

    def getsize(self,m): # Получение иформации при изменении размера экрана

        if m.config['fullscreen'] == False:
            self.width, self.height = self.screen.get_size()
    

    def fpslimit(self,m): # Ограничение кадров в секунду для корректной работы программы

        self.clock.tick(m.config['maxfps']) # <-- Ставит ограничение соответствующее значению в конфигураторе (config.json)


    def gradient(self,color1, color2, steps): # принимает на вход два кортежа RGB и количество шагов, что бы выдать градиент (массив, содержащий большое количество кортежей)

        gradient = []
        
        for step in range(steps + 1):
            r = int(color1[0] + (color2[0] - color1[0]) * step / steps)
            g = int(color1[1] + (color2[1] - color1[1]) * step / steps)
            b = int(color1[2] + (color2[2] - color1[2]) * step / steps)
            gradient.append((r, g, b))
        
        return gradient