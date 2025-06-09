with open('24_21717.txt') as file:
    data = file.readline()

data = data.split('RSQ')

ans = 100000
for i in range(len(data) - 129):
    l = 'RSQ' + 'RSQ'.join(data[i:i+129]) + 'RSQ'
    konec = data[i+129]
    cnt = 0
    for j in konec:
        cnt += 1
        if j != 'Q':
            break
    if not konec:
        cnt += 1
    ans = min(ans, len(l) + cnt)

print(ans)