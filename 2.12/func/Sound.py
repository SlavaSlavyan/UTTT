import pygame
from pathlib import Path

class Sound:
    
    def __init__(self,m):
        
        pygame.mixer.init()

        self.sounds = {}
        files = [f.name for f in Path('data\\assets\\sounds').iterdir() if f.is_file()]

        for f in files:
            if f.split('.')[-1] == 'mp3':
                self.sounds[f.rsplit('.', 1)[0]] = pygame.mixer.Sound(f"data\\assets\\sounds\\{f}")

    def play(self,m,soundname:str):
        
        try:
            
            sound = self.sounds[soundname]
            sound.set_volume(round(m.config['sound-volume']/100,3))
            sound.play()
            
        except:
            print(f'No such sound {soundname}')