
#1
""" f = open('1.txt')
cnt = 0

for s in f:
    a = list(map(int, s.split()))
    
    for x in a:
        if (a[x] + a[x+1] == a[x+2]) or (a[x+1] + a[x+2] == a[x]) or\
            (a[x] + a[x+2] == a[x+1]):
                cnt += 1
print(cnt) """

#2
""" f = open('2.txt')
cnt = 0
for s in f:
    a = list(map(int, s.split()))
    rept = []
    notrept = []
    for x in a:
        if a.count(x) == 1:
            notrept.append(x)
        else:
            rept.append(x)
    if len(rept) == 2 and (max(notrept) + min(notrept)) <= sum(rept):
        cnt +=1
print(cnt) """

#3
""" f = open('3.txt')
cnt = 0

for s in f:
    a = list(map(int, s.split()))
    rept = []
    notrept = []
    for x in a:
        if a.count(x) == 1:
            notrept.append(x)
        else:
            rept.append(x)
        
    if ((len(rept) >= 1) and (sum(notrept) % 2 != 0)):
        cnt += 1

print(cnt) """

#4
""" f = open('4.txt')
cnt = 0

for s in f:
    a = list(map(int, s.split()))
    rept = []
    notrept = []
    for x in a:
        if a.count(x) == 1:
            notrept.append(x)
        else:
            rept.append(x)
        
    if ((len(notrept) == 4) and (sum(rept) < sum(notrept))):
        cnt += 1
        print(rept, notrept)

print(cnt)
 """

#5
""" f = open('5.txt')
cnt = 0

for s in f:
    a = list(map(int, s.split()))
    rept = []
    notrept = []
    for x in a:
        if a.count(x) == 1:
            notrept.append(x)
        else:
            rept.append(x)
        
    if len(rept) != 0 and (sum(notrept) / len(notrept)) > (sum(rept) / len(rept)):
        cnt += 1
        print(rept, notrept)

print(cnt) """

#6
def isSquad(a):
   for i in range(5):
       if a[i] ** 2 in a and a[i] != 1:
           return True
   return False

def isIncreaseSequence(a):
   return a[0] < a[1] < a[2] or a[1] < a[2] < a[3] or a[2] < a[3] < a[4]

f = open('9_1.txt')
cnt = 0

for a in f:
   a = list(map(int, a.split()))
   if isSquad(a) and isIncreaseSequence(a):
       cnt += 1

print(cnt)