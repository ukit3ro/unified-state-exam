#1
""" Q = list(range(42, 103))
P = list(range(22, 73))
A = []
for x in range(1000):
    if ((not((not(x in A)) and (x in P))) or (x in Q)) == False:
        A.append(x)
print(A) """

#2
""" Q = list(range(32, 93))
P = list(range(12, 63))
A  = []
for x in range(1000):
    if (((not(x in A)) and (x in Q)) <= (x in P)) == False:
        A.append(x)
print(A) """

#3
""" Q = list(range(8, 26))
P = list(range(15, 31))
A  = []
for x in range(1000):
    if (((x in P) and (x in Q)) <= (x in A)) == False:
        A.append(x)
print(A) """

#4
""" Q = list(range(21, 59))
P = list(range(1, 40))
A  = list(range(1000))
for x in range(1000):
    if (((x in Q) <= (not(x in P))) <= (not(x in A))) == False:
        A.remove(x)
print(A) """

#5
""" Q = list(range(8, 18))
P = list(range(3, 12))
A  = list(range(1000))
for x in range(1000):
    if (((x in A) <= (x in P)) or (x in Q)) == False:
        A.remove(x)
print(A) """

#6
""" Q = list(range(15, 40))
P = list(range(10, 18))
A  = list(range(1000))
for x in range(1000):
    if (((x in Q) <= (x in P)) <= (not(x in A))) == False:
        A.remove(x)
print(A) """

#7
""" P = list(range(25, 121))
Q = list(range(54, 76))
A  = []
for x in range(1000):
    if ((x in Q) <= (((x in P) == (x in Q)) or (not(x in P) <= (x in A)))) == False:
        A.append(x)
print(A) """

#8
""" P = list(range(10, 58))
Q = list(range(12, 69))
A  = list(range(1000))
for x in range(1000):
    if (((x in Q) <= (x in P)) <= (not(x in A))) == False:
        A.remove(x)
print(A) """

#9
""" P = list(range(13, 38))
Q = list(range(22, 52))
A = []
def aoa(n, m):
    return n % m == 0

for x in range(1, 1000):
    if (((x in Q) <= ((aoa(x, 18)) or (x in P))) <= (x in A)) == True:
        A.append(x)
print(A) """

#11
def D(n, m):
  return n % m == 0

res = []
B = list(range(45, 91))
for A in range(1, 1000):
  flag = 1
  for x in range(1, 1000):
      if D(x, 52) and not((not (x in B)) or D(x, A)):
          flag = 0
          break
  if flag:
      res.append(A)
print(len(res))

#12
""" def aoa(n, m):
    return n % m == 0

for A in range(1, 1000):
    A_right = True
    for x in range(1, 10000):
        if ((aoa(x, A) and aoa(x, 42)) <= (aoa(x, 8) and aoa(x, 150))) == False:
            A_right = False
            break
    if A_right == True:
        print(A) """
        
#13
#5 прототип ДЕЛ + отрезки
def func(x, y, A):
    return ((9 * x + y < A) or (x + 14 * y > 49) or (x + y < 25))
for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if func(x, y, A) == False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A)
        break
    