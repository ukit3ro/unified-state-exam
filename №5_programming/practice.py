


#7
print(bin(201)) # так как нужное нам число строго больше
 
#11
for n in range(1, 1000):
    n2 = bin(n)[2:]
    if n2.count('1') % 2 == 0:
        n2 += '0'
    else:
        n2 += '1'
    if n2.count('1') % 2 == 0:
        n2 += '0'
    else:
        n2 += '1'
    R = int(n2, 2)
    if R > 3123:
        print(n)
        break
    

#12
for n in range(1, 1000):
    n2 = bin(n)[2:]
    n2 += str(n2.count('1') % 2)
    n2 += str(n2.count('1') % 2)
    R = int(n2, 2)
    if R > 2222:
        print(R)
        break


#13
a = []
for n in range(1, 1000):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 += n2[0] + n2[1]
    else:
        n2 = '1' + n2 + '0'
    R = int(n2, 2)
    if R > 410:
        a.append(R)
print(min(a))


#14
b = []
for n in range(1, 1000):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 = '1' + n2 + '10'
    else:
        n2 = '11' + n2 + '0'
    R = int(n2, 2)
    if R > 260:
        b.append(R)
print(min(b))


#15
c = []
for n in range(1, 1000):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 += bin(n2.count('1'))[2:]
    else:
        n2 = '1' + n2 + '00'
    R = int(n2, 2)
    if R > 432:
        print(n)
        break     


#16
def R(n):
    n2 = bin(n)[2:]
    if n2.count('1') % 2 == 0:
        n2 += '0'
        n2 = '10' + n2[2:]
    else:
        n2 += '1'
        n2 = '11' + n2[2:]
    return int(n2, 2)
for n in range(1, 1000):
    if R(n) >= 256:
        print(n)



