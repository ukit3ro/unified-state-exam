from itertools import product, permutations

#1
""" cnt = 0
for i in product('WORD', repeat = 5):
    s = ''.join(i)
    if s.count('R') == 1:
        cnt += 1
print(cnt) """

#2
""" cnt = 0
chet = [2, 4, 6, 8]
for i in product('01234567', repeat = 4):
    s = ''.join(i)
    if s[0] != '0' and int(s[0]) % 2 != 0 and s.count('6') == 1:
        cnt += 1
print(cnt) """

#3
""" cnt = 0
for i in product('012345', repeat = 4):
    s = ''.join(i)
    if s[0] != '0' and s.count('1') == 1 and s.count('14') == 0 and s.count('41') == 0:
        cnt += 1
print(cnt) """

#4
""" cnt = 0
for i in product('01234567', repeat = 5):
    s = ''.join(i)
    if s[0] != '0' and s.count('5') <= 1\
        and s[-1] != '3' and s[-1] != '4' and s[0] != '1' and s[0] != '3' and s[0] != '5'\
            and s[0] != '7':
                cnt += 1
print(cnt)  """

#5
""" cnt = 0
for i in permutations('0123456789', r = 6):
    s = ''.join(i)
    if s[0] != '0' and s[-1] in '05':
        s = s.replace('0', '2').replace('4', '2').replace('6', '2').replace('8', '2')
        s = s.replace('3', '1').replace('5', '1').replace('7', '1').replace('9', '1')
        if '22' not in s and '11' not in s:
            cnt += 1
print(cnt) """

#6
""" cnt = 0
for i in permutations('КОМЕТА', r = 6):
    s = ''.join(i)
    s = s.replace('О', '1').replace('Е', '1').replace('А', '1')
    s = s.replace('К', '2').replace('М', '2').replace('Т', '2')
    if '22' not in s and '11' not in s:
        cnt += 1
print(cnt) """

#7
""" cnt = 0
for i in permutations('ГЕПАРД', r = 6):
    s = ''.join(i)
    if s[0] != 'П':
        cnt += 1
print(cnt) """

#8
""" cnt = 0
for i in permutations('ПИРОГ', r = 4):
    s = ''.join(i)
    if s[0] != 'П' and 'ГИ' not in s:
        cnt += 1
print(cnt) """

#9
""" cnt = 0
for i in permutations('ВЕРНЫЙ', r = 6):
    s = ''.join(i)
    if s[0] != 'Й' and 'ЫЕЙ' not in s:
        cnt += 1
print(cnt) """

#10
""" cnt = 0
for i in permutations('КАПКАН', r = 6):
    s = ''.join(i)
    if s.count('КК') == 0 and s.count('АА') == 0:
        cnt += 1
print(cnt // 4) """

#11
""" cnt = 0
for i in product('01234', repeat = 4):
    s = ''.join(i)
    if (int(s[0]) > int(s[1]) > int(s[2]) > int(s[3])):
        cnt += 1
print(cnt) """


#13
cnt = 0
for i in product('ПРИНЦЕССА', repeat = 13):
    s = ''.join(i)
    if s[0] in 'ИЕА' and s[-1] in 'ПРНЦС' and 'ПРИНЦЕССА' in s:
        cnt += 1
print(cnt)
