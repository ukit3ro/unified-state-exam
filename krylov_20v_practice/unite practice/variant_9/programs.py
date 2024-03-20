#2 wyxz
""" print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if ((not((x <= y) <= w)) and z) == True:
                    print(x, y, w, z) """
#5
""" for n in range(100, 1000):
    n2 = str(n)
    newie = str(int(n2[0])**2 + int(n2[1])**2) +\
        str(int(n2[1])**2 + int(n2[2])**2)
    if newie == '9752':
        print(n) """
#6
""" from math import tan, radians
tg30 = tan(radians(30))
tg150 = tan(radians(150))
cnt = 0
for x in range(0, 120):
    for y in range(0, 120):
        if x > 0 and y > tg30 * x and y < tg150 * x + 111:
            cnt += 1
print(cnt) """

#8
""" from itertools import product
numb = 0
for n in product('АТОМ', repeat = 4):
    numb += 1
    s = ''.join(n)
    if s[0] == 'О':
        print(numb)
        break """
    
#9
""" f = open('9.txt')
nuzh = []
nuzh2 = [] 
for s in f:
    s = s.replace(',', '.')
    a = list(map(float, s.split()))            
    for i in a:
        if i >= 2.0 and i <= 17.0:
            nuzh.append(i)
    for n in a:
        if n > 12.0 and n <= 17:
            nuzh2.append(n)
print((len(nuzh2) / len(nuzh))*100) """

#12
""" s = '1' * 2022
while '11111' in s or '555' in s:
    if '11111' in s:
        s = s.replace('11111', '555', 1)
    else:
        s = s.replace('555', '5', 1)
print(s) """

#13


#14
""" s = 5**2022 - 2 * 5**1010 + 25**850 + 2500
cnt = 0
while s > 0:
    if s % 5 == 4:
        cnt += 1
    s = s // 5
print(cnt) """

#15
""" B = list(range(10, 16))
C = list(range(20, 28))
A = []
for x in range(100):
    if (not(((x in B) or (x in C)) <= (x in A))) == True:
        A.append(x)
print(A) """

#16
""" def F(n):
    if n <= 1:
        return 1
    if n % 2 != 0 and n > 1:
        return 5 * n + F(n-1) + F(2)
    if n % 2 == 0 and n > 1:
        return 3 * F(n-1)
print(F(23)) """

#17
""" summs = []
squares = []
nums = list(range(1,600))
for j in nums:
    squares.append(j**2)

f = open('17var09.txt')    
a = [int(s) for s in f]
for i in range(len(a) - 1):
    if a[i] in squares or a[i + 1] in squares:
        summs.append(a[i] + a[i+1])
print(len(summs), max(summs)) """
    
#19
""" def WIN1(s):
    return (s + 1) >= 180 or (s * 2) >= 180

def LOSS1(s):
    return (not(WIN1(s))) and WIN1(s + 1) and WIN1(s * 2)

def WIN2(s):
    return LOSS1(s+1) or LOSS1(s * 2)

for s in range(1, 179):
    if WIN2(s):
        print(s)
 """
#20

#21

#23
""" def t(s, e):
    if s > e:
        return 0
    if s == e:
        return 1
    if s < e:
        return t(s + 2, e) + t(s +7, e)
print(t(5, 49)) """

#25

