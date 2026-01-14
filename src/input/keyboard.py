import pygame

class KeyBoard:

    def __init__(self,mainself):

        self.keys = {
            "up":1073741906,
            "left":1073741904,
            "down":1073741905,
            "right":1073741903,
            "back":8,
            "select":13
        }

        for name,id in self.keys.items():
            self.keys[name] = {"id":id,"press":False,"hold":False,"release":False}

    def main(self,mainself,event):

        for name in self.keys:
        
            if event.type == pygame.KEYDOWN:
                #print(event.key)
                if event.key == self.keys[name]['id']:

                    self.keys[name]['press'] = True
                    self.keys[name]['hold'] = True

                    print(f"Key down: {event.key} {name}")

            if event.type == pygame.KEYUP:
                if event.key == self.keys[name]['id']:

                    self.keys[name]['release'] = True
                    self.keys[name]['hold'] = False

                    print(f"Key up: {event.key} {name}")
    
    def reset(self,mainself):

        for name in self.keys:

            self.keys[name]['press'] = False
            self.keys[name]['release'] = False