
from ipaddress import *

#1
""" print(bin(112))
print(bin(96))
print(int('1100000', 2)) """

#2
""" ip_add = ip_address('116.109.66.45')
for mask in range(33):
    try:
        ip_net = ip_network(f'116.109.64.0/{mask}')
        
        if ip_add in ip_net:
            print(ip_net.netmask)
    except:
        continue """

#3
""" ip_add = ip_address('129.41.201.127')
for mask in range(33):
    try:
        ip_net = ip_network(f'129.41.200.0/{mask}')
        
        if ip_add in ip_net:
            print(ip_net.netmask)
    except:
        continue """
        
#4
""" ip_add = ip_address('244.55.138.112')
for mask in range(33):
    try:
        ip_net = ip_network(f'244.55.138.96/{mask}')
        
        if ip_add in ip_net:
            print(ip_net.netmask)
    except:
        continue """
        
#5
""" ip_add = ip_address('50.63.212.2')
for mask in range(33):
    try:
        ip_net = ip_network(f'50.63.192.0/{mask}')
        
        if ip_add in ip_net:
            print(bin(int(ip_net.netmask)).count('0'))
    except:
        continue """
        
#6
""" ip_add = ip_address('50.63.212.2')
for mask in range(33):
    try:
        ip_net = ip_network(f'50.63.192.0/{mask}')
        
        if ip_add in ip_network:
            print(ip_net.netmask)
    except:
        continue """
        
#7
""" ip_net = ip_network('192.168.32.160/255.255.255.240', False)
cnt = 0

for ip_add in ip_net:
    if (bin(int(ip_add)).count('1')) % 2 == 0:
        cnt += 1
print(cnt) """

#8
""" ip_net = ip_network('142.96.56.118/255.255.255.240', False)
cnt = 0

for ip_add in ip_net:
    if bin(int(ip_add))[-16:].count('1') > bin(int(ip_add))[:-16].count('1'):
        cnt += 1
print(cnt) """

#9
""" for i in range(9):
    A = '1' * i + '0'* 8
    A = int(A[:8], 2)
    
    ip_net = ip_network(f'255.201.33.160/255.255.{A}.0', False)

    for ip_add in ip_net:
        if (bin(int(ip_add))[-16:].count('1') >= bin(int(ip_add))[:-16].count('1')) == False:
            break
    else:
        print(A) """
        
#10
""" for A in range(0, 256):
    
    ip_net = ip_network(f'127.254.{A}.15/255.255.224.0', False)
    
    for ip_add in ip_net:
        if (bin(int(ip_add))[-16:].count('1') <= bin(int(ip_add))[:-16].count('1')) == False:
            break
    else:
        print(A)  """
        
#11
""" ip_add = ip_address('149.64.150.52')
for mask in range(33):
    try:
        ip_net = ip_network(f'149.64.144.0/{mask}')
        if ip_add in ip_net:
            print(ip_net.netmask)
    except:
        continue """
        
#12
ip_add = ip_address('156.211.64.98')
for mask in range(33):
    try:
        ip_net = ip_network(f'156.211.64.0/{mask}')
        
        if ip_add in ip_net:
            print(bin(int(ip_net.netmask)).count('1'))
    except:
        continue