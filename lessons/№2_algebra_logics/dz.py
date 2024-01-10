

#1
""" print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (y and x) or z or (not(w))
                if not F:
                    print(x, y, z, w) """

#2
""" print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (not(y)) or x or (z and (not(w)))
                if not F:
                    print(x, y, z, w) """

#3
""" print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            F = (y <= x) and z and (not((z == y)))
            if F:
                print(x, y, z) """

#4
""" print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            F = ((not(z)) or (not(y))) <= (x == z)
            if not F:
                print(x, y, z) """

#5
""" print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x or y) and (not(y == z)) and (not(w))
                if F:
                    print(x, y, z, w) """

#6
""" print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((y <= z) <= (x and y)) and (x <= w)
                if F:
                    print(x, y, z, w) """
                    
#7
""" print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x and (not(y))) or (y == z) or w
                if not F:
                    print(x, y, z, w) """
                    
#8
""" print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((y <= x) == (w <= (not(z)))) and (w or x)
                print(x, y, w, z, int(F)) """

#9
""" print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x or y) and not(y == z) and not(w)
                if F:
                    print(x, y, z, w) """
                    
#10
""" print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x or y) and (not(y) == z) and w
                if F:
                    print(x, y, z, w, int(F)) """

#11
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (not(x) or ((z <= w) and (w <= z))) or not((y <= w))
                if not F:
                    print(x, y, z, w)