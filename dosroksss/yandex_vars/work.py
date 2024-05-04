#2
""" print('x y w z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x and (not z)) or (y == z) or (not w)) == False:
                    print(x, y, z, w) """
                
#5
""" for n in range(1000):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 += '01'
    if n % 2 != 0:
        n2 = '1' + n2 + '1'
    R = int(n2, 2)
    if R > 156:
        print(n)
        break """
    
    
#6
from turtle import *
""" tracer(0)
k = 20
left(90)
pendown()

for _ in range(2):
    forward(13*k)
    right(90)
    forward(18*k)
    right(90)
penup()
forward(5*k)
right(90)
forward(9*k)
left(90)
pendown()
for _ in range(2):
    forward(11*k)
    right(90)
    forward(7*k)
    right(90)

penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*k, y*k)
        dot(4)
done() """
    

#8
""" numb = 1
from itertools import product
for i in sorted(product('ПАРУС', repeat = 5)):
    s = ''.join(i)
    if (s.count('У') <= 1 and 'АА' not in s):
        print(i, numb)
        break
    numb += 1 """

#9
""" cnt = 0
for s in open('9.txt'):
    a = list(map(int, s.split()))
    if (max(a) < (sum(a) - max(a)) and (a[0] + a[1] == a[2]  +a[3] or\
        a[0] + a[3] == a[1]  +a[2] or a[0] + a[2] == a[1]  +a[3])):
        cnt += 1
print(cnt) """

#12
""" s = '8' * 45
while '1111' in s or '8888' in s:
    if '1111' in s:
        s = s.replace('1111', '88', 1)
    else:
        s = s.replace('8888', '11', 1)
print(s) """

#13
""" from ipaddress import *
cnt = 0
ip_net = ip_network('105.224.200.224/255.255.255.224', False)
for ip_add in ip_net:
    if bin(int(ip_add)).count('1') % 4 == 0:
        cnt += 1
print(cnt) """
        

#14
""" for x in '0123456789ABCDEFGHIJKLMNOPQ':
    if (int('123' + x + '24', 27) + int('135' + x + '78', 27)) % 26 == 0:
        print((int('123' + x + '24', 27) + int('135' + x + '78', 27)) // 26) """

#15
""" B = list(range(24, 91))
C = list(range(47, 116))
A = list(range(100))
for x in range(100):
    if ((x in C) <= ((not(x in A)) and (x in B)) <= (not(x in C))) == False:
        A.remove(x)
print(A) """
#16
""" import sys
sys.setrecursionlimit(3000)
def F(n):
    if n <= 7:
        return 1
    if n > 7:
        return n + 2 + F(n - 1)
print(F(2024) - F(2020)) """

#17
""" f = open('17.txt')
a = [int(s) for s in f]
summi = []
krat = max([i for i in a if i % 19 == 0])
    
for i in range(len(a) - 1):
    if a[i] > krat or a[i+1] > krat:
        summi.append(a[i] + a[i+1])
print(len(summi), max(summi)) """

#19-21
""" def f(a, b, m):
    if a + b >= 123:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a+1,b,m-1), f(a,b+1,m-1), f(a*2, b, m-1), f(a, b*2, m-1)]
    return any(h) if (m - 1) % 2 == 0 else any(h)
print(19, [s for s in range(1, 110) if f(13, s, 2)]) """
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
""" def t(s, e):
    if s > e:
        return 0
    if s == e:
        return 1
    if s < e:
        return t(s + 1, e) + t(s * 2, e)
print(t(4, 8)*t(8, 10)*t(10,15)) """

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
""" from fnmatch import fnmatch
for x in range(0, 10**10, 2024):
    if fnmatch(str(x), '1*2322?2'):
        print(x, x // 2024) """


