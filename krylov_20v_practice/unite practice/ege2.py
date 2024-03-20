
#2
""" print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((not(y <= x)) or (y == w) or z) == 0:
                    print(x, y, z, w)
                     """
#5
""" def convert(num, base):
    digits = '0123'
    if num < base:
        return digits[num]
    else:
        return convert( num // base, base) + digits[num % base]
for n in range(1, 1000):
    n2 = convert(n, 4)
    if n % 4 == 0:
        n2 += n2[-2] + n2[-1]
    else:
        n2 += convert(((n % 4) * 2), 4)
    
    R = int(n2, 4)
    if R < 369:
        print(n) """
        
#6
""" from turtle import *
tracer(0)
left(90)
pendown()
k = 15

for i in range(2):
    forward(15*k)
    left(90)
    forward(20*k)
    left(90)
penup()
right(90)
backward(7*k)
left(90)
forward(9*k)

pendown()
for i in range(2):
    forward(17*k)
    right(90)
    forward(15*k)
    right(90)

penup()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x*k, y*k)
        dot(4)
done() """

#8
""" from itertools import product
numb = 1
cnt = 0
for i in sorted(product('РЕПЛИКА', repeat = 6)):
    s = ''.join(i)
    if numb % 2 == 0 and s[0] != 'К' and s.count('И') >= 2:
        cnt += 1
    numb += 1
print(cnt) """

#9
""" f = open('2.txt')
cnt = 0
for s in f:
    a = list(map(int, s.split()))
    a1 = min(a)
    if len(set(a)) == 5:
        
     """
#12
""" for n in range(3, 10001):
    s = '1' + '2' * 67
    while '12' in s or '5522' in s or '2222' in s:
        if '12' in s:
            s = s.replace('12', '55', 1)
        if '2222' in s:
            s = s.replace('2222', '1', 1)
        if '5522' in s:
            s = s.replace('5522', '21', 1)
    
    if (s.count('2'*2) + s.count('1') + s.count('5'*5)) == 142:
        print(n)
        break """
        
#14
""" for x in '0123456789ABCDEFGHIJKLM':
    if (int('2' + x + x + '341011', 23) + int('220' + x + '4', 23) + int('110' + x + '6', 23)) % 22 == 0:
        print((int('2' + x + x + '341011', 23) + int('220' + x + '4', 23) + int('110' + x + '6', 23)) // 22) """
        
#15
""" def fucc(x, y, A):
    return (x**2 + y**2 > 128) or (y < -x + A)
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
        
#16
import sys
sys.setrecursionlimit(3000)

def F(n):
    if n == 1:
        return 3
    if n > 1:
        return 3 * n + 2 * F(n - 1)
print(F(2024) - 4 * F(2022))

#17
""" f = open('17var02.txt')
a = [int(s) for s in f]
summi = []

for i in range(len(a) - 2):
    if ((a[i] + a[i+1] + a[i+2]) < 7100) and ((100 <=a[i] <= 999 and 100 <= a[i+1] <= 999 and (999<=a[i+2] or a[i+2] <= 100))\
        or (100 <=a[i+1] <= 999 and 100 <= a[i+2] <= 999 and (999<=a[i] or a[i] <= 100)) or\
            (100 <=a[i] <= 999 and 100 <= a[i+2] <= 999 and (999<=a[i+1] or a[i+1] <= 100))):
        summi.append(a[i] + a[i+1] + a[i+2])
print(len(summi), max(summi)) """

#19
""" def WIN1(s):
    return (s + 1) >= 223 or (s * 3) >= 223
def LOSS1(s):
    return (not(WIN1(s))) and WIN1(s + 1) and WIN1(s * 3)

def WIN2(s):
    return LOSS1(s+1) or LOSS1(s * 3)
for s in range(1, 223):
    if WIN2(s):
        print(s) """
        
#23
""" def t11(s, e):
    if s > e or s == 18:
        return 0
    if s == e:
        return 1
    if s < e:
        return t11(s + 1, e) + t11(s + 4, e) + t11(s * 2, e)
print(t11(4,11)*t11(11, 28)) """


#25
""" from fnmatch import fnmatch
for x in range(9000101, 10**10):
    if fnmatch(str(x), r'9*?001?1'):
        if x % 12007 == 0:
            print(x, x// 12007) """