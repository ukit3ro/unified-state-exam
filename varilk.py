
#2
""" print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((x == y) and (w <= z)) == False and\
                    ((x <=y) <= (w == z)) == False):
                    print(x, y, z, w) """
                    
#6
""" from turtle import *
tracer(0)
left(90)
pendown()
k = 20
begin_fill()
for _ in range(8):
    right(45)
    forward(8*k)
end_fill()
canvas = getcanvas()
penup()
cnt = 0
for x in range(-10, 20):
    for y in range(-20, 10):
        if canvas.find_overlapping(x*k, y*k, x*k, y*k) == (5, ):
            cnt += 1
print(cnt)

done() """

#8
""" from itertools import product
numb = 0
for i in sorted(product('СВЕТА', repeat = 5)):
    s = ''.join(i)
    numb += 1
    if s == 'СВЕТА':
        print(numb) """

#9
""" cnt = 0
for s in open('99.txt'):
    a = list(map(int, s.split()))
    if len(a) == len(set(a)):
        if (((min(a) + max(a)) / 2) > ((sum(a) - min(a) - max(a)) / 4)):
            cnt += 1
print(cnt) """

#12
""" def check(x):
    return all(x % i != 0 for i in range(2, round(x ** .5) + 1))
summe = []
for n in range(150):
    for n1 in range(150):
        s = '0' + '1' * n + '2' * n1
        if len(s) > 40:
            while '01' in s or '02' in s:
                s = s.replace('02', '1110', 1).replace('01', '220', 1)
            if check(sum(map(int, s))):
                summe.append(n + n1 * 2)
print(min(summe)) """

#13
""" from ipaddress import *
for mask in range(31):
    ip1 = ip_network(f'120.91.176.213/{mask}', 0)
    ip2 = ip_network(f'120.91.174.205/{mask}', 0)
    if ip1 == ip2:
        print(ip1.netmask) """
        
#14
""" ans = []
for x in range(37):
    for y in range(37):
        if (1*37**7 + 2*37**6 + x*37**5 + 6*37**4 + 4*37**3 + 3*37**2 + y*37**1 + 7*37**0) % 36 == 0:
            ans.append(y*37+x)
print(max(ans)) """

#15
""" def f(x,y,a): 
    return (x + 2 * y > 48) or (y > x) or (x + 3 * y < a)
for a in range(100, 0, -1):
    if any(f(x,y,a) == 0 for x in range(200) for y in range(200)):
        print(a)
        break """
        
#16
""" def f(n):
    if n >= 1000: 
        return 1000
    if n % 2 == 0: 
        return n * f(n + 1)
    return n * f(n + 1) // 2
print(f(998) // f(1001)) """

#17
""" def f(x): 
    return 1000 <= x < 10000
a = [int(x) for x in open('17.txt')]
mx19 = max(x for x in a if x % 100 == 19)
ans = []
for i in range(2, len(a)):
    if sum(f(x) for x in a[i-2:i+1]) == 2:
        if any(x % 3 == 0 for x in a[i-2:i+1]):
            if sum(a[i-2:i+1]) > mx19:
                ans.append(sum(a[i-2:i+1]))
print(len(ans), max(ans)) """

#19-21
""" def f(s, m):
    if s >= 108: return m % 2 == 0
    if m == 0: return 0
    h = [f(s + 1, m - 1)]
    if s % 2 != 0: h += [f(s * 2, m - 1)]
    else: h += [f(s * 1.5, m - 1)]
    return any(h) if m % 2 != 0 else all(h)

print('19)', max(s for s in range(1, 108) if f(s, 2)))
print('20)', *[s for s in range(1, 108) if not f(s, 1) and f(s, 3)][:2])
print('21)', max(s for s in range(1, 108) if not f(s, 2) and f(s, 4))) """

#23
""" def f(x,y):
    if x == y: return 1
    if x > y or x == 12: return 0
    return f(x+1, y) + f(x*2, y) + f(x**2, y)

print(f(3, 25)) """

#25
""" from fnmatch import *
for x in range(0, 10**10, 2024):
    if fnmatch(str(x), '3?6906*4'):
        print(x) """