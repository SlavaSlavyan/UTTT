import pygame

class Text:
    
    def __init__(self,m):
        
        m.log.write('[DEBUG] Инициализация класса Display.Text')
        self.f3_font = pygame.font.Font("data\\font\\text.ttf", 9) 
    
    def F3(self,m):
        
        text = [
            "Please use F3 only for DEBUG. Text can reduse much lags :(",
            "",
            f"Version: {m.config['vers']}",
            f"Max FPS: {m.config['max-fps']}",
            f"FPS: {round(m.Disp.fps)}",
            f"Logs: {m.log.logging}",
            f"Screen: {m.Disp.width}x{m.Disp.height}",
            f"Status: {m.status}",
            f"Anim: {m.Disp.anim}",
            f"Fullscreen: {m.config['fullscreen']}",
            f"Theme: {m.config['them']}",
            f"Language: {m.config['language']}",
            f"Zoom: {m.config['zoom']}",
            ""
        ]
        
        for i in range(len(text)):
            m.Disp.screen.blit(self.f3_font.render(text[i], False, (255,255,255)), (10, 10+7*i))