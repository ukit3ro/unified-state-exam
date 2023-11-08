""" #1
def F(n):
    if n < 3:
        return 1
    if n >= 3:
        return F(n-2) * (n + 3)
print(F(7))

#2
def G(n):
    if n == 1:
        return 4
    if n > 1:
        return 5 * G(n-1) - 2 * n
print(G(6))

#3
def H(n):
    if n == 1:
        return 1
    if n % 2 == 0 and n > 1:
        return H(n-1) + 3
    if n % 2 != 0 and n > 1:
        return H(n - 3) + 2 *n
print(H(50))

#4
import sys
sys.setrecursionlimit(3000)
def J(n):
    if n == 1:
        return 1
    if n > 1:
        return n *J(n - 1) + 1
print(J(2123) / J(2120))

#5
def L(n):
    if n == 1 or n == 0:
        return 5
    if n > 1 and n % 5 == 0:
        return L(n - 5) // 3 + 9
    if n > 1 and n % 5 > 0:
        return L(n - (n % 5)) + n * 2
print(L(42))

#6
def P(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n % 2 == 0 and n > 1:
        return 7 + (3 * P(n-2)/2)
    if n % 2 != 0 and n > 1:
        return 6 *n + (P(n-2) + P(n-1) + 8)/5
print(P(71))

#7
def Q(n):
    if n == 2:
        return 1
    if n > 2:
        return 4 * Q(n-1) + 2 * S(n-1) - n * 3 + 8
def S(n):
    if n == 2:
        return 1
    if n > 2:
        return 3 * Q(n-1) + 3 * S(n-1) + n
print(Q(16) + S(16)) """

""" #8
cnt = 0
def Z(n):
    if n <= 19:
        return n * n * n + 22
    if n % 3 == 0 and n > 19:
        return Z(n-4) + Z(n-8)
    if n % 3 != 0 and n > 19:
        return Z(n-9) + n + 7
for n in range(1, 101):
    if '1' or '3' or '5' or '7' or '9' not in str(Z(n)):
        cnt += 1
print(cnt) """

#9
def R(n):
    if n <= 3:
        return 1
    if n % 2 == 0 and n > 3:
        return R(n/5 - 3)
    if n > 3 and n % 2 != 0:
        return n * n * n
for n in range( 1000):
    if R(n) > 559:
        print('sfsfdsf', n)
        break