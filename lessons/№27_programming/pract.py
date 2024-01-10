

#1
#файл A обычно содержит меньше чисел, но алгоритм нужно писать максимиально качественный
# f = open('27.1.A.txt') # открываем файл
# n = int(f.readline())
# a = []
# for s in f:
#     a.append(int(s))

# cnt = 0

# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         if (a[i] + a[j]) % 6  == 0:
#             cnt += 1
# print(cnt)

#2
# f = open('27.2.A.txt')
# n = int(f.readline())
# a = []

# for s in f:
#     a.append(int(s))
    
# xnt = 0
# for i in range(len(a)):
#     for j in range(i+9, len(a)):
#         if (a[i] * a[j]) % 15 == 0:
#             xnt += 1
# print(xnt)

#3
# f = open('27.3.A.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
  
# xnt = 0
# for i in range(len(a)):
#     for j in range(i + 9, len(a)):
#         if (a[i] + a[j]) % 24 == 0:
#             xnt += 1
# print(xnt)

#4
# f = open('27.4.A.txt')
# n = int(f.readline())
# a = [int(s) for s in f]

# pari = []   
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         pari.append(a[i] + a[j] + (j - i))
# print(max(pari))

#5
# f = open('27.5.A.txt')
# k = int(f.readline())
# n = int(f.readline())
# a = [int(s) for s in f]
# pari = []

# for i in range(len(a)):
#     for j in range(i + k, len(a)):
#         pari.append(a[i] + a[j])
# print(max(pari))

#6
# f = open('27.6.A.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# triki = []

# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         for y in range(j + 1, len(a)):
#             triki.append(a[i]*a[j]*a[y])
# print(max(triki))

#7
# f = open('27.7.A.txt')
# n = int(f.readline())
# a = [int(s) for s in f]

# needed = []

# for i in range(len(a)):
#     for j in range(i, len(a)):
#         if sum(a[i:j+1]) % 101 == 0:
#             needed.append([sum(a[i:j+1]), (j + 1) - i])
# needed.sort(reverse=True)
# print(needed[:5])

#8
f = open('27.7.A.txt')
n = int(f.readline())
a = [int(s) for s in f]

needed = []

def nechet(a):
    cnt = 0
    for x in a:
        if x % 2 != 0:
            cnt += 1
    return cnt



for i in range(len(a)):
    for j in range(i, len(a)):
        if nechet(a[i:j+1]) % 20 == 0:
            needed.append(sum(a[i:j+1]))
print(max(needed))




