import pygame

from display.game import Game

class Display:

    def __init__(self,m):
        
        self.mouse_pos = pygame.mouse.get_pos()
        self.anim = 'game_start'
        self.colors = {
            "dark":{
                "global":{
                    "text":(255,255,255)
                },
                "game":{
                    "bg":(40, 44, 52),
                    "darkbg":(33, 37, 43),
                    "activecell":(171,178,191),
                    "passivecell":(92, 99, 112),
                    "player0":(97, 175, 239),
                    "playerX":(198, 107, 60),
                    "active-passive":self.gradient((171,178,191),(92, 99, 112),120),
                    "0toX":self.gradient((97, 175, 239),(198, 107, 60),120)
                }
            }
        }
        self.offset = [0,0]
        self.ratio = [m.width/100,m.height/100]
        self.Game = Game(m,self)
    
    def main(self,m):

        self.ratio = [m.width/100,m.height/100]

        if self.anim == 'game_start':

            self.Game.start(m)
        
        if m.F3:
            self.F3(m)
        
        self.cursor(m)
    
    def cursor(self,m):

        self.mouse_pos = pygame.mouse.get_pos()
    
    def F3(self,m):

        inputText = [
            "Made by sll :3","",
            "=====[GLOBAL]=====","",
            f"Screen: {m.width}x{m.height}",
            f"Status: {m.status}",
            f"Anim: {self.anim}",
            f"Keys: {m.keys}",
            f"Mouse: {m.mouse}",
            f"FPS: {m.fps}",
            f"Max fps: {m.maxfps}",
            f"Mouse pos: {self.mouse_pos[0]-m.width//2,-(self.mouse_pos[1]-m.height//2)}",
            f"Main offset: {self.offset}"
        ]

        for key,value in m.config.items():
            if key == "zoom":
                value = str(value)[:3]
            inputText.insert(4,f"{key}: {value}")
        
        if m.status == "game":
            inputText.append("")
            inputText.append("=====[GAME]=====")
            inputText.append("")
            inputText.append("Cells:")
            for i in m.Game.cells:
                line = ""
                for j in i:
                    if j == None:
                        line = line + "- "
                    elif j == 0:
                        line = line + "0 "
                    elif j == 1:
                        line = line + "X "
                    else:
                        line = line + "E "

                inputText.append(line)
            inputText.append(f"Player: {m.Game.player}")
            inputText.append(f"Selected cell: {m.Game.selected_cell}")
            inputText.append(f"Last pos: {m.Game.x,m.Game.y}")

        font = pygame.font.Font(f"font\\text.ttf", 8)
        for i in range(len(inputText)):
            text = font.render(str(inputText[i]), False, m.Disp.colors[m.config['them']]['global']['text'])
            m.screen.blit(text, (10,10+8*i))
            

    def gradient(self,color1, color2, steps):

        gradient = []
        
        for step in range(steps + 1):
            r = int(color1[0] + (color2[0] - color1[0]) * step / steps)
            g = int(color1[1] + (color2[1] - color1[1]) * step / steps)
            b = int(color1[2] + (color2[2] - color1[2]) * step / steps)
            gradient.append((r, g, b))
        
        return gradient