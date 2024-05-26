#2
""" print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (not(z <= w) or x or (not y)) == False:
                    print(x, y, z, w) """
                
#5
""" for n in range(1, 1000):
    n2 = (bin(n - (n % 4)))[2:]
    s1 = sum(map(int, n2))
    n2 += str(s1 % 2)
    s2 = sum(map(int, n2))
    n2 += str(s2 % 2)
    R = int(n2, 2)
    if R > 100:
        print(R)
        break """
#6
""" from turtle import *
k = 15
left(90)
tracer(0)
pendown()


for _ in range(10):
    right(120)
    forward(12*k)
    right(60)
    forward(12*k)

penup()
for x in range(-10, 20):
    for y in range(-20, 20):
        goto(x*k, y*k)
        dot(3)
done() """

#8
""" cnt = 0
from itertools import product
for i in product('01234', repeat = 3):
    s = ''.join(i)
    if s[0] != '0':
        if (s[0] > s[1] > s[2]):
            cnt += 1
print(cnt) """

#9
#autorun

#12
""" for n in range(1, 100):
    s = '>' + '0' * 15 + '1' * n + '2' * 15
    while '>0' in s or '>1' in s or '>2' in s:
        if '>0' in s:
            s = s.replace('>0', '22>', 1)
        if '>1' in s:
            s = s.replace('>1', '2>', 1)
        if '>2' in s:
            s = s.replace('>2', '1>', 1)
    s1 = str(s).replace('>', '')
    k = 0
    sn = sum(map(int, s1))
    
    for i in range(1, sn + 1):
        if sn % i == 0:
            k += 1
            if k > 2:
                break
    if k == 2:
        print(n)
        break """

#13
""" from ipaddress import *
for A in range(0, 256):
    ip_net = ip_network(f'126.255.{A}.100/255.255.240.0', False)
    for ip_add in ip_net:
        if (bin(int(ip_add))[:-16].count('1') >= bin(int(ip_add))[-16:].count('1')) == False:
            break
    else:
        print(A) """
        

#14
""" s = 3**2020 - 3**1020 + 9**800 - 81
cnt = 0
while s > 0:
    if s % 3 == 2:
        cnt += 1
    s = s // 3
print(cnt) """

#15
""" def aoa(n, m):
    return n % m == 0

for A in range(1, 1000):
    A_right = True
    for x in range(1, 1000):
        if (not(aoa(x, A)) <= (aoa(x, 26) <= (not(aoa(x, 169))))) == False:
            A_right = False
            break
    if A_right == True:
        print(A) """


#16
""" f = [0]*1000
for n in range(1000):
    if n  == 1:
        f[n] = 1
    if n % 2 == 0:
        f[n] = n + 3 * f[n - 1]
    if n > 1 and n % 2 != 0:
        f[n] = 2 + 2 * f[n - 2]
print(f[23]) """  
    
#17
""" f = open('17var14.txt')
a = [int(s) for s in f]
summi = []
    
for i in range(len(a) - 1):
    if (str(a[i])[-1] == '7' and str(a[i+1])[-1] == '7'):
        summi.append(a[i] - a[i+1])
    if (str(a[i])[-1] == '7' and str(a[i+1]) == '7'):
        summi.append((a[i] - a[i+1]))
print(len(summi), min(summi))
 """

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


