from ipaddress import ip_network

for mask in range(16, 25):
    net = ip_network(f'152.65.245.132/{mask}',0)
    for i in net:
        s = f'{int(i):032b}'
        if not (s[:16].count('0') >= s[16:].count('0')):
            break
    else:
        print(net.netmask)