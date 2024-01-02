#1
# def convert(num, base):
#     digits = '0123'
#     if num < base:
#         return digits[num]
#     else:
#         return convert(num // base, base) + digits[num % base]

# a = []
 
# for n in range(1, 1000):
#     n2 = convert(n, 4)
#     if n % 4 == 0:
#         n2 +=  n2[-2] + n2[-1]
#     else:
#         n2 += convert(((n % 4) * 2), 4)
    
#     R = int(n2, 4)
#     if R < 369:
#         print(n)
#2
# def convert(num, base):
#     digits = '0123456'
#     if num < base:
#         return digits[num]
#     else:
#         return convert(num // base, base) + digits[num % base]

# a = []
 
# for n in range(1, 1000):
#     n2 = convert(n, 4)
#     if n % 4 == 0:
#         n2 +=  n2[-2] + n2[-1]
#     else:
#         n2 += convert(((n % 4) * 2), 4)
    
#     R = int(n2, 4)
#     if R > 1025:
#         print(n)
#         break

# for n in range(1, 1000):
#     n2 = bin(n)[2:]   
#     n3 = n2.count('1')
#     if n3 % 2 == 0:
#         n2 = '11' + n2[2:]
#     else:
#         n2 = '10' + n2[2:]
        
#     R = int(n2, 2)
#     if R > 26:
#         print(n)
#         break
        



for n in range(1000, 100, -1):
    n2 = str(n)
    
    k1 = int(n2[0])**2 + int(n2[1])**2
    k2 = int(n2[1])**2 + int(n2[2])**2
    
    if k1 < k2:
        R = int(str(k2) + str(k1))
    else:
        R = int(str(k1) + str(k2))
    
    if R == 7434:
        print(n)
        break
    
    




