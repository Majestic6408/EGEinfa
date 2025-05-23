with open('24_19254.txt') as file:
    data = file.readline()

ans = 0
data = data.split('FSRQ')
for i in range(len(data) - 80):
    sub_str = 'FSRQ'.join(data[i:i+81])
    ans = max(ans, len(sub_str))

print(ans)