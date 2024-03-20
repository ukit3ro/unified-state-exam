
#2
""" print('a b c d')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if ((not c) and (((not a) <= (not d)) <= (not b))) == True:
                    print(a, b, c, d) """

#5
""" for n in range(1, 1000):
    n2 = bin(n)[2:]
    
    if n % 4 == 0:
        n2 += n2[-2:]
    if n % 4 != 0:
        n2 += (bin((n % 4))[2:])

    if n2[-1] == '0':
        n2 = n2[:-1]
    
    R = int(n2, 2)
    if R > 213:
        print(R)
        break """
        
#6
""" from turtle import *
k = 10
left(90)
pendown()
tracer(0)

for _ in range(15):
    for i in range(20):
        forward(40*k)
        right(90)
    left(90)

penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*k, y*k)
        dot(4)
done() """
    
#8
""" from itertools import permutations
cnt = 0
chet = '0246'
for i in permutations('01234567', r = 4):
    s = ''.join(i)
    if s[0] != '0':
        if s[0] == '3' and s[-1] == '0':
            for j in s:
                if j in chet:
                    s = s.replace(j, '0')
            if s.count('00') == 0:
                cnt += 1
                print(s)
print(cnt) """

#9
""" cnt = 0
for s in open('9.txt'):
    a = list(map(int, s.split()))
    povt = []
    nepovt = []
    for n in a:
        if a.count(n) == 3:
            povt.append(n)
        if a.count(n) == 1:
            nepovt.append(n)
    if ((len(set(povt)) == 2 and len(set(nepovt)) == 2) and\
        min(a) not in povt):
        cnt += 1
        print(a)
print(cnt) """

#12
""" for n in range(3, 10001):
    s = '7' + '3' * n
    while '733' in s or '331' in s or '3333' in s:
        if '733' in s:
            s = s.replace('733', '411', 1)
        if '331' in s:
            s = s.replace('331', '24', 1)
        if '3333' in s:
            s = s.replace('3333', '7', 1)
    if sum(list(map(int, s))) == 64:
        print(n)
        break """
        
#13
""" from ipaddress import *
ip_net = ip_network('192.168.32.200/255.255.255.224', False)
cnt = 0

for ip_add in ip_net:
    if int(ip_add) % 3 == 0:
        cnt += 1
print(cnt)   """

#14
""" for y in '0123456789ABCDE':
    if (int('ABCD' + y, 15) + int('123' + y + '4', 15)) % 14 == 0:
        print((int('ABCD' + y, 15) + int('123' + y + '4', 15)) // 14) """
        

#15
""" for A in range(1000):
    flag = True
    for x in range(1000):
        for y in range(1000):
            if ((2 * x + y < A) or (y > 17) or (x > y)) == False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A)
        break """
        
#16
""" def F(n):
    if n <= 1:
        return 42
    elif (n > 1 and n % 2 == 0):
        return F(n - 2) + F(n - 3) + n
    else:
        return F(n - 1) + F(n - 3)
print(F(99)) """
""" f = [0] * 10000
for n in range(1, 10000):
    if n <= 1:
        f[n] = 42
    if (n > 1 and n % 2 == 0):
        f[n] = f[n - 2] + f[n - 3] + n
    if n > 1 and n % 2 != 0:
        f[n] = f[n - 1] + f[n - 3]
print(f[99]) """
        
    
    

#17
""" f = open('17.txt')
a = []
for s in f:
    a.append(int(s))
summi = []

for i in range(len(a) - 3):
    if (int(a[i] > 1000) + int(a[i+1] > 1000) + int(a[i+2] > 1000) + int(a[i+3] > 1000)) == 2\
        and (a[i] + a[i+1] + a[i+2] + a[i+3] <= 3947):
            if (int(str(a[i])[-2:] == '47') + int(str(a[i+1])[-2:] == '47')\
                + int(str(a[i+2])[-2:] == '47') + int(str(a[i+3])[-2:] == '47') >= 1):
                summi.append(a[i] + a[i+1] + a[i+2] + a[i+3])
print(len(summi), max(summi)) """
                
#23
""" def t20(s, e):
    if s > e or s == 15:
        return 0
    if s == e:
        return 1
    if s < e:
        return t20(s + 2, e) + t20(s * 2, e) + t20(s**3, e)
print(t20(3,50)*t20(50, 200)) """

#25
""" from fnmatch import fnmatch
for x in range(19071320, 10**10+1):
    if fnmatch(str(x), r'19?71*32?'):
        if x % 2024 == 0:
            print(x, x // 2024) """
        