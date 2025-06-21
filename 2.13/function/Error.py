import turtle
import datetime

class Error:

    def __init__(self):

        turtle.Screen().setup(1200,800)
        turtle.Screen().title("Error!")
        turtle.bgcolor((0,0,0))
        turtle.pencolor((1,1,1))
        turtle.hideturtle()
        turtle.tracer(0)

    def main(self,error):

        turtle.teleport(0,turtle.Screen().window_height()//2-40)
        turtle.write(f"[{datetime.datetime.now().strftime('%Y.%m.%d %H:%M:%S')}]",False,'center',("Courier",16,"normal"))
        turtle.teleport(5-turtle.Screen().window_width()//2,-turtle.Screen().window_height()//2)
        turtle.write(error,False,'left',("Courier",8,"normal"))

        turtle.done()