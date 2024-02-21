from turtle import *

#1
""" speed(0)
left(90)
pendown()
k = 15

for i in range(12):
    right(60)
    forward(5*k)
    left(30)
    backward(5*k)
done() """

#2
""" speed(0)
pendown()
k = 15

for i in range(5):
    forward(10*k)
    right(144)
    forward(10*k)
    left(72)
done() """

#3
""" tracer(0)
pendown()
k = 20

for i in range(9):
    forward(5*k)
    right(90)
    forward(4*k)
    right(90)

penup()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*k, y*k)
        dot(4)
done() """

#4
""" tracer(0)
pendown()
left(90)
k = 40

for i in range(16):
    forward(5*k)
    left(70)
    back(2*k)
    right(10)

penup()

for x in range(-10, 10):
    for y in range(-10, 10):
        goto(x*k, y*k)
        dot(4)
done() """

tracer(0)
pendown()
left(90)
k = 40

for i in range(12):
    forward(5*k)
    right(120)

penup()

for x in range(-10, 10):
    for y in range(-10, 10):
        goto(x*k, y*k)
        dot(4)
done()
     
    