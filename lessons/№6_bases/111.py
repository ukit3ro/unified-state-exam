#1
from turtle import *
# k = 30
# tracer(0)

# left(90)
# pendown()

# for i in range(7):
#     forward(10*k)
#     right(120)
    
# penup()
# for x in range(-10, 10):
#     for y in range(-10,20):
#         goto(x*k, y*k)
#         dot(4)

# done()


#2
# k = 30
# tracer(0)

# pendown()

# for i in range(8):
#     forward(6*k)
#     right(120)
    
# penup()
# for x in range(-10, 10):
#     for y in range(-10,20):
#         goto(x*k, y*k)
#         dot(4)

# done()

#3
# tracer(0)
# left(90)
# k = 20

# pendown()

# right(315)
# for i in range(7):
#     forward(16*k)
#     right(45)
#     forward(8*k)
#     right(135)
 
# penup()

# for x in range(-20, 10):
#     for y in range(-10, 20):
#         goto(x*k, y*k)
#         dot(4)

# done()

#4
# tracer(0)
# left(90)
# k = 30

# pendown()


# for i in range(7):
#     forward(5*k)
#     right(45)
#     forward(10*k)
#     right(135)
 
# penup()

# for x in range(-20, 10):
#     for y in range(-10, 20):
#         goto(x*k, y*k)
#         dot(4)

# done()


#5
# tracer(0)
# left(90)
# k = 30

# pendown()

# begin_fill()
# for i in range(3):
#     forward(111*k)
#     right(120)
# end_fill()

# cnt = 0
# canvas = getcanvas()

# for x in range(-100, 100):
#     for y in range(-100, 100):
#         if canvas.find_overlapping(x*k, y*k, x*k, y*k) == (5, ):
#             cnt += 1

# print(cnt)
# done()


#6
# tracer(0)
# left(90)
# k = 10

# pendown()

# begin_fill()
# for i in range(12):
#     right(90)
#     forward(120*k)
#     right(90)
#     forward(14*k)
# end_fill()

# cnt = 0
# canvas = getcanvas()

# for x in range(-200, 500):
#     for y in range(-200, 200):
#         if canvas.find_overlapping(x*k, y*k, x*k, y*k):
#             cnt += 1

# print(cnt)
# done()


#7
# speed(0)
# k = 20

# begin_fill()
# for i in range(4):
#     circle(5*k, -180)
#     left(90)
# end_fill()

# cnt = 0
# canvas = getcanvas()
# for x in range(-100, 100):
#     for y in range(-100, 100):
#         if canvas.find_overlapping(x*k, y*k, x*k, y*k) == (5, ):
#             cnt += 1
# print(cnt)
# done()


