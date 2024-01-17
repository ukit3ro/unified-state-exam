cnt from itertools import *


#1
numb = 1
for i in product('АБВГДЕЖЗИК', repeat=3):
    s = ''.join(i)
    if s == 'АГА':
        print(numb)
    numb += 1


#2
number = 1
for i in product('АДИН', repeat=5):
    s = ''.join(i)
    if s == 'ДИАНА':
        print(number, s)
    number += 1
    

#3
namber = 1
for i in product('EMNOY', repeat=5):
    if namber == 1055:
        print(i)
    namber += 1
    

#4
nember = 1
for i in product('CLMSU', repeat=5):
    if i[0] == 'S':
        print(nember)
        break
    nember += 1
    

#5
ntmber = 1
for i in product('АДИН', repeat=5):
    if i.count('А') == 0:
        print(ntmber)
        break
    ntmber += 1


#6
npmber = 1
for i in product('АЕКНРС', repeat=6):
    if i.count('А') <= 3 and i.count('Н') ==2:
        print(npmber)
        break
    npmber += 1


#7
nr = 1
for i in product('АИЛПС', repeat=5):
    if nr == 2791:
        print(i)
        break
    nr += 1


#8
cnt = 0
for i in product('LOST', repeat=7):
    if i.count('O') == 3:
        cnt += 1
print(cnt)


#9
cou = 0
for i in product('PLAN', repeat=6):
    if 0 < i.count('A') <= 4:
        cou += 1
print(cou)


#10       
couq = 0
for i in product('QWER123', repeat=5):
    if i.count('1') + i.count('2') + i.count('3') == 2:
        couq += 1
print(couq)


#11
""" sogl = 'БНДРЛ'
glas = 'АЕО'
coqqqq = 0
for i in product('БАНДЕРОЛЬ', repeat=7):
    if sum([i.count(letter) for letter in glas]) > sum([i.count(letter) for letter in sogl]):
        coqqqq += 1
print(coqqqq)
 """

#12
""" cccc = 0
for i in product('012345678', repeat=6)
    if (i.count('3') == 1) """
    

#13
cccc1 = 0
for i in product('01234567', repeat=5):
    sss = ''.join(i)
    if (i.count('5') == 2 and i[0] != 0\
        and '12' not in sss and '21' not in sss\
        and '32' not in sss and '23' not in sss\
        and '52' not in sss and '25' not in s\
        and '72' not in sss and '27' not in sss):\
        cccc1 += 1
print(cccc1)


#14
from itertools import *
#прототип на простой перебор
cwad = 0 # переменная счётчик
for i in product('КОРСЕТ', repeat=4): #цикл перебора вариантов 
    ss = ''.join(i) #строка для проверки условия
    if (i.count('О') <= 1 and i[0] != 'О' and i[-1] != 'О'\ #условие
        and 'ОР' not in ss and 'РО' not in ss):
            cwad += 1
print(cwad)



#15
#прототип с перебором только слов с уникальными буквами
cbnc = 0
for i in permutations('КАСПЕР', r=6): # именно это отличается
    cbnc += 1
print(cbnc)


#16
asfdg = 0
for i in permutations('QWERTYU', r=5):
    sds = ''.join(i)
    if i[0] != 'W' and 'QE' not in sds:
        asfdg += 1
print(asfdg)


#17
asfdgq = 0
for i in permutations('МАСЛО', r=5):
    sdsg = ''.join(i)
    if i[0] != 'С' and 'МО' not in sdsg:
        asfdgq += 1
print(asfdgq)

#18
cnttt = 0
for i in permutations('КАПРАЛ', r=6):
    sos = ''.join(i)
    if 'АА' not in sos:
        cnttt += 1
print(cnttt//2)
    

#19
#прототип с перебором только слов с уникальными буквами
cnttt2 = 0
for i in set(permutations('КАРЕТА', r=4)): #если упомянута "перестановка, то +set"
    sas = ''.join(i)
    if 'АА' not in sas:
        cnttt2 += 1
print(cnttt2)

#20
cnttt3 = 0
for i in permutations('012345678', r=5):
    if i[0] != '0' and (i.count('1') + i.count('3') + i.count('5') + i.count('7')) == 3:
        cnttt3 += 1
print(cnttt3)