for n in range(4, 10000):
    s = '5' + '2' * n
    while '52' or '1122' or '2222' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '2222' in s:
            s = s.replace('1122', '25', 1)
        if '3322' in s:
            s = s.replace('2222', '5', 1)
    if (s.count("5") * 5 + s.count("2") * 2 + s.count("1") * 1) == 64:
        print(n)
