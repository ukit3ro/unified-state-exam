 
 
#2
""" f = open('dz/2.txt')
s = f.readline()
a = s.split('C', ' ')
print(len(max(a, key=len)))  """

#3
""" f = open('3.txt')
s = f.readline()
s = s.replace('E', 'I')
s = s.replace('O', 'I')
s = s.replace('M', 'K')
for i in range(1000):
    if 'IM' in s:
        print(i) """
        
""" f = open('123123.txt')
cnt = 0
for s in f:
    if 1 < s.count('C') <= s.count('AB'):
        cnt += 1
print(cnt) """

""" from string import *
f = open('1234.txt')
ans = []
for s in f:
    if s.count('a') < 20:
        for symb in ascii_lowercase:
            ans.append(s.rindex[symb] - s.in dex[symb])
print(max(ans))    """         
