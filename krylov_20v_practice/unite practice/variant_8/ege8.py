
#2
""" print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if ((not(w <= (not(x <= y)))) and ((not x ) <= ((not y) == z))) """
                
                
#5
""" import math
for n in range(100):
    n2 = bin(n)[2:]
    
    if n2.count('1') % 2 == 0:
        midpos = math.ceil(len(n2) / 2)
        n3 = n2[:midpos] + '1' + n2[midpos:]
    
    else:
        n3 = n2
    
    R = int(n2, 2)
    if R <= 26:
        print(n) """
        
#8
""" n = 0
from itertools import product
for i in sorted(product('ПОЛЬЗА', repeat=6)):
    n += 1
    s = ''.join(i)
    if s.count('Ь') <= 1 and s.count('А') == 1 and s.count('З') <=2:
        print(n)
        break """
        
#9
""" cnt = 0
for s in open('9_8.txt'):
    a = list(map(int, s.split()))
    loc= 0
    if min(a)**2 > sum(a) - min(a):
        for j in a:
            if j % 2 == 0:
                loc += 1
        if loc == 0:
            cnt += 1
print(cnt) """

#12
""" s = '22' + '1' * 2023
while '2111' in s or '1112' in s:
    s = s.replace('111', '1')
    if '21' in s:
        s = s.replace('21', '12', 1)
    else:
        s = s.replace('12', '1', 1)
print(s) """

#14
""" s = 1331**650 - 55 * 121**610 + 77 * 11**510 - 3 * 11**100 - 221
cnt = 0
while s > 0:
    if s % 11 == 0:
        cnt += 1
        s = s // 11
print(cnt) """

#15
""" def trg(n, m, k):
    a = sorted([n, m, k])
    return (a[0] + a[1]) > a[2]

for A in range(1000):
    for x in range(1000):
        if (not((trg(x, 12, 20) == (not(max(x, 5) > 28))) and trg(x, A, 3))) == False:
            break
    else:
        print(A) """

#16
""" a = [1] * 40
for i in range(3, 40):
    if i % 2 != 0:
        a[i] = a[i-1] - a[i-2]
    else:
        a[i] = sum(a[1:i])
print(a[39]) """

#17
""" f = open('17var08.txt')
a = [int(s) for s in f]
summi = []
maxo = max(a)

for i in range(len(a) - 2):
    if ((str(a[i])[-1] != '3' and str(a[i+1])[-1] != '3' and\
        str(a[i+2])[-1] != '3') and ((a[i]**2 + a[i+1]**2 +\
            a[i+2]**2) > maxo)):
        summi.append(a[i]**2 + a[i+1]**2 + a[i+2]**2)
print(len(summi), min(summi)) """

#23
""" def t(s, e):
    if s < e or s == 4:
        return 0
    if s == e:
        return 1
    if s > e:
        return t(s - 1, e) + t(s // 2, e)
print(t(60, 20)*t(20,1)) """

#25
""" from fnmatch import fnmatch
for x in range(332107, 10**9):
    if fnmatch(str(x), r'33*21?7'):
        if x % 2079 == 0:
            print(x, x // 2079) """