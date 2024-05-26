#2
""" print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x <= y) and z and (not w)) == True:
                    print(x, y, z, w) """
                
#5
""" for n in range(1, 1000):
    n2 = (bin(n - (n % 4)))[2:]
    s1 = sum(map(int, n2))
    n2 += str(s1 % 2)
    s2 = sum(map(int, n2))
    n2 += str(s2 % 2)
    R = int(n2, 2)
    if R < 64:
        print(n) """
    
#6
""" from turtle import *
k = 15
left(90)
tracer(0)
pendown()

right(180)
forward(2*k)
right(90)
forward(30*k)
right(90)
forward(2*k)
right(30)
for _ in range(6):
    forward(5*k)
    right(120)
    forward(5*k)
    right(240)

penup()
for x in range(-40, 20):
    for y in range(-5, 20):
        goto(x*k, y*k)
        dot(4)
done() """


#8
""" cnt = 0
from itertools import product
for i in product('0123', repeat = 3):
    s = ''.join(i)
    if s[0] != '0':
        if (s[0] >= s[1] >= s[2]):
            cnt += 1
print(cnt) """


#9
#autorun

#12
""" s = '1' * 65
while '11111' in s or '15' in s:
    if '11111' in s:
        s = s.replace('11111', '15', 1)
    else:
        s = s.replace('15', '1', 1)
print(s) """

#13
""" from ipaddress import *
for A in range(0, 256):
    ip_net = ip_network(f'64.129.{A}.10/255.255.252.0', False)
    for ip_add in ip_net:
        if (bin(int(ip_add))[-16:].count('1') >= bin(int(ip_add))[:-16].count('1')) == False:
            break
    else:
        print(A)
        break """
        

#14
""" s = 3**2021 + 5 * 3**2000 + 3**501 + 5 * 3**500 + 1
cnt = 0
while s > 0:
    if s % 9 == 0:
        cnt += 1
    s = s // 9
print(cnt) """

#15
""" B = list(range(4, 19))
C = list(range(12, 41))
A = list(range(100))
for x in range(100):
    if (not(x in A) <= ((x in B) == (x in C))) == False:
        A.remove(x)
print(A) """
#16
""" f = [0]*30000
for n in range(3000):
    if n  == 1:
        f[n] == 1
    if n == 2:
        f[n] == 2
    if f[n] > 2:
        f[n] = n * (n - 1) + f[n - 1] + f[n - 2]
    
print(f[100])  
     """
#17
""" f = open('17var12.txt')
a = [int(s) for s in f]
summi = []
    
for i in range(len(a) - 1):
    if (a[i] % 5 == 0 and a[i+1] % 5 == 0):
        summi.append(a[i] + a[i+1])
print(len(summi), min(summi)) """


#23
""" def t(s, e):
    if s > e:
        return 0
    if s == e:
        return 1
    if s < e:
        return t(s + 2, e) + t(s + 10, e)
print(t(7, 71)) """

#25
""" for i in range(1, 800000, -1):
    if i %  """
