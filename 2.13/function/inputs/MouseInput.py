import pygame

class MouseInput:
    
    def __init__(self,m):
        
        m.Log.write("Инициализация класса обработки нажатий мыши.","DEBUG")
        
        self.mouse = {
            "RT":{"hold":False,"press":False,"release":False},
            "MID":{"hold":False,"press":False,"release":False},
            "LT":{"hold":False,"press":False,"release":False}
        }
        
        self.weel = 0
    
    def main(self,m,event):
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if event.button == 1:
                
                self.mouse['LT']['hold'] = True
                self.mouse['LT']['press'] = True
                m.Log.write(f"Зажата ЛКМ.")
            
            if event.button == 2:
                
                self.mouse['MID']['hold'] = True
                self.mouse['MID']['press'] = True
                m.Log.write(f"Зажата CКМ.")
            
            if event.button == 3:
                
                self.mouse['RT']['hold'] = True
                self.mouse['RT']['press'] = True
                m.Log.write(f"Зажата ПКМ.")
        
        if event.type == pygame.MOUSEBUTTONUP:
                
            if event.button == 1:
                
                self.mouse['LT']['hold'] = False
                self.mouse['LT']['release'] = True
                m.Log.write(f"Разжата ЛКМ.")
            
            if event.button == 2:
                
                self.mouse['MID']['hold'] = False
                self.mouse['MID']['release'] = True
                m.Log.write(f"Разжата СКМ.")
            
            if event.button == 3:
                
                self.mouse['RT']['hold'] = False
                self.mouse['RT']['release'] = True
                m.Log.write(f"Разжата ПКМ.")
        
        if event.type == pygame.MOUSEWHEEL:
            
            if event.y > 0:
                
                if self.weel < 0:
                    self.weel = 0
                
                self.weel += 1
                
            if event.y < 0:
                
                if self.weel > 0:
                    self.weel = 0
                
                self.weel -= 1
    
    def reload_mouse(self,m):
        
        for button in self.mouse.values():
            
            button['press'] = False
            button['release'] = False
    
    def is_point_in_polygon(self,m,points, pos):

        x, y = pos
        n = len(points)
        inside = False

        p1x, p1y = points[0]
        for i in range(n + 1):
            p2x, p2y = points[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y

        return inside
