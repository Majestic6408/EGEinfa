from ipaddress import ip_network

net = ip_network('214.187.224.0/255.255.224.0', 0)

cnt = 0
for i in net:
    s = f'{i:b}'
    if s.count('1') % 6 != 0 and str(s)[-4:] == '1000':
        cnt += 1

print(cnt)