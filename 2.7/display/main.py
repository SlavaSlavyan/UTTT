import pygame

from functions.load import File

class Display:

    def __init__(self,m):
        
        self.anim = 'None'
        self.colors = File.load(f'themes\\{m.config['theme']}')

    def main(self,m):

        if self.anim == 'game_start':
            pass

        else:
            Display.errorOfAnim(self,m)
        
        if m.F3 == True:
            text = [
                'Made by SLL >:3',"",
                f"[GLOBAL]",'',[
                    f'Screen: {m.width}x{m.height}',
                    f'FPS: {m.fps}',
                    f'Status: {m.status}',
                    f"Config:",list(m.config.items())
                ]
            ]
            Display.F3(m,text,0,0)

        return m
    
    def errorOfAnim(self,m):

        m.screen.fill(self.colors['global']['background'])
        Display.title(m,(m.width//2,m.height//2),"Error of Anim!",150,self.colors['global']['title'])
    
    def F3(m,inputText,indentNum,textNum):

        font = pygame.font.Font(f"assets\\fonts\\text.ttf", 9)

        for i in range(len(inputText)):
            if isinstance(inputText[i],list):
                Display.F3(m,inputText[i],indentNum+1,textNum+i)
            else:
                text = font.render(str(inputText[i]), False, (255,255,255))
                m.screen.blit(text, (10+9*indentNum,10+9*(i+textNum)))
    
    def text(m,pos,inputText,size,color):
        
        size = round(size*m.config['zoom'])

        font = pygame.font.Font(f"assets\\fonts\\text.ttf", size)
        for i in range(len(inputText)):
            text = font.render(str(inputText[i]), True, color)
            m.screen.blit(text, (pos[0],pos[1]+size*i))
    
    def title(m,pos,inputText,size,color):
        
        size = round(size*m.config['zoom'])

        font = pygame.font.Font(f"assets\\fonts\\title.ttf", size)
        text = font.render(str(inputText), True, color)
        text_rect = text.get_rect()
        text_rect.center = pos
        m.screen.blit(text, text_rect)