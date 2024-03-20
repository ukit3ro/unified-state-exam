#1
""" cnt = 0
for s in open('1.txt'):
    a = list(map(int, s.split()))
    povt = []
    nepovt = []
    
    for n in a:
        if a.count(n) == 3:
            povt.append(n)
        if a.count(n) == 1:
            nepovt.append(n)
    povt = set(povt)
    if ((len(povt) == 2 and len(nepovt) == 2) and (max(a) not in povt)):
        cnt += 1
print(cnt) """

#2
""" cnt = 0
for s in open('2.txt'):
    a = list(map(int, s.split()))
    povt = []
    nepovt = []
    
    for n in a:
        if a.count(n) == 2:
            povt.append(n)
        if a.count(n) == 1:
            nepovt.append(n)
    povt = set(povt)
    if ((len(povt) == 3 and len(nepovt) == 2) and (min(a) not in povt)):
        cnt += 1
print(cnt) """

#3
""" cnt = 0
for s in open('3.txt'):
    a = list(map(int, s.split()))
    povt = []
    povt2 = [1, 2, 3]
    nepovt = []
    [1, 1, 0, 3, 4]
    for n in a:
        if a.count(n) == 3:
            povt.append(n)
        if a.count(n) == 2:
            povt2.append(n)
        if a.count(n) == 1:
            nepovt.append(n)
    if ((len(set(povt)) == 1 and len(set(povt2)) == 1 and len(nepovt) == 3) and\
        ((sum(nepovt) / 3) <= povt[0])):
        cnt += 1
print(cnt)
 """
#4
""" cnt = 0
for s in open('4.txt'):
    a = list(map(int, s.split()))
    povt = []
    povt2 = []
    nepovt = []
    
    for n in a:
        if a.count(n) == 4:
            povt.append(n)
        if a.count(n) == 2:
            povt2.append(n)
        if a.count(n) == 1:
            nepovt.append(n)
    if ((len(set(povt)) == 1 and len(set(povt2)) == 1 and len(nepovt) == 2) and\
        ((sum(nepovt) / 2) >= max(povt[0], povt2[0]))):
        cnt += 1
print(cnt) """

#5
""" f = open('5.txt')
cnt = 0

for s in f:
    a = list(map(int, s.split()))
    if ((max(a) * 2 < (sum(a) - max(a))) and ((a[0] + a[1] == a[2] + a[3]) or\
        (a[0] + a[3] == a[1] + a[2]))):
            cnt += 1
print(cnt) """

#6
""" f = open('6.txt')
cnt = 0
for s in f:
    a = list(map(int, s.split()))
    if ((min(a) * 5 < (sum(a) - min(a))) and ((a[0] * a[1] == a[2] * a[3]) or\
        (a[0] * a[3] == a[1] * a[2]))):
            cnt += 1
print(cnt) """

#7
""" f = open('5.txt')
cnt = 0
for s in f:
    a = list(map(int, s.split()))
    a.sort()
    if ((max(a)**2 > (a[0] * a[1] * a[2] * a[3]) // max(a)) and\
    (a[3] - a[2] == a[2] - a[1] == a[1] - a[0])):
        cnt += 1
print(cnt) """



#8
""" f = open('5.txt')
cnt = 0
for s in f:
    a = list(map(int, s.split()))
    achet = [i for i in a if i % 2 == 0]
    if (min(a)**2 > (sum(a) - min(a))) and len(achet) == 0:
        cnt += 1
print(cnt) """

#9
""" f = open('9.txt')
nuzh = []
nuzh2 = [] 
for s in f:
    s = s.replace(',', '.')
    a = list(map(float, s.split()))            
    for i in a:
        if i >= 2.0 and i <= 17.0:
            nuzh.append(i)
    for n in a:
        if n > 12.0 and n <= 17:
            nuzh2.append(n)
print((len(nuzh2) / len(nuzh))*100) """


#10
""" f = open('10.txt')
nuzh = []
nuzh2 = [] 
for s in f:
    s = s.replace(',', '.')
    a = list(map(float, s.split()))            
    for i in a:
        if i >= 6.0 and i <= 14.0:
            nuzh.append(i)
    for n in a:
        if n > 9.0 and n <= 14.0:
            nuzh2.append(n)
print((len(nuzh2) / len(nuzh))*100) """

#11
""" minimum = []
nuzh = []
for s in open('9.txt'):
    s = s.replace(',', '.')
    a = list(map(float, s.split()))
    minimum.append(min(a))


print(set(nuzh)) """
