



#1
def F(n):
    if n < 2:
        return 1
    if n >= 2:
        return F(n-1) * (n+5)
        
print(F(9))


#2
def T(n):
    if n == 1:
        return 3
    if n > 1:
        return 4 * T(n-1) - 3 * n
print(T(5))


#3
def E(n):
    if n == 1:
        return 1
    if n % 2 == 0 and n > 1:
        return E(n-1) + 7
    if n % 2 != 0 and n > 1:
        return E(n-2) + 4 * n
print(E(100))


#4
import sys #здесь мы импортируем встроенную библиотеку sys, чтобы изменить изначальный максимум глубины рекурсии с помощью специального метода.
sys.setrecursionlimit(3000)
def J(n):
    if n ==1:
        return 1
    if n > 1:
        return n * J(n-1)
print(J(2023) / J(2021))


#6
def D(n):
    if n <= 4:
        return 0
    if n > 4 and n% 4 == 0:
        return D(n-1) + 3 * n
    if n > 4 and n % 4 > 0:
        return D(n - (n % 4)) + 8 * n - 2
print(D(43)) 


#7
def A(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 2 == 0 and n > 1:
        return 2 + (4 * A(n-2) / 3) // 1
    if n % 2 != 0 and n > 1:
        return 2 * n + ((A(n-1) + A(n-3) + 7) / 4) // 1
print(A(32))    


#8
def Q(n):
    if n == 2:
        return 1
    if n > 2:
        return 3 * Q(n - 1) + 4 * Q(n - 1) - n * 2 + 4
def D(n):
    if n == 2:
        return 1
    if n > 2:
        return 4 * D(n - 1) + 3 * D(n - 1) + 6
print(Q(8) + D(8)) 


#9
cnt = 0
def P(n):
    if n > 17:
        return n * n * n * n + 9
    if n % 2 == 0:
        return 2 * P(n + 3) + P(n + 2)
    if n % 2 != 0 and n <= 17:
        return P(n + 9) + P(n + 4) + n
for n in range(1, 251):
    if '4' not in str(P(n)):
        cnt += 1
print(cnt)


#10
def Y(n):
    if n <= 2:
        return n * n
    if n % 2 == 0 and n > 2:
        return n + 7 * Y(n-1)
    if n % 2 != 0 and n > 2:
        return 3 * n * n + Y(n-2)
caunt = 0
for n in range(1, 665):
    if Y(n) % 5 == 0:
        caunt += 1
print(caunt)   


#11
def K(n):
    if n <= 4:
        return 2
    if n % 2 == 0 and n > 4:
        return K( n / 6 - 2)
    if n % 2 != 0 and n > 4:
        return n * n * n * n  
for n in range(1, 1000):
    if K(n) > 783:
        print(n)
        break
    
    
#12    
    

