from ipaddress import ip_network

net = ip_network('112.208.0.0/255.255.128.0', 0)

cnt = 0
for i in net:
    s = f'{i:b}'
    if s.count('1') % 11 == 0:
        cnt += 1

print(cnt)
