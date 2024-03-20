#2
""" print('x y w z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((x <= y) <= z) or (w <= (y and z))) == False:
                    print(x, y, z, w) """
                
#5
""" for i in range(100, 1000):
    s = str(i)
    a1 = int(s[0]) + int(s[1]) + int(s[2])
    a2 = int(s[0]) * int(s[1]) * int(s[2])
    if a1 > a2:
        f = str(a1) + str(a2)
    if a2 > a1:
        f = str(a2) + str(a1)
    
    if f == '33621':
        print(i) """
#6
""" from turtle import """

#8
""" numb = 1
from itertools import product
for i in sorted(product('МАСЛО', repeat = 5)):
    if i.count('А') <= 1 and i.count('Л') == 0 and i.count('М') == 2:
        print(i, numb)
        break
    numb += 1 """
#9
#autorun
#12
""" s = '1' * 50
while '11111' in s or '15' in s:
    if '11111' in s:
        s = s.replace('11111', '15', 1)
    else:
        s = s.replace('15', '1', 1)
print(s) """
#14
""" s = 2 * 3**2022 + 5 * 3**1800 + 3**1001 + 4 * 3**1000 + 3
cnt = 0
while s > 0:
    if s % 9 == 0:
        cnt += 1
    s = s // 9
print(cnt) """

#15
""" B = list(range(14, 21))
C = list(range(15, 28))
A = list(range(100))
for x in range(100):
    if (not(x in A) <= ((x in B) == (x in C))) == False:
        A.remove(x)
print(A) """
#16
""" def F(n):
    if n <= 1:
        return 1
    if n > 1 and n % 2 != 0:
        return 3 + F(n - 1) * F(n - 2)  - F(n - 1) - F(n - 2)
    if n > 1 and n % 2 == 0:
        return 2 * F(n - 1)
print(F(12))    """
    
#17
""" f = open('17var11.txt')
a = [int(s) for s in f]
summi = []
    
for i in range(len(a) - 1):
    if (a[i] % 3 == 0 and a[i+1] % 3 == 0):
        summi.append(a[i] + a[i+1])
print(len(summi), max(summi)) """

#23
""" def t(s, e):
    if s > e:
        return 0
    if s == e:
        return 1
    if s < e:
        return t(s + 2, e) + t(s + 10, e)
print(t(5, 71)) """

#25
""" for i in range(1, 800000, -1):
    if i %  """


