import pygame

class Mouse:

    def __init__(self,mainself):

        self.buttons = []

        for i in range(3):
            self.buttons.append({"press":False,"hold":False,"release":False})
        
        self.weel = 0

        self.pos = pygame.mouse.get_pos()

    def main(self,mainself,event):
        
        if event.type == pygame.MOUSEBUTTONDOWN:

            for i in range(3): 
                if event.button == i+1:

                    self.buttons[i]["press"] = True
                    self.buttons[i]["hold"] = True

                    print(f"Mouse down: {event.button} {self.pos}")
        
        if event.type == pygame.MOUSEBUTTONUP:

            for i in range(3): 
                if event.button == i+1:

                    self.buttons[i]["release"] = True
                    self.buttons[i]["hold"] = False

                    print(f"Mouse up: {event.button} {self.pos}")
        
        if event.type == pygame.MOUSEWHEEL:

            self.weel = event.y

            if event.y != 0:
                print(f"Mouse wheel: {event.y}")
    
    def reset(self,mainself):

        for button in self.buttons:

            button['press'] = False
            button['release'] = False