from itertools import *

#1
""" numb = 0
for i in sorted(product('LEMON', repeat = 5)):
    s = ''.join(i)
    numb += 1
    if s[0] == 'N':
        print(s, numb)
        break """
        
#2
""" numb = 0
for i in sorted(product('GOLD', repeat = 4)):
    s = ''.join(i)
    numb += 1
    if s.count('D') == 0:
        print(s, numb)
        break """
        
#3
""" numb = 0
cnt = 0
for i in sorted(product('МОНТАЖЕР', repeat = 6)):
    s = ''.join(i)
    numb += 1
    if (numb % 3 == 0 and s[0] == 'О' and (s.count('Ж') == 2 or\
        s.count('Ж') == 3)):
        cnt += 1
print(cnt) """

#4
""" cnt = 0
for i in product('ABCD1259', repeat = 6):
    s = ''.join(i)
    if s.count('1') + s.count('2') + s.count('5') + s.count('9') == 4:
        cnt += 1
print(cnt) """

#5
""" cnt = 0
glas = 'ИАОЕ'
sogl = 'ЧКБМНЩ'
for i in product('ЧКИБАМОНЩЕ', repeat = 6):
    s = ''.join(i)
    c1 = 0
    c2 = 0
    if (s.count('Щ') == 1 and s[0] in glas):     
        for j in s:
            if j in glas:
                c1 += 1
            if j in sogl:
                c2 += 1
        if c1 > c2:
            cnt += 1
print(cnt) """

#6
""" cnt = 0
chet = '0246'
nechet = '135'

for i in product('0123456', repeat = 6):
    s = ''.join(i)
    if s[0] != '0' and s.count('5') == 2:
        for j in s:
            if j in chet:
                s = s.replace(j, '*')
        if s.count('*5') == 0 and s.count('5*') == 0:
            cnt += 1
print(cnt) """

#7
""" cnt = 0

for i in permutations('АДЖИКА', r = 6):
    s = ''.join(i)
    if s.count('АА') == 0:
        cnt += 1
print(cnt//2) """

#8
""" cnt = 0
chet = '02468'
nechet = '13579'
for i in permutations('0123456789', r = 4):
    s = ''.join(i)
    if s[0] != '0':
        for j in s:
            if j in chet:
                s = s.replace(j, '0')
            if j in nechet:
                s = s.replace(j, '1')
        if s.count('00') == 0 and s.count('11') == 0:
            cnt += 1
print(cnt) """
        
                
            
        
    