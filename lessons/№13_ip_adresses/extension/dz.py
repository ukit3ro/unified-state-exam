from ipaddress import *

#1
""" ip_net = ip_network('142.96.56.118/255.255.255.240', False)

cnt = 0
for ip_add in ip_net:
    if bin(int(ip_add))[-16:].count('1') > bin(int(ip_add))[:-16].count('1'):
        cnt += 1
print(cnt) """

#2
""" for A in range(0, 256):
    if len(bin(A)[2:]) == 8 and '01' not in bin(A)[2:] or A == 0:
        ip_net = ip_network(f'255.201.33.160/255.255.{A}.0', False)
        for ip_add in ip_net:
            if (bin(int(ip_add))[:-16].count('1') >= bin(int(ip_add))[-16:].count('1')) == False:
                break
        else:
            print(A)
            break """
            
#3
""" cnt = 0
ip_net = ip_network('231.168.192.196/255.255.255.240', False)
for ip_add in ip_net:
    if bin(int(ip_add)).count('1') % 2 != 0:
        cnt += 1
print(cnt) """

#another but the same

#1
""" mask = [int('1'*i+'0'*(8-i),2) for i in range(9)]
print(*[m for m in mask if 255&m==240]) """

#2
""" mask = [int('1'*i+'0'*(8-i),2) for i in range(9)]
print(*[m for m in mask if 66&m==64]) """

#3
""" mask = [int('1'*i+'0'*(8-i),2) for i in range(9)]
print(*[m for m in mask if 112&m==96]) """

#4
""" ip_add = ip_address('156.211.113.106')
for mask in range(33):
    try:
        ip_net = ip_network(f'156.211.112.0/{mask}')
        
        if ip_add in ip_net:
            print(bin(int(ip_net.netmask)).count('1'))
    except:
        continue """
        
#5
""" ip_add = ip_address('208.92.69.167')
for mask in range(33):
    try:
        ip_net = ip_network(f'208.92.64.0/{mask}')
        
        if ip_add in ip_net:
            print(bin(int(ip_net.netmask))[2:].count('0'))
    except:
        continue """


#and more

#1
""" cnt = 0
ip_net = ip_network('192.168.32.176/255.255.255.240', False)
for ip_add in ip_net:
    if bin(int(ip_add)).count('1') % 2 != 0:
        cnt += 1
print(cnt) """

#2
""" cnt = 0
ip_net = ip_network('231.168.192.142/255.255.255.240', False)
for ip_add in ip_net:
    if bin(int(ip_add)).count('1') % 2 == 0:
        cnt += 1
print(cnt) """

#3
""" ip_net = ip_network('252.32.33.87/255.255.0.0', False)

cnt = 0
for ip_add in ip_net:
    if bin(int(ip_add))[-16:].count('1') > bin(int(ip_add))[:-16].count('1') * 2:
        cnt += 1
print(cnt) """

#4
""" ip_add = ip_address('50.63.212.2')
for mask in range(33):
    try:
        ip_net = ip_network(f'50.63.192.0/{mask}')
        
        if ip_add in ip_net:
            print(bin(int(ip_net.netmask))[2:].count('0'))
    except:
        continue """
        
#5



ip_add = ip_address('244.55.138.100')
for mask in range(33):
    try:
        ip_net = ip_network(f'244.55.138.96/{mask}')
        
        if ip_add in ip_net:
            print(ip_net.netmask)
    except:
        continue