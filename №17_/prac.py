#7
""" f = open('17.1.txt')
a = []
for s in f:
    a.append(int(s))
summa = []
for i in range(0, len(a)-1):
    if a[i] % 11 == 0 and a[i+1] % 11 == 0:
        summa.append(a[i] + a[i+1])
print(len(summa), min(summa))
 """

#8
""" f1 = open('17.2.txt')
a = []
for s in f:
    a.append(int(s))
summi = []
for i in range(len(a)):
    if a[i] > 1234 or a[i+1] > 1234:
        summi.append(a[i]**2 + a[i+1]**2)
print(len(summi), max(summi)) """


#9
""" f2 = open('17.3.txt')
a = []
for s in f2:
    a.append(int(s))
summi = []
for i in range(len(a) - 1):
    if  (a[i] * a[i+1]) % 74 == 0:
        summi.append(a[i] + a[i+1])
print(len(summi), max(summi)) """


#10
f3 = open('17.4.txt')
a = []
for s in f3:
    a.append(int(s))
summi = []
for i in range(len(a) - 1):
    if str(a[i])[-1] == str(a[i+1])[-1] and str(a[i+1])[-1] in '13579':
        summi.append(a[i] + a[i+1])
print(len(summi), max(summi))


#11
""" f4 = open('17.5.txt')
a = []
for s in f4:
    a.append(int(s))
summi = []
for i in range(len(a) - 1):
    if a[i] > 0 and a[i]**(1/3) """