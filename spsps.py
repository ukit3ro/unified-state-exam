
#1
# for n in range(1, 1000):
#     n2 = bin(n)[2:]
#     if n2.count('1') % 2 == 0:
#         n2 += '0'
#     else:
#         n2 += '1'
#     if n2.count('1') % 2 == 0:
#         n2 += '0'
#     else:
#         n2 += '1'
    
#     R = int(n2, 2)
#     if R > 3123:
#         print(n)
#         break

#2
# a = []
# for n in range(1, 1000):
#     n2 = bin(n)[2:]
#     if n % 2 == 0:
#         n2 += n2[0] + n2[1]
#     else:
#         n2 = '1' + n2 +'0'
#     R = int(n2, 2)
#     if R > 410:
#         a.append(R)
# print(min(a))

#3
# def R(n):
#     n2 = bin(n)[2:]
    
#     if n2.count('1') % 2 == 0:
#         n2 += '0'
#         n2 = '10' + n2[2:]
#     else:
#         n2 += '1'
#         n2 = '11' + n2[2:]
#     return int(n2, 2)

# for n in range(1, 1000):
#     if R(n) >= 256:
#         print(n)
#         break


#4
# for i in range(10000, 1000, -1):
#     s = str(i)
#     k1 = int(s[0]) + int(s[1])
#     k2 = int(s[2]) + int(s[3])
    
#     first = str(min(k1, k2))
#     second = str(max(k1, k2))
#     s1 = first + second
    
#     if s1 == '117':
#         print(i)
#         break

#5
for i in range(10000, 1000, -1):
    s = str(i)
    k1 = int(s[0]) + int(s[1])
    k2 = int(s[1]) + int(s[2])
    k3 = int(s[2]) + int(s[3])
    first = str(k1 + k2 + k3 - max(k1, k2, k3) - min(k1, k2, k3))
    second = str(max(k1, k2, k3))
    s1 = first + second
    if s1 == '613':
        print(i)
        break

