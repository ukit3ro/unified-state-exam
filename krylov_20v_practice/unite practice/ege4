#2
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((not(w <= x)) or ((not z) <= (not y)) or z) == 0:
#                     print(x, y, z, w)

#5
# def convert(num, base):
#     digits = '0123'
#     if num < base:
#         return digits[num]
#     else:
#         return convert( num // base, base) + digits[num % base]

# for n in range(1, 1000):
#     n2 = convert(n, 4)
#     if n % 4 == 0:
#         n2 += n2[-2] + n2[-1]
#     else:
#         n2 += convert(((n % 4) * 2), 4)
    
#     R = int(n2, 4)
#     if R >= 1088:
#         print(n)
#         break

#6
# from turtle import *
# tracer(0)
# k = 10
# penup()
# left(90)

# for i in range(3):
#     pendown()
#     for j in range(2):
#         forward(10*k)
#         right(90)
#         forward(10*k)
#         right(90)
#     penup()
#     forward(10*k)
#     right(90)
#     forward(5*k)
#     left(90)

# for x in range(-30, 30):
#     for y in range(-30, 40):
#         goto(x*k, y*k)
#         dot(4)

# done()

#8
# from itertools import product
# words = []
# cnt = 0
# for i in product(sorted('ИНТЕГРАЛ'), repeat = 5):
#     cnt +=1
#     s = ''.join(i)
#     if s[0] != 'Т' and (s.count('Н') == 1 or s.count('Н') ==2) and cnt % 2 != 0:
#         words.append(s)
# print(len(words))

#12
# def F(n):
#     s = '4' + '1' * n
#     while '31' in s or '411' in s or '1111' in s:
#         if '31' in s:
#             s = s.replace('31', '1', 1)
#         if '411' in s:
#             s = s.replace('411', '13', 1)
#         if '1111' in s:
#             s = s.replace('1111', '4', 1)
#     summ = s.count('4') * 4 + s.count('1')
#     if summ == 34:
#         return 1
# print(F(1315))

#14
# for x in '0123456789ABCDEFGHI':
#     if (int('3' + x + '2' + x + '1' + x + '0' + x + '1', 19) + int(x + '2024', 19) + int('1' + x + '077', 19)) % 18 == 0:
#         print((int('3' + x + '2' + x + '1' + x + '0' + x + '1', 19) + int(x + '2024', 19) + int('1' + x + '077', 19)) // 18)

#15
# def frac(x, y, A):
#     return ((x >=20) or (y >= 40) or (y <= x + A) or (y >= 3 * x - A))

# s = []
# for A in range(-1000, 1000):
#     flag = True
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if frac(x, y, A) == 0:
#                 flag = False
#                 break
#         if flag == False:
#             break
#     if flag:
#         print(A)
#         break

#16
# import sys
# sys.setrecursionlimit(3000)
# def F(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n > 2:
#         return n * (n - 1) + F(n - 1) - F(n - 2)
# print(F(2024) + F(2020) - F(2019))

#17
# f = open('17var04.txt')
# a = []
# for s in f:
#     a.append(int(s))
# summi = []

# for i in range(len(a) - 2):
#     cnt = 0
#     if a[i] > 0:
#         if len(str(a[i])) == 5:
#             cnt += 1
#     elif a[i] < 0:
#         if len(str(a[i])) == 6:
#             cnt += 1
#     if a[i+1] > 0:
#         if len(str(a[i+1])) == 5:
#             cnt += 1
#     elif a[i+1] < 0:
#         if len(str(a[i+1])) == 6:
#             cnt += 1
#     if a[i+2] > 0:
#         if len(str(a[i+2])) == 5:
#             cnt += 1
#     elif a[i+2] < 0:
#         if len(str(a[i+2])) == 6:
#             cnt += 1
#     if (cnt <= 2 and (a[i] + a[i+1] + a[i+2]) > -700):
#         summi.append(a[i] + a[i+1] + a[i+2])
# print(len(summi), min(summi))

#23
# def task1(s, e):
#     if s > e or s == 21:
#         return 0
#     if s == e:
#         return 1
#     if s < e:
#         return task1(s + 2, e) + task1(s + 3, e) + task1(s * 5, e)
    
# print(task1(1,6)*task1(6,35))

#25
import fnmatch
for x in range(179083, 10**8+1):
    if fnmatch.fnmatch(str(x), r'?79?8*3'):
        if x % 3377 == 0:
            print(x, x // 3377)