from itertools import *
#1
cbnc = 0
for i in permutations('ВОЛЯ', r=4): # именно это отличается
    cbnc += 1
print(cbnc)

#2
cbnc1 = 0
for i in permutations('TOUGH', r=4):
    ss = ''.join(i)
    if 'U' != ss[0]:
        cbnc1 += 1
print(cbnc1)

#3
# cbnc2 = 0
# glas = 'аие'
# for i in permutations('ТАРКНИЩЕ', r=4):
#     ss = ''.join(i)
#     if ss[0] not in glas and ss[2] not in glas and ss[1] in glas and ss[3] in glas:
#         cbnc2 += 1
# print(cbnc2)

#4
import itertools
alphabet = "0123456789"
ar = itertools.permutations(alphabet, 6) #Размещение
arl = []
for e in ar:
    arl.append(list(e))
count = 0
for e in arl:
    flag = True
    for i in range(len(e)-1):
        if (e[0] == "0") or (int(e[i]) % 2 == 0 and int(e[i+1]) % 2 == 0) or (int(e[i]) % 2 != 0 and int(e[i+1]) % 2 != 0):
            flag = False
    if flag:
        count += 1
print(count)

#5
