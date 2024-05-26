#2
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((not (x <= y)) or ((not w) <= (not z)) or w) == False:
#                     print(x, y, z, w)   #xyzw
                    
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
#     if R > 1025:
#         print(n)
#         break #66

#6
# from turtle import *
# tracer(0)
# penup()
# left(90)
# k = 20

# for i in range(3):
#     pendown()
#     for j in range(2):
#         forward(10*k)
#         right(90)
#         forward(10*k)
#         right(90)
#     penup()
#     forward(5*k)
#     right(90)
#     forward(5*k)
#     left(90)

# for x in range(-40, 40):
#     for y in range(-40, 40):
#         goto(x*k, y*k)
#         dot(4)
# done() #80

#8
# from itertools import product
# words = []
# cnt = 0
# for i in product(sorted('ФЛАМИНГО'), repeat = 5):
#     cnt +=1
#     s = ''.join(i)
#     if s[0] != 'Н' and s.count('О') <= 1 and cnt % 2 != 0:
#         words.append(s)
# print(len(words)) #11907

#10 25

#12
# for n in range(3, 10001):
#     s = '4' + '1' * n
#     while '31' in s or '411' in s or '1111' in s:
#         if '31' in s:
#             s = s.replace('31', '1', 1)
#         if '411' in s:
#             s = s.replace('411', '13', 1)
#         if '1111' in s:
#             s = s.replace('1111', '4', 1)
#     if s.count('4')*4 + s.count('1') == 36:
#         print(n)
#         break #1507

#14
# for x in '0123456789ABCDEFGHIJKLMNO':
#     if (int('1' + x + '2' + x + '3' + x + '4' + x + '5', 25) + int('2' + x + '024', 25) + int('1' + x + '099', 25)) % 24 == 0:
#         print((int('1' + x + '2' + x + '3' + x + '4' + x + '5', 25) + int('2' + x + '024', 25) + int('1' + x + '099', 25)) // 24)
#11727433732

#15
# def func(x, y, A):
#     return ((x < 4) or ( x >= 20) or (y >= 3 * x + A) or (y < 100))
# s = []
# for A in range(-1000, 1000):
#     flag = True
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if func(x, y, A) == False:
#                 flag = False
#                 break
#         if flag == False:
#             break
#     if flag == True:
#         s.append(A)
# print(max(s)) #43

#16
""" import sys
sys.setrecursionlimit(3000)
def F(n):
     if n == 1:
         return 1
     if n == 2:
        return 2
     if n > 2:
         return n * (n - 1) + F(n - 1) + F(n - 2) 
print(F(2024) - F(2022) - 2 * F(2021) - F(2020)) """
            
#17
# f = open('17var03.txt')
# a = []
# for s in f:
#     a.append(int(s))
# #17590
# summi = []
# for i in range(len(a) -2):
#     if (10000 >a[i] >= 1000 or 10000 >a[i+1] >= 1000 or 10000 > a[i+2] >= 1000 )\
#         and (a[i] + a[i+1] + a[i+2]) > 17590:
#         summi.append(a[i] + a[i+1] + a[i+2])
# print(len(summi), min(summi))
#575 18038

#23
# def task1(s, e):
#     if s > e or s == 6 or s == 17:
#         return 0
#     if s == e:
#         return 1
#     if s < e:
#         return task1(s + 2, e) + task1(s + 3, e) + task1(s * 5, e)
# print(task1(1, 31)) #961

#25
# import fnmatch
# for x in range(119803, 10**8+1):
#     if fnmatch.fnmatch(str(x), r'?19*8?3'):
#         if x % 5171 == 0:
#             print(x, x // 5171)
# '11908813 2303
# 71995833 13923
# 81975863 15853
# 91955893 17783'    

#27    

#5
for n in range(1, 1000):
    n = n - (n % 4)
    n2 = bin(n)[2:]
    
    n2 += str(n2.count('1') % 2)
    n2 += str(n2.count('1') % 2)
    R = int(n2, 2)
    if R > 56:
        print(R)
        break
