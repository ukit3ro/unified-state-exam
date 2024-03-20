#1
""" def fucc(x, y, A):
    return (4 * x + y < A) or (x < y) or (22 <= x)

for A in range(-1000, 1000):
    A_flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if fucc(x, y, A) == False:
                A_flag = False
                break
        if A_flag == False:
            break
    if A_flag == True:
        print(A)
        break """
    
#2
""" def func1(x, y, A):
    return (x**2 + y**2 > 128) or (y < -x + A)

for A in range(-1000, 1000):
    flag = True
    for x in range(1, 1000):
        for y in range(1,1000):
            if func1(x, y, A) == False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A)
        break  """



#5
def d3l(n, m):
    return n % m == 0

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if ((d3l(x, 13) <= (not(d3l(x, 21)))) or (x + A >= 500)) == False:
            flag = False
            break
    if flag == True:
        print(A)
        break
        
#6
""" def d3l(n, m):
    return n % m == 0

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if ((d3l(x, 20) <= (not(d3l(x, 11)))) or (x + A >= 300)) == False:
            flag = False
            break
    if flag == True:
        print(A)
        break  """  
        
#7
""" def trg(n, m, k):
    a = sorted([n, m, k])
    return (a[0] + a[1]) > a[2]

for A in range(1000):
    for x in range(1000):
        if (not((trg(x, 11, 18) == (not(max(x, 5) > 15))) and trg(x, A, 5))) == False: 
            break
    else:
        print(A) """


#8
""" def trg(n, m, k):
    a = sorted([n, m, k])
    return (a[0] + a[1]) > a[2]

for A in range(100):
    for x in range(100):
        if (not((trg(x, 12, 20) == (not(max(x, 5) > 28))) and trg(x, A, 3))) == False:
            break
    else:
        print(A) """
        
        
        
        
#9 another prototype
""" B = list(range(10, 16))
C = list(range(20, 28))
A = []
for x in range(1000):
    if (not(((x in B) or (x in C)) <= (x in A))) == True:
        A.append(x)
print(A)
 """
#10
""" B = list(range(30, 42))
C = list(range(50, 57))
A = []
for x in range(1000):
    if (not(((x in B) or (x in C)) <= (x in A))) == True:
        A.append(x)
print(A) """


#11
""" B = list(range(14, 21))
C = list(range(15, 28))
A = list(range(100))
for x in range(100):
    if (not(x in A) <= ((x in B) == (x in C))) == False:
        A.remove(x)
print(A) """

#12
""" B = list(range(4, 19))
C = list(range(12, 41))
A = list(range(100))
for x in range(100):
    if (not(x in A) <= ((x in B) == (x in C))) == False:
        A.remove(x)
print(A) """



#13
""" maxi = []
def d3l(n, m):
    return n % m == 0
for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if ((not(d3l(x, A))) <= (d3l(x, 18) <= (not(d3l(x, 81))))) == False:
            flag = False
            break
    if flag == True:
        maxi.append(A)
print(max(maxi)) """




#17
""" def fucc(x, y, A):
    return (x >= A) or (y >= A) or (x * y <= 200)
for A in range(0, 1000):
    A_flag = True
    for x in range(1000):
        for y in range(1000):
            if fucc(x, y, A) == False:
                A_flag = False
                break
        if A_flag == False:
            break
    if A_flag == True:
        print(A) """
        
        
        
#null1
""" Q = [26, 55]
P = [19, 75]
A = list(range(100))
for x in range(100):
     if (((x in Q) <= (x in P)) or (x in A)) == False:
         A.remove(x)
print(A)"""

