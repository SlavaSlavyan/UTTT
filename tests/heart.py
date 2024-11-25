from turtle import *
import math

bgcolor('black')
pencolor('white')
shape("square")
shapesize(1, 1)
hideturtle()
up()
tracer(0)

x = -100
k = 0

math.pow(-x,2)
while x != 100:
    x+=0.1
    teleport(x,x**(2/3)+0.9*math.sin(k*x)*math.sqrt(3+abs(-x**2)))
    stamp()
    
done()