from data.func.read import *

gamescreen = []
c = [1,-1]

class GameScreen:

    def __init__(self,swh,anim,game):
            
        self.screen = swh[0]
        self.width = swh[1]
        self.height = swh[2]
        self.anim = anim
        self.game = game
    
    def main(self):

        self.screen.fill(getcolor(2))

        global gamescreen

        if self.anim == 2:
            gamescreen = [self.height]
            self.anim = 2.1
        
        elif self.anim == 2.1:

            for o in c:
                for i in c:
                    GameScreen.cubebutton(self,-155*i,-80*o,gamescreen[0],-i,-o)
            GameScreen.title(self,250,gamescreen[0])
            
            gamescreen[0] /= 1.05



        return self.anim
    
    def cubebutton(self,endposX,endposY,offset,angleX,angleY):

        x = self.width // 2 + endposX + offset*angleX
        y = self.height // 2 - endposY - offset*angleY

        pos = [(x-150,y-75),(x+150,y-75),(x+150,y+75),(x-150,y+75)]

        pygame.draw.polygon(self.screen, getcolor(3), pos)

        text = pygame.font.Font('data\\font\\TeletactileRus.ttf', 40).render(getstr((angleX+1)//2+2*((angleY+1)//2)+6), True, getcolor(4))
        self.screen.blit(text, text.get_rect(center=(self.width // 2 + endposX + offset*angleX,self.height // 2 - endposY - offset*angleY)))
    
    def title(self,endpos,offset):

        x = self.width//2
        y = self.height//2+offset+endpos

        text = pygame.font.Font('data\\font\\TeletactileRus.ttf', 50).render(getstr(5), True, getcolor(10))
        self.screen.blit(text, text.get_rect(center=(self.width // 2, self.height // 2-offset-endpos)))