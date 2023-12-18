#задание №1
i = int(input('Введите любое число: '))
print(f'Последняя цифра вашего числа - {i%10}')


#задание №2
a = 3
b = 2
c = 1
print(f'Программа выведет - {a*2 + b + c}')


#задание №3
a = 6
b = 8
c = 9
a = (b-a) * 2
print(a + b + c)


#задание #4
a = int(input()) 
if a % 2 == 0: 
    print('Четное') 
else: 
    print('Нечетное')
    

#задание №8
s = '3' * 30
while '333' in s or '555' in s:
    if '333' in s:
        s = s.replace('333', '5', 1)
    else:
        s = s.replace('555', '3', 1)
print(s)


#задача №9
s = '1' * 9 + '2' * 22
while '111' in s or '222' in s:
    while '111' in s:
        s = s.replace('111', '2', 1)
    while '222' in s:
        s = s.replace('222', '1', 1)
print(s)


#задача №10
s = '5' + 4 * '99'
while '54' in s or '644' in s or '744' in s:
    if '54' in s:
        s = s.replace('54', '6', 1)
    elif '7444' in s:
        s = s.replace('7444', '5', 1)
    elif '644' in s:
        s = s.replace('644', '7', 1)
print(s)


#задача №11
s = '3' * 6 + '5' *24
while '3333' or '5555' in s:
    if '3333' in s:
        s = s.replace('3333', '55', 1)
    elif '5555' in s:
        s = s.replace('5555', '33', 1)
print(s)


#задача #12 (13 и 14 похожие)
s = 1 + '4'*81 #создаём нужную строку
while '14' or '244' or '3444' in s: #буквально переписываем цикл
    if '14' in s:
        s = s.replace('14', '3', 1)
    elif '244' in s:
        s = s.replace('244', '1', 1)
    elif '3444' in s:
        s = s.replace('3444', '2', 1)
print(s)


#задача №15
for n in range(91, 1000):
    s = '3' * n
    while '333' in s:
        s = s.replace('333', '1', 1)
        s = s.replace('111', '3', 1)
    if s == '133':
        print(n)
        
        
#задача №16
for n in range(81, 1000):
    s = '2' * n
    while '222' in s:
        s = s.replace('222', '5', 1)
        s = s.replace('555', '2' 1)
    if s == '5522':
        print(n)


#задача №17
s = '>' + '2' * 40 + '3' * 40 + '5' * 20
while '>2' or '>3' or '>5' in s:
    if '>2' in s:
        s = s.replace('>2', '33>', 1)
    if '>3' in s:
        s = s.replace('>3', '3>', 1)
    if '>5' in s:
        s = s.replace('>5', '2>', 1)
print(s.count('3')*3 + s.count('2')*2 + s.count('5')*2)


#задача №18
for n in range(4, 2000):
    s = '5' + '2' * n
    while '52' or '2222' or '3322' in s:
        if '52' in s:
            s = s.replace('52', '33', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
        if '3322' in s:
            s = s.replace('3322', '25', 1)
    summ = s.count('2')*2 + s.count('3')*3 + s.count('5')*5