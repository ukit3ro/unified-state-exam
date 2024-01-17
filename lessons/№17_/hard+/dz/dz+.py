""" f = open('17.2.txt')
a = [int(s) for s in f]
chet = [x for x in a if x % 2 == 0]

midle_arythm = sum(chet) / len(chet)
sum_pari = []

for i in range(len(a) - 1):
    if ((a[i] % 9 == 0 and a[i+1] % 9 != 0) or (a[i] % 9 != 0 and a[i+1] % 9 == 0))and\
        (a[i] < midle_arythm or a[i+1] < midle_arythm):
            sum_pari.append(a[i] + a[i+1])"""
            
#1
""" f = open('1.txt')
a = [int(s) for s in f]
summa = []

for i in range(len(a) - 2):
    if (a[i] < 0 or a[i+1] < 0 or a[i+2] < 0):
        summa.append(a[i] + a[i+1] + a[i+2])

print(len(summa), min(summa)) """

#2
""" f = open('2.txt')
a = [int(s) for s in f]

norm = [x for x in a if x % 17 == 0]
midle_norm = sum(norm) / len(norm)

summa = []

for i in range(len(a) - 1):
    if (a[i] > midle_norm and a[i+1] > midle_norm) and (str(a[i])[-2:] == '33'\
        or str(a[i+1])[-2:] == '33'):
        summa.append(a[i] + a[i+1])
print(len(summa), max(summa)) """

#3
""" f = open('3.txt')
a = [int(s) for s in f]
summa = []

norm = [x for x in a if str(x)[-1] == '7']
mini = (min(norm))**2

for i in range(len(a) -1):
    if ((a[i] % 7 == 0 and a[i+1] % 7 != 0) or (a[i] % 7 != 0 and a[i+1] % 7 == 0))\
        and (str(a[i])[-1] == str(a[i+1])[-1]) and ((a[i]**2 + a[i+1]**2) < mini):
            summa.append(a[i]**2 + a[i+1]**2)

print(len(summa), max(summa))
 """

#4
""" f = open('4.txt')
a = [int(s) for s in f]
mini = min(a)
summa = []

for i in range(len(a) - 1):
    if (a[i] % 123 == mini or a[i+1] % 123 == mini):
        summa.append(a[i] + a[i+1])

print(len(summa), max(summa)) """

#5
""" f = open('5.txt')
a = [int(s) for s in f]
twodigit = [ x for x in a if 10 <= x <= 99]
summi = []

for i in range(len(a) - 1):
    if ((a[i] in twodigit and not(a[i+1] in twodigit)) or (a[i+1] in twodigit and not(a[i] in twodigit)))\
        and (a[i] + a[i+1]) % min(twodigit) == 0:
            summi.append(a[i] + a[i+1])
print(len(summi), max(summi)) """

#6
""" f = open('6.txt')
a = [int(s) for s in f]
zaza = [x for x in a if str(x)[-2:]  == '17']
zaza1 = max(zaza)
summi = []

for i in range(len(a) - 2):
    if (((len(str(a[i])) == 5) + (len(str(a[i+1])) == 5) + (len(str(a[i+2])) == 5)) == 2)\
        and ((a[i] + a[i+1] + a[i+2]) < zaza1):
            summi.append(a[i] + a[i+1] + a[i+2])
print(len(summi), max(summi)) """

#7

def convert(num, base):
     digits = '0123456789'
     if num < base:
         return digits[num]
     else:
         return convert(num // base, base) + digits[num % base]


f = open('7.txt')
a = [int(s) for s in f]

crat = [x for x in a if x % 5 == 0]
ggcrrat = []
for r in crat:
    ggcrrat.append(1 / r)
sumcrat = sum(ggcrrat)
garm_crat  = len(crat) / sumcrat
summi = []

for i in range(len(a) - 2):
    devet = convert((a[i] * a[i+1] * a[i+2]), 9)
    if (str(devet) == str(devet)[::-1]) and (3 / ((1 / a[i]) + (1 / a[i+1]) + (1 / a[i+2]))) < garm_crat:
        summi.append(a[i]*a[i+1]*a[i+2])

print(len(summi), min(summi))
 