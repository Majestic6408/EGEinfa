from ipaddress import ip_network

for A in range(0, 256):
    net = ip_network(f'192.214.{A}.184/255.255.255.224', 0)
    for i in net:
        s = f'{int(i):032b}'
        if not(s.count('1') > 15):
            break
    else:
        print(A)