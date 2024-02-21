#2
""" print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x or (y <= z) or ((not y) <= ((not z) == w)))
                print(x, y, z, w, int(F)) """
                
#5
""" for n in range(1, 1000):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 += '0'
    else:
        n2 += '1'
        
    if n2.count('1') % 3 == 0:
        n2 = '11' + n2[2:]

    else:
        n2 = '10' + n2[2:]

    R = int(n2, 2)
    if R >= 26:
        print(n)
        break """

#6      
""" from turtle import *
speed(0)
penup()
left(90)
k = 10

right(90)
right(30)
pendown()
for i in range(10):
    forward(25*k)
    right(90)

done() """

#8
""" from itertools import product
count = 0
for num in product('01234567', repeat=5):
    s = ''.join(num)
    if s[0] != '0':
        if s.count('4') == 2:
            if all(pair not in s for pair in '14 41 34 43 54 45 74 47'.split()):
                count += 1
print(count) """

#9
f = open('5.txt')
cnt = 0
for s in f:
    a = list(map(int, s.split()))
    if ((max(a) * 2 < (sum(a) - max(a))) and ((a[0] + a[1] == a[2] + a[3]) or\
        (a[0] + a[3] == a[1] + a[2]) or (a[0] + a[2] == a[1] + a[3]))):
        cnt += 1
print(cnt)

#12
""" s = '22' + '1' * 2023 + '22'
while '211' in s or '112' in s:
    s = s.replace('11', '1', 1)
    if '21' in s:
        s = s.replace('21', '12', 1)
    else:
        s = s.replace('12', '1', 1)
print(s) """

#14
""" s = 4* 25**2022 - 2 * 5**2000 + 125**1011 - 3 * 5**100 - 660
cnt2 = 0
while s > 0:
    if s % 5 == 4:
        cnt2 += 1
    s = s // 5
print(cnt2) """

#15
""" def aoa(n, m):
    return n % m == 0

for A in range(1, 1000):
    A_right = True
    for x in range(1, 1000):
        if ((aoa(x, 13) <= (not aoa(x, 21))) or (x + A >= 500)) == False:
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
    if n % 2 == 0 and n > 2:
        return 2 * (n - 1) + F(n - 1) + 2
    
    if n % 2 != 0 and n > 2:
        return 2 * (n + 1) + F(n - 2) - 5
print(F(32)) """

#17
""" f = open('17var05.txt')
a = [int(s) for s in f]

summi = []
maxi = max(a)
for i in range(len(a) - 1):
    if (a[i] + a[i+1]) == maxi:
        summi.append(a[i]**2 + a[i+1]**2)
print(len(summi), max(summi)) """

#23
""" def t11(s, e):
    if s < e:
        return 0
    if s == e:
        return 1
    if s > e:
        return t11(s-1, e) + t11(s//2, e)
print(t11(50,20)*t11(20,1)) """

#25
""" from fnmatch import fnmatch
for x in range(11223, 10**8):
    if fnmatch(str(x), r'11*223'):
        if x % 149 == 0:
            print(x, x // 149) """
            
            