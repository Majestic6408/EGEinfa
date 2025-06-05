from ipaddress import ip_address, ip_network

ip1 = ip_address('216.54.187.235')
ip2 = ip_address('216.54.174.128')

for mask in range(10, 31):
    net1 = ip_network(f'{ip1}/{mask}', 0)
    net2 = ip_network(f'{ip2}/{mask}', 0)
    if net1.network_address != net2.network_address:
        if ip1 in net1.hosts() and ip2 in net2.hosts():
            print(mask)