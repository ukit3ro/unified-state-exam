#2
""" print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (not((x == y) or (x == w)) or z or (not(y <= w)))  == False:
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
    if R > 63:
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
for i in sorted(product('ЕКОР', repeat = 6)):
    s = ''.join(i)
    numb += 1
    if s[0] == 'О' and 'ЕЕ' not in s:
        print(numb, s)
        break """

#9
""" f = open('XD1.txt')
cnt = 0
for s in f:
    a = list(map(int, s.split()))
    if ((max(a) + min(a)) < (2 * (sum(a) - max(a) - min(a)))):
        cnt += 1   
print(cnt) """

#12
""" for n in range(1, 1000):
    s = '>' + '1' * 23 + '2' * n + '3' * 25
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '1>', 1)
        if '>2' in s:
            s = s.replace('>2', '>3', 1)
        if '>3' in s:
            s = s.replace('>3', '>11', 1)
    s1 = str(s).replace('>', '')
    print(s1)
    n2 = sum(map(int, s1))
    k = 0
    for i in range(1, n2 + 1):
        if n2 % i == 0:
            k += 1
            if k > 2:
                break
    if k == 2:
        print(n)
        break """

#13     
""" from ipaddress import *
ip_add = ip_address('99.188.115.211')
for mask in range(33):
    try:
        ip_net = ip_network(f'99.188.115.192/{mask}')
        
        if ip_add in ip_net:
            print(bin(int(ip_net.netmask))[2:].count('1'))
    except:
        continue """
#14
""" for x in '0123456789ABC':
    if (int('186' + x + '4', 13) + int('5' + x + '716', 13)) % 11 == 0:
        print((int('186' + x + '4', 13) + int('5' + x + '716', 13)) // 11) """

#15
""" def F(x, y, A):
    return (x < A) and (y < A) and (x * y > 1200)
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
        return 3 + F(n - 1)
    if n > 2 and n % 2 != 0:    
        return 2 * n + F(n - 2)
print(F(42)) """

#17
""" f = open('17var20.txt')
a = [int(s) for s in f]
summi = []

    
for i in range(len(a) - 1):
    if ((a[i] > 300) + (a[i+1] > 300)) >= 1:
        summi.append(a[i]**2 + a[i+1]**2)
print(len(summi), min(summi)) """

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


