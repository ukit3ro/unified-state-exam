
#1
# cbnc = 0
# for i in permutations('ВОЛЯ', r=4): # именно это отличается
#     cbnc += 1
# print(cbnc)

# #2
# cbnc1 = 0
# for i in permutations('TOUGH', r=4):
#     ss = ''.join(i)
#     if 'U' != ss[0]:
#         cbnc1 += 1
# print(cbnc1)

#3
# cbnc2 = 0
# glas = 'аие'
# for i in permutations('ТАРКНИЩЕ', r=4):
#     ss = ''.join(i)
#     if ss[0] not in glas and ss[2] not in glas and ss[1] in glas and ss[3] in glas:
#         cbnc2 += 1
# print(cbnc2)

#4
# import itertools
# alphabet = "0123456789"
# ar = itertools.permutations(alphabet, 6) #Размещение
# arl = []
# for e in ar:
#     arl.append(list(e))
# count = 0
# for e in arl:
#     flag = True
#     for i in range(len(e)-1):
#         if (e[0] == "0") or (int(e[i]) % 2 == 0 and int(e[i+1]) % 2 == 0) or (int(e[i]) % 2 != 0 and int(e[i+1]) % 2 != 0):
#             flag = False
#     if flag:
#         count += 1
# print(count)

#5
from itertools import *
# cnt = 0
# for i in permutations("0123456789", r = 6):
#     if ''.join(i)[0] != "0" and (''.join(i)[-1] == "5" or ''.join(i)[-1] == "0"):
#         flag = True
#         for j in range(len(i) - 1):
#             if int(i[j]) % 2 != int(i[j + 1]) % 2:
#                 continue
#             flag = False
#             break
#         if flag:
#             cnt += 1
# print(cnt)

# #6
# from itertools import permutations
# cnt = 0 
# for i in permutations("ABCDEFG", r = 5):
#     if ''.join(i).count("AE") == 0 and ''.join(i).count("EA") == 0:
#         cnt += 1
# print(cnt)
#7

# caunt = 0
# for i in permutations('СЕРБИЯ', r = 5):
#     if ''.join(i).count('ИЯ') == 0 and ''.join(i).count('ЯИ') == 0 and\
#         ''.join(i).count('ИЕ') == 0 and''.join(i).count('ЕИ') == 0  \
#             and ''.join(i).count('ЕЯ') == 0 and ''.join(i).count('ЯЕ') == 0\
#                 and ''.join(i).count('ИЯ') == 0 and ''.join(i).count('СР') == 0\
#                 and ''.join(i).count('РС') == 0 and ''.join(i).count('СБ') == 0\
#                 and ''.join(i).count('БС') == 0 and ''.join(i).count('БР') == 0\
#                 and ''.join(i).count('РБ') == 0 and ''.join(i).count('ИЯ') == 0:
#                     caunt += 1
# print(caunt)


#8
# cnt1 = 0 
# for i in permutations("ГЕПАРД", r = 6):
#     if ''.join(i)[0] != 'П' :
#         cnt1 += 1
# print(cnt1)

#9
cnt2 = 0
for i in permutations('NORTHE', 4):
    if i[0] != "О" and 'ТН' not in "".join(i):
        cnt2 += 1
print(cnt2)

#10
cnt3 = 0
for i in permutations('ABCDEFG', 5):
    if i[0] != 'E' and 'BG' not in ''.join(i):
        cnt3 += 1
print(cnt3)

#11
cnt4 = 0
for i in permutations('МАЛИНА', 5):
    if ''.join(i).count('А') < 2:
        cnt4 += 1
print(cnt4)

#12
cnt5 = 0
for i in set(permutations('ВАРЕНЬЕ', 5)):
    if ''.join(i).count('ЕЕ') == 0:
        cnt5 += 1
print(cnt5)

#13

from itertools import permutations

# Функция для проверки, что в числе ровно четыре нечетные цифры
def has_four_odd_digits(number):
    return sum(1 for digit in number if int(digit) % 2 != 0) == 4

# Перебор всех шестизначных чисел с различными цифрами
count = 0
for number_tuple in permutations('0123456789', 6):
    # Пропускаем числа, начинающиеся с нуля
    if number_tuple[0] == '0':
        continue
    number = ''.join(number_tuple)
    if has_four_odd_digits(number):
        count += 1

print(count)


#15
kkk = 0
for i in set(permutations('ВЕДЬМАК', r = 7)):
    if i[0] not in 'МАК' and i[1] not in 'МАК'\
        and i[-1] != 'К':
            kkk += 1
print(kkk)

