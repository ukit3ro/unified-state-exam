
#1
""" f = open('1.txt')
cnt = 0

for s in f:
    a = list(map(int, s.split()))
    
    if ((max(a) - min(a) > (sum(a) - min(a) - max(a)) - max(a))\
        and ((a[0] + a[1] == a[2] + a[3]) or (a[0] + a[2] == a[1] + a[3])\
            or (a[0] + a[3] == a[1] + a[2]))):
        cnt += 1
print(cnt) """

#2
""" count = 0
for s in open('2.txt'):
    M = sorted([int(x) for x in s.split()])
    if M[-1] ** 2 < (M[0] * M[1] * M[2]) or all(M[1] - M[0] == M[i+1] - M[i] for i in range(len(M)-1)):
        count += 1
print(count) """

#3
""" cnt = 0
for s in open('3.txt'):
    a = list(map(int, s.split()))
    povt = []
    nepovt = []
    
    for n in a:
        if a.count(n) == 2:
            povt.append(n)
        if a.count(n) == 1:
            nepovt.append(n)
    povt = set(povt)
    if (len(povt) == 2 and len(nepovt) == 4) and (min(a) in povt):
        cnt += 1
print(cnt) """

#11
""" cnt = 0
for s in open('11.txt'):
    a = sorted([int(x) for x in s.split()])
    
    if ((a[2] % 5 == 0 and a[2] % 6 != 0) and (1000 > (a[0] + a[-1])**2)):
        cnt += 1
print(cnt) """

#dopka

#9
""" cnt = 0
for s in open('9.txt'):
    a = [int(x) for x in s.split()]
    
    if ((a[0] + a[1] == a[2]) or (a[0] + a[2] == a[1])\
        or (a[1] + a[2] == a[0])):
        cnt += 1
print(cnt) """

#10
""" cnt = 0
for s in open('10.txt'):
    a = sorted([int(x) for x in s.split()])
    
    if ((a[0] % 2 != 0 and a[1] % 2 != 0 and a[2] % 2 != 0 and a[3] % 2 != 0)\
        and (a[0]**2 > sum(a) - a[0])):
        cnt += 1
print(cnt) """

#11
""" cnt = 0
for s in open('111.txt'):
    a = sorted([int(x) for x in s.split()])
    
    if (len(set(a)) == len(a) and ((a[0] + a[4])*3 >=\
        (a[1] + a[2] + a[3])*2)):
        cnt += 1
print(cnt) """

#12
""" cnt = 0
for s in open('12.txt'):
    a = sorted([int(x) for x in s.split()])
    nepovt = []
    povt = []
    for n in a:
        if a.count(n) == 2:
            povt.append(n)
        if a.count(n) == 1:
            nepovt.append(n)
    nepovt = sorted(nepovt)       
    if ((len(set(a))+1 == len(a)) and (nepovt[0] + nepovt[3] <=\
        povt[0] * 2)):
        cnt += 1
print(cnt) """

#13
""" cnt = 0
for s in open('13.txt'):
    a = sorted([int(x) for x in s.split()])
    nepovt = []
    povt = []
    for n in a:
        if a.count(n) == 2:
            povt.append(n)
        if a.count(n) == 1:
            nepovt.append(n)
    nepovt = sorted(nepovt)       
    if (len(povt) == 4 and len(nepovt) == 3):
        if (sum(povt)/len(povt))\
        <(sum(nepovt)/len(nepovt)):
            cnt += 1
print(cnt) """

#14
""" cnt = 0
for s in open('14.txt'):
    a = sorted([int(x) for x in s.split()])
    nepovt = []
    povt = []
    for n in a:
        if a.count(n) == 3:
            povt.append(n)
        if a.count(n) == 1:
            nepovt.append(n)
    nepovt = sorted(nepovt)
         
    if (len(povt) == 3 and len(nepovt) == 3):
        if (sum(povt) < nepovt[0] * nepovt[1] * nepovt[2]):
            cnt += 1
print(cnt) """

#15
""" cnt = 0
for s in open('15.txt'):
    a = sorted([int(x) for x in s.split()])
    nepovt = []
    povt = []
    for n in a:
        if a.count(n) == 2:
            povt.append(n)
        if a.count(n) == 1:
            nepovt.append(n)
    nepovt = sorted(nepovt)
         
    if (len(povt) == 4 and len(nepovt) == 4):
        if min(a) in povt:
            cnt += 1
print(cnt) """

#16
""" cnt = 0
for s in open('16.txt'):
    a = sorted([int(x) for x in s.split()])
    if a[0] * a[1] == a[2] * a[3] or a[0] * a[2] == a[1] * a[3]\
        or a[0] * a[3] == a[1] * a[2]:
            if max(a)**2 > max(a) * min(a):
                cnt += 1
print(cnt) """



