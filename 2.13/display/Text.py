import pygame

class Text:
    
    def __init__(self,m):
        
        m.Log.write("Инициализация мастера отображения текста.","DEBUG")
        
        self.f3_font = pygame.font.Font("data\\font\\text.ttf", 9)
        
        self.text = m.JsonManager.load(m,f"data\\language\\{m.config['language']}",True)
        
    def F3(self,m, text:str|list|dict, line_num:int=0, tab_num:int=0) -> int:
        
        if isinstance(text,list):
            
            for line in text:
                line_num = self.F3(m,line,line_num,tab_num+1)
            
            line_num -= 1
        
        elif isinstance(text,dict):
            
            for key, value in text.items():
                if isinstance(value,dict):
                    line_num = self.F3(m,f"{key}:",line_num,tab_num)
                    line_num = self.F3(m,value,line_num,tab_num)
                else:

                    if isinstance(value,float):
                        value = round(value,3)

                    line_num = self.F3(m,f"{key}: {value}",line_num,tab_num+1)
            
            line_num -= 1
        
        else:

            if isinstance(text,float):
                value = round(text,3)

            m.Disp.screen.blit(self.f3_font.render(str(text), False, m.Disp.colors['Main']['f3-text']), (2+12*tab_num, 9+9*line_num))
                          
        line_num += 1
        
        return line_num

    def paragraf(self,m, text:str|list, pos:tuple, size:int, color:tuple, align:str="center"):

        font = pygame.font.Font("data\\font\\text.ttf", round(size*m.Disp.zoom))
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        
        pos = (m.Disp.width // 2 + pos[0]*m.Disp.zoom, m.Disp.height // 2 - pos[1]*m.Disp.zoom)
        
        if align == "left": text_rect.topleft = pos
        elif align == "center": text_rect.center = pos
        elif align == "right": text_rect.topright = pos
        
        m.Disp.screen.blit(text_surface, text_rect)
    
    def title(self,m, text:str, pos:tuple, size:int, color:tuple):

        font = pygame.font.Font("data\\font\\title.ttf", round(size*m.Disp.zoom))
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        
        pos = (m.Disp.width // 2 + pos[0]*m.Disp.zoom, m.Disp.height // 2 - pos[1]*m.Disp.zoom)
        
        text_rect.center = pos
        
        m.Disp.screen.blit(text_surface, text_rect)