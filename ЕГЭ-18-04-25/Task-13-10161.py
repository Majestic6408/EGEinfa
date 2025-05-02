from ipaddress import ip_address, ip_network

ip1 = ip_address('211.115.61.154')
ip2 = ip_address('211.115.59.137')

for mask in range(33):
    net1 = ip_network(f'{ip1}/{mask}', 0)
    net2 = ip_network(f'{ip2}/{mask}', 0)
    if net1.network_address == net2.network_address:
        print(net1.netmask)