from turtle import *

#1
""" left(90)
pendown()
speed(0)
k = 25

for _ in range(6):
    forward(6*k)
    right(90)

penup()

forward(3*k)
right(270)
forward(5*k)
right(90)

pendown()
for _ in range(6):
    forward(11*k)
    right(90)
    forward(8*k)
    right(90)
penup()

for x in range(-100, 100):
    for y in range(-100, 100 ):
        setpos(x*k, y*k)
        dot(4)
done() """

#2
""" left(90)
pendown()
tracer(0)
k = 25

for _ in range(8):
    forward(7*k)
    right(90)
penup()

forward(2*k)
right(90)
forward(3*k)
left(90)
pendown()

for i in range(2):
    forward(6*k)
    right(90)
    forward(8*k)
    right(90)

penup()
for x in range(-10, 20):
    for y in range(-10, 40):
        setpos(x*k, y*k)
        dot(4)
done() """

#3
from math import *
cnt = 0
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if x> 0 and\
            y > tan(radians(30))*x and\
                y < tan(radians(150)) * x + 101:
                    cnt +=1
print(cnt)
    