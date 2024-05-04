f = open('17var01.txt')
a = [int(s) for s in f]
summi = []
n = min([i for i in a if str(i)[-2:] == '25'])

for i in range(len(a) - 2):
    if (((10 <= a[i] < 100) +  (10 <= a[i+1] < 100) + (10 <= a[i+2] < 100)) == 1\
        and ((a[i] + a[i+1] + a[i+2]) < n)):
        summi.append((a[i] + a[i+1] + a[i+2]))
print(len(summi), max(summi))
