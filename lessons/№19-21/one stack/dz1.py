#1 (19)
""" def WIN1(s):
    return ((s * 3) >= 51 and (s * 3) % 2 != 0) or ((s + 1) >= 51 and (s + 1) % 2 != 0) or ((s + 3) >= 51 and (s + 3) % 2 != 0)

for s in range(1, 51):
    if WIN1(s * 3)  or WIN1(s + 1) or WIN1(s + 3) :
            print(s) """
            
#1 (20)
""" def WIN1(s):
    return ((s * 3) >= 51 and (s * 3) % 2 != 0) or ((s + 1) >= 51 and (s + 1) % 2 != 0) or ((s + 3) >= 51 and (s + 3) % 2 != 0)

def LOSS1(s):
    return (not(WIN1(s))) and WIN1(s + 1) and WIN1(s * 3) and WIN1(s + 3)

def WIN2(s):
    return LOSS1(s+1) or LOSS1(s * 3) or LOSS1(s + 3)

for s in range(1, 51):
    if WIN2(s):
            print(s) """
            
#2(19)
from functools import lru_cache

def moves(x, s):
    return (x + 3, s), (x+s, s), (x, s + 3), (x, s + x)

@lru_cache
def game(x, s):
    if any(sum(m) >= 101 for m in moves(x, s)): return 'WIN1'
    
x = 10

for s in range(1, 91):
    if game(x, s) == 'WIN1':
        print(s)