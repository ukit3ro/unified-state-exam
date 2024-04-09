
cnt = 0
for s in open('91.txt'):
    a = list(map(str, s.split(',')))
    print(a)
    for x in a:
        if ((int(a[0]) %  4 == 0 or int(a[0]) % 400 == 0) and int(a[0]) % 100 != 0)\
            and a[1] == 10 and a[2] == 'ж':
                cnt += 1
print(cnt)
