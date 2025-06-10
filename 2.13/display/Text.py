import pygame

class Text:
    
    def __init__(self,m):
        
        m.Log.write("Инициализация мастера отображения текста.","DEBUG")
        
        self.f3_font = pygame.font.Font("data\\font\\text.ttf", 9)
        
    def F3(self,m, text:str|list|dict, line:int=0, tab:int=0) -> int:
        
        if isinstance(text,str):
            m.Disp.screen.blit(self.f3_font.render(text, False, m.Disp.colors['Main']['f3-text']), (2+12*tab, 9+9*line))
            
        elif isinstance(text,dict):
            
            for key, value in text.items():
                
                if isinstance(value,list) or isinstance(value,dict):
                    
                    m.Disp.screen.blit(self.f3_font.render(f"{key}:", False, m.Disp.colors['Main']['f3-text']), (2+12*tab, 9+9*line))
                    line += 1
                    for i in value.items():
                        line = self.F3(m,i,line,tab+1)
               
                else:
                    m.Disp.screen.blit(self.f3_font.render(f"{key}:{value}", False, m.Disp.colors['Main']['f3-text']), (2+12*tab, 9+9*line))
        
        elif isinstance(text,list):
            
            for i in text:
                line = self.F3(m,i,line,tab+1) 
                          
        line += 1
        
        return line