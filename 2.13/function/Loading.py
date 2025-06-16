import turtle
import math

turtle.Screen().setup(600,400)
turtle.Screen().title("Loading")
turtle.bgcolor((0,0,0))
turtle.pencolor((1,1,1))
turtle.hideturtle()
turtle.tracer(0)

rotateX = 0
rotateY = 0

while True:
    
    turtle.clear()
    
    turtle.teleport((math.cos(rotateX*10)*20),0)
    turtle.write("Loading UTTT",False,'center',("Courier",30,"normal"))
    
    points = []
    points2 = []
    
    for i in range(1,10):
        points.append((math.cos(rotateX*(math.pi*i))*200,-100 + math.sin(rotateY*(math.pi*i))*50))
        points2.append((math.cos(-rotateX*(math.pi*i))*200,-100 + math.sin(-rotateY*(math.pi*i))*50))
    
    for i in range(len(points)-1):
        
        for i in range(len(points)):
            
            turtle.teleport(points[i][0],points[i][1])
            turtle.goto(points[-1][0],points[-1][1])
        
        points.pop(-1)
    
    for i in range(len(points2)-1):
        
        for i in range(len(points2)):
            
            turtle.teleport(-points2[i][0],points2[i][1])
            turtle.goto(-points2[-1][0],points2[-1][1])
        
        points2.pop(-1)
    
    turtle.update()

    rotateX += 0.002
    rotateY += 0.002