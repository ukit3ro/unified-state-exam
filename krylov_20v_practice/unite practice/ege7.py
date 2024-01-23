#2
""" print('x y z w F') """
""" for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (not(y <= (not(z <= w)))  and ((not z) <= ((not w) == x)))
                print(x, y, z, w, int(F)) """
                
#5
""" import math


for n in range(1, 1000):
    n2 = bin(n)[2:]
    
    if n2.count('1') % 2 == 0:
        middle_position = math.ceil(len(n2) / 2)
        n3 = n2[:middle_position] + '1' + n2[middle_position:]
    
    if n2.count('1') % 2 != 0:
        n3  = n2

    R = int(n3, 2)
    if R >= 26:
        print(n)
        break """
        
#8
""" numb = 1
from itertools import product
for i in sorted(product('СОРНЯК', repeat = 6)):
    s = ''.join(i)
    if s.count('К') <= 3 and s.count('Я') == 2:
        print(numb, s)
        break
    numb += 1 """
    
#9
""" f = open('9.txt')
cnt = 0
for s in f:
    a = list(map(int, s.split())) """
    
    

#12
""" s = '22' + '1'*2024 + '22'
while '2111' in s or '1112' in s:
    s = s.replace('111', '1', 1)
    if '21' in s:
        s = s.replace('21', '12', 1)
    else:
        s = s.replace('12', '1', 1)
print(s) """

#14
""" s = 243**540 - 6 * 9**530 + 21 * 3**511 - 3 * 3**70 - 200
cnt = 0
while s > 0:
    if s % 9 == 8:
        cnt += 1
    s = s // 9
print(cnt) """

#15
""" def treug(n, m, k):
    return (n + m > k and n + k > m and k + m > n)

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if ((not((treug(x, 11, 18)) == (not(max(x, 5)) > 15))) or treug(x, A, 5)) == False:
            flag == False
            break
    if flag == True:
        print(A)
        break """
        
#17
""" f = open('17var07.txt')
a = [int(s) for s in f]
summi = []
mini = max(a)

for i in range(len(a)-2):
    if (a[i] + a[i+1] + a[i+2] < mini and (a[i] % 10 == 0 and (a[i+1] % 10 != 0 and a[i+2] % 10 !=0) or\
        (a[i] % 10 != 0 and a[i+1] % 10 == 0 and a[i+2] % 10 !=0) or\
            (a[i] % 10 != 0 and a[i+1] % 10 != 0 and a[i+2] % 10 ==0))):
        summi.append(a[i] + a[i+1] + a[i+2])
print(len(summi), max(summi)) """

#20
""" def WIN1(s):
    return (s + 2) >= 153 or (s * 2) >= 153

def LOSS1(s):
    return (not(WIN1(s))) and WIN1(s + 2) and WIN1(s * 2)

def WIN2(s):
    return LOSS1(s+2) or LOSS1(s * 2)

for s in range(1, 46):
    if WIN2(s):
        print(s) """
        
#21
""" def WIN1(s):
    return (s + 1) >= 153 or (s * 2) >= 153

def LOSS1(s):
    return (not(WIN1(s))) and WIN1(s + 1) and WIN1(s * 2)

def WIN2(s):
    return LOSS1(s+1) or LOSS1(s * 2)

def LOSS12(s):
    return (WIN2(s+1) and WIN1(2*s))

for s in range(1, 153):
    if LOSS12(s):
        print(s) """
        
#23
""" def task11(s, e):
    if s < e or s == 10:
        return 0
    if s == e:
        return 1
    if s > e:
        return task11(s - 1, e) + task11(s // 2, e)
print(task11(50, 20)*task11(20, 1)) """

#25
from fnmatch import fnmatch
for x in range(322104, 10**9):
    if fnmatch(str(x), r'32*21?4'):
        if x % 2049 == 0:
            print(x, x // 2049)