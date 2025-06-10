import turtle
import threading

def start_main():

    from function.Main import Main

    Start = Main(VERS)
    Start.Log.write("Запуск основного цикла...\n","DEBUG")

    turtle.bye()

    while True:
        
        Start.main()

VERS = "2.13.11 DEV"

turtle.Screen().setup(600,400)
turtle.Screen().title("Loading")
turtle.bgcolor((0,0,0))
turtle.pencolor((1,1,1))
turtle.hideturtle()
turtle.tracer(0)
turtle.write("Loading UTTT...",False,'center',("Courier",30,"normal"))
turtle.update()

main = threading.Thread(target=start_main)
main = start_main()

turtle.done()