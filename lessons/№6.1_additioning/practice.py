from turtle import *

#1
k = 30
tracer(0)
for i in range(24):
    forward(3*k)
    left(60)

penup()
for x in range(-10, 20):
    for y in range(-10, 20):
        goto(x*k, y*k)
        dot(4)
done()

