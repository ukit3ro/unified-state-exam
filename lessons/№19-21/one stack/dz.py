#19
""" def WIN1(s):
    return (s + 1) >= 46 or (s * 2) >= 46

for s in range(1, 46):
    if WIN1(s + 1) or WIN1(s * 2):
        print(s) """
        
#20
""" def WIN1(s):
    return (s + 2) >= 46 or (s * 2) >= 46

def LOSS1(s):
    return (not(WIN1(s))) and WIN1(s + 2) and WIN1(s * 2)

def WIN2(s):
    return LOSS1(s+2) or LOSS1(s * 2)

for s in range(1, 46):
    if WIN2(s):
        print(s) """
        
#21
""" def WIN1(s):
    return (s + 2) >= 46 or (s * 2) >= 46

def LOSS1(s):
    return (not(WIN1(s))) and WIN1(s + 2) and WIN1(s * 2)

def WIN2(s):
    return LOSS1(s+2) or LOSS1(s * 2)

def LOSS12(s):
    return (WIN2(s+2) and WIN1(2*s))

for s in range(1, 46):
    if LOSS12(s):
        print(s) """