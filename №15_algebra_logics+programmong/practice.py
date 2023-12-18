#рассмотрю несколько прототипов решения задач и попытаюсь на их основе выполнить домашнуюю работу

#1 (дел прототип)
""" def aoa(n, m):
    return n % m == 0

for A in range(1, 1000):
    A_right = True
    for x in range(1, 1000):
        if ((aoa(x, A) and aoa(x, 17)) <= aoa(x, 34)) == False:
            A_right = False
            break
    if A_right == True:
        print(A) """
        


#2 (прототип побитовой конъюнкции)
for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if ((x & A != 0) <= (((x & 23 == 0) and (x & 8 == 0)) <= (x & 7 != 0))) == False:
            flag = False
            break
    if flag == True:
        print(A)

#3 (прототип неравенств на плоскости)
""" for A in range(-1000, 1000):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if func(x, y, A) == False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A)
        break """

#4 (прототип задания на отрезки)
P = list(range(5, 31))
Q = list(range(14, 24))
A = list(range(1000))
for x in range(1000):
    if (((x in P) == (x in Q)) <= (x not in A)) == False:
        A.remove(x)
print(A)
#длина отрезка = большее - меньшее

#5 прототип ДЕЛ + отрезки
