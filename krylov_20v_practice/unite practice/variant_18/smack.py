
#2
""" print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (((w == (not y)) or (w == (not z))) and x and (y <= z)):
                    print(x, y, w, z) """

#5
""" for n in range(8, 1000):
    n = n - (n % 8) + (n % 2)
    n2 = bin(n)[2:]
    n2 += str(sum(map(int, n2)) % 2)
    n2 += str(sum(map(int, n2)) % 2)
    R = int(n2, 2)
    if R > 97:
        print(R)
        break """

#6
""" from turtle import *
tracer(0)
left(90)
pendown()
k = 15

for _ in range(7):
    circle() """
    
#8
""" from itertools import product
cnt = 0
for i in product('ЕГЭ', repeat=5):
    s = ''.join(i)
    if s[0] != 'Г':
            cnt += 1
print(cnt) """

#12
""" for n in range(1000):
    s = '>' + '1' * 16 + '2' * n + '3' * 16
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '1>', 1)
        if '>2' in s:
            s = s.replace('>2', '>3', 1)
        if '>3' in s:
            s = s.replace('>3', '>1', 1)
    s = s.replace('>', '')
    s1 = sum(map(int, s))
    k  = 0
    for i in range(1, s1 + 1):
        if s1 % i == 0:
            k += 1
            if k > 2:
                break
    if k == 2:
        print(n)
        break """
        
#13
""" from ipaddress import *
ip_add = ip_address('244.55.138.100')
for mask in range(33):
    try:
        ip_net = ip_network(f'240.0.0.0/{mask}')
        print(ip_net.netmask)
    except:
        continue """
        
#14
""" for x in '0123456789ABCDEFG':
    if (int('135' + x + '9', 17) + int('9'+ x + '531', 17)) % 9 == 0:
        print((int('135' + x + '9', 17) + int('9'+ x + '531', 17)) // 9) """

#15
""" def c(x, y, A):
    return (x >= A) or (y >= A) or (x * y <= 270)

for A in range(1000):
    flag = True
    for x in range(1000):
        for y in range(1000):
            if c(x, y, A) == False:
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
    if n == 2:
        return 2
    if n > 2:
        return n * (n - 1) * F(n - 1)
print(F(123) / F(120)) """

#17
""" f = open('17var18.txt')
summi = []
a = [int(s) for s in f]
for i in range(len(a) - 1):
    if (a[i] + a[i+1] >= 50 and a[i] >= 0 and a[i+1] >= 0):
        summi.append(a[i] * a[i+1])
print(len(summi), min(summi))  """  

#19
from functools import lru_cache
def step(a, b):
    return (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2)

""" @lru_cache(None)
def game(a, b):
    if a + b >= 123:
        return 'END'
    if any(x + y >= 123 for x, y in step(a, b)):
        return 'WIN1'
    if all(game(x, y) == 'WIN1' for x, y in step(a, b)):
        return 'LOSS1'
    if any(game(x, y) == 'LOSS1' for x, y in step(a, b)):
        return 'WIN2'
    if all(game(x, y) == 'WIN1' or game(x, y) == 'WIN2' for x, y in step(a, b)):
        return 'LOSS12'
for s in range(1, 113 + 1):
    if any(game(x, y) == 'WIN1' for x, y in step(9, s)):
        print(s) """
""" for s in range(1, 113 + 1):
    if game(9, s) == 'WIN2':
        print(s) """
""" for s in range(1, 113 + 1):
    if game(9, s) == 'LOSS12':
        print(s) """
#23
""" def c(s, e):
    if s > e:
        return 0
    if s == e:
        return 1
    if s < e:
        return c(s + 2, e) + c(s * 2, e) + c(s * 3, e)
print(c(2,6)*c(6,28)) """

""" def f(s, m):
    if s>=202:
        return m%2==0
    if m==0:
        return 0
    h=[f(s+1, m-1),f(s+4, m-1), f(s*3, m-1) ]
    return any(h) if (m-1)%2==0 else all(h)
print([s for s in range(1, 202) if f(s, 2)])
 """
 
 
""" print('x y w z F1 F2')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                F1 = ((x == y) and (w <= z))
                F2 = ((x <= y) <= (w == z))
                print(x, y, w, z, int(F1), ' ',int(F2)) """
                
                
from itertools import *
cnt = 0
words = []
for i in product('КОФЕ', repeat = 5):
    s = ''.join(i)
    cnt += 1
    if (s.count('Е') == 0 and s.count('Ф') == 1):
        words.append([s, cnt])
print(words[-1])
