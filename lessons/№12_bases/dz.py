#0
""" s = '8' * 70
while '2222' in s or '8888' in s:
    if '2222' in s:
        s = s.replace('2222', '88', 1)
    else:
        s = s.replace('8888', '22', 1)
print(s) """

#1
""" s = '1' * 44 + '2' * 21
while '111' in s:
    s = s.replace('111', '2', 1)
    s = s.replace('22', '1', 1)
print(s)  212""" 

#2
""" for n in range(1, 1000):
    s = '1' * 10 + '2' * n
    
    while '21' in s:
        s = s.replace('21', '5', 1)
        
    if (s.count('1') + s.count('2') * 2) == 34:
        print(n)
        break  12"""
        
#3
""" s = '8' * 68
while '222' in s or '888' in s:
    if '222' in s:
        s = s.replace('222', '8', 1)
    else:
        s = s.replace('888', '2', 1)
print(s) 28 """