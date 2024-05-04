
#5
""" for n in range(1000):
    n2 = bin(n)[2:]
    if n % 5 == 0:
        n2 += n2[-2:]
    if n % 5 != 0:
        n2 += bin(((n % 5) * 2))[2:]
    R = int(n2, 2)
    if R < 150:
        print(n)
 """

#8
""" from itertools import product
cnt = 0
for i in product('0123456', repeat = 6):
    s = ''.join(i)
    if s[0] not in '0135':
        if s[-1] not in '0246' and s.count('5') <= 1:
            cnt += 1
print(cnt) """
        
    

#9
cnt = 0
for s in open('71.txt'):
    a = list(map(int, s.split()))
    if ((len(set(a)) == 4) and (sum(set(a)) < 100)):
        cnt += 1
print(cnt)

#12
""" for n in range(1000):
    s = '>' + 56 * '0' + 49 * '1' + n * '2'
    while ">1" in s or ">2" in s or ">0" in s:
        if ">1" in s:
           s = s.replace(">1", "12>", 1)
        if ">2" in s:
           s = s.replace(">2", "5>", 1)
        if ">0" in s:
           s = s.replace(">0", "22>", 1)
    s1 = str(s) .replace('>', '').replace('<', '')
    n2 = sum(map(int, s1))
    k = 0
    for i in range(1, n2 + 1):
        if n2 % i == 0:
            k += 1
            if k > 2:
                break
    if k == 2:
        print(n)
        break """

#13
""" from ipaddress import *
ip_add = ip_address('185.49.83.72')
for mask in range(33):
    try:
        ip_net = ip_network(f'185.49.80.0/{mask}')
        
        if ip_add in ip_net:
            print(ip_net.netmask)
    except:
        continue """

#15
""" for A in range(1, 2000):
    flag = True
    for x in range(1, 2000):
        if ((x & 56 != 0) <= ((x & A == 0) <= (x & 35 != 0))) == False:
            flag = False
            break
    if flag == True:
        print(A)
        break """

#16
""" f = [0]*2000
for n in range(2000):
    if n == 1:
        f[n] = 1
    if n == 2:
        f[n] = 3
    if n > 2:
        f[n] = f[n - 1] + n * f[n - 2]
print(f[1890]//f[1885]) """