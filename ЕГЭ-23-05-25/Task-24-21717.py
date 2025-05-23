with open('24_21717.txt') as file:
    data = file.readline()

ans = 10 ** 10
data = data.split('RSQ')
for i in range(len(data) - 129):
    sub_str = 'RSQ' + 'RSQ'.join(data[i:i+129]) + 'RSQ'
    cnt = 0
    if not data[i + 129]:
        cnt += 1
    else:
        for j in data[i + 129]:
            cnt += 1
            if j != 'Q':
                break
        ans = min(ans, len(sub_str) + cnt)
print(ans)