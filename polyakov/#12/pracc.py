#128, 168, 187, 220, 224, 236, 247, 255, 260, 271, 288, 313

#128
""" s = '222' + '5' * 18
while '222' in s or '888' in s:
    while '555' in s:
        s = s.replace('555', '8', 1)
    
    if '222' in s:
        s = s.replace('222', '8', 1)
    else:
        s = s.replace('888', '2', 1)
print(s) 228 """

#168
""" s = '4' + '6' * 125 + '4'
while '63' in s or '664' in s or '6665' in s:
    if '63' in s:
        s = s.replace('63', '4', 1)
    else: 
        if '644' in s:
            s = s.replace('644', '5', 1)
        else:
            if '6665' in s:
                s = s.replace('6665', '3', 1)
print(s) """

#187
""" s = '561' * 102
while '56' in s or '1111' in s:
    s = s.replace('56', '1', 1)
    s = s.replace('1111', '1', 1)
print(s) """

#220
""" for n in range(101, 1, -1):
    s = '3' * n
    while '333' in s:
        s = s.replace('333', '4', 1)
        s = s.replace('4444', '3', 1)
    
    if s == '43':
        print(n)
        break """

#224


        
    
#236
""" s = '>' + '1' * 11 + '2' * 12 + '3' * 30
while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s:
        s = s.replace('>1', '22>', 1)
    if '>2' in s:
        s = s.replace('>2', '2>', 1)
    if '>3' in s:
        s = s.replace('>3', '1>', 1)
print(s.count('1') + s.count('2') * 2 + s.count('3') * 3) """

#247
""" a = []
for n in range(51, 100):
    s = '1' * n
    while '111' in s:
        s = s.replace('111', '22', 1)
        s = s.replace('222', '11', 1)
    a.append(s)
for x in a:
    print(x.count('1')) """
 
    
#255
""" 123
132
213
231
312
321 """
a = []
s = '>' + '1' * 20 + '3' * 40  + '2' * 15 + '<'
while '><' not in s:
    s = s.replace('>1', '3>', 1)
    s = s.replace('>2', '2>', 1)
    s = s.replace('>3', '1>', 1)
    s = s.replace('3<', '<1', 1)
    s = s.replace('2<', '<3', 1)
    s = s.replace('1<', '<2', 1)
    
a.append(s.count('1') + s.count('2') * 2 + s.count('3') * 3)
print(max(a))

#260



#271

#288

#313
        