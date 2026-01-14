import pygame
import sys

from src.main.event import Event
from src.main.display import Display
from src.utils.scene_manager import Scenes

class Program:

    def __init__(self):

        self.config = {
            "max-fps":-1,
            "language":"RU"
        }
        
        pygame.init()
        pygame.mouse.set_visible(False)

        self.Event = Event(self)
        self.Display = Display(self)
        self.Scenes = Scenes(self)

        self.Scenes.load_scene(self,'game')

        self.status = 'game'

    def start(self):

        print('start')

        while True:
            
            self.Event.main(self)
            self.Display.main(self)
            self.Display.Clock.tick(self.config['max-fps'])

    def stop(self):

        print("exit")

        pygame.quit()
        sys.exit()