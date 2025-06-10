import pygame

class Text:
    
    def __init__(self,m):
        
        m.Log.write("Инициализация мастера отображения текста.","DEBUG")
        
        self.f3_font = pygame.font.Font("data\\font\\text.ttf", 9)
        
    def F3(self,m, text:str|list|dict, line_num:int=0, tab_num:int=0) -> int:
        
        if isinstance(text,list):
            
            for line in text:
                line_num = self.F3(m,line,line_num,tab_num+1)
            
            line_num -= 1
        
        elif isinstance(text,dict):
            
            for key, value in text.items():
                line_num = self.F3(m,f"{key}: {value}",line_num,tab_num+1)
            
            line_num -= 1
        
        else:
            m.Disp.screen.blit(self.f3_font.render(str(text), False, m.Disp.colors['Main']['f3-text']), (2+12*tab_num, 9+9*line_num))
                          
        line_num += 1
        
        return line_num