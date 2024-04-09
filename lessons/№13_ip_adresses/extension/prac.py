from ipaddress import *
#1
""" ip_net = ip_network('252.67.33.87/255.255.0.0', False)

cnt = 0
for ip_add in ip_net:
    if bin(int(ip_add))[-16:].count('1') > bin(int(ip_add))[:-16].count('1'):
        cnt += 1
print(cnt) """

#2
""" for A in range(0, 256):
    if len(bin(A)[2:]) == 8 and '01' not in bin(A)[2:] or A == 0:
        ip_net = ip_network(f'255.224.33.160/255.255.{A}.0', False)
        for ip_add in ip_net:
            if (bin(int(ip_add))[:-16].count('1') >= bin(int(ip_add))[-16:].count('1')) == False:
                break
        else:
            print(A) """
            
#3
""" for A in range(0, 256):
    if len(bin(A)[2:]) == 8 and '01' not in bin(A)[2:] or A == 0:
        ip_net = ip_network(f'199.59.130.3/255.255.{A}.0', False)
        for ip_add in ip_net:
            if (bin(int(ip_add))[:-16].count('1') >= bin(int(ip_add))[-16:].count('1')) == False:
                break
        else:
            print(A) """
            
            
#5
""" cnt = 0
ip_net = ip_network('192.158.32.160/255.255.255.240')
for ip_add in ip_net:
    if bin(int(ip_add)).count('1') % 2 == 0:
        cnt += 1
print(cnt) """