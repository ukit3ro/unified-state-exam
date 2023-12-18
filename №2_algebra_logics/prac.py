

#1
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (z and (not(x)) or w or (not(y))) == False:
                    print(x, y, z, w)
#далее сопостовляем с данной нам в задании таблицей

#2
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (w or (not(z))) and x and (not(y)):
                    print(x, y, z , w)

#3
print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if ((y or z) == ((z and (not(y))) <= (not(x)))) == False:
                print(x, y, z)
                

#4
print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            F = (z <= ((not(x)) and y)) <= (z == y)
            if F == 0:
                print(x, y, z)


#5
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (y and (not(x))) or (x == w) or z
                if F == 0:
                    print(x, y, z, w)


#6
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (w or x or z) and ((x <= z) <= (y <= w))
                if F == 0:
                    print(x, y, z, w)


#7
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((z <= x) or ((not(w)) and y)) == (y == x)
                if F:
                    print(x, y, z, w)


#8
print('x y z w ')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((z <= w) or (y == w)) and ((x or z) == y)
                if F:
                    print(x, y, z, w)


#9
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((x <= y) == ((not(w)))) and (z or y)
                print(x, y, z, w, bool(F))


#10
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (not(x)) and ((z <= y) <= w)
                print(x, y, z, w, int(F))


#12
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (w == (z <= x)) and y
                print(x, y, z, w, int(F))


#13
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x or (not(y))) and (not(y == z)) and (not(w))
                if F:
                    print(x, y, z, w)


#14
print('x y z w F1 F2')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F1 = (w == x) and (z <= y)
                F2 = (w <= x) <= (y == z)
                print(x, y, z, w, int(F1), int(F2))

