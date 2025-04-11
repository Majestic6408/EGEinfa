from ipaddress import ip_network

for mask in range(33):
    net = ip_network(f'246.51.128.202/{mask}', 0)
    for i in net:
        s = f'{int(i):032b}'
        if not(s[:16].count('0') <= s[16:].count('0')):
            break
    else:
        print(net.netmask)