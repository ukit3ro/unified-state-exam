#https://education.yandex.ru/ege/variants/2e54e71c-dc2d-4835-9353-440269bf6ace/task/1
#2
""" print('k l m n')
for k in range(2):
    for l in range(2):
        for m in range(2):
            for n in range(2):
                if ((not n) or k and (not m) or (l == m)) == False:
                    print(k, l, m, n) """
                
#5
""" for n in range(1000):
    n2 = bin(n)[2:]
    if n % 2 != 0:
        n2 += '10'
    if n % 2 == 0:
        n2 = '1' + n2 + '1'
    R = int(n2, 2)
    if R > 179:
        print(n)
        break """
    
    
#6
""" from turtle import *
tracer(0)
k = 20
left(90)
pendown()

for _ in range(2):
    forward(12*k)
    right(90)
    forward(19*k)
    right(90)
penup()
forward(4*k)
right(90)
forward(6*k)
left(90)
pendown()
for _ in range(2):
    forward(12*k)
    right(90)
    forward(6*k)
    right(90)

penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(4)
done() """
    

#8
""" numb = 1
from itertools import product
for i in sorted(product('ШАТЕР', repeat = 5)):
    s = ''.join(i)
    print(s)
    if (s.count('А') <= 1 and 'ЕЕ' not in s):
        print(i, numb)
        break
    numb += 1 """

#9
""" cnt = 0
for s in open('9.txt'):
    a = list(map(int, s.split()))
    if (max(a) < (sum(a) - max(a)) and (a[0] + a[1] == a[2]  +a[3] or\
        a[0] + a[3] == a[1]  +a[2] or a[0] + a[2] == a[1]  +a[3]) and (sum(a)%2==0)):
        cnt += 1
print(cnt) """

#12
""" s = '7' * 47
while '2222' in s or '7777' in s:
    if '2222' in s:
        s = s.replace('2222', '77', 1)
    else:
        s = s.replace('7777', '22', 1)
print(s)
 """
#13
""" from ipaddress import *
cnt = 0
ip_net = ip_network('114.179.203.128/255.255.255.192', False)
for ip_add in ip_net:
    if bin(int(ip_add)).count('1') % 3 == 0:
        cnt += 1
print(cnt) """
        

#14
""" for x in '0123456789ABCDEFGHIJKLMNOPQRS':
    if (int('42' + x + '158', 29) + int('16' + x + '234', 29)) % 28 == 0:
        print((int('42' + x + '158', 29) + int('16' + x + '234', 29)) // 28) """

#15
""" B = list(range(74, 195))
C = list(range(152, 224))
A = []
for x in range(300):
    if ((not(x in A) and (x in B)) <= ((x in B) <= (not(x in C)))) == True:
        A.append(x)
print(A) """
#16
""" import sys
sys.setrecursionlimit(3000)
def F(n):
    if n <= 12:
        return 1
    if n > 12:
        return F(n - 1) + n - 2
print(F(2024) - F(2020)) """

#17
""" f = open('17.txt')
a = [int(s) for s in f]
summi = []
krat = max([i for i in a if i % 21 == 0])
    
for i in range(len(a) - 1):
    if ((a[i] > krat) + (a[i+1] > krat)) >= 1:
        summi.append(a[i] + a[i+1])
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
        return t(s + 1, e) + t(s * 2, e)
print(t(3, 6)*t(6, 12)*t(12,16)) """

#24
""" s = open('24.txt').readline()
s = s.replace('E', 'A').replace('K', 'L').replace('M', 'L').replace('N', 'L')\
    .replace('O', 'A').replace('U', 'A')
while 'AA' in s:
    s = s.replace('AA', 'A A')
while 'LL' in s:
    s = s.replace('LL', 'L L')
print(max(len(c) for c in s.split())) """

#25
from fnmatch import fnmatch
for x in range(0, 10**10, 2024):
    if fnmatch(str(x), '10*2024?'):
        print(x, x // 2024)


