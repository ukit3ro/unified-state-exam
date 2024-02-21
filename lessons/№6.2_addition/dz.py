from turtle import *
from math import *

#1
""" left(90)
k = 5
cnt = 0
speed(0)
pendown()
begin_fill()
for i in range(4):
    forward(137*k)
    right(120)
end_fill()
canvas = getcanvas()
penup()

for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if canvas.find_overlapping(x*k, y*k, x*k, y*k) == (5, 0):
            cnt += 1
done() """
#1
""" cnt = 0
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if x> 0 and\
            y > tan(radians(30))*x and\
                y < tan(radians(150)) * x + 137:
                    cnt +=1
print(cnt) """

#2
""" left(90)
k = 15
pendown()
cnt = 0
speed(0)

begin_fill()
for _ in range(12):
    right(90)
    forward(125*k)
    forward(17*k)
end_fill()
canvas = getcanvas()

for x in range(-100, 3000):
    for y in range(-3000, 100):
       if canvas.find_overlapping(x * k, y * k, x * k, y * k) != ():
           cnt += 1
           
print(cnt) """
    
#3
""" left(90)
k = 25
pendown()
cnt = 0
tracer(0)

right(90)
for i in range(3):
    right(45)
    forward(10*k)
    right(45)
right(315)
forward(10*k)
for _ in range(2):
    right(90)
    forward(10*k)

penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x*k, y*k)
        dot(4)
done() """

#4
""" left(90)
k = 25
pendown()
tracer(0)

for _ in range(4):
    right(90)
    forward(5*k)
penup()

for x in range(-10, 10):
    for y in range(-10, 10):
        setpos(x*k, y*k)
        dot(4)
done() """