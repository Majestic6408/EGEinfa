from ipaddress import ip_network

for A in range(0, 256):
    net = ip_network(f'248.112.{A}.35/255.255.255.240', 0)
    for i in net:
        s = f'{int(i):032b}'
        if not(s[:16].count('0') <= s[16:].count('0')):
            break
    else:
        print(A)