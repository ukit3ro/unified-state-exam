
#1
""" f = open('9.9.txt')
cnt = 0
for s in f:
    a = list(map(int, s.split()))
    a.sort()
    
    
    if (a[0] + a[1] == a[2]):
        cnt += 1
print(cnt) """

#2
""" f = open('9.10.txt')
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
""" f = open('9.11.txt')
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
    
    if len(rept) != 0 and sum(notrept) % 2 == 0:
        cnt += 1
print(cnt) """

#4
""" f = open('9.12.txt')
cnt = 0
for s in f:
    a = list(map(int, s.split()))
    if len(set(a)) == 5:
        chet = []
        notchet = []
        for x in a:
            if x % 2 == 0:
                chet.append(x)
            else:
                notchet.append(x)
        if len(chet) > len(notchet) and sum(chet) > sum(notchet):
            cnt += 1
            
print(cnt) """

#5
""" f = open('9.13.txt')
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
        
    if len(set(a)) == 5 and sum(rept) > sum(notrept):
        cnt += 1
print(cnt) """

#6
""" f = open('9.14.txt')
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
print(cnt) """

#7
f = open('9.15.txt')
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
    
    if len(rept) == 4 and rept.count(rept[0]) == 2 and (sum(rept) / len(rept)) < (sum(notrept) / len(notrept)):
        cnt += 1
print(cnt) 
