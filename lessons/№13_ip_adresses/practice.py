
from ipaddress import *

#8
""" ip_net = ip_network('142.108.56.118/255.255.255.240', False)
cnt = 0

for ip_add in ip_net:
    if bin(int(ip_add))[-16:].count('1') > bin(int(ip_add))[:-16].count('1'):
        cnt += 1
print(cnt) """

#9
""" ip_net = ip_network('252.67.33.87/255.252.0.0', False)
cnt = 0

for ip_add in ip_net:
    if bin(int(ip_add))[-16:].count('1') >  2 * bin(int(ip_add))[:-16].count('1'):
        cnt += 1

print(cnt) """

#10
for i in range(9):
    A = '1' * i + '0'* 8
    A = int(A[:8], 2)
    ip_net = ip_network(f'255.211.33.160/255.255.{A}.0')
    for ip_add in ip_net:
        if (bin(int(ip_add))[:-16].count('1') >= bin(int(ip_add))[-16:].count('1')) == False:
            break
    else:
        print(A)
        
#11 аналогично

#12
""" for A in range(0, 256):
    ip_net = ip_network(f'127.154.{A}.10/255.255.224.0', False)
    for ip_add in ip_net:
        if bin(int(ip_add))[:-16].count('1') а дальше по шаблону """