from itertools import *
#1
""" numb = 1
for i in product('ABCDEFGHIJ', repeat=3):
    s = ''.join(i)
    if s == 'GIF':
        print(s, numb)
    numb += 1 """
    

#2
""" numb = 1
for i in product('АИЛП', repeat=5):
    s = ''.join(i)
    if s == 'ПИАЛА':
        print(s, numb)
    numb += 1 """
    
    
#3
""" numb = 1
for i in product('EIQTU', repeat=6):
    s = ''.join(i)
    if numb == 9115:
        print(s, numb)
    numb += 1 """


#4
""" numb = 1
for i in product('FNOST', repeat=3):
    if i.count('F') == 0:
        print(i, numb)
        break
    numb += 1 """
    

#5
""" numb = 1
for i in product('АЙЛФ', repeat=4):
    if i.count('А') == 0 and i.count('Л') == 0:
        print(i, numb)
        break
    numb += 1 """
    

#6
""" codews = []
for i in product('CHAIN', repeat=5):
    if i.count('H') == 1:
        codews.append(i)
print(len(codews)) """


#8
""" codews = []
for i in product('WXYZ', repeat=5):
    if i.count('X') != 0 and i.count('X') <= 3:
        codews.append(i)
print(len(codews)) """


#9
""" codews = []
for i in product('ABCD123', repeat=4):
    if i.count('1') == 1 and i.count('2') == 0 and i.count('3') == 0\
        or i.count('2') == 1 and i.count('1') == 0 and i.count('3') == 0\
        or i.count('3') == 1 and i.count('2') == 0 and i.count('1') == 0:
        codews.append(i)
print(len(codews)) """


#10
""" sogl = 'ЛГРТМ'
glas = 'АОИ'
coqqqq = 0
for i in product('АЛГОРИТМ', repeat=7):
    if sum([i.count(letter) for letter in glas]) < sum([i.count(letter) for letter in sogl]):
        coqqqq += 1
print(coqqqq) """


#10
""" cccc1 = 0
for i in product('01234567', repeat=5):
    sss = ''.join(i)
    if (i.count('4') == 2 and i[0] != 0\
        and '14' not in sss and '41' not in sss\
        and '34' not in sss and '43' not in sss\
        and '54' not in sss and '45' not in sss\
        and '74' not in sss and '47' not in sss):\
        cccc1 += 1
print(cccc1) """


#12
""" codews = 0
for i in product('ПАЛЬТО', repeat=5):
    ss = ''.join(i)
    if (i.count('О') <= 2 and i[0] != 'О' and i[-1] != 'О'\
        and 'ОЛ' not in ss and 'ЛО' not in ss):
        codews += 1
print(codews) """


#13
""" codews = 0
for i in product('БИГМЭН', repeat=6):
    ss = ''.join(i)
    if (i.count('Б') == 1 and i.count('И') == 1 and i.count('Г') == 1\
        and i.count('М') == 1 and i.count('Э') == 1 and i.count('Н') == 1):
        codews += 1
print(codews) """


#14
""" codews = 0
for i in permutations('ПАРНИК', r=5):
    ss = ''.join(i)
    if i.count('ИА') == 0:
        codews += 1
print(codews) """

#15
""" cnttt = 0
for i in permutations('ДИАНА', r=5):
    sos = ''.join(i)
    if 'АА' not in sos:
        cnttt += 1
print(cnttt//2) """


#16
cccc1 = 0
cccc1 = 0
for i in product('01234', repeat=10):
    sss = ''.join(i)
    if ((i.count('2') + i.count('4') + i.count('0') + i.count('6') + i.count('8')) == 3 and i[0] != 0\
        and '00' not in sss and '02' not in sss\
        and '20' not in sss and '04' not in sss\
        and '40' not in sss and '06' not in sss\
        and '60' not in sss and '08' not in sss)\
        and '80' not in sss and '22' not in sss\
        and '24' not in sss and '42' not in sss\
        and '26' not in sss and '62' not in sss\
        and '28' not in sss and '82' not in sss\
        and '48' not in sss and '84' not in sss\
        and '44' not in sss and '88' not in sss:\
        cccc1 += 1
print(cccc1)
