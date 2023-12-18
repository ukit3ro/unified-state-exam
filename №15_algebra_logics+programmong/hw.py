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

#2
""" def aoa(n, m):
    return n % m == 0

for A in range(1, 1000):
    A_right = True
    for x in range(1, 1000):
        if (aoa(x,15) <= (not(aoa(x, A)) <= (not(aoa(x, 3))))) == False:
            A_right = False
            break
    if A_right == True:
        print(A) """

#3
""" def aoa(n, m):
    return n % m == 0

for A in range(1, 1000):
    A_right = True
    for x in range(1, 10000):
        if ((aoa(x,A) and aoa(x, 8)) <= ((not(aoa(x, 8))) or aoa(x, 240))) == False:
            A_right = False
            break
    if A_right == True:
        print(A)
        break """
        

#4 (конъюнкция)
""" for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if ((x & 23 == 0) <= ((x & 13 != 0) <= (x & A != 0))) == False:
            flag = False
            break
    if flag == True:
        print(A)
        break """
        
        
#5
""" for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if (((x & 41 != 0) and (x & 50 != 0)) <= ((x & A != 0) or (x & 76 != 0))) == False:
            flag = False
            break
    if flag == True:
        print(A)
        break """


#6
""" def func(x, A):
    return (x & 60 != 0) or (x & 47 == 0) or (x & A != 0)

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if func(x, A) == False:
            flag = False
            break
    if flag == True:
        print(A)
        break """

#7
""" def func(x, y, A):
    return ((2 * y + x != 17) or (A > 7 * x) and (A > 3 * y))

for A in range(-1000, 1000):
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



#8
""" def func(x, y, A):
   return (y - 2*x < A) or (x >= 25) or (y >= 40)

for A in range(-1000, 1000):
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


#9
""" def func(x, y, A):
    return ((10 * x - y + 37 != 0) or (A < x) or (A < y))

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if func(x, y, A) == False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A) """


#10
""" def func(x, y, A):
    return (((x >= 8) or (2 * x < y)) or (x * x < A))

for A in range(-1000, 1000):
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


#10 
""" def aoa(n, m):
    return n % m == 0

for A in range(1, 1000):
    A_right = True
    for x in range(1, 1000):
        if (((x + 40 < A) or (x + A < 40)) <= aoa(x, A)) == False:
            A_right = False
            break
    if A_right == True:
        print(A) """
        
#uslozhnenka
#11
for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if ((x & 54 != 0) and (x & 45 != 0) or (x & A == 0) or (x &) ) == False:
            flag = False
            break
    if flag == True:
        print(A)