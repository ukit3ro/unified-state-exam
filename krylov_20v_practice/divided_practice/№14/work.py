
#1
""" for x in '0123456789ABCDEFGHI':
    if (int('1' + x + '1' + x + '1' + x + '1' + x + '1', 23) + int('20' + x + '24', 23) +\
        int('1' + x + '235', 23)) % 22 == 0:
            print((int('1' + x + '1' + x + '1' + x + '1' + x + '1', 23) + int('20' + x + '24', 23) +\
        int('1' + x + '235', 23)) // 22) """


#5
""" s = 4 * 25**2022 - 2 * 5**2000 + 125**1011 - 3 * 5**100 - 660
cnt = 0
while s > 0:
    if s % 5 == 4:
        cnt += 1
    s = s // 5
print(cnt) """

#6
""" s = 4**2022 - 6 * 4**522 + 5 * 64**510 - 3 * 2**330 - 100
cnt = 0
while s > 0:
    if s % 8 == 7:
        cnt += 1
    s = s // 8
print(cnt)
 """
 
#11
""" s = 2 * 3**2022 + 5 * 3**1800 + 3**1001 + 4 * 3**1000 + 3
cnt = 0
while s > 0:
    if s % 9 == 0:
        cnt += 1
    s = s // 9
print(cnt)
 """
