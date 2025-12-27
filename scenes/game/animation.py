import pygame

class Animation:

    def __init__(self,mainself):

        self.counter = 1.001
        self.speed = 0.1

    def main(self,mainself):

        self.max_screen_size = max(mainself.Display.width, mainself.Display.height)

        counter = self.counter-0.001

        self.back_rect(mainself,counter)
        self.big_cells_grid(mainself,counter)

        self.cells_grid(mainself,mainself.Display.colors[5],(0,0),size=(counter-1)/-4)

        self.select(mainself,mainself.Scenes.game.Select.select_points,counter)

        for y in range(-1,2):
            for x in range(-1,2):
                
                if not (y == 0 and x == 0):
                    self.cells_grid(mainself,mainself.Display.colors[5],(200*x,200*y),(self.max_screen_size*x*(counter*(1 + abs(x+y))),self.max_screen_size*y*(counter*(1 + abs(x+y)))))

        if self.speed > 0:
            self.counter /= (1 + self.speed*mainself.Display.speed)
        if self.speed < 0:
            self.counter *= (1 - self.speed*mainself.Display.speed)

    def back_rect(self,mainself,counter: float = 0):

        z = mainself.Display.zoom

        pygame.draw.rect(mainself.Display.screen,mainself.Display.colors[3],
                        (mainself.Display.width//2 -300*z*-(counter-1),
                        mainself.Display.height//2 -300*z*-(counter-1),
                        600*z*-(counter-1),600*z*-(counter-1)))
        
    def big_cells_grid(self,mainself,counter: float = 0):

        z = mainself.Display.zoom

        pygame.draw.line(mainself.Display.screen,mainself.Display.colors[4],
                        (mainself.Display.width//2 + 300*z - self.max_screen_size*counter,
                        mainself.Display.height//2 - 100*z),
                        (mainself.Display.width//2 - 300*z - self.max_screen_size*counter,
                        mainself.Display.height//2 - 100*z),
                        round(5*z))

        pygame.draw.line(mainself.Display.screen,mainself.Display.colors[4],
                        (mainself.Display.width//2 + 300*z + self.max_screen_size*counter,
                        mainself.Display.height//2 + 100*z),
                        (mainself.Display.width//2 - 300*z + self.max_screen_size*counter,
                        mainself.Display.height//2 + 100*z),
                        round(5*z))
        
        pygame.draw.line(mainself.Display.screen,mainself.Display.colors[4],
                        (mainself.Display.width//2 - 100*z,
                        mainself.Display.height//2 + 300*z + self.max_screen_size*counter),
                        (mainself.Display.width//2 - 100*z ,
                        mainself.Display.height//2 - 300*z + self.max_screen_size*counter),
                        round(5*z))
        
        pygame.draw.line(mainself.Display.screen,mainself.Display.colors[4],
                        (mainself.Display.width//2 + 100*z,
                        mainself.Display.height//2 + 300*z - self.max_screen_size*counter),
                        (mainself.Display.width//2 + 100*z,
                        mainself.Display.height//2 - 300*z - self.max_screen_size*counter),
                        round(5*z))
        
    def cells_grid(self,mainself,color: tuple, end_pos: tuple, offset: tuple = (0,0), size: float = 0.25, width: float = 3):

        z = mainself.Display.zoom

        pygame.draw.line(mainself.Display.screen,color,
                        (mainself.Display.width//2 + 300*size*z + end_pos[0]*z+offset[0],
                        mainself.Display.height//2 - 100*size*z - end_pos[1]*z-offset[1]),
                        (mainself.Display.width//2 - 300*size*z + end_pos[0]*z+offset[0],
                        mainself.Display.height//2 - 100*size*z - end_pos[1]*z-offset[1]),
                        round(width*z))

        pygame.draw.line(mainself.Display.screen,color,
                        (mainself.Display.width//2 + 300*size*z + end_pos[0]*z+offset[0],
                        mainself.Display.height//2 + 100*size*z - end_pos[1]*z-offset[1]),
                        (mainself.Display.width//2 - 300*size*z + end_pos[0]*z+offset[0],
                        mainself.Display.height//2 + 100*size*z - end_pos[1]*z-offset[1]),
                        round(width*z))
        
        pygame.draw.line(mainself.Display.screen,color,
                        (mainself.Display.width//2 - 100*size*z + end_pos[0]*z+offset[0],
                        mainself.Display.height//2 + 300*size*z - end_pos[1]*z-offset[1]),
                        (mainself.Display.width//2 - 100*size*z + end_pos[0]*z+offset[0] ,
                        mainself.Display.height//2 - 300*size*z - end_pos[1]*z-offset[1]),
                        round(width*z))
        
        pygame.draw.line(mainself.Display.screen,color,
                        (mainself.Display.width//2 + 100*size*z + end_pos[0]*z+offset[0],
                        mainself.Display.height//2 + 300*size*z - end_pos[1]*z-offset[1]),
                        (mainself.Display.width//2 + 100*size*z + end_pos[0]*z+offset[0],
                        mainself.Display.height//2 - 300*size*z - end_pos[1]*z-offset[1]),
                        round(width*z))
    
    def select(self,mainself,points: list, counter: float):

        z = mainself.Display.zoom

        parts = []
        
        for Y in range(-1,2,2):
            for X in range(-1,2,2):

                parts.append([])

                for point in points:

                    x = mainself.Display.width//2 - 320*z*X + point[0]*X * 50*z + self.max_screen_size*counter*-X
                    y = mainself.Display.height//2 - 320*z*Y + point[1]*Y * 50*z + self.max_screen_size*counter*-Y

                    parts[-1].append((x,y))

        for part in parts:
            pygame.draw.polygon(mainself.Display.screen,mainself.Display.colors[6],part)