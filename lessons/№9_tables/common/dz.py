
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
cnt = 0
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
print(cnt)

#11
""" cnt = 0
for s in open('11.txt'):
    a = sorted([int(x) for x in s.split()])
    
    if ((a[2] % 5 == 0 and a[2] % 6 != 0) and (1000 > (a[0] + a[-1])**2)):
        cnt += 1
print(cnt) """
