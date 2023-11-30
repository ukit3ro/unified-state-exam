#1
# файл dz1
""" f = open('dz1.txt')
a = []
for s in f:
    a.append(int(s))
    
summi = []
for i in range(len(a)-1):
    if str(a)[i] in '02468' and str(a)[i+1]:
        summi.append(a[i] + a[i+1])
print(len(summi), max(summi)) """

'1496 19039'

""" f = open('17.66.txt')
a = []
for s in f:
    a.append(int(s))
    
summi = []
for i in range(len(a)-1):
    if a[i] > 850 or a[i+1] > 850:
        summi.append(a[i]**2 + a[i+1]**2)
print(len(summi), max(summi)) """
'3166196682525'


""" f = open('17.33.txt')
a = []
for s in f:
    a.append(int(s))
    
summi = []
for i in range(len(a)-1):
    if (a[i] * a[i+1]) % 2 != 0:
        summi.append(a[i] + a[i+1])
print(len(summi), max(summi)) """
'1214 19732'


""" f = open('17.44.txt')
a = []
for s in f:
    a.append(int(s))
    
summi = []
for i in range(len(a) - 1):
    if str(a[i])[-1] == str(a[i+1])[-1] and str(a[i+1])[-1] in '02468':
        summi.append(abs(a[i]) * abs(a[i+1]))
print(len(summi), max(summi)) """
'23387665200'

""" f = open('17.11.txt')
a = []
for s in f:
    a.append(int(s))
summi = []
for i in range(len(a) - 1):
    if a[i] >=0 and a[i]**0.5 == int(a[i]**0.5) or a[i+1] >= 0 and a[i+1]**0.5 == int(a[i+1]**0.5):
        summi.append(a[i] + a[i+1])
print(len(summi), min(summi)) """


import math
f = open('17.77.txt')
a = []
for s in f:
    a.append(int(s))
summi = []
for i in range(len(a) -2):
    if a[i] % 8 == 0 or a[i+1] % 8 == 0 or a[i+2] % 8 == 0 and \
        math.gcd(a[i], a[i+1]) > 5 or math.gcd(a[i+2], a[i+1]) > 5 or math.gcd(a[i], a[i+2]) > 5:
        summi.append(a[i] + a[i+1] + a[i+2])
print(len(summi), max(summi))
'376 27915'
