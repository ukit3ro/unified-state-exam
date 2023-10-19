


#1
def task23(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    if start < end:
        return task23(start+1, end) + task23(start*3, end)
print(task23(1,14))


#2
def task24(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    if start < end:
        return task23(start+1, end) + task23(start*3, end)
print(task24(2,56))


#3
def task25(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    if start < end:
        return task25(start+2, end) + task25(start*2, end) + task25(start**2, end)
print(task23(3,72))


#4
def task26(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    if start == 27:
        return 0
    if start < end:
        return task26(start+2, end) + task26(start*2, end)
print(task26(3, 15)* task26(15,72))


#5
def task27(start, end):
    if start > end or start == 44:
        return 0
    if start == end:
        return 1
    if start < end:
        return task27(start+2, end) + task27(start*3, end)
print(task27(2, 24) * task27(24, 144))


#6
def task28(start, end):
    if start < end:
        return 0
    if start == end:
        return 1
    if start > end:
        return task28(start-1, end) + task28(start // 3, end)
print(task28(49, 11) * task28(11, 1))


#7
def task29(start, end):
    if start < end:
        return 0
    if start == end:
        return 1
    if start > end:
        return task29(start - 2, end) + task29(start // 2, end) + task29(start // 3, end)
print(task29(37, 13) * task29(13, 2))


#8
def task30(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    if start < end:
        return task30(start + 1, end) + task30(start + 10, end)
print(task30(2, 45))


#9
def task31(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    if start < end:
        return task31(start + 2, end) + task31(start * 2, end) + task31(start * 2 + 1, end)
print(task31(3, 90))


#10
def task32(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    if start < end:
        return task32(start + 1, end) + task32(int(str(start) + '1'), end)
print(task32(1, 928))


#11
def task33(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    if start < end:
        return task33(start + 1, end) + task33(int('1' + bin(start)[2:], 2), end)
print(task33(1, int('1111111', 2)))


#12
def task34(start, end, comands):
    if start > end or comands > 1:
        return 0
    if start == end and comands == 1:
        return 1
    return task34(start + 1, end, comands + 0) + task34(start + 2, end, comands + 0) + task34(start * 2, end, comands + 1) + task34(start * 3, end, comands + 1)
print(task34(1, 13, 0))


#13
def task35(start, end, cmds):
    if start > end or '***' in cmds or '+++' in cmds:
        return 0 
    if start == end:
        return 1
    if start < end:
        return task35(start + 1, end, cmds + '+') + task35(start * 2, end, cmds + '*')
    