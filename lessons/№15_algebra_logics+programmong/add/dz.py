
#1
""" def  d3l(n, m):
    return n % m == 0

for A in range(1, 1000):
    flag = True
    for x in range(1, 10000):
        if ((d3l(x, A) and d3l(x, 8)) <= ((not(d3l(x, 8))) or d3l(x, 513))) == False:
            flag = False
            break
    if flag == True:
        print(A)
        break """

#2
""" def  d3l(n, m):
    return n % m == 0

for A in range(1, 1000):
    flag = True
    for x in range(1, 10000):
        if (((d3l(x, 24) and d3l(x, 36)) <= d3l(x, A)) and (A**2 - A - 5000 < 112))== False:
            flag = False
            break
    if flag == True:
        print(A) """
        
#3
""" def funcc(x, A):
    return ((x & 75 == 0) or ((x & 80 == 0) <= (x & A != 0)))

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if funcc(x, A) == False:
            flag = False
            break
    if flag == True:
        print(A)
        break         """
        
#4
""" def funcc(x, A):
    return ((x & 56 != 0) or (x & 17 != 0)) <= ((x & 15 == 0) <= (x & A != 0))

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if funcc(x, A) == False:
            flag = False
            break
    if flag == True:
        print(A)
        break  """
        
#5
""" def funcc(x, y, A):
    return (x > 15) or (y < x) or (x * x * 2 < A)

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        for y in range(1000):
            if funcc(x, y, A) == False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A)
        break  """
        
#6
""" def funcc(x, y, A):
    return (x + 2 * y > A) or (x <= 15) or (y <= 30)

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        for y in range(1000):
            if funcc(x, y, A) == False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A) """
        
#7
""" def funcc(x, y, A):
    return (10 * y - x + 31 != 0) or (A < x) or (A < y)

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if funcc(x, y, A) == False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A) """

#8
def funcc(x, y, A):
    return ((x > 10) <= (x * y + 11 * x >= A)) and ((y * x + y > A) <= (y >= 1)) 
cnt = 0
for A in range(0, 1000):
    flag = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if funcc(x, y, A) == False:
                flag = False
            break
        if flag == False:
            break
    if flag == True:
        cnt += 1
print(cnt)

#9
""" def  d3l(n, m):
    return n % m == 0

for A in range(1, 1000):
    flag = True
    for x in range(1, 10000):
        if ((d3l(x, A) and d3l(x, 7)) <= ((not(d3l(x, 7))) or d3l(x, 311)))== False:
            flag = False
            break
    if flag == True:
        print(A)
        break """
        
#10
""" def  d3l(n, m):
    return n % m == 0
def fucc(x, A):
    return ((x + 40 < A) or (x + A < 40)) <= (d3l(x, A))
for A in range(1, 1000):
    flag = True
    for x in range(1, 10000):
        if fucc(x, A)== False and d3l(x, A) == False:
            flag = False
            break
    if flag == True:
        print(A) """
        
#11
""" def funcc(x, y, A):
    return (x**2 - 11 * x + 28 > 0) or (y**2 - 9 * y + 14 > 0) or (x**2 + y**2 > A) 

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if funcc(x, y, A) == False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A) """
        
#12
""" def treug(n, m, k):
    a = sorted([n, m, k])
    return (a[0] + a[1]) > a[2]

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if (not((treug(x, 11, 24) == (not(max(x,7) > 32))) and treug(x, A, 7))) == False:
            flag = False
            break
    if flag == True:
        print(A) """

#13
""" def angle(a, b, c):
    return (a + b + c) == 180

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if (angle(47, A, x + 40) == (angle(A, x, 45) and (not(A + 30 < 156)))) == False:
            flag = False
            break
    if flag == True:
        print(A)
        break """
        


        
        
        