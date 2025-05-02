from ipaddress import ip_network

net = ip_network('102.141.0.0/255.255.192.0')
cnt = 0
for i in net:
    s = f'{int(i):032b}'
    if s.count('1') % 7 == 0 and str(s)[-4:] == '1011': 
        cnt += 1

print(cnt)