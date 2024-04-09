#2
""" print('x y w z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((x <= y) <= w) or (z <= (y and w))) == False:
                    print(x, y, z, w) """
                
#5
""" for i in range(100, 1000):
    s = str(i)
    a1 = int(s[0]) + int(s[1]) + int(s[2])
    a2 = int(s[0]) * int(s[1]) * int(s[2])
    if a1 > a2:
        f = str(a1) + str(a2)
    if a2 > a1:
        f = str(a2) + str(a1)
    
    if f == '24019':
        print(i) """
#6
""" from turtle import """

#8
""" numb = 1
from itertools import product
for i in sorted(product('ВАЛИК', repeat = 6)):
    if i.count('А') <= 2 and i.count('В') == 2 and i.count('И') == 0:
        print(i, numb)
        break
    numb += 1 """

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
def t(s, e):
    if s > e:
        return 0
    if s == e:
        return 1
    if s < e:
        return t(s + 2, e) + t(s + 10, e)
print(t(7, 71))

#25
""" for i in range(1, 800000, -1):
    if i %  """


