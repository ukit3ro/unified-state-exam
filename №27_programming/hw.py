
#1
# f = open('27-3-A_2021.txt')
# n = int(f.readline())
# a = []
# for s in f:
#     a.append(int(s))
    
# cnt = 0

# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if (a[i] + a[j]) % 6 == 0:
#             cnt += 1
# print(cnt)


#2
# f = open('27-3-A_2022.txt')
# n = int(f.readline())
# a = [int(s) for s in f]

# cnt = 0

# for i in range(n):
#     for j in range(i + 9, n):
#         if (a[i] * a[j]) % 15 == 0:
#             cnt += 1
# print(cnt)

#3
# f = open('27.1.A_2023.txt')
# k = int(f.readline())
# n = int(f.readline())
# a = [int(s) for s in f]
# pari = []

# for i in range(n):
#     for j in range(i + k, n):
#         pari.append(a[i] + a[j])
# print(max(pari))

#4
# f = open('27_1428Udh.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# troiki = []

# for i in range(n):
#     for j in range(i + 1, n):
#         for y in range(j + 1, n):
#             troiki.append(a[i]*a[j]*a[y])
# print(max(troiki))


#5
# f = open('27.1.A_BlQdp91.txt')
# n = int(f.readline())
# a = [int(s) for s in f]

# needed = []

# for i in range(n):
#     for j in range(i, n):
#         if sum(a[i:j+1]) % 51 == 0:
#             needed.append([sum(a[i:j+1]), (j + 1) - i])

# needed.sort(reverse=True)
# print(needed[:5])

#7
f = open('#6.txt')
n = int(f.readline())
a = [int(s) for s in f]

needed = []

def chet(a):
    cnt = 0
    for x in a:
        if x % 2 == 0:
            cnt += 1
    return cnt

for i in range(n):
    for j in range(i, n):
        if chet(a[i:j+1]) % 17 == 0:
            needed.append(sum(a[i:j+1]))
print(max(needed))

#7
# f = open('#7.txt')
# g = f.readline()
# #49
# n = 500
# k = 2
# a = [int(s) for s in f]

# needed = []

# for i in range(n):
#     for j in range(i, n):
#         for y in range(j, n):
#             if ((a[j]- a[i]) >= 2 and (a[y] - a[i]) >= 2 and (a[y] - a[j]) >= 2) and (a[i]+a[j]+a[y]) % 49 == 0:
#                 needed.append(a[i]*a[j]*a[y])
# print(min(needed))
                
        

        

