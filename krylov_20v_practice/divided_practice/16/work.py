
#1
""" import sys
sys.setrecursionlimit(3000)
def F(n):
    if n == 1:
        return 5
    if n > 1:
        return 2 * n + 1 + F(n - 1)
print(F(2024) - F(2022)) """

#2
""" import sys
sys.setrecursionlimit(3000)
def F(n):
    if n == 1:
        return 3
    if n > 1:
        return 3 * n + 2 * F(n - 1)
print(F(2024) - 4 * F(2022)) """

#3
""" a = [1] * 3000
for i in range(100):
    if i == 1:
        a[i] = 1
    elif i == 2:
        a[i] == 2
    else:
        a[i] = i * (i - 1) + a[i - 1] + a[i - 2]
print(a[2024] - a[2022] - 2 * a[2021] - a[2020]) """
     
     
#4
""" import sys
sys.setrecursionlimit(3000)
def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return n * (n - 1) + F(n - 1) - F(n - 2)
print(F(2024) + F(2020) - F(2019)) """

#5
""" def F(n):
    if n < 3:
        return n
    if n > 2 and n % 2 == 0:
        return 2 * (n - 1) + F(n - 1) + 2
    if n > 2 and n % 2 != 0:
        return 2 * (n + 1) + F(n - 2) - 5
print(F(32)) """

#7
""" a = [1] * 40
for i in range(40):
    if i < 3:
        a[i] = 1
    if i > 2 and i % 2 != 0:
        a[i] = a[i - 1] + a[i - 2]
    if i > 2 and i % 2 == 0:
        a[i] = sum(a[1:i])
print(a[24]) """

#10
""" import sys
sys.setrecursionlimit(10000)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n**2 + F(n - 1)
print(F(2023) - F(2019))
 """
 
 
#11
def F(n):
    if n <= 1:
        return 1
    if n > 1 and n % 2 != 0:
        return 3 + F(n - 1) * F(n - 2) - F(n - 1) - F(n - 2)
    if n > 1 and n % 2 == 0:
        return 2 * F(n - 1)
print(F(12))
