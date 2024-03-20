
#1
""" a = []
for s in open('1.txt'):
    a.append(int(s))
summi = []
for i in range(len(a) - 1):
    if a[i] % 123 == min(a) or a[i+1] % 123 == min(a):
        summi.append(a[i] + a[i+1])
print(len(summi), max(summi)) """

#2
""" a = []
for s in open('2.txt'):
    a.append(int(s))
summi = []
g = []
for h in a:
    if h % 2 != 0:
        g.append(h)
g1 = sum(g) / len(g)
        
for i in range(len(a) - 1):
    if (a[i] > g1 and a[i+1] % 7 == 0 and a[i] % 7 !=0) or \
        (a[i+1] > g1 and a[i] % 7 == 0 and a[i+1] % 7 !=0):
        summi.append(a[i] + a[i+1])
print(len(summi), min(summi)) """

#3
""" a = []
for s in open('3.txt'):
    a.append(int(s))
summi = []
g = []
for h in a:
    if (str(h))[-1] == '6':
        g.append(h)
g1 = max(g)**2
        
for i in range(len(a) - 1):
    if ((str(a[i])[-1] == '6' and str(a[i+1])[-1] != '6' and\
        a[i]**2 + a[i+1]**2 < g1) or \
        (str(a[i+1])[-1] == '6' and str(a[i])[-1] != '6' and\
        a[i]**2 + a[i+1]**2 < g1)):
            summi.append(a[i]**2 + a[i+1]**2)
print(len(summi), max(summi)) """

#4
""" f = open("17.4.txt")
data = [int(x) for x in f]
res = []
max_13 = max([x for x in data if abs(x) % 100 == 13])
for i in range(len(data) - 2):
    if (int(len(str(abs(data[i]))) == 5) + int(len(str(abs(data[i + 1]))) == 5) + int(len(str(abs(data[i + 2]))) == 5)) == 2 and sum(data[i:i + 3]) <= max_13:
        res.append(data[i] + data[i + 1] + data[i + 2])
print(len(res), max(res)) """

#5
data = []
for s in open('5.txt'):
    data.append(int(s))
summi = []

        
for i in range(len(data) - 2):
    if (int(len(str(abs(data[i]))) == 5) + int(len(str(abs(data[i + 1]))) == 5)) <= 2 and sum(data[i:i + 3]) >= -85600:
        summi.append(data[i] + data[i + 1] + data[i + 2])

print(len(summi), max(summi))

