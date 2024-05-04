#2
""" from math import *
cnt = 0
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if x > 0 and\
            y > tan(radians(30))*x and\
                y < tan(radians(150)) * x + 111:
                    cnt += 1
print(cnt) """

#3
from math import *
""" cnt = 0
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if x> 0 and\
            y > tan(radians(30))*x and\
                y < tan(radians(150)) * x + 123:
                    cnt +=1
print(cnt) """

#4
""" from turtle import *
pendown()
k = 10
cnt = 0
speed(0)

begin_fill()
for _ in range(2):
    right(90)
    forward(120*k)
    right(90)
    forward(14*k)
end_fill()
canvas = getcanvas()

for x in range(-1000, 1000):
    for y in range(-1000, 1000):
       if canvas.find_overlapping(x * k, y * k, x * k, y * k) != ():
           cnt += 1
           
print(cnt) """

#5
""" cnt = 0
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if (y < x + 12*(2**(1/2)) and y > x - 12*(2**(1/2)) and\
            y > -x - 12*(2**(1/2)) and y < -x):
            cnt += 1
print(cnt) """

#6
""" 
from turtle import *
left(90)
speed(0)
pendown()
k = 20


for _ in range(10):
    forward(2*k)
    right(120)
    for i in range(2):
        right(330)
        forward(4*k)
penup()
for x in range(1,20):
    for y in range(1, 10):
        goto(x*k, y*k)
        dot(4)
done() """