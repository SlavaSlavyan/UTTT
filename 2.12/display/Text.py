import pygame

class Text:
    
    def __init__(self,m):
        
        self.text = m.JsonManager.load(f"data\\lang\\{m.config['language']}")
            
        self.f3_font = pygame.font.Font("data\\font\\text.ttf", 9)
    
    def title(self,m,text: str,size: int,pos: tuple,color: tuple):
        
        font = pygame.font.Font("data\\font\\title.ttf", round(size))
        t = font.render(text, True, color)
        text_rect = t.get_rect(center=(m.Disp.width // 2 + pos[0], m.Disp.height // 2 - pos[1]))
        m.Disp.screen.blit(t, text_rect)
    
    def F3(self,m):
        
        text = [
            "Please use F3 only for DEBUG. Text can reduse much lags :(",
            "",
            f"Version: {m.vers}",
            f"Max FPS: {m.config['max-fps']}",
            f"FPS: {round(m.Disp.fps)}",
            f"Screen: {m.Disp.width}x{m.Disp.height}",
            f"Status: {m.status}",
            f"Anim: {m.Disp.anim}",
            f"Fullscreen: {m.config['fullscreen']}",
            f"Theme: {m.config['them']}",
            f"Language: {m.config['language']}",
            f"Zoom: {m.config['zoom']}",
            f"Mouse pos: {m.PI.MI.mouse_pos}, [{m.PI.MI.mouse_pos[0] - m.Disp.width//2},{-m.PI.MI.mouse_pos[1] + m.Disp.height//2}]",
            f"Main timer: {m.Time.timers['main']['min']}:{m.Time.timers['main']['sec']:02}",
            ""
        ]
        
        for i in range(len(text)):
            m.Disp.screen.blit(self.f3_font.render(text[i], False, m.Disp.colors['main']['f3-text']), (10, 10+7*i))