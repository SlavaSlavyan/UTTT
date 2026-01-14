import turtle
import math
import sys

class Loading:

    def __init__(self):

        turtle.Screen().setup(500,500)
        turtle.Screen().title("SLL LOAD YOOO =)")
        turtle.bgcolor((0,0,0))
        turtle.hideturtle()
        turtle.tracer(0)

        root = turtle.Screen().getcanvas().winfo_toplevel()
        root.protocol("WM_DELETE_WINDOW", lambda: None)

        self.counter = 0

        self.bg_pos = 50
    
    def main(self):
            
        while True:

            turtle.clear()

            turtle.pencolor((0.15,0,0.15))
            self.bg(self.bg_pos,self.bg_pos)
            turtle.pencolor((0.25,0,0.25))
            self.bg(-self.bg_pos/2,self.bg_pos/2)

            for i in range(8):
                self.circle(math.cos(self.counter/20+math.pi/16*i)*150,math.sin(self.counter/20+math.pi/16*i)*150,1/8*(i+1))
                self.cross(math.cos(self.counter/20+math.pi+math.pi/16*i)*150,math.sin(self.counter/20+math.pi+math.pi/16*i)*150,1/8*(i+1))

            #turtle.width(1)
            #turtle.pencolor((0,0,1))
            #turtle.teleport(-turtle.Screen().window_width()//2,0)
            #turtle.goto(turtle.Screen().window_width()//2,0)
            #turtle.pencolor((0,1,0))
            #turtle.teleport(0,turtle.Screen().window_height()//2)
            #turtle.goto(0,-turtle.Screen().window_height()//2)

            turtle.update()

            self.counter += 1
            self.bg_pos -= 1

            if self.bg_pos < 0:
                self.bg_pos += 100
    
    def bg(self, bg_pos_x:float, bg_pos_y:float):

        turtle.width(1)

        for i in range(turtle.Screen().window_width()//50+1):
            turtle.teleport(-turtle.Screen().window_width()//2+50*i+bg_pos_x,
                            -turtle.Screen().window_height()//2)
            turtle.goto(-turtle.Screen().window_width()//2+50*i+bg_pos_x,
                            turtle.Screen().window_height()//2)
        
            turtle.teleport(-turtle.Screen().window_width()//2,
                            -turtle.Screen().window_height()//2+50*i+bg_pos_y)
            turtle.goto(turtle.Screen().window_width()//2,
                            -turtle.Screen().window_height()//2+50*i+bg_pos_y)
    
    def circle(self,x,y,c):

        y -= 25

        turtle.width(1)

        turtle.pencolor((c,c,c))
        
        turtle.fillcolor((0,0,0))
        turtle.teleport(x,y)
        turtle.begin_fill()
        turtle.circle(25,steps=8)
        turtle.end_fill()

        turtle.fillcolor((c,c,c))
        turtle.teleport(x,y+5)
        turtle.begin_fill()
        turtle.circle(20,steps=8)
        turtle.end_fill()

        turtle.fillcolor((0,0,0))
        turtle.teleport(x,y+10)
        turtle.begin_fill()
        turtle.circle(15,steps=8)
        turtle.end_fill()
    
    def cross(self,x,y,c):

        turtle.width(11.5)
        turtle.pencolor((c,c,c))
        for i in range(-1,2,2):
            turtle.teleport(x-17,y-17*i)
            turtle.goto(x+17,y+17*i)

        turtle.width(10)
        turtle.pencolor((0,0,0))
        for i in range(-1,2,2):
            turtle.teleport(x-17,y-17*i)
            turtle.goto(x+17,y+17*i)
    
        turtle.width(6)
        turtle.pencolor((c,c,c))
        for i in range(-1,2,2):
            turtle.teleport(x-17,y-17*i)
            turtle.goto(x+17,y+17*i)

if sys.argv[-1] == "LOADING":
    Loading().main()