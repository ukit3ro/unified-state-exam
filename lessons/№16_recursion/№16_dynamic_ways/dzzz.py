
#1
""" f = [0]*1000
for n in range(1000):
    if n < 3:
        f[n] = 1
    if n > 3:
        f[n] = f[n - 2] * (n // 3)
print(f[16]) """

#2
""" from math import factorial
f = [0]*10000
for n in range(1, 10000):
    if n >= 5000:
        f[n] = factorial(n)
    else:
        f[n] = f[n + 1] // (n + 1)
print(f[12] / f[4]) """

#3
""" f = [0] * 10000
for n in range(10000):
    if (n < 4 and n % 2 != 0):
        f[n] == 1
    if (n > 3 and n % 2 == 0):
        f[n] = f[n - 1] + f[n - 2] + f[n - 3]
print(f[4008] - f[4002]) """


