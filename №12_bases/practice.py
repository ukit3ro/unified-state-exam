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
