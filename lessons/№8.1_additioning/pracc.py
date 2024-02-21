from itertools import *

#1
""" numb = 0
for i in sorted(product('UMSCL', repeat = 5)):
    s = ''.join(i)
    numb += 1
    if s[0] == 'S':
        print(s, numb)
        break """
        
#2
""" numb = 0
for i in sorted(product('СКАНЕР', repeat = 6)):
    s = ''.join(i)
    numb += 1
    if s.count('А') <= 3 and s.count('Н') == 2:
        print(s, numb)
        break """
        
#3
""" numb = 0
cnt = 0
for i in sorted(product('ИНФОРМАТ', repeat = 5)):
    s = ''.join(i)
    numb += 1
    if (s[0] != 'О' and (s.count('Н') == 1 or s.count('Н') == 2) and\
        numb % 2 != 0):
        cnt += 1
print(cnt) """

#4
""" numb = 0
cnt = 0
for i in sorted(product('ГВАРДИЯ', repeat = 6)):
    s = ''.join(i)
    numb += 1
    if s[0] != 'Д' and numb % 2 == 0 and s.count('Р') >= 2:
        cnt += 1
print(cnt) """

#5
""" cnt = 0
for i in product('QWER123', repeat = 5):
    s = ''.join(i)
    if s.count('1') + s.count('2') + s.count('3') == 2:
        cnt += 1
print(cnt) """

#6
""" cnt = 0
glas = 'АЕО'
sogl = 'БНДРЛ'
for i in product('БАНДЕРОЛЬ', repeat = 7):
    s = ''.join(i)
    c1 = 0
    c2 = 0
    for j in s:
        if j in glas:
            c1 += 1
        if j in sogl:
            c2 += 1
    if c1 > c2:
        cnt += 1
print(cnt) """

#7
""" cnt = 0
chet = '02468'
for i in product('012345678', repeat = 6):
    s = ''.join(i)
    if s[0] != '0' and s.count('3') == 1:
        for j in s:
            if j in chet:
                s = s.replace(j, '*', 1)
        if s.count('*3') == 0 and s.count('3*') == 0:
            cnt += 1
print(cnt) """

#8
""" cnt = 0
nechet = '135'
for i in product('0123456', repeat = 5):
    s = ''.join(i)
    if s[0] != '0' and s.count('2') == 2:
        for j in s:
            if j in nechet:
                s = s.replace(j, '*', 1)
        if s.count('*2') == 0 and s.count('2*') == 0:
            cnt += 1
print(cnt) """

#9
""" cnt = 0
for i in permutations('КАРЕТА', r = 4):
    s = ''.join(i)
    if "AA" not in s:
            cnt += 1
print(cnt) """

#10
""" chet = '02468'
nechet = '13579'
cnt = 0
for i in product('0123456789', repeat = 6):
    s = ''.join(i)
    if s[0] != '0' and len(set(s)) == len(s):
        for j in s:
            if j in chet:
                s = s.replace(j, '0')
            if j in nechet:
                s = s.replace(j, '1')
        if s.count('11') == 0 and s.count('00') == 0:
            cnt += 1
print(cnt) """



        
        
        
