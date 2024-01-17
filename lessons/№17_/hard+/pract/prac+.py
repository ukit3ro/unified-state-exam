

#2
""" f = open('17.2.txt')
a = [int(s) for s in f]
chet = [x for x in a if x % 2 == 0]

midle_arythm = sum(chet) / len(chet)
sum_pari = []

for i in range(len(a) - 1):
    if ((a[i] % 9 == 0 and a[i+1] % 9 != 0) or (a[i] % 9 != 0 and a[i+1] % 9 == 0))and\
        (a[i] < midle_arythm or a[i+1] < midle_arythm):
            sum_pari.append(a[i] + a[i+1])

print(len(sum_pari), max(sum_pari)) """

#3
""" f = open('17.3.txt')
a = [int(s) for s in f]
a6 = [x for x in a if str(x)[-1] == '6']
max6 = max(a6)
sum_pari = []

for i in range(len(a) - 1):
    if (((str(a[i])[-1] == '6' and str(a[i+1])[-1] != '6')) or\
        (str(a[i])[-1] != '6' and str(a[i+1])[-1] == '6')) and\
            (a[i]**2 + a[i+1]**2 < max6**2):
                sum_pari.append(a[i]**2 + a[i+1]**2)
print(len(sum_pari), max(sum_pari)) """

#4
""" f = open('17.4.txt')
a = [int(s) for s in f]
sum_pari = []
min13 = min([x for x in a if x % 13 == 0])

for i in range(len(a) - 1):
    if a[i] % min13 == 0 and a[i+1] % min13 == 0:
        sum_pari.append(a[i] + a[i+1])

print(len(sum_pari), max(sum_pari)) """

#5
""" f = open('17.5.txt')
a = [int(s) for s in f]
sum_pari = []

for i in range(len(a) - 1):
    if a[i] % 117 == min(a) or a[i+1] % 117 == min(a):
        sum_pari.append(a[i] + a[i+1])

print(len(sum_pari), max(sum_pari)) """

#6
""" f = open('17.6.txt')
a = [int(s) for s in f]
sum_pari = []

for i in range(len(a) - 1):
    if (((len(str(a[i])) == 2) + (len(str(a[i+1])) == 2)) == 1 and\
        (a[i] + a[i+1]) % 10 == 0):
            sum_pari.append(a[i] + a[i+1])

print(len(sum_pari), max(sum_pari))    """    

from random import *
for i in range(3):
    print(randint(1,11))

