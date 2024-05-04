#https://education.yandex.ru/ege/variants/7c6369e8-bc02-4d5f-a0f8-a590afea969e/task/2

#2
""" print('u w x y')
for u in range(2):
    for w in range(2):
        for x in range(2):
            for y in range(2):
                if ((not((y <= w) == x)) and u):
                    print(u, w, x, y) """
                
#5
""" def f(n, osn):
    s = ''
    while n > 0:
        s += str(n % osn)
        n //= osn
    s = s[::-1]
    return s
for n in range(1, 200):
    n2 = f(n, 7)
    if n % 7 == 0:
        n2 = n2 + n2[-2:]     
    if n % 7 != 0:
        n2 = n2 + f(((n % 7) * 2), 7)
    R = int(n2, 7)
    if R < 220:
        print(n) """
        
    
    
#6
""" from turtle import *
tracer(0)
k = 20
left(90)
pendown()

right(135)
for _ in range(7):
    forward(7*k)
    right(45)
    forward(8*k)
    right(135)

penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*k, y*k)
        dot(4)
done() """
    
#8
""" from itertools import product
cnt = 0
for i in product('ВОЗДУХ', repeat = 5):
    s = ''.join(i)z
    for n in s:
        if n == 'В' or n == 'Х':
            s = s.replace(n, '*', 1)
    
    if (s.count('О') == 1 or s.count('У') == 1): 
        if '*О' not in s and 'О*' not in s and '*У' not in s and 'У*' not in s:
                cnt += 1
        
print(cnt) """

#9
""" cnt = 0
for s in open('9.txt'):
    a = list(map(int, s.split()))
    povt = []
    for n in a:
        if a.count(n) == 3:
            povt.append(n)
    if (len(set(a)) == 5 and sum(a) < 502 and len(set(povt)) == 1):
        cnt += 1
print(cnt) """

#12
""" for n in range(3, 10001):
    s = '8' + '5' * n
    while '8858' in s or '555' in s:
        if '8858' in s:
            s = s.replace('8858', '4', 1)
        else:
            s = s.replace('555', '58', 1)
        if '5858' in s:
            s = s.replace('5858', '85', 1)
    if sum(map(int, s)) == 66:
        print(n) """

#13
""" from ipaddress import *
ip_net = ip_network('95.112.224.0/255.255.255.128')
for add in ip_net:
    print(add) """
    
        
#14
""" s = 7 * 49**120 - 6 * 343**65 - 5 * 7**40
n = ''
while s > 0:
    n += str(s % 7)
    s //= 7

print(n.count('6')) """

#15
""" def fucc(x, y, A):
    return ((x >= A) or (121 >= x**2)) and ((y**2 < 49) or (A < y))

for A in range(-10, 1000):
    A_flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if fucc(x, y, A) == False:
                A_flag = False
                break
        if A_flag == False:
            break
    if A_flag == True:
        print(A) """
        
    
#16
""" f = [0] * 1000
for n in range(1000):
    if n <= 1:
        f[n] = 1
    if n > 1 and n % 3 == 0:
        f[n] = f[n - 1] + n // 3
    if n > 1 and n %  3 != 0:
        f[n] = f[n - 1] + f[n - 2]
print(f[54] - f[52] - f[50]) """
    

#17
""" f = open('17.txt')
a = [int(s) for s in f]
summi = []
for i in range(len(a) - 2):
    if ((((a[i] % 2 == 0) + (a[i+1] % 2 == 0) + (a[i+2] % 2 == 0)) <= 2) and\
        ((a[i] + a[i+1] + a[i+2]) <= sorted(a)[-3])):
        summi.append(a[i] + a[i+1] + a[i+2])
print(len(summi), max(summi)) """

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
    if s > e or s == 11:
        return 0
    if s == e:
        return 1
    if s < e:
        return t(s + 1, e) + t(s + 4, e) + t(s * 3, e)
print(t(7, 27)*t(27, 42)) """

#24
""" s = open('24.txt').readline()
s = s.replace('AHAHA', ' ')

print(max(len(c) for c in s.split())) """
    
#25
""" from fnmatch import fnmatch
for x in range(0, 2*10**10, 42):
    if fnmatch(str(x), '?2*4*0'):
        if fnmatch(str(x), '1*7*') == False:
            print(x, x // 42) """


