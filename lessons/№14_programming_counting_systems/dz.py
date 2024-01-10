#1
s = 64**13 + 32**6 - 16**2
cnt = 0
while s > 0:
    if s % 2 == 1:
        cnt += 1
    s = s // 2
print(cnt)

#2
d = 4096**3125 - 512**625 + 64**125 - 8**25
print(oct(d)[2:].count('7'))

#3
f = 32**540 + 16**231 - 2**10
print(bin(f)[2:].count('1'))

#4
g = 512**230 + 256**64 - 32**23
print(bin(g)[2:].count('0'))

#5
cnt2 = 0
h = 625**134 * 125**32 + 25**52 - 5
while h > 0:
    if h % 5 == 4:
        cnt2 += 1
    h = h // 5
print(cnt2)

#6
j = 343**21 + 49**14 + 7
cnt3 = 0
while j > 0:
    if j % 7 == 0:
        cnt3 += 1
    j = j //7
print(cnt3)

#7
k = 7777**290 - 777**29 + 77**2 - 7
nemvewr = []
while k > 0:
    nemvewr.append(k % 20)
    k = k // 20
print(len(set(nemvewr)))

#8
for n in range(4, 20):
    if int('132', n+1) == int('132', n) + int('34', 8):
        print(n)

#9
for x in range(7, 20):
    if int('416', 7) == int('18', 9) + int('165', x):
        print(x)
        
#10
for x in '0123456789ABCDEFGH':
    if (int('ab5' + x + '3', 18) + int('ef' + x + '13', 18)) % 17 == 0:
        print((int('ab5' + x + '3', 18) + int('ef' + x + '13', 18)) // 17)

#11
for x in '0123456789ABCDEFGHIJ':
    if (int('13' + x + 'CF', 20) + int('47GH' + x, 20)) % 19 == 0:
        print((int('13' + x + 'CF', 20) + int('47GH' + x, 20)) // 19)

#12
alph = list(range(5))

for x in alph:

    s = int(f"10{x}01", 5) + int(f"{x}0000", 5)

    if s % 4 == 0:

        print(s // 4)

#13
for x in range(0, 37):
    if ((3*37**3 + 2*37**2 + x*37**1 + 4*37**0) + (5*37**3 + x*37**2 + 2*37**1 + 9*37**0)) % 63 == 0:
        print(((3*37**3 + 2*37**2 + x*37**1 + 4*37**0) + (5*37**3 + x*37**2 + 2*37**1 + 9*37**0)) // 63)
    
#14
for x in '0123456789ABCD':
    for y in '0123456789ABCD':
        if (int(f'abcd3{y}2{x}1', 14) + int(f'192{x}9', 14)) % 107 == 0:
            print(x, y, (int(f'abcd3{y}2{x}1', 14) + int(f'192{x}9', 14)) // 107)
            
#15
for p in range(12, 36):
    for x in range(0, p):
        for y in range(0, p):
            if ((1*p**3 + x*p**2 + y*p**1 + 1*p**0) + (x*p**3 + y*p**2 + x*p**1 + 9*p**0)) == (13*p**3 + 6*p**2 + 5*p**1 + y*p**0):
                print(x*p**2 + x*p**1 + y*p**0)        

#17
for x in '0123456789ABCDEFGHIJK':
    if (int(str((int(f'5ag{x}2', 22) + int(f'6{x}2{x}7', 22))), 9)).count('7') == 2:
        print(x)









