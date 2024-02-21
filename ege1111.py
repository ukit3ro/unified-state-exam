
#2
""" print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (y and (x or z) or (not(y or z)) or w) == 0:
                    print(x, y, z, w) """
                    
#5
""" for n in range(10, 1000):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 += n2[-1] + n2[-2]
    if n % 2 != 0:
        n2 += '0'
        n2 == '1' + n2
    R = int(n2, 2)
    if R < 100:
        print(n) """
        
#6
""" from turtle import *
tracer(0)
pendown()
k = 15
left(90)
for i in range(2):
    forward(5*k)
    left(90)
    backward(13*k)
    left(90)
penup()
backward(10*k)
right(90)
forward(9*k)
left(90)
pendown()
for i in range(2):
    forward(11*k)
    right(90)
    forward(7*k)
    right(90)

penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*k, y*k)
        dot(4)
done() """

#8
""" cnt = 0
from itertools import product
for i in product('012345678', repeat = 5):
    s = ''.join(i)
    if s[0] != '0' and s.count('5') == 1 and s.count('00') == 0 and\
        s.count('11') == 0 and s.count('22') == 0 and s.count('33') == 0\
            and s.count('44') == 0 and s.count('66') == 0 and s.count('77')\
                == 0 and s.count('88') == 0 and s.count('99') == 0:
                    cnt += 1
print(cnt) """

#12
""" asa = []
for n in range(3, 10001):
    s = '3' + '5' * n
    while '333' in s or '555' in s:
        if '555' in s:
            s = s.replace('555', '3')
        if '333' in s:
            s = s.replace('333', '5')
    asa.append(s.count('5')*5 + s.count('3')*3)
print(max(asa)) """

#13
""" from ipaddress import *
ip_net = ip_network('192.168.32.48/255.255.255.240', False)
cnt = 0

for ip_add in ip_net:
    if (bin(int(ip_add)).count('1')) % 2 == 0:
        cnt += 1
print(cnt) """

#14
""" cnt = 0
s = 2 * 729**333 + 2*243**334 - 81**335 + 2 * 27**336 - 2 * 9**337 - 338
s = str(s)
while s > 0:
    s = s // 9
for i in s:
    if i != '0':
        cnt += 1
print(cnt) """

#15
""" for A in range(1000):
    flagi = True
    for x in range(1000):
        if ((x & A == 0) or (not(x & 37 == 0)) or (not(x & 12 == 0))) == False:
            flagi = False
            break
    if flagi == True:
        print(A) """
        
#16
""" import sys
sys.setrecursionlimit(10000)
def F(n):
    if n <= 3:
        return 1
    if n > 3:
        return (n + 3) * F(n - 2)
print(F(2028)/F(2024)) """

#17
""" f = open('17.txt')
a = [int(s) for s in f]
troiki = []
maxis = 63933
for i in range(len(a) - 2):
    if ((str(a[i])[-1] == '3' or str(a[i+1])[-1] == '3' or str(a[i+2])[-1] == '3') and\
       ((a[i] + a[i+1] + a[i+2]  ) <= maxis)):
           troiki.append(a[i] + a[i+1] + a[i+2])
           print(a[i], a[i+1], a[i+2])
print(len(troiki), max(troiki)) """

#19
""" def WIN1(s):
    return (s + 3) >= 301 or (s * 3) >= 301

for s in range(1, 302):
    if WIN1(s + 3) or WIN1(s * 3):
        print(s)
        break """
        
#23
""" def t11(s, e):
    if s > e or s == 16:
        return 0
    if s == e:
        return 1
    if s < e:
        return t11(s + 1, e) + t11(s + 3, e) + t11(s**2, e)
print(t11(3,20)*t11(20, 26))
 """
 
#24
f = open('24.txt')



