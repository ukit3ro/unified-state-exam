#дополнительное дз
#1
def t41(s, e):
    if s > e:
        return 0
    if s == e:
        return 1
    else:
        return t41(s + 2, e) + t41(s * 3, e)
print(t41(1, 27))

#2
def t78(s, e):
    if s > e:
        return 0
    if s == e:
        return 1
    else:
        return t78(s + 1, e) + t78(s *2, e) + t78(s**2, e)
print(t78(3,122))

#3
def t111(s, e):
    if s > e:
        return 0
    if s == e:
        return 1
    if s < e:
        return t111(s + 1, e) + t111(s + 3, e) + t111(s * 2, e)
print(t111(1,3) * t111(3,19))

#4
def t222(s, e):
    if s < e:
        return 0
    if s == e:
        return 1
    if s > e:
        return t222(s - 1, e) + t222(s // 2, e) + t222(s // 3, e)
print(t222(32, 10) * t222(10, 4))

#5
def t333(s, e):
    if s > e or s == 35:
        return 0
    if s == e:
        return 1
    if s < e:
        return t333(s + 1, e) + t333(s * 3, e) + t333(s * 4, e)
print(t333(3, 9) * t333(9, 70))