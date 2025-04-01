import pygame
import math

# Класс для отображения начального логатипа (SLL)
class Logo:
    
    def __init__(self,m,d):
        
        m.log.write('[DEBUG] Инициализация класса Display.Logo')
        
        self.colors = d.colors['logo']
        
        self.offset = [100,200,400] # эта переменная отвечает за смещение всех объектов на экране. 100 = ширина\высота экрана
        self.rotate = 0 # эта переменная постоянно увеличивается на определённую константу и создаёт эффект "кручения"
    
    def main(self,m):
        
        # Заполнение всего кадра цветом заднего фона
        m.Disp.screen.fill(self.colors['bg']) 
        
        # вызов функций на отрисовку каждой буквы
        self.letter(m,"S",-200,self.offset[0])
        self.letter(m,"L",0,self.offset[1])
        self.letter(m,"L",200,self.offset[2])

        # если отключено, анимации будут работать со скоростью зависящей от фпс
        # pygame работает так, что fps это не просто скорость отображение, а именно скорость работы программы.
        # по этому нужно использовать определённые функции для правильного отображения
        # смещение постоянно делится по определённой формуле из-за чего получается анимация
        # 1 + "неизменяемая скорость деления расчитанная под 60 фпс" * (60/фпс)
        # если фпс будет равен 60, то смещение будет поделено на 1.05
        # если фпс будет больше 60, то деление будет замедленно (при 120 фпс деление будет равно 1.025)
        # если фпс будет больше 60, то деление будет ускорено (при 30 фпс деление будет равно 1.1)
        # По похожей схеме работает вращение
        
        if m.Disp.fps != 0: # если фпс не равен 0
            
            if m.config['animation-smoothing']:
                sm = m.Disp.fps
            else:
                sm = 60

            self.rotate += 0.03*(60/sm)
            
            if m.Disp.anim == 'logo_start':
                self.offset = [i / (1 + 0.05*(60/sm)) for i in self.offset]

                if round(self.offset[-1], 1) == 0:

                    m.Disp.anim = 'logo_wait'
                    self.offset = [i * -1 for i in self.offset]
                    self.offset.reverse()
                    m.Time.addtimer(m,"logo",-1,(0,1,0))
            
            elif m.Disp.anim == 'logo_wait':

                if m.Time.timers['logo']['min'] <= -1:
                    m.Time.removetimer(m,'logo')
                    m.Disp.anim = 'logo_end'
                
            if m.Disp.anim == 'logo_end':

                self.offset = [i * (1 + 0.05*(60/sm)) for i in self.offset]

                if self.offset[-1]/100*m.Disp.width < -m.Disp.width:

                    m.Disp.anim = 'startscreen_start'
                    m.status = 'startscreen_start'

    
        
    # функция для вывода определённой буквы с особыми настройками
    def letter(self,m,letter: str, pos: float, offset: float):
        
        # принимает letter как id буквы, 
        # pos как конечную точку анимации по оси x
        # offset как неоходимое смещение по оси x
        
        z = m.config['zoom'] + m.Disp.sm_zoom # получение множителя размера из конфигурации
        
        # "x" и "y" отвечают за центр фигуры, от которого можно построить координаты
        # x расчитывается по формуле:
        # "Ширина окна"/2 + "конечная точка" * "размер" + "смещение" - "константа для центрирования фигуры" * "размер"
        x = m.Disp.width//2 + pos*z + m.Disp.width*(offset/100) -75*z 
        # y расчитывается по формуле: "Высота окна"/2 + "константа для центрирования фигуры" * "размер"
        y = m.Disp.height//2 + 125*z
        
        # Выбор определённого трафарета буквы
        # Трафарет фигуры - это двухмерный массив с координатами каждой точки фигуры
        # Каждая точка состоит из двух переменных x и y +- координаты точки * размер
        if letter == "S":
            pos = [[x,y],[x+150*z,y],[x+150*z,y-150*z],[x+50*z,y-150*z],[x+50*z,y-200*z],[x+150*z,y-200*z],[x+150*z,y-250*z],[x,y-250*z],[x,y-100*z],[x+100*z,y-100*z],[x+100*z,y-50*z],[x,y-50*z]]
        else:
            pos = [[x,y],[x+150*z,y],[x+150*z,y-50*z],[x+50*z,y-50*z],[x+50*z,y-250*z],[x,y-250*z]]
        
        pos2 = [] # Этот массив нужен для "тени" фигуры
        
        # Во второй массив копируется все координаты из первого с определённой функцией
        # x = "оригинал x" + "константа длинны тени" * "размер" + "косинус из переменной rotate"
        # y = "оригинал y" + "константа длинны тени" * "размер" + "синус из переменной rotate"
        for dot in pos:
            pos2.append([dot[0]+50*z*math.cos(self.rotate),dot[1]+50*z*math.sin(self.rotate)])
        
        # отрисовывание псевдо 3д рёбер фигуры
        for i in range(len(pos)):
            pygame.draw.polygon(m.Disp.screen, self.colors['text'], [pos[i-1],pos[i],pos2[i],pos2[i-1]])
        
        # Очиска лишних рёбер скрытых за фигурой
        pygame.draw.polygon(m.Disp.screen, self.colors['bg'], pos)
        
        # Добавление контура
        for i in range(len(pos)):    
            pygame.draw.line(m.Disp.screen, self.colors['text'], pos[i-1], pos[i], 1)