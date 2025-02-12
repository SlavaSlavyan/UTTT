import pygame

from display.game import Game

class Display:

    def __init__(self,m):
        
        self.mouse_pos = pygame.mouse.get_pos()
        self.anim = 'game_start'
        self.colors = {
            "dark":{
                "global":{
                    "text":(255,255,255),
                    "mouse":(229, 192, 123)
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
        self.F3update = 0
        self.F3text = [[],[]]
        self.Game = Game(m,self)
    
    def main(self,m):

        self.ratio = [m.width/100,m.height/100]

        if self.anim == 'game_start':
            self.Game.start(m)

        elif self.anim == 'game':
            self.Game.main(m)
        
        elif self.anim == 'game_end':
            self.Game.end(m)
        
        if m.F3:
            self.F3(m)
        
        self.cursor(m)
    
    def cursor(self,m):

        self.mouse_pos = pygame.mouse.get_pos()
        x,y = self.mouse_pos
        
        pos = [(x,y),(x,y+16),(x+10,y+12)]
        pygame.draw.polygon(m.screen, self.colors[m.config['them']]['global']['mouse'], pos)
        for i in range(len(pos)):
            pygame.draw.aaline(m.screen, self.colors[m.config['them']]['global']['mouse'], pos[i-1], pos[i])
    
    def F3(self,m):

        z = 8

        if self.F3update == 0:

            self.F3text[0] = [
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
                self.F3text[0].insert(5,f"{key}: {value}")

        font = pygame.font.Font(f"font\\text.ttf", z)
        for i in range(len(self.F3text[0])):
            text = font.render(str(self.F3text[0][i]), False, m.Disp.colors[m.config['them']]['global']['text'])
            m.screen.blit(text, (10,10+z*i))
        
        if self.F3update == 0:

            self.F3text[1] = [
                "Status and Anim variables","",
                f"=====[STATUS|{m.status}]=====",""
            ]

            if m.status == "loading":
                self.F3text[1].append("Idk just wait <3")
            
            if m.status == "game":
                self.F3text[1].append(":cells")
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
                    self.F3text[1].append(line)

                self.F3text[1].append("")
                self.F3text[1].append(f"{m.Game.player} :player")
                self.F3text[1].append(f"{m.Game.selected_cell} :selected cell")
                self.F3text[1].append(f"{m.Game.x,m.Game.y} :last pos")
            
            self.F3text[1].append("")
            self.F3text[1].append(f"=====[ANIM|{self.anim}]=====")
            self.F3text[1].append("")

            if self.anim == "game" or self.anim == "game_start":
                self.F3text[1].append(f"{round(self.Game.selectsize,2)} :select size")
                self.F3text[1].append(f"{self.Game.selectpos} :select pos")
                self.F3text[1].append(f"{[round(self.Game.selectoffset[0],2),round(self.Game.selectoffset[1],2)]} :select offset")
                self.F3text[1].append(f"{self.Game.selectcolor} :select color")
                self.F3text[1].append("")
                self.F3text[1].append(":colors")
                for key,value in self.Game.colors.items():
                    if isinstance(value,tuple):
                        self.F3text[1].append(f"{value} :{key}  ")
                if self.anim == "game_start":
                    self.F3text[1].append("")
                    self.F3text[1].append(":offset")
                    for i in range(len(self.Game.offset)):
                        self.F3text[1].append(f"[{round(self.Game.offset[i],2)}].{i}  ")
        
        font = pygame.font.Font(f"font\\text.ttf", z)
        for i in range(len(self.F3text[1])):
            text = font.render(str(self.F3text[1][i]), False, m.Disp.colors[m.config['them']]['global']['text'])
            text_width = text.get_width()
            screen_width = m.screen.get_width()
            x_position = screen_width - text_width - 10
            m.screen.blit(text, (x_position, 10 + z * i))
        
        if self.F3update == 0:
            self.F3update = 30
        else:
            self.F3update -= 1

    def gradient(self,color1, color2, steps):

        gradient = []
        
        for step in range(steps + 1):
            r = int(color1[0] + (color2[0] - color1[0]) * step / steps)
            g = int(color1[1] + (color2[1] - color1[1]) * step / steps)
            b = int(color1[2] + (color2[2] - color1[2]) * step / steps)
            gradient.append((r, g, b))
        
        return gradient