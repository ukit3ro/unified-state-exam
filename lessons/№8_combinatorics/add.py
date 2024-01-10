from itertools import product, permutations
# cnt = 0
# #1
# for p in product('МАНГУСТ', repeat = 6):
#     if p.count('М') == 2 and p.count('У') >= 1 and p[0] != 'А':
#         cnt += 1
# print(cnt)

#2
# c = 0
# for j in range(1, 11):
#     for i in permutations('0123456789', j):
#         x = ''.join(i)
#         if x[0] != '0' and (x[-1] == '5' or x[-1] == '0'):
#             c += 1
# print(c + 1)

#3
# c = 0

# p = product('012345678', repeat = 5)

# for i in p:
#     s = ''.join(i)
#     if s[0] != '0' and s.count('3') == 2:
#         for j in s:
#             if j in '1357':
#                 s = s.replace(j, '*')
#             if '2*' not in s and '*2' not in s:
#                 c += 1
# print(c)

#4
# cnt = 0
# vol = 'ЕЭ'
# for i in product('ЕГЭ', repeat = 5):
#     s = ''.join(i)
#     if s[0] in vol:
#         cnt += 1
# print(cnt)

#5
# cnt = 0
# for i in product('слон', repeat = 5):
#     s = ''.join(i)
#     if s.count('с') == 1:
#         cnt += 1
# print(cnt)

#6
# cnt = 0

# for i in product('ABCX', repeat = 5):
#     s = ''.join(i)
#     if i.count('X') == 0:
#         cnt += 1
#     elif s[-1] == 'X' and i.count('X') == 1:
#         cnt += 1
#     else:
#         cnt += 0
# print(cnt)

#7
# words = list(product('АОУ', repeat = 5))
# print(words[209])

#8
# words = list(product('АОУ', repeat = 5))

# for i in words:
#     s = ''.join(i)
#     if s[0] == 'О':
#         print(words.index(i))
#         break

#9
# cnt = 0
# m = []
# for p in product(sorted('МАНГУСТ'), repeat = 6):
#     cnt += 1
#     if p.count('М') == 2 and p[0] != 'У' and p.count('Г') <=1:
#         m.append(cnt)
# print(max(m))

