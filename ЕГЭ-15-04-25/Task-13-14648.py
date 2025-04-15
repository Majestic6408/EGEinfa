from ipaddress import ip_network, ip_address

cnt = 0
ip = ip_address('218.48.192.56')
net_ip = ip_address('218.48.192.0')
for mask in range(16, 25):
    net = ip_network(f'218.48.192.0/{mask}', 0)
    if net.num_addresses >= 502 and ip in net and net_ip == net.network_address and ip != net.broadcast_address and ip != net.network_address:
        cnt += 1

print(cnt)

cnt1 = 0
for mask in range(16, 25):
    net = ip_network(f'218.48.192.56/{mask}', 0)
    if net.num_addresses >= 502 and ip in net and net_ip == net.network_address:
        cnt1 += 1

print(cnt)