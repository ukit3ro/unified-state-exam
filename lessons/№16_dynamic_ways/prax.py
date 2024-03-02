

#2
""" f = [0]*10000
for n in range(10000):
    if n == 1:
        f[n] = 1
    if n > 1:
        f[n] = n * f[n - 1]
print(f[2023] / f[2021]) """

#3
""" f = [0]*10000
for n in range(10000):
    if n == 1:
        f[n] == 1
    if n > 1:
        f[n] = n**3 + f[n - 1]
print(f[2024] - f[2020]) """

#4
""" f = [0]*10000
for n in range(10000):
    if n == 1:
        f[n] = 1
    if n == 2:
        f[n] == 2
    if n > 2:
        f[n] = (n - 1) * (n - 2) + f[n - 1] + f[n - 2]
print(f[2021] - f[2019] - 2*f[2018] - f[2017]) """