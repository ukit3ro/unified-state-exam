
#2
""" print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (((not x) or y) and (x == (not z)) and w) == True:
                    print(x, y, w, z) """
                    
#5
""" cnt = 0
for n in range(1000):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 += '00'
    if n % 2 != 0:
        n2 += '10'
    if n2.count('1') % 2 == 0:
        n2 += '0'
    if n2.count('1') % 2 != 0:
        n2 += '1'
    r = int(n2, 2)
    if r in list(range(130, 351 )):
        cnt += 1
print(cnt) """

#6
""" from turtle import *
k = 15
left(90)
tracer(0)
pendown()

for _ in range(5):
    left(60)
    forward(4*k)
    left(120)
    forward(4*k)
penup()

for x in range(-10, 10):
    for y in range(-10, 10):
        goto(x*k, y*k)
        dot(4)
done() """

#8
""" from itertools import permutations
print((list(permutations('ИДИЛЛИЯ', r = 7)))) """

#9
""" cnt = 0
for s in open('9.txt'):
    s = s.replace(',', '.')
    a = list(map(float, s.split()))
    if (((a[0] + a[1] + a[11]) / 3) > ((a[5] + a[6] + a[7]) / 3)):
        cnt += 1
print(cnt) """

#12
""" s = '2' * 30 + '4' * 54 + '6' * 10
while '6404' in s or '2206' in s or '440' in s:
    if '6404' in s:
        s = s.replace('6404', '02', 1)
    if '2206' in s:
        s = s.replace('2206', '04', 1)
    if '440' in s:
        s = s.replace('440', '06', 1)
print(s.count('6')) """

#13
""" from ipaddress import *
for add in range(33):
    try:
        ip_net = ip_network(f'{add}/255.255.254.0 ')
        
        if add in ip_net:
            print(add)
    except:
        continue """
        
#14
""" for n in range(10000):
    s = 243**5 + 3**7 - 2 - n
    n1 = ''
    while s > 0:
        n1 += str(s%3)
        s //= 3
    if n1.count('2') == 20:
        print(n)
        break """
        
#15
""" X = list(range(12, 94))
Y = list(range(54, 151))
Z = list(range(200))
for x in range(200):
    if ((x in Y) <= ((not(x in X)) and not(x in Z) <= (not(x in Y)))) == True:
        Z.remove(x)
print(Z) """

#16
""" def F(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + F(n/2)
    if n % 2 != 0 and n > 1:
        return n * F(n - 1)
print(F(37)) """

#17
f = open('17.txt')
a = [int(s) for s in f]
print(a)
summi = []
for i in range(len(a) - 1):
    if (a[i] % 5 == 0 and a[i+1] % 5 == 0):
        print(a[i], a[i+1])
        summi.append(a[i] + a[i+1])
print(len(summi), max(summi))


        
     