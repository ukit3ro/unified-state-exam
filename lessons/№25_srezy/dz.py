import fnmatch

""" for x in range(21504140, 10**9+1):
    if fnmatch.fnmatch(str(x), r'215*414?'):
        if x % 127 == 0:
            print(x, x // 127) """
""" 
21504148 169324
"""

""" for x in range(1004009, 10**8+1):
    if fnmatch.fnmatch(str(x), r'10?4??9'):
        if x % 151 == 0:
            print(x, x // 151) """
""" 
1014569 6719
1034199 6849
1044769 6919
1064399 7049
1074969 7119
1084029 7179
1094599 7249 
""" 


""" for x in range(123050, 10**6):
    if fnmatch.fnmatch(str(x), r'123*5*'):
        if x % 42 == 0:
            print(x, x // 42) """
""" 
123354 2937
123522 2941
123564 2942
123858 2949 
"""

""" for x in range(530120, 550000):
    if fnmatch.fnmatch(str(x), r'53?12*'):
        if x % 56 == 0:
            print(x, int(str(x)[0]) * int(str(x)[1]) * int(str(x)[-2]) * int(str(x)[-1])) """

""" 
533120 0
534128 240 
"""

