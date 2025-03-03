from ipaddress import *

net = ip_network('192.168.32.48/255.255.255.240', 0)

cnt = 0
for x in net:
    s = f'{x:b}'
    if s.count('1') % 2 != 0:
        cnt += 1

print(cnt)