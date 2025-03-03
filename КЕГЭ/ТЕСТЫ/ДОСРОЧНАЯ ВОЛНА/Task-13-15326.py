from ipaddress import *

net = ip_network('105.224.200.224/255.255.255.224', 0)

cnt = 0
for x in net:
    s = f'{x:b}'
    if s.count('1') % 4 == 0:
        cnt += 1

print(cnt)