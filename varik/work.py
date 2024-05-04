#https://education.yandex.ru/ege/variants/d92fe816-e46a-4796-be3b-f730d3f6ee62/task/1

#2
""" print('a b c d')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if ((a <= b) and (b <= c) and (c <= d)) == True:
                    print(a, b, c, d) """
                
#5
""" def f(n, osn):
    s = ''
    while n > 0:
        s += str(n % osn)
        n //= osn
    s = s[::-1]
    return s
for n in range(1, 200):
    n2 = f(n, 5)
    if n % 25 == 0:
        n2 = n2[-5:] + n2     
    if n % 25 != 0:
        n2 = n2 + f((n % 25), 5)
    R = int(n2, 5)
    if R > 10000:
        print(n)
        break """
    
    
#6
""" from turtle import *
tracer(0)
k = 20
left(90)
pendown()

right(60)
forward(4*k)
right(120)

from math import sqrt
for _ in range(4):
    forward(3*k)
    right(240)
    forward(3*k)
    right(120)
forward(4*k)
right(90)
forward((8 * sqrt(3))*k)
right(90)
forward(8*k)

penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*k, y*k)
        dot(4)
done() """
    

#8
""" numb = 1
from itertools import product
for i in sorted(product('АЕКПТЧ', repeat = 7)):
    s = ''.join(i)
    if s == 'ПЕЧАТКА':
        print(i, numb)
        break
    numb += 1 """

#9
""" cnt = 0
for s in open('9.txt'):
    a = list(map(int, s.split()))
    if (a[0] == a[1] and a[2] == a[3]) or (a[0] == a[2] and a[1] == a[3]) or\
        (a[0] == a[3] and a[1] == a[2]):
        cnt += 1
print(cnt) """

#12
""" for n in range(3, 10001):
    s = '5' + '2' * n
    while '52' in s or '2222' in s or '1112' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
            s = s.replace('2222', '5', 1)
        else:
            s = s.replace('1112', '2', 1)
    if sum(map(int, s)) == 1685:
        print(n) """

#13
""" from ipaddress import *
ip_add = ip_address('20.24.110.42')
for mask in range(33):
    try:
        ip_net = ip_network(f'20.24.96.0/{mask}')
        
        if ip_add in ip_net:
            print(bin(int(ip_net.netmask)).count('1'))
    except:
        continue """
        

#14
""" s = 18 * 7**108 - 5 * 49**76 + 343**35 - 50
while s != 0:
    s = int(s)
    s //= 49

print(sum(map(int, str(s * -1)))) """

#15
""" def fucc(x, y, A):
    return (3 * x + y > A) and  (y < x) and (x < 30)

for A in range(1, 1000):
    A_flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if fucc(x, y, A) == True:
                A_flag = False
                break
        if A_flag == False:
            break
    if A_flag == True:
        print(A)
        break """
    
#16
""" import sys
sys.setrecursionlimit(100000)
def F(n):
    if n > 10000:
        return 42
    if n % 2 == 0 and n <= 10000:
        return 2 * n + F(n + 3) + F(n + 4) + F(n + 6)
    if n % 2 != 0 and n <= 10000:
        return -(n + F(n + 1) + F(n + 3))
print(F(9996) - F(9994)) """

#17
""" f = open('17.txt')
a = [int(s) for s in f]
summi = []
    
for i in range(len(a) - 4):
    if (a[i] + a[i+1] < (a[i+2] + a[i+3]) > a[i+4] + a[i+5] and\
        (a[i] + a[i+1] > 0) and (a[i+2] + a[i+3] > 0) \
            and (a[i+4] + a[i+5] > 0)):
        summi.append(a[i+2] * a[i+3])
print(len(summi), min(summi)) """

#19-21
""" def f(a, b, m):
    if a + b >= 231:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a+4,b,m-4), f(a,b+4,m-4), f(a*3, b, m-4), f(a, b*3, m-4)]
    return any(h) if (m - 1) % 2 == 0 else any(h)
print(19, [s for s in range(1, 218) if f(10, s, 4)]) """
""" def f(a, b, m):
    if a + b >= 123:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a+1,b,m-1), f(a,b+1,m-1), f(a*2, b, m-1), f(a, b*2, m-1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)
print(20, [s for s in range(1, 110) if not f(13, s, 1) and f(13, s, 3)]) """
""" def f(a, b, m):
    if a + b >= 123:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a+1,b,m-1), f(a,b+1,m-1), f(a*2, b, m-1), f(a, b*2, m-1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)
print(20, [s for s in range(1, 110) if not f(13, s, 2) and f(13, s, 4)]) """


#23
""" import sys
sys.setrecursionlimit(1000)
def t(s, e):
    if s > e or s == 81:
        return 0
    if s == e:
        return 1
    if s < e:
        return t(s + int(s[0]), e) + t(s + 3, e) + t(2 * s - 1, e)
print(t(42, 73)*t(73, 89)) """

#24
""" s = open('24.txt').readline()
s = s.replace('B', 'A').replace('C', 'A').replace('7', '6').replace('8', '6')\
    .replace('9', '6')
while 'AA' in s:
    s = s.replace('AA', 'A A')
while '66' in s:
    s = s.replace('66', '6 6')
print(max(len(c) for c in s.split()))
     """
#25
from fnmatch import fnmatch
for x in range(0, 2*10**10, 42):
    if fnmatch(str(x), '?2*4*0'):
        if fnmatch(str(x), '1*7*') == False:
            print(x, x // 42)


