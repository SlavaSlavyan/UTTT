import pygame

class StartScreen:

    def __init__(self,m):

        m.Log.write("Инициализация отображения сцены StartScreen.","DEBUG")
        
        self.offset = [100]
        
        for i in range(5):
            self.offset.append(self.offset[-1]*2)

        self.btns = []

        for i in range(4):
            self.btns.append(Button(m,-25-60*i))

    def main(self,m):

        m.Disp.screen.fill(m.Disp.colors['StartScreen']['bg'])

        m.Disp.Text.title(m,m.Disp.Text.text['StartScreen'][1],(0,200+m.Disp.height*self.offset[1]/100),200,m.Disp.colors['StartScreen']['title'])
        m.Disp.Text.title(m,m.Disp.Text.text['StartScreen'][0],(0,100+m.Disp.height*self.offset[0]/100),100,m.Disp.colors['StartScreen']['title'])

        for i in range(len(self.btns)):
            self.btns[i].main(m,-self.offset[i+2],i+2)

        self.offset = [i / (1 + 0.07*m.Disp.anim_speed) for i in self.offset]

class Button:
    
    def __init__(self,m,pos):

        m.Log.write(f"Создан новый класс кнопки [StartScreen.Button]. Pos = {pos}.","DEBUG")
        
        self.pos = pos
        self.grad_btn = 0
        self.size = 1

    def main(self,m,offset,btn_num):

        if self.grad_btn < 0:self.grad_btn = 0
        if self.grad_btn > 1:self.grad_btn = 1
        if self.size < 1:self.size = 1
        if self.size > 1.4:self.size = 1.4

        z = m.Disp.zoom
        
        self.points = [[-200,25],[200,25],[200,-25],[-200,-25]]

        for point in self.points:
            point[0] = point[0]*z + m.Disp.width//2
            point[1] = -point[1]*z + m.Disp.height//2 - self.pos*z - offset/100*m.Disp.height*z

        pygame.draw.polygon(m.Disp.screen,m.Disp.colors['StartScreen']['button_bg'],self.points)

        m.Disp.Text.paragraf(m,m.Disp.Text.text['StartScreen'][btn_num],(0,self.pos + offset/100*m.Disp.height*z),30*self.size,m.Disp.colors['StartScreen']['grad-button-text'][round(self.grad_btn*100)])

        self.grad_btn -= 1/30*m.Disp.anim_speed
        self.size -= 1/30*m.Disp.anim_speed

        