from turtle import * #импортируем нужную для решения задачи библиотеку
k = 5 # коэффициент, на который мы умножаем для масштабирования рисунка в большую сторону

#задание №5
""" pen()
tracer(0)
for i in range(124):
    right(30)
    forward(5*k)
done()
 """

#задание №6
""" pen()
tracer(0)
for i in range(24):
    right(60)
    forward(10*k)
    left(30)
    backward(20*k)
done() """


#задание №7
""" pen()
tracer(0)
k = 10
for i in range(13):
    forward(6*k)
    right(90)
penup()
for x in range(10):
    for y in range(-10, 10):
        goto(x*k, y*k)
        dot(5)
done() """

#задание №8
""" pen() #опускаем перо
tracer(0) #анимация рисования на 0
k = 10 # коэффициент масштабирования
right(45)
forward(5*k) #перемещение вперёд умножается на масштаб
for i in range(7): #цикл сколько раз надо повторить
    right(45)
    forward(12*k)
    right(135)
    forward(6*k)

penup() #поднимаем перо
for x in range(-10, 10): #рисуем координатные точки
    for y in range(-20, 10):
        goto(x*k, y*k) #масштабируем для видимости
        dot(3)
done() """


#задание №9
""" pen()
tracer(0)
k = 5
for i in range(): """