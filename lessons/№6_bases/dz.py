from turtle import *
k = 20


#1
""" pen()
speed(10000)
for i in range(13):
    right(45)
    forward(10*k)
    right(10)
done() """

#2
""" pen()
speed(10000)
right(45)
forward(k*4)
for i in range(10):
    right(45)
    forward(k*7)
    right(135)
    forward(k*4)
penup()
for x in range(10):
    for y in range(-10, 10):
        goto(x*k, y*k)
        dot(4)
done() """

#3
""" pen()
tracer(0)
right(40)
for i in range(6):
    right(120)
    forward(3*k)
    left(60)
    backward(3*k)
penup()
for x in range(-10,10):
    for y in range(-10, 10):
        goto(x*k, y*k)
        dot(4)
done() """

#4
""" pen()
speed(1000000)
for i in range(5):
    forward(10*k)
    right(144)
    forward(10*k)
    left(72)
done() """

#5
""" pen()
speed(1000000)
for o in range(8):
    right(60)
    forward(k*7)
done() """

#6
""" pen()
speed(1000000)
for o in range(8):
    forward(k*2)
    left(540)
    backward(k*2)
    right(450)
    forward(k*5)
penup()
for x in range(-10,10):
    for y in range(-10, 10):
        goto(x*k, y*k)
        dot(4)
done() """

#7
""" pen()
tracer(0)
for i in range(30):
    forward(k*4)
    right(120)
penup()
for x in range(-10,10):
    for y in range(-10, 10):
        goto(x*k, y*k)
        dot(4)
done() """

""" pen()
tracer(0)
for u in range(6):
    forward(k*6)
    right(300)
penup()
forward(3*k)
right(270)
forward(5*k)
right(90)
pendown()
for i in range(2):
    forward(7*k)
    right(270)
    forward(9*k)
    right(270)
penup()
for x in range(-10,10):
    for y in range(-10, 10):
        goto(x*k, y*k)
        dot(4)
done()
 """

#8
""" pen()
tracer(0)
for i in range(6):
    forward(6*k)
    right(90)
penup()
forward(3*k)
right(270)
forward(5*k)
right(90)
pendown()
for u in range(6):
    forward(11*k)
    right(90)
    forward(8*k)
    right(90)
penup()
for x in range(-10,10):
    for y in range(-20, 10):
        goto(x*k, y*k)
        dot(4)
done()
 """
 
#9
""" pen()
tracer(0)
for i in range(4):
    forward(10*k)
    right(270)

penup()
forward(3*k)
right(270)
forward(5*k)
right(90)

pendown()
for u in range(2):
    forward(10*k)
    right(270)
    forward(12*k)
    right(270)

penup()
for x in range(-10,20):
    for y in range(-20, 20):
        goto(x*k, y*k)
        dot(4)
done() """


#additional
pendown()
speed(100000)

for i in range(2):
    forward(17*k)
    left(90)
    forward(10*k)
    left(90)

penup()

back(4*k)
right(90)
back(3*k)
left(90)

pendown()

for i in range(2):
    forward(40*k)
    right(90)
    forward(10*k)
    right(90)
penup()

for x in range(-10,50):
    for y in range(-10, 20):
        goto(x*k, y*k)
        dot(4)

done()
