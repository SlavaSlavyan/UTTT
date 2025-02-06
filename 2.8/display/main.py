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
                    "active-passive":self.gradient((92, 99, 112),(171,178,191),30),
                    "0toX":self.gradient((97, 175, 239),(198, 107, 60),30)
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

        elif self.anim == 'game':
            self.Game.main(m)
        
        if m.F3:
            self.F3(m)
        
        self.cursor(m)
    
    def cursor(self,m):

        self.mouse_pos = pygame.mouse.get_pos()
    
    def F3(self,m):

        z = 8

        inputText = [
            "WARNING!!! F3 mode can summon lags, please use F3 only in debug.",
            "Made by sll :3","",
            "=====[GLOBAL]=====","","",
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
            inputText.insert(5,f"{key}: {value}")

        font = pygame.font.Font(f"font\\text.ttf", z)
        for i in range(len(inputText)):
            text = font.render(str(inputText[i]), False, m.Disp.colors[m.config['them']]['global']['text'])
            m.screen.blit(text, (10,10+z*i))
        
        inputText = [
            "Status and Anim variables","",
            f"=====[STATUS|{m.status}]=====",""
        ]

        if m.status == "loading":
            inputText.append("Idk just wait <3")
        
        if m.status == "game":
            inputText.append(":cells")
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

                line = line + " "
                inputText.append(line)

            inputText.append("")
            inputText.append(f"{m.Game.player} :player")
            inputText.append(f"{m.Game.selected_cell} :selected cell")
            inputText.append(f"{m.Game.x,m.Game.y} :last pos")
        
        inputText.append("")
        inputText.append(f"=====[ANIM|{self.anim}]=====")
        inputText.append("")

        if self.anim == "game" or self.anim == "game_start":
            inputText.append(f"{round(self.Game.selectsize,2)} :select size")
            inputText.append(f"{self.Game.selectpos} :select pos")
            inputText.append(f"{[round(self.Game.selectoffset[0],2),round(self.Game.selectoffset[1],2)]} :select offset")
            inputText.append(f"{self.Game.selectcolor} :select color")
            inputText.append("")
            inputText.append(":colors")
            for key,value in self.Game.colors.items():
                if isinstance(value,tuple):
                    inputText.append(f"{value} :{key}  ")
            if self.anim == "game_start":
                inputText.append("")
                inputText.append(":offset")
                for i in range(len(self.Game.offset)):
                    inputText.append(f"[{round(self.Game.offset[i],2)}].{i}  ")
            
        
        font = pygame.font.Font(f"font\\text.ttf", z)
        for i in range(len(inputText)):
            text = font.render(str(inputText[i]), False, m.Disp.colors[m.config['them']]['global']['text'])
            text_width = text.get_width()
            screen_width = m.screen.get_width()
            x_position = screen_width - text_width - 10
            m.screen.blit(text, (x_position, 10 + z * i))

    def gradient(self,color1, color2, steps):

        gradient = []
        
        for step in range(steps + 1):
            r = int(color1[0] + (color2[0] - color1[0]) * step / steps)
            g = int(color1[1] + (color2[1] - color1[1]) * step / steps)
            b = int(color1[2] + (color2[2] - color1[2]) * step / steps)
            gradient.append((r, g, b))
        
        return gradient