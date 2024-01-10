
#1
""" def aoa(n, m):
    return n % m == 0

for A in range(1, 1000):
    A_right = True
    for x in range(1, 1000):
        if ((aoa(x, A) and (not(aoa(x, 36)))) <= (not(aoa(x, 12)))) == False:
            A_right = False
            break
    if A_right == True:
        print(A)
        break """
    
#2
""" def aoa(n, m):
    return n % m == 0

for A in range(1, 1000):
    A_right = True
    for x in range(1, 1000):
        if (aoa(x, A) <= ((not(aoa(x, 28))) or aoa(x, 42))) == False:
            A_right = False
            break
    if A_right == True:
        print(A)
        break """
        
#3
""" def aoa(n, m):
    return n % m == 0

for A in range(1, 1000):
    A_right = True
    for x in range(1, 1000):
        if (aoa(x, A) <= (aoa(x, 21) or aoa(x, 35))) == False:
            A_right = False
            break
    if A_right == True:
        print(A)
        break """
    
#4
""" def func(x, y, A):
    return ((2 * y + 3 * x < A) or (x > 15) or (y > 35))

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if func(x, y, A) == False:
                flag = False
                break
    if flag == True:
        print(A)
        break """
            
#5
""" def func(x, y, A):
    return ((x >= 13) or (x < 4 * y) or (x * y < A))

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if func(x, y, A) == False:
                flag = False
                break
    if flag == True:
        print(A)
        break """
        
#6
""" P = list(range(17, 54))
Q = list(range(37, 83))
A = []
for x in range(1000):
    if (((x in P) and (x in Q)) <= (x in A)) == False:
        A.append(x)
print(A)  """     
        
#7
""" P = list(range(4, 20))
Q = list(range(10, 55))
A = []
for x in range(1000):
    if ((x in A) or ((not(x in P)) <= (not(x in Q)))) == False:
        A.append(x)
print(len(A)) """

#8
""" P = list(range(10, 49))
Q = list(range(33, 88))
A = list(range(1000))
for x in range(1000):
    if (((x in P) <= (not(x in Q))) <= (not(x in A))) == False:
        A.remove(x)
print(len(A))  """         

#9
""" P = list(range(5, 20))
Q = list(range(18, 32))
A = list(range(1000))
for x in range(1000):
    if (((x in A) <= (x in P)) or (x in Q)) == False:
        A.remove(x)
print(len(A))  """

#10
""" def func(x, y, A):
    return ((y + 3 * x < A) or (2 * y + x > 50) or (4 * y - x < 40))

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if func(x, y, A) == False:
                flag = False
                break
    if flag == True:
        print(A)
        break """

#11
""" def aoa(n, m):
    return n % m == 0

def been(n):
    return bin(n)[-1] == '0'

for A in range(1, 1000):
    A_right = True
    for x in range(1, 1000):
        if (aoa(A, 256) or (not(been(A)) <= (aoa(A, x) and (not(been(x)))))) == False:
            A_right = False
            break
    if A_right == True:
        print(A)
        break """

#13
# P = list(range(27, 130))
# Q = list(range(50, 62))
# R = list(range(38, 94))

# A = []
# for x in range(1000):
#     if (((x not in P) or (x in Q)) or ((not(x in A)) <= (not(x in R)))) == False:
#         A.append(x)
# print(len(A))
#wrong

#additional
P = list(range(4, 32))
Q = list(range(11, 64))
A = []
for x in range(1000):
    if ((x in A) or ((not(x in P)) <= (not(x in Q)))) == False:
        A.append(x)
print(len(A))
        