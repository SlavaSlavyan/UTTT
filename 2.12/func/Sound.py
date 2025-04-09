import pygame
import random

class Sound:
    
    def __init__(self,m):
        
        pygame.mixer.init()
        self.sounds = {
            "click1":pygame.mixer.Sound("data\\assets\\sounds\\click1.mp3"),
            "click2":pygame.mixer.Sound("data\\assets\\sounds\\click2.mp3"),
            "click3":pygame.mixer.Sound("data\\assets\\sounds\\click3.mp3"),
            "startscreen_select":pygame.mixer.Sound("data\\assets\\sounds\\startscreen_select.mp3")
        }
    
    def click(self,m):
        
        sound = self.sounds[f"click{random.randint(1,3)}"]
        sound.set_volume(round(m.config['sound-volume']/100,3))
        sound.play()
    
    def play(self,m,soundname:str):
        
        try:
            
            sound = self.sounds[soundname]
            sound.set_volume(round(m.config['sound-volume']/100,3))
            sound.play()
            
        except:
            print(f'No such sound {soundname}')