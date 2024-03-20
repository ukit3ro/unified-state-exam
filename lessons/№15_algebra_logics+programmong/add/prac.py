

#14 
""" def trg(n, m, k):
    return (n + m + k) - max(n, m, k) > max(n, m, k)

for A in range(1,1000):
    for x in range(1, 1000):
        if (not((trg(x, 10, 17) == ((not(max(x, 8) > 18))))and trg(x, A, 4))) == False:
            break
    else:
        print(A) """
        
#15
""" def trg(n, m, k):
    a = sorted([n, m, k])
    return (a[0] + a[1]) > a[2]

for A in range(1, 1000):
    for x in range(1, 1000):
        if (not((trg(x, 5, 24) == (not(max(x, 8) > 31))) and trg(x, A, 8))) == False:
            break
    else:
        print(A) """
        
#16
""" def angle(a, b, c):
    return (a + b + c) == 180 """

        