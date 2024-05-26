#2
""" print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((x == (not y)) or (x == (not z))) and w and (y <= z))  == True:
                    print(x, y, z, w) """
                
#5
from math import sqrt
""" for n in range(1000):
    n -= (n % 8)
    n += (n % 2)
    n2 = bin(n)[2:]
    n3 = sum(map(int, n2))
    n2 += str(n3 % 2)
    n3 = sum(map(int, n2))
    n2 += str((n3) % 2)
    R = int(n2, 2)
    if R > 90:
        print(R)
        break """
    
    
#6
""" from turtle import *
tracer(0)
k = 15
left(90)
pendown()

right(60*k)
for _ in range(4):
    forward(8*k)
    right(120)
    forward(4*k)
    right(240)
right(120)
forward(2*k)
right(90)
forward(16*sqrt(3)*k)
right(90)
forward(2*k)

penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*k, y*k)
        dot(4)
done() """
    

#8
cnt = 0
from itertools import product
for i in sorted(product('01234567', repeat = 4)):
    s = ''.join(i)
    s = list(s)
    if s[0] != '0':
        subcnt = 0
        for j in range(len(s) - 1):
            if s[j] == s[j + 1]:
                subcnt += 1
        if subcnt == 1:
            cnt += 1
        
print(cnt)


#12
""" s = '1' + '5' * 25
while '15' in s or '1' in s:
    if '15' in s:
        s = s.replace('15', '5551', 1)
    else:
        if '1' in s:
            s = s.replace('1', '5', 1)
print(s.count('5')) """

#13     
""" from ipaddress import *
ip_add = ip_address('244.55.138.100')
for mask in range(33):
    try:
        ip_net = ip_network(f'244.55.138.96/{mask}')
        
        if ip_add in ip_net:
            print(ip_net.netmask)
    except:
        continue """
#14
""" for x in '0123456789ABCDE':  
    if (int('135' + x + '7', 15) + int('7' + x + '531', 15)) % 14 == 0:
        print((int('135' + x + '7', 15) + int('7' + x + '531', 15)) // 14) """

#15
""" def F(x, y, A):
    return (x >= A) or (y >= A) or (x * y <= 200)
for A in range(2000):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if F(x, y, A) == False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A) """
            
#16
""" def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n - 1)
print(F(446) / F(443)) """

#17
""" f = open('17var17.txt')
a = [int(s) for s in f]
summi = []
    
for i in range(len(a) - 1):
    if (a[i] + a[i+1] >= 100):
        if ((a[i] < 0) + (a[i+1] < 0)) >= 1:
            summi.append(a[i] * a[i+1])
print(len(summi), max(summi))
 """
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
        return t(s + 5, e) + t(s + 4, e) + t(s * 3, e) 
print(t(2, 6)*t(6, 30)) """

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


