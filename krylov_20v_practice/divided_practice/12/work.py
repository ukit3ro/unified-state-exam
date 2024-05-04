
#1
""" for n in range(3, 10001):
    n2 = '1' + '2' * n
    while '12' in n2 or '3322' in n2 or '2222' in n2:
        if '12' in n2:
            n2 = n2.replace('12', '33', 1)
        if '2222' in n2:
            n2 = n2.replace('2222', '1', 1)
        if '3322' in n2:
            n2 = n2.replace('3322', '21', 1)
    
    if n2.count('2')*2 + n2.count('3')*3 + n2.count('1') == 218:
        print(n)
        break """
        
#2
""" for n in range(3, 10001):
    n2 = '1' + '2' * n
    while '12' in n2 or '5522' in n2 or '2222' in n2:
        if '12' in n2:
            n2 = n2.replace('12', '55', 1)
        if '2222' in n2:
            n2 = n2.replace('2222', '1', 1)
        if '5522' in n2:
            n2 = n2.replace('5522', '21', 1)
    
    if n2.count('2')*2 + n2.count('5')*5 + n2.count('1') == 142:
        print(n)
        break """

#5
""" s = '22' + '1' * 2023 + '22'

while '211' in s or '112' in s:
    s = s.replace('11', '1', 1)
    if '21' in s:
        s = s.replace('21', '12', 1)
    else:
        s = s.replace('12', '1', 1)
print(s) """

#6
""" s = '22' + '1' * 2050 + '22'

while '211' in s or '112' in s:
    s = s.replace('11', '1', 1)
    if '21' in s:
        s = s.replace('21', '12', 1)
    else:
        s = s.replace('12', '1', 1)
print(s) """

#14
""" for n in range(1000):
    s = '>' + '0' * 15 + '1' * n + '2' * 15
    
    while '>0' in s or '>1' in s  or '>2' in s:
        if '>0' in s:
            s = s.replace('>0', '22>')
        if '>1' in s:
            s = s.replace('>1', '2>')
        if '>2' in s:
            s = s.replace('>2', '1>')
    n2 = (s.count('2')*2 + s.count('1'))
    '10'
    k = 0
    for i in range(1, n2 + 1):
        if n2 % i == 0:
            k += 1
            if k > 2:
                break
    if k == 2:
        print(n)
        break """
        
#17
""" s = '1' + '5' * 25

while '15' in s or '1' in s:
    if '15' in s:
        s = s.replace('15', '5551', 1)
    else:
        if '1' in s:
            s = s.replace('1', '5', 1)
print(s.count('5')) """
    
    


