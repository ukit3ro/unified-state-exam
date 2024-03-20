
#2
""" print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((z <= y) <= x) or (not w)) == 0:
                    print(x, y, z, w) """
                    
#5
""" for i in range(100, 1000):
    s = str(i)
    a1 = int(s[0])**2 + int(s[1])**2
    a2 = int(s[1])**2 + int(s[2])**2
    if a1 > a2:
        f = str(a1) + str(a2)
    if a2 > a1:
        f = str(a2) + str(a1)
    
    if f == '7434':
        print(i) """
        
#6
""" from turtle import *
tracer(0)
left(90)
pendown()
k = 30

for o in range(10):
    forward(7*k)
    right(120)

penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*k, y*k)
        dot(4)

done() """

#8
""" numb = 1
from itertools import product
for i in sorted(product('ПРАВО', repeat = 4)):
    if i[0] == 'П':
        print(numb)
        break
    numb += 1 """

#9


#12
""" s = '1' * 2022
while '11' in s or '555' in s:
    if '11' in s:
        s = s.replace('11', '555', 1)
    else:
        s = s.replace('555', '5', 1)
print(s) """

#14
""" s = 4**2022 - 2 * 4**1111 + 16**600 + 192
cnt = 0
while s > 0:
    if s % 4 == 3:
        cnt += 1
    s = s // 4
print(cnt)   """

#15
""" B = list(range(30, 42))
C = list(range(50, 57))
A = []
for x in range(1000):
    if (not(((x in B) or (x in C)) <= (x in A))) == False:
        A.append(x)
print(A) """

#16
""" import sys
sys.setrecursionlimit(10000)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n**2 + F(n - 1)
print(F(2023) - F(2019)) """

#17
""" f = open('17var10.txt')
a = [int(s) for s in f]
summi = []
kvadr = []
for s in range(-100, 100):
    kvadr.append(s**2)
    
for i in range(len(a) - 1):
    if (a[i] in kvadr or a[i+1] in kvadr):
        summi.append(a[i] + a[i+1])
print(len(summi), min(summi)) """

#20
""" def WIN1(s):
    return (s + 1) >= 177 or (s * 2) >= 177

def LOSS1(s):
    return (not(WIN1(s))) and WIN1(s + 1) and WIN1(s * 2)

def WIN2(s):
    return LOSS1(s + 1) or LOSS1(s * 2)

for s in range(1, 178):
    if WIN2(s):
        print(s) """
        
#21
""" def WIN1(s):
    return (s + 1) >= 177 or (s * 2) >= 177

def LOSS1(s):
    return (not(WIN1(s))) and WIN1(s + 1) and WIN1(s * 2)

def WIN2(s):
    return LOSS1(s+1) or LOSS1(s * 2)

def LOSS12(s):
    return (WIN2(s+1) and WIN1(2*s))

for s in range(1, 177):
    if LOSS12(s):
        print(s) """
        
#23
""" def t11(s, e):
    if s > e:
        return 0
    if s == e:
        return 1
    if s < e:
        return t11(s+2, e) + t11(s + 7, e)
print(t11(7,51)) """

#25
""" print(4**1/2) """

#111
""" def t(s, e, k5=0, k3=0, k45=0):
    if s > e or k5 > 4 or k45 > 5: 
        return 0
    elif s == e and k5 <= 4 and k3 >= 2 and k45 == 5: 
        return 1
    else:
        return t(s * 5, e, k5 + 1, k3, k45) + t(s * 3, e, k5, k3 + 1, k45) + t(s + 45, e, k5, k3, k45 + 1)
print(t(1, 2970)) """

""" print(round(0.5)) """