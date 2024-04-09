from ipaddress import *
#1
""" ip_net = ip_network('142.108.56.118/255.255.255.240', False)
cnt = 0

for ip_add in ip_net:
    if bin(int(ip_add))[-16:].count('1') > bin(int(ip_add))[:-16].count('1'):
        cnt += 1
print(cnt)
 """
#2
""" ip_net = ip_network('116.29.170.89/255.255.255.224', False)
cnt = 0

for ip_add in ip_net:
    if bin(int(ip_add))[:-16].count('1') >= bin(int(ip_add))[-16:].count('1'):
        cnt += 1
print(cnt) """


#5
""" ip_net = ip_network('252.67.33.87/255.252.0.0', False)
cnt = 0

for ip_add in ip_net:
    if bin(int(ip_add))[-16:].count('1') > bin(int(ip_add))[:-16].count('1') * 2:
        cnt += 1
print(cnt) """

#7
""" for A in range(0, 256):
    if len(bin(A)[2:]) == 8 and '01' not in bin(A)[2:] or A == 0:
        ip_net = ip_network(f'255.211.33.160/255.255.{A}.0', False)
        for ip_add in ip_net:
            if (bin(int(ip_add))[:-16].count('1') >= bin(int(ip_add))[-16:].count('1')) == False:
                break
        else:
            print(A)
            break """
            
#8
""" for A in range(0, 256):
    if len(bin(A)[2:]) == 8 and '01' not in bin(A)[2:] or A == 0:
        ip_net = ip_network(f'191.239.130.3/255.255.{A}.0', False)
        for ip_add in ip_net:
            if (bin(int(ip_add))[:-16].count('1') >= bin(int(ip_add))[-16:].count('1')) == False:
                break
        else:
            print(A)
            break """
            
#11
""" for A in range(0, 256):
    ip_net = ip_network(f'32.0.{A}.5/255.255.240.0', 0)
    for ip_add in ip_net:
        if (bin(int(ip_add))[-16:].count('1') >= bin(int(ip_add))[:-16].count('1')) == False:
            break
    else:
        print(A)
        break """

#12


#15
""" ip_add = ip_address('44.44.229.28')
for mask in range(33):
    try:
        ip_net = ip_network(f'44.44.224.0/{mask}')
        
        if ip_add in ip_net:
            print(bin(int(ip_net.netmask)).count('1'))
    except:
        continue """

#16
""" ip_add = ip_address('244.55.229.28')
for mask in range(33):
    try:
        ip_net = ip_network(f'244.0.0.0/{mask}')
        
        if ip_add in ip_net:
            print(bin(int(ip_net.netmask))[2:].count('0'))
    except:
        continue
 """

#17
""" ip_add = ip_address('244.55.138.100')
for mask in range(33):
    try:
        ip_net = ip_network(f'244.55.138.96/{mask}')
        
        if ip_add in ip_net:
            print(ip_net.netmask)
    except:
        continue """

#19
""" ip_add = ip_address('42.118.219.133')
for mask in range(33):
    try:
        ip_net = ip_network(f'42.118.216.0/{mask}')
        
        if ip_add in ip_net:
            print(bin(int(ip_net.netmask))[2:].count('1'))
    except:
        continue """