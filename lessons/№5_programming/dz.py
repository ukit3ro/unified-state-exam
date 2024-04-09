""" 

#4
print(bin(20))

#6
for n in range(1, 1000):
    n2 = bin(n)[2:]
    if n2.count('1') % 2 == 0:
        n2 += '00'
    else:
        n2 += '11'
        
    R = int(n2, 2)
    if R > 115:
        print(n)
        break


#7
for n in range(1, 1000):
    n2 = bin(n)[2:]
    n2 += n2[:-1]
    if n2.count('1') % 2 == 0:
        n2 += '0'
    else:
        n2 += '1'
    if n2.count('1') % 2 == 0:
        n2 += '0'
    else:
        n2 += '1'
    R = int(n2, 2)
    if R > 80:
        print(R)
        break
    

#9
for n in range(10, 1000):
    n2 = bin(n)[2:]
    n2 += n2[1]
    if n2.count('1') % 2 == 0:
        n2 += '0'
    else:
        n2 += '1'
    if n2.count('1') % 2 == 0:
        n2 += '1'
    else:
        n2 += '0'
    R = int(n2, 2)
    if R > 160:
        print(n)
        break
    

#10
for n in range(1, 1000):
    n2 = bin(n)[2:]
    n2 += str(n2.count('1') % 2)
    n2 += str(n2.count('1') % 2)
    R = int(n2, 2)
    if R > 1096:
        print(f'Ответ к 10 номеру : {n}')
        break


#11
for n in range(1, 1000):
    n2 = bin(n)[2:]
    n2 += str(n2.count('1') % 2)
    n2 += str(n2.count('1') % 2)
    R = int(n2, 2)
    if R > 680:
        print(f'Ответ к 11 номеру : {R}')
        break


#12
a = []
for n in range(1, 1000):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 += n2[-1] + n2[-2]
    else:
        n2 = '1' + n2 + '0'
    R = int(n2, 2)
    if R > 1038:
        print(f'Ответ к 12 номеру {n}')
        break
    

#13
def R(n):
    n2 = bin(n)[2:]
    if n2.count('1') % 2 == 0:
        n2 += '10'
        n2 = '10' + n2[2:]
    else:
        n2 += '01'
        n2 = '11' + n2[2:]
    return int(n2, 2)
for n in range(1, 1000):
    if R(n) >= 102:
        print(n, 'dfdfdffd')
        break
    

#14
a = []
for n in range(20, 256):
    n2 = bin(n)[2:]
    if (int(n2[1]) + int(n2[4])) % 2 == 0:
        n2 = '1' + bin((int(n2[1]) + int(n2[4])))[2:]
    elif int(n2[1]) % 2 != 0:
        n2 += '1'
    else:
        pass
    R = int(n2, 2)
    if R % 2 != 0 and '5' in str(R):
        a.append(R)
print(len(a))
 """
 
#addition
#1
""" a = []
for n in range(1, 100):
    n2 = bin(n)[2:]
    if len(n2) % 2 == 0:
        n2 = n2[:len(n2)//2] + '1' + n2[len(n2)//2:]
    else:
        n3 = n2
         
    R = int(n3, 2)
    if R <= 68:
        print(n) """

#2
""" for n in range(1, 1000):
    n2 = bin(n)[2:]
    n2 = n2.replace('0', '2')
    for j in n2:
        if j == 1:
           n2 = n2.replace(j, '11', 1)
        if j == '2':
            n2 = n2.replace(j, '10', 1)
         
    R = int(n2, 2)
    if R < 777 and R % 2 == 0:
        print(R) """

#3
""" def R(n):
    n -= n % 8
    n2 = bin(n)[2:]
    n2 += str(n2.count('1') % 2)
    n2 += str(n2.count('1') % 2)
    
    return int(n2, 2)
for n in range(1, 1000):
    if R(n) < 86:
        print(bin(n)[2:]) """
        
#4
for n in range(1, 1000):
    n2 = bin(n)[2:]
    if n % 5 == 0:
        n2 += bin(int(str(n)[-3:]))[2:]
    else:
        n2 += bin((n % 5)*4)[2:]
    R = int(n2, 2)
    if R > 150:
        print(n)
        break
        
        
        

    