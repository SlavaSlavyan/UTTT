import pygame
import math

class Logo:

    def __init__(self,m):

        m.Log.write("Инициализация отображения сцены Logo.","DEBUG")

        self.rotate = 0
        self.offset = [100,150,200]

    def main(self,m):

        m.Disp.screen.fill(m.Disp.colors['Logo']['bg'])

        self.letter(m,"s",(-200,0),(self.offset[0],0))
        self.letter(m,"l",(0,0),(self.offset[1],0))
        self.letter(m,"l",(200,0),(self.offset[2],0))

        self.rotate += 0.03*m.Disp.anim_speed
        if m.Disp.anim_speed != 0:
            self.offset = [i/1.06*m.Disp.anim_speed for i in self.offset]

    def letter(self, m, symbol:str, pos:tuple, offset:tuple):

        z = m.Disp.zoom

        if symbol == "s":
            points = [[0,0],[3,0],[3,3],[1,3],[1,4],[3,4],[3,5],[0,5],[0,2],[2,2],[2,1],[0,1]]
        if symbol == "l":
            points = [[0,0],[3,0],[3,1],[1,1],[1,5],[0,5]]
        
        for point in points:

            for cord in range(2):
                point[cord] *= 50*z

            point[0] = m.Disp.width//2 + point[0] - 75*z + pos[0]*z + m.Disp.width*(offset[0]/100)
            point[1] = m.Disp.height//2 - point[1] + 125*z - pos[1]*z - m.Disp.height*(offset[1]/100)
        
        points2 = []

        for point in points:
            points2.append((point[0] + math.cos(self.rotate)*50*z,point[1] - math.sin(self.rotate)*50*z))
        
        for i in range(len(points)):
            pygame.draw.polygon(m.Disp.screen,m.Disp.colors['Logo']['text'],(points[i-1],points2[i-1],points2[i],points[i]))

        pygame.draw.polygon(m.Disp.screen,m.Disp.colors['Logo']['bg'],points)
        pygame.draw.polygon(m.Disp.screen,m.Disp.colors['Logo']['text'],points,1)