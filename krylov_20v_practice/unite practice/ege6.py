
#2
""" print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (y and (x <= w) or ((not x) <= ((not w) == z)))
                print(x, y, z, w, int(F)) """
                
#5
""" for n in range(1000, 1, -1):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 += '0'
    else:
        n2 += '1'
        
    if n2.count('1') % 3 == 0:
        n2 = '11' + n2[2:]

    if n2.count('1') % 3 != 0:
        n2 = '10' + n2[2:]

    R = int(n2, 2)
    if R <= 37:
        print(n)
        break """
        
#6
""" from turtle import *
tracer(0)
penup()
left(90)
k = 5
cnt = 0

right(90)

right(45)
pendown()

for i in range(10):
    forward(30*k)
    right(90)

for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*k, y*k)
        dot(4)

done() """

#8
""" from itertools import product
cnt = 0
for n in product('0123', repeat = 5):
    s = ''.join(n)
    if ((s[0] != '0') and (s.count('3') == 1) and ('03' not in s) and ('30' not in s)):
        cnt += 1
print(cnt)  """

#9
""" f = open('9.txt')
cnt = 0
for s in f:
    a = list(map(int, s.split()))
    mini = min(a)
    if ((mini * 5 < (sum(a) - mini)) and ((a[0] * a[1] == a[2] * a[3]) or\
        (a[0] * a[3] == a[2] * a[1]) or (a[0] * a[2] == a[1] * a[3]))):
        cnt += 1
print(cnt) """

#12
""" s = '22' + '1' * 2050 + '22'
while '211' in s or '112' in s:
    s = s.replace('11', '1', 1)
    if '21' in s:
        s = s.replace('21', '12', 1)
    else:
        s = s.replace('12', '1', 1)
print(s) """

#14
""" s = 4**2022 - 6 * 4**522 + 5 * 64**510 - 3 * 2**330 - 100
cnt2 = 0
while s > 0:
    if s % 8 == 7:
        cnt2 += 1
    s = s // 8
print(cnt2) """

#15 
""" def aoa(n, m):
    return n % m == 0

for A in range(1, 1000):
    A_right = True
    for x in range(1, 1000):
        if ((aoa(x, 20) <= (not aoa(x, 11))) or (x + A >= 300)) == False:
            A_right = False
            break
    if A_right == True:
        print(A)
        break
 """
 
#16
""" def F(n):
    if n < 3:
        return n
    if (n > 2 and n % 2 == 0):
        return 3 * (n - 1) + F(n - 1) + 5
    if (n > 2 and n % 2 != 0):
        return 3 * (n + 1) + F(n - 2) - 2

print(F(35)) """

#17
""" f = open('17var06.txt')
a = [int(s) for s in f]
summi = []
f = [x for x in a if x % 2 == 0]
fmax = max(f)

for i in range(len(a) - 1):
    if (a[i] + a[i+1]) == fmax:
        summi.append(a[i]**2 + a[i+1]**2)
print(len(summi), max(summi)) """

#23
""" def t11(s, e):
    if s < e:
        return 0
    if s == e:
        return 1
    if s > e:
        return t11(s - 1, e) + t11(s // 2, e)
print(t11(60, 10)*t11(10,2)) """

#25
from fnmatch import fnmatch
for x in range(32823, 10**8):
    if fnmatch(str(x), r'32*823'):
        if x % 123 == 0:
            print(x, x // 123)