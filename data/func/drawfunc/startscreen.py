from data.func.drawfunc.logo import *

startscreen = []

class StartScreen:

    def __init__(self,swh,anim):
            
        self.screen = swh[0]
        self.width = swh[1]
        self.height = swh[2]
        self.anim = anim
    
    def main(self):

        global startscreen

        if self.anim == 1:
            startscreen = [[0,gradient(getcolor(0),getcolor(2),120),gradient(getcolor(0),getcolor(3),121),gradient(getcolor(0),getcolor(3),121)],
                           [self.width,self.width*2,self.width*4,self.width*8]]
            self.anim = 1.1

        if startscreen[0][0] != 120:
            self.screen.fill(startscreen[0][1][startscreen[0][0]])
            startscreen[0][0] += 1
        
        else:
            self.screen.fill(getcolor(2))
        
        if self.anim == 1.1:

            for i in range(3):
                StartScreen.button(self,25+55*i,startscreen[1][i],i+2,-400,-400,i+1)
            
            StartScreen.title(self,130,startscreen[1][3])

            startscreen[1] = [i / 1.07 for i in startscreen[1]]

            if round(startscreen[1][3]) == 0:
                self.anim = 1.2

        elif self.anim == 1.2:

            self.screen.fill(getcolor(2))
            startscreen[0] = [0,gradient(getcolor(2),getcolor(2),120),gradient(getcolor(3),getcolor(3),121),gradient(getcolor(3),getcolor(3),121)]
            
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for i in range(3):
                StartScreen.button(self,25+55*i,0,i+2,mouse_x,mouse_y,i+1)
            
            StartScreen.title(self,130,0)
        
        elif self.anim == 1.3:

            self.screen.fill(getcolor(2))
            
            for i in range(3):
                StartScreen.button(self,25+55*i,0,i+2,-400,-400,i+1)
            
            StartScreen.title(self,130,0)

            startscreen[1] = [0.1,0.2,0.4,0.8]
            self.anim = 1.4
        
        elif self.anim == 1.4:

            for i in range(3):
                StartScreen.button(self,25+55*i,startscreen[1][i],i+2,-400,-400,i+1)
            
            StartScreen.title(self,130,startscreen[1][3])

            startscreen[1] = [i * 1.11 for i in startscreen[1]]

            if startscreen[1][0] >= self.height:

                from data.func.main import status
                self.anim = status+1

                if status == 3:
                    pygame.quit()
                    sys.exit()            

        return self.anim

    def button(self,endpos,offset,textnum,mouseX,mouseY,buttonNum):

        x = self.width//2
        y = self.height//2+offset+endpos
        mouseX = self.width//2 - mouseX
        mouseY = self.height//2 - mouseY

        pos = [(x-200,y+25),(x+200,y+25),(x+200,y-25),(x-200,y-25)]
        pygame.draw.polygon(self.screen, startscreen[0][2][startscreen[0][0]], pos)


        if self.anim != 1.4 and self.anim != 1.3:

            from data.func.main import Main

            arg = Main.startscreen(mouseX,mouseY)

            if arg == buttonNum:
                color = getcolor(6)

            else:
                color = getcolor(4)

        else:
            
            from data.func.main import status

            if status == buttonNum:
                color = getcolor(6)

            else:
                color = getcolor(4)

        text = pygame.font.Font('data\\font\\TeletactileRus.ttf', 40).render(getstr(textnum), True, color)

        self.screen.blit(text, text.get_rect(center=(self.width // 2, self.height // 2+offset+endpos)))
    
    def title(self,endpos,offset):

        x = self.width//2
        y = self.height//2+offset+endpos

        for i in range(2):

            text = pygame.font.Font('data\\font\\TeletactileRus.ttf', 100-50*i).render(getstr(i), True, getcolor(7-2*i))
            self.screen.blit(text, text.get_rect(center=(self.width // 2, self.height // 2-offset-endpos+70*i)))