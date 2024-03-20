
#1
""" print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x <= (y and (not z))) or w) == False:
                    print(x, y, z, w) """
                    
#2
""" print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                    F = (((w <= x) == (z <= y)) and ((not y) or w))
                    print(x, y, z, w, int(F)) """
                    
#3
""" print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (((z <= y) == (x <= (not w))) and (x or y))
                if F == False:
                    print(x, y, z, w, int(F)) """
                    
#4
""" print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((w <= y) <= (x <= z))
                if F == False:
                    print(x, y, z, w, int(F)) """
                    
#5
""" print('x y z w F1 F2')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F1 = ((x <= w) == (z <= y))
                F2 = ((x <= w) == ((not y) == z))
                if F1 == False and F2 == True:
                    print(x, y, z, w, int(F1), int(F2)) """
                    
#6
from itertools import *
from fnmatch import fnmatch

def f1(x, y, z, w):
    return (x <= w) == (z <= y)

def f2(x, y, z, w):
    return (x <= w) and ((not y) == z)

templates = ['0?000?', '0?11?0', '00?001']

tbl = [list(xyzw) + [int(f1(*xyzw)), int(f2(*xyzw))]
       for xyzw in product([0, 1], repeat=4)]

def apply(s, p):
    sp = [s[p[i]] for i in range(4)] + s[4:]
    return ''.join(map(str, sp))

for p in permutations(range(4)):
    tblp = [apply(s, p) for s in tbl]
    match = set(s for s in tblp
    if any(fnmatch(s, t) for t in templates))
    if len(match) >= len(templates) and all(any(fnmatch(m, t) for m in match) for t in templates):
        print(''.join('xyzw'[i] for i in p))
        