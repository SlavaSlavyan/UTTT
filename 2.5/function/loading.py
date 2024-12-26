from turtle import *
import math
import json
import time
import sys

tracer(0)
bgcolor('black')
pencolor('white')
hideturtle()

P = (3.14159)

pos1 = []
pos2 = []

for i in range(4):
    pos1.append(P*((i+1)/2))
print(pos1)
pos2 = pos1
var = 0
size = 3
normal_size = (size)
run = True

while run:
    clear()
    teleport(math.sin(pos1[0])*(50*size),math.cos(pos1[0])*(25*size)+27*size)
    for i in range(-1,4):
        goto(math.sin(pos1[i])*(50*size),math.cos(pos1[i])*(25*size)+27*size)
    
    teleport(math.sin(pos2[0])*(50*size),math.cos(pos2[0])*(25*size)-27*size)
    for i in range(-1,4):
        goto(math.sin(pos2[i])*(50*size),math.cos(pos2[i])*(25*size)-27*size)

    for i in range(4):
        teleport(math.sin(pos1[i])*(50*size),math.cos(pos1[i])*(25*size)+27*size)
        goto(math.sin(pos2[i])*(50*size),math.cos(pos2[i])*(25*size)-27*size)

    update()

    pos1 = [i + 0.001 for i in pos1]
    pos2 = pos1
    pos2 = [i + math.sin(var) for i in pos2]
    var += 0.002
    size = normal_size + math.cos(var)

sys.exit() 