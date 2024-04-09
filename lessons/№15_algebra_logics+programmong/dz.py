
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
""" def funcc(x, y, A):
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
print(cnt) """

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
        
#adjustments for new 8t nums

#1
""" Q = list(range(20, 41))
P = list(range(10, 26))
A = []
for x in range(-100, 100):
    if (((x in P) and (not(x in Q))) <= (x in A)) == False:
        A.append(x)
print(A) """

#2
""" Q = list(range(25, 41))
P = list(range(8, 17))
A = []
for x in range(-100, 100):
    if (((x in P) or (x in Q)) <= (x in A)) == False:
        A.append(x)
print(A) """

#3
""" P = list(range(7, 16))
Q = list(range(20, 39))
A = list(range(1, 1000))
for x in range(1,1000):
    if (((x not in P) <= (x in Q)) or (x not in A)) == False:
        A.remove(x)
print(A) """

#4
""" Q = list(range(15, 41))
P = list(range(5, 26))
A = []
for x in range(1, 100):
    if (((x in P) and (x not in Q)) <= (x in A)) == False:
        A.append(x)
print(A) """

#5
""" Q = list(range(8, 32))
P = list(range(12, 24))
A = []
for x in range(1, 100):
    if (((x in P) and (x in Q)) <= (x in A)) == False:
        A.append(x)
print(A) """

#6
""" Q = list(range(8, 32))
P = list(range(12, 24))
A = []
for x in range(1, 100):
    if (((x in P) and (x in Q)) <= (x in A)) == False:
        A.append(x)
print(A) """


a = []
for n in range(1, 1000):
    h = n
    f = n%5
    f3 = ''
    h3 = ''
    while h >0:
        h3 = h3+str(h%3)
        h=h//3
    if len(h3)%2!=0:
        h3='1'+h3
    summa = sum(list(map(int,h3)))
    if summa%2==0:
        h3 = h3+h3[:2]
    else:
        while f>0:
            f3 = f3 + str(f%3)
            f = f//3
        h3 = h3 + f3
    h3 = list(h3)
    if h3[0]=='2':
        h3.remove(h3[0])
    if h3[-1]==h3[-2]:
        h3.remove(h3[-1])
    r = ''.join(h3)
    r10 = int(r, 3)
    if r10 > 150:
        a.append(r10)
print(min(a))
        
        