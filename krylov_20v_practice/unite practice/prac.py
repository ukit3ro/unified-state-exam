
""" f = open('24.3.txt')
s = f.readline()
a = s.split('0')
res = []
for i in range(len(a) - 1):
    res.append(len(a[i] + 'O' + a[i+1]))
print(max(res))

for i in range(1000):
    if 'UT'* i in s:
        print(i) """
        
""" s = s.replace('N', 'F')
s = s.replace('FF', 'F F')
s = s.replace('FF', 'F F')
a = s.split()
print(len(max(a, key=len))) """







