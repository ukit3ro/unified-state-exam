#2
""" print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (not((x == y) or (x == z)) or w or (not(y <= z)))  == False:
                    print(x, y, z, w) """
                
#5
""" for n in range(1000):
    n2 = bin(n)[2:]
    n3 = ''
    for i in n2:
        if i == '0':
            n3 += '00'
        else:
            n3 += '11'
    R = int(n3, 2)
    if R > 32:
        print(R)
        break """
    
    
#6
""" from turtle import *
tracer(0)
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
""" numb = 0
from itertools import product
for i in product('123456', repeat = 5):
    s = ''.join(i)
    if s[0] != '0':
        if s.count('1') == 1:
            numb += 1
print(numb) """

#9
""" f = open('XD1.txt')
cnt = 0
for s in f:
    a = list(map(int, s.split()))
    if ((max(a) + min(a)) < (2 * (sum(a) - max(a) - min(a)))):
        cnt += 1   
print(cnt) """

#12
""" s = '1' + '2' * 70
while '12' in s or '1' in s:
    if '12' in s:
        s = s.replace('12', '221', 1)
    else:
        if '1' in s:
            s = s.replace('1', '2', 1)
print(s.count('2')) """

#13     
""" from ipaddress import *
ip_add = ip_address('42.118.219.133')
for mask in range(33):
    try:
        ip_net = ip_network(f'42.118.216.0/{mask}')
        
        if ip_add in ip_net:
            print(bin(int(ip_net.netmask))[2:].count('1'))
    except:
        continue """
#14
""" for x in '0123456789ABCDEFGHIJK':
    for y in '0123456789ABCDEFGHIJK':
        if (int('12' + '5' + x + '9', 21) + int('36' + '5' + '99', 21)) % 18 == 0:
            print((int('12' + '5' + x + '9', 21) + int('36' + '5' + '99', 21)) // 18) """

#15
""" def F(x, y, A):
    return (x < A) and (y < A) and (x * y > 601)
for A in range(2000):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if F(x, y, A) == True:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A) """
            
#16
""" import sys
sys.setrecursionlimit(3000)
def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2 and n % 2 == 0:    
        return 2 + F(n - 1)
    if n > 2 and n % 2 != 0:    
        return 3 * n + F(n - 2)
print(F(43)) """

#17
""" f = open('17var19.txt')
a = [int(s) for s in f]
summi = []
for i in range(len(a) - 1):
    if ((a[i] > 700) + (a[i+1] > 700)) >= 1:
        summi.append(a[i]**2 + a[i+1]**2)
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
        return t(s + 3, e) + t(s + 4, e) + t(s * 3, e) 
print(t(1, 7)*t(7, 30)) """

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


