# for n in range(4, 10000):
#     s = '5' + '2' * n
#     while '52' or '1122' or '2222' in s:
#         if '52' in s:
#             s = s.replace('52', '11', 1)
#         if '2222' in s:
#             s = s.replace('1122', '25', 1)
#         if '3322' in s:
#             s = s.replace('2222', '5', 1)
#     if (s.count("5") * 5 + s.count("2") * 2 + s.count("1") * 1) == 64:
#         print(n)




for n in range (50):
    for x in range (50):
        for z in range (50):
            s = '0' + '1' * n + '2' * x + '3' * z
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01','30',1)
                s = s.replace('02','101',1)
                s = s.replace('03','202',1)
            if s.count('1') == 15 and s.count('2') == 10 and s.count('3') == 60:
                    print(n)
