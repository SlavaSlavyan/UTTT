import pygame

# Этот класс отвечает за вывод текста, а так же его хранение
class Text:
    
    def __init__(self,m):
        
        m.log.write('[DEBUG] Инициализация класса Display.Text')
        self.text = m.Manager.load(m,f"data\\lang\\{m.config['language']}") # Все текстовые лайны
        
        if self.text[1]:
            self.text = self.text[0]
        else:
            m.log.write('[FATAL] Не удалось загрузить файлы с текстовой информацией!')
            m.end()
            
        self.f3_font = pygame.font.Font("data\\font\\text.ttf", 9) # сохранённые настройки текста дебага
    
    def title(self,m,text: str,size: int,pos: tuple,color: tuple):
        
        font = pygame.font.Font("data\\font\\title.ttf", size)
        t = font.render(text, True, color)  # Создаем текст
        text_rect = t.get_rect(center=(m.Disp.width // 2 + pos[0], m.Disp.height // 2 - pos[1]))  # Получаем прямоугольник текста и центрируем его
        m.Disp.screen.blit(t, text_rect)
    
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
            f"Animation smoothing: {m.config['animation-smoothing']}",
            f"Mouse pos: {m.PI.MI.mouse_pos}",
            f"Main timer: {m.Time.timers['main']['min']}:{m.Time.timers['main']['sec']:02}",
            ""
        ]
        
        # Отрисовка каждой строчки массива
        for i in range(len(text)):
            m.Disp.screen.blit(self.f3_font.render(text[i], False, m.Disp.colors['main']['f3-text']), (10, 10+7*i))