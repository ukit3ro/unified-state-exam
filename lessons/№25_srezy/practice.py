""" 
#23456*7?8
#1
for x in range(234560708, 10**9):
    if str(x)[0:5] == '23456' and str(x)[-1] == '8' and str(x)[-3] == '7' and x % 61 == 0:
        print(x, x// 61)


#134*5*
#2
for x in range(1, 10**6 + 1):
    if str(x)[:3] == '134' and '5' in str(x) and x % 63 == 0:
        print(x, x//63)
 """

""" #37*87?
#3
for x in range(370869, 10**6 + 1):
    if str(x)[:2] == '37' and str(x)[-3:-1] == '87' and x % 103 == 0:
        print(x, x//103) """
        

from fnmatch import *
#4
#51?32*8
""" for x in range(94, 10**7, 94):
    if fnmatch(str(x), '51?32*8'):
        print(x, int(str(x)[0]) * int(str(x)[1]) * int(str(x)[-2]) * int(str(x)[-1])) """
        

#5
#154*8*
""" for x in range(99, 10**6, 99):
    if fnmatch(str(x), '154*8*'):
        print(x, x//99) """
        

#6
#64*32?2
""" for x in range(102, 10**6, 102):
    if fnmatch(str(x), '64*32?2'):
        print(x, x // 102) """


#7

