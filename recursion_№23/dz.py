

#1
def t23(ss, ee):
    if ss > ee:
        return 0
    if ss == ee:
        return 1
    if ss < ee:
        return t23(ss + 2, ee) + t23(ss * 2, ee)
print(t23(1,25))

#2
def t24(s, e):
    if s > e:
        return 0
    if s == e:
        return 1
    if s < e:
        return t24(s + 1, e) + t24(s * 4, e)
print(t24(2, 55))

#3
def t25(s, e):
    if s > e:
        return 0
    if s == e:
        return 1
    if s < e:
        return t25(s+1, e) + t25(s*2, e) + t25(s**2, e)
print(t25(3,27))

#4
def t26(s, e):
    if s > e:
        return 0
    elif s == e:
        return 1
    elif s == 26:
        return 0
    else:
        return t26(s+2, e) + t26(s*2, e)
    
print(t26(2, 14) * t26(14, 56))

#5
def t27(s, e):
    if s > e:
        return 0
    elif s == e:
        return 1
    elif s == 20:
        return 0
    else:
        return t27(s+2, e) + t27(s*3, e)
print(t27(2, 24) * t27(24, 100))

#6
def t28(s, e):
    if s < e:
        return 0
    if s == e:
        return 1
    if s > e:
        return t28(s-1, e) + t28(s//2, e)
print(t28(156, 63) * t28(63, 3))

#7
def t29(s, e):
    if s < e:
        return 0
    elif s == e:
        return 1
    else:
        return t29(s-1, e) + t29(s//2, e) + t29(s//3, e)
print(t29(131, 41) * t29(41, 3))

#8
def t30(s, e):
    if s > e:
        return 0
    elif s == e:
        return 1
    else:
        return t30(s+1, e) + t30(s+10, e)
print(t30(3,35))

#9
def t31(s, e):
    if s > e:
        return 0
    elif s == e:
        return 1
    else:
        return t31(s+1, e) + t31(s*2, e) + t31(s * 2 + 1, e)
print(t31(2, 16))

#10
def t32(s, e):
    if s > e:
        return 0
    elif s == e:
        return 1
    else:
        return t32(s+1, e) + t32(int(str(s) + '1'), e)
print(t32(1, 875))

#11
def t33(s, e):
    if s > e:
        return 0
    elif s == e:
        return 1
    elif s == 26:
        return 0
    else:
        return t33(s+1, e) + t33(int('1' + str(s)), e)
print(t33(1, 123))

#12
def t34(s, e):
    if s > e:
        return 0
    elif s == e:
        return 1
    else:
        return t34(s+1, e) + t34(s*2, e)
print(t34(1, 10))

# 13
def t35(s, e):
    if s > e:
        return 0
    elif s == e:
        return 1
    else:
        return t35(s+2, e) + t35(s*3, e)
print(t35(1,15))

#14
def t36(s, e):
    if s > e:
        return 0
    elif s == e:
        return 1
    else:
        return t36(s+5, e) + t36(s*2, e)
print(t36(1,12)*t36(12,24))

#15
def t37(s, e):
    if s > e:
        return 0
    elif s == e:
        return 1
    elif s == 5:
        return 0
    else:
        return t37(s+1, e) + t37(s*3, e)
print(t37(1,21))

#16
def t38(s, e, cmds):
    if s > e or cmds < 2:
        return 0
    elif s == e:
        return 1
    else:
        return t38(s+2, e, cmds + 0) + t38(s+3, e, cmds + 0) + t38(s*2, e, cmds + 1) + t38(s*3, e, cmds + 1)
print(t38(1,51, 0))





def in9(a):
    n = ''
    k = ''
    while a > 0:
        n = n + str(a % 9)
        a = a // 9
    n =  list(reversed(n))
    for j in range(len(n)):
        k += n[j]
    return k

#17
def t39(s, e):
    if s < e:
        return 0
    elif s == e:
        return 1
    else:
        return t39(s-1, e) + t39(s-3, e) + t39(int(in9(s//3)), e)
print(t39(52, 16))


