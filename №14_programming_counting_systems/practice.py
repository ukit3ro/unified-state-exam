
#1
s = 32**7 + 8**5 + 16
print(bin(s)[2:].count('1'))


#2
s = 512*11 +  64**6 - 8
print(oct(s)[2:])

#3
s = 11**2222 + 7**1111 - 3**777
print(bin(s)[2:].count('1'))


#4
s = 512**125 + 128**625 - 32**125
print(bin(s)[2:].count('0'))


#5
s = 256**123 + 64**12 - 16
cnt2 = 0
while s > 0:
    if s % 4 == 3:
        cnt2 += 1
    s = s // 4
print(cnt2)

#6
s = 200**3333 - 100**2222 + 50**1111 - 11
cnt2 = 0
while s > 0:
    if s % 3 == 2:
        cnt2 += 1
    s = s // 3
print(cnt2)


#7
s = 64**2023 + 32**2022 - 8**2021 - 2
print(set(hex(s)[2:]))


#8
s = 64*2023 + 32*2022 * 8**2021 - 2
nemvewr = []
while s > 0:
    nemvewr.append(s % 20)
    s = s // 20
print(len(set(nemvewr)))


#9
for n in range(3, 10):
    if int('121', n+1) == int('121', n) + int('13', 16):
        print(n)


#10
for x in range(2, 20):
    if int('111', x) + int('13', 5) == int('515', 6):
        print(x)
        

#12
for x in '0123456789ABCDEFGH':
    if (int('2671' + x, 18) + int('8513' + x, 18)) % 13 == 0:
        print((int('2671' + x, 18) + int('8513' + x, 18)) // 13)


#13
for x in '0123456789ABCDEF':
    if (int('d79' + x + '1', 16) + int('48a3' + x, 16)) % 14 == 0:
        print((int('d49' + x + '1', 16) + int('48a3' + x, 16)) // 14)
        

#14
for x in range(0, 37):
    if ((6*37**3 + 5*37**2 + 4*37**1 + x*37**0) + (5*37**3 + x*37**2 + 4*37**1 + 7*37**0)) % 79 == 0:
        print(((6*37**3 + 5*37**2 + 4*37**1 + x*37**0) + (5*37**3 + x*37**2 + 4*37**1 + 7*37**0)) // 79)
        

#15
for x in '0123456789ABCDEFGHIJ':
    for y in '0123456789ABCDEFGHIJ':
        if (int(f'b{y}11cb{x}g17', 20) + int(f'8a{x}17', 20)) % 107 == 0:
            print(x, y, (int(f'b{y}11cb{x}g17', 20) + int(f'8a{x}17', 20)) // 107)


#16
for p in range(10, 36):
    for x in range(0, p):
        for y in range(0, p):
            if ((1*p**3 + 7*p**2 + x*p**1 + 8*p**0) + (y*p**3 + x*p**2 + y*p**1 + 6*p**0)) == (9*p**3 + y*p**2 + y*p**1 + 0*p**0):
                print(x*p**2 + x*p**1 + y*p**0)        
    

#17

