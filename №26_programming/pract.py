f = open('lalala.txt')

vmestim, n = map(int, f.readline().split())
weight = []
needed = []
for s in f:
    weight.append(int(s))
weight.sort()
for we in weight:
    if sum(needed) + we <= vmestim:
        needed.append(we)
    elif sum(needed[:-1]) + we <=
print(len(needed))
