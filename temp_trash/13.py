
#2
""" print('a b c d')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if (((not a) and (not b)) or (b == c) or d) == False:
                    print(a, b, c, d) """
                    

#5
""" for n in range(1000):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 += '00'
    if n % 2 != 0:
        n2 += '11'
    r = int(n2, 2)
    if r < 134:
        print(n) """

#6
""" from turtle import *
tracer(0)
left(90)
k = 15
pendown()
for _ in range(4):
    forward(14*k)
    right(90)
for _ in range(5):
    forward(5*k)
    right(45)

penup()
for x in range(0, 20):
    for y in range(0, 20):
        goto(x*k, y*k)
        dot(4)
done() """

#8
""" from itertools import product
cnt = 0
for i in product('ABCDE', repeat = 5):
    s = ''.join(i)
    if s[0] != 'E' and s[-1] != 'A':
        cnt += 1
print(cnt) """

#9
""" cnt = 0
for i in open('91.txt'):
    a = list(map(int, i.split()))
    povt = []
    nepovt = []
    for s in a:
        if a.count(s) == 1:
            nepovt.append(s)
        if a.count(s) > 1:
            povt.append(s)
    if len(povt) > 0 and len(nepovt) > 0:
        if (sum(nepovt) / len(nepovt) < sum(povt) / len(povt)):
            cnt += 1
print(cnt) """

#12
""" s = '7' * 79
while '7777' in s or '3333' in s:
    if '3333' in s:
        s = s.replace('3333', '77', 1)
    if '7777' in s:
        s = s.replace('7777', '33', 1)
print(s) """

#13
""" from ipaddress import *
ip_add = ip_address('10.18.134.220')
for mask in range(33):
    try:
        ip_net = ip_network(f'{mask}/255.255.255.192')
        print(mask)
    except:
        continue """
        
#14
""" for x in range(14):
    for y in range(14):
        if (int(f'{y}AA{x}', 12) + int(f'{x}02{y}', 14)) % 80 == 0:
            print((int(f'{y}AA{x}', 12) + int(f'{x}02{y}', 14)) // 80)
            break """
                
#15
""" for A in range(1000):
    flag = True
    for x in range(1000):
        if ((x & 51 == 0) or ((x & 41 == 0) <= (x & A == 0))) == False:
            flag = False
            break
    if flag == True:
        print(A) """
        
#16
""" def F(n):
    if n <= 2:
        return 2
    if n > 2:
        return 3 * F(n - 1) - F(n - 2)
print(F(6)) """

#17
""" summi = []
a = [int(s) for s in open('17.txt')]
min3 = min([j for j in a if str(j)[-1] == '3'])
for i in range(len(a) - 1):
    if ((str(a[i])[-1] == str(a[i+1])[-1]) and ((a[i] % 3 == 0) + (a[i+1] % 3 == 0) == 1)\
        and (a[i]**2 + a[i+1]**2 <= min3**2)):
            summi.append(a[i]**2 + a[i+1]**2)
print(len(summi), max(summi)) """

#19-21
""" from functools import lru_cache
def step(a, b):
    return (a + 1, b), (a, b + 1), (a+4, b), (a, b + 4), (a*3, b), (a, b*3)

@lru_cache
def game(a, b):
    if a + b >= 89:
        return 'END'
    if any(x + y >= 89 for x, y in step(a, b)):
        return 'WIN1'
    if all(game(x, y) == 'WIN1' for x, y in step(a, b)):
        return 'LOSS1'
    if any(game(x, y) == 'LOSS1' for x, y in step(a, b)):
        return 'WIN2'
    if all(game(x, y) == 'WIN1' or game(x, y) == 'WIN2' for x, y in step(a,b)):
        return 'LOSS12'
for s in range(1, 89):
    if game() """
    
#23
""" def t(s, e):
    if s > e:
        return 0
    if s == e:
        return 1
    if s < e:
        return t(s +1, e) + t(s * 2, e)
print(t(1,12)*t(12,25)*t(25,40)) """

#24
""" f = open('24.txt') """

#25
"""   """

#
""" from ipaddress import *
ip_net = ip_network('192.168.32.160/255.255.255.240', False)
cnt = 0
for addr in ip_net:
    if bin(int(addr))[2:].count('0') > 21:
        cnt += 1
print(cnt) """
#14
""" s = 7*512**3200 + 6*256**3100 - 5*64**3000 - 4*8**2900 - 1542
c = 0
while s > 0:
    if s % 64 == 0:
        c += 1
    s //= 64
print(c) """
#14.1
""" for x in range(130):
    s1 = 2 * 130**4 + 3 * 130**3 + x * 130**2 + 3 * 130 + 2
    s2 = 3 * 130**4 + x * 130**3 + 2 * 130**2 + 5 * 130 + 3
    if (s1 + s2) % 23 == 0:
        print(x) """

#16
f = [0]*4000
for n in range(1, 4000):
    if n < 3:
        f[n] = 3
    else:
        f[n] = 2 * n + 5 + f[n-2]
print(f[3027]-f[3023])

