from ipaddress import ip_address, ip_network

ip1 = ip_address('95.24.2.9')
ip2 = ip_address('95.24.3.10')
ans = []
for mask in range(10, 31):
    net1 = ip_network(f'{ip1}/{mask}', 0)
    net2 = ip_network(f'{ip2}/{mask}', 0)
    if net1.network_address != net2.network_address:
        if ip1 in net1.hosts() and ip2 in net2.hosts():
            cnt1 = 0
            cnt2 = 0
            for i in net1.hosts():
                s = f'{int(i):032b}'
                if s[-1] == '0':
                    cnt1 += 1
            for i in net2.hosts():
                s = f'{int(i):032b}'
                if s[-1] == '0':
                    cnt2 += 1
            ans.append([cnt1, cnt2])

print(max(ans))