import pygame
import math

class Display:

    def __init__(self,mainself):

        self.points_letter_s = [[0,0],[3,0],[3,3],[1,3],[1,4],[3,4],[3,5],[0,5],[0,2],[2,2],[2,1],[0,1]]
        self.points_letter_l = [[0,0],[3,0],[3,1],[1,1],[1,5],[0,5]]

        self.black_gray = mainself.Display.gradient(mainself.Display.colors[0],mainself.Display.colors[2],100)
        self.yellow_gray = mainself.Display.gradient(mainself.Display.colors[1],mainself.Display.colors[2],100)

        self.counter = 0

        self.grad_t = 0

    def main(self,mainself):

        mainself.Display.screen.fill(self.black_gray[round(self.grad_t)])

        self.draw_letter(mainself,"s",-200)
        self.draw_letter(mainself,"l",0)
        self.draw_letter(mainself,"l",200)

        if self.counter >= 60:
            self.grad_t += 100/60 * mainself.Display.speed

        if round(self.grad_t) > 100:
            mainself.Display.anim = 'menu'

        self.counter += 1 * mainself.Display.speed
    
    def draw_letter(self,mainself,letter:str,anchor_point:float):

        if letter == "s":
            points_letter = self.points_letter_s
        if letter == "l":
            points_letter = self.points_letter_l

        z = mainself.Display.zoom

        projection_letter = []

        for i in range(len(points_letter)):
            
            x = points_letter[i][0] * 40 * z - 60 * z + anchor_point * z + mainself.Display.width//2
            y = -points_letter[i][1] * 40 * z + 100 * z + mainself.Display.height//2

            projection_letter.append((x,y))
        
        second_projection_letter = []

        for i in range(len(points_letter)):

            x = projection_letter[i][0] + math.cos(math.pi/2*self.counter/60)*40
            y = projection_letter[i][1] + math.sin(math.pi/2*self.counter/60)*40
            
            second_projection_letter.append((x,y))

        for i in range(len(points_letter)):
            pygame.draw.polygon(mainself.Display.screen, self.yellow_gray[round(self.grad_t)], [projection_letter[i-1],second_projection_letter[i-1],second_projection_letter[i],projection_letter[i]])
        
        pygame.draw.polygon(mainself.Display.screen, self.black_gray[round(self.grad_t)],projection_letter)
        pygame.draw.polygon(mainself.Display.screen, self.yellow_gray[round(self.grad_t)],projection_letter,1)