import pygame
import math

class Display:

    def __init__(self,mainself):

        self.points_letter_s = [[0,0],[3,0],[3,3],[1,3],[1,4],[3,4],[3,5],[0,5],[0,2],[2,2],[2,1],[0,1]]
        self.points_letter_l = [[0,0],[3,0],[3,1],[1,1],[1,5],[0,5]]

        self.offset = []
        for i in range(3):
            self.offset.append(-mainself.Display.width*(2+i))

        self.counter = 0

    def main(self,mainself):

        z = mainself.Display.zoom
        
        mainself.Display.screen.fill(mainself.Display.colors[0])

        self.draw_letter(mainself,"s",-200,0)
        self.draw_letter(mainself,"l",0,0)
        self.draw_letter(mainself,"l",200,0)

        self.counter += 1 * mainself.Display.speed
    
    def draw_letter(self,mainself,letter:str,anchor_point:float,offset:float):

        if letter == "s":
            points_letter = self.points_letter_s
        if letter == "l":
            points_letter = self.points_letter_l

        z = mainself.Display.zoom

        projection_letter = []

        for i in range(len(points_letter)):
            
            x = points_letter[i][0] * 40 * z - 60 * z + anchor_point * z + offset * z + mainself.Display.width//2
            y = -points_letter[i][1] * 40 * z + 100 * z + mainself.Display.height//2

            projection_letter.append((x,y))
        
        second_projection_letter = []

        for i in range(len(points_letter)):

            x = projection_letter[i][0] + math.cos(math.pi/2*self.counter/60)*40
            y = projection_letter[i][1] + math.sin(math.pi/2*self.counter/60)*40
            
            second_projection_letter.append((x,y))
            
        #for i in range(len(points_letter)):
            #pygame.draw.line(mainself.Display.screen, mainself.Display.colors[1], projection_letter[i-1], projection_letter[i],1)

        for i in range(len(points_letter)):
            pygame.draw.polygon(mainself.Display.screen, mainself.Display.colors[1], [projection_letter[i-1],second_projection_letter[i-1],second_projection_letter[i],projection_letter[i]])
        
        pygame.draw.polygon(mainself.Display.screen, mainself.Display.colors[0],projection_letter)
        pygame.draw.polygon(mainself.Display.screen, mainself.Display.colors[1],projection_letter,1)