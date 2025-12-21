import pygame
import sys

from src.main.event import Event
from src.main.display import Display
from src.manager.sceneLoad import Scenes

class Program:

    def __init__(self):

        self.config = {
            "zoom":1,
            "max-fps":60
        }
        
        pygame.init()

        self.Event = Event(self)
        self.Display = Display(self)
        self.Scenes = Scenes(self)

    def start(self):

        while True:
            
            self.Event.main(self)
            self.Display.main(self)
            self.Display.Clock.tick(self.config['max-fps'])

    def stop(self):

        print("exit")

        pygame.quit()
        sys.exit()