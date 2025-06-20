import pygame

class KeyInput:

    def __init__(self,m):

        m.Log.write("Инициализация класса обработки нажатий клавиатуры.","DEBUG")
        
        self.mode = "CONTROL"
        
        self.keys = {
            pygame.K_ESCAPE:"esc",
            pygame.K_F1:"f1",
            pygame.K_F2:"f2",
            pygame.K_F3:"f3",
            pygame.K_F5:"f5",
            pygame.K_F6:"f6",
            pygame.K_F11:"f11",
        }
        
        for id,name in self.keys.items():
            self.keys[id] = {"hold":False,"press":False,"release":False,"name":name}
        
    def main(self,m,event):
        
        for key in self.keys:

            if event.type == pygame.KEYDOWN:
                
                if self.mode == "CONTROL":
                
                    if event.key == key:
                        
                        self.keys[key]["hold"] = True
                        self.keys[key]["press"] = True
                        m.Log.write(f"Зажата клавиша {self.keys[key]['name']}.")
                
            if event.type == pygame.KEYUP:
                
                if self.mode == "CONTROL":
                
                    if event.key == key:
                        
                        self.keys[key]["hold"] = False
                        self.keys[key]["release"] = True
                        m.Log.write(f"Разжата клавиша {self.keys[key]['name']}.")
    
    def reload_keyboard(self,m):
        
        for key in self.keys:
            
            self.keys[key]["press"] = False
            self.keys[key]["release"] = False
    
    def logic_main(self,m):
        
        if self.keys[pygame.K_F3]['press']:
            
            m.Log.write("Пользователь запустил эвент смены статуса режима debug.","DEBUG")
            m.config['debug'] = not m.config['debug']
        
        if self.keys[pygame.K_F11]['press']:
            
            m.Log.write("Пользователь запустил эвент смены статуса режима экрана.","DEBUG")
            m.config['fullscreen'] = not m.config['fullscreen']
            m.Disp.reload_screen(m)