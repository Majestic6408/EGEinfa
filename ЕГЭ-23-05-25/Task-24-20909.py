with open('24_20909.txt') as file:
    data = file.readline()

ans = 0
data = data.split('AB')
for i in range(len(data) - 100):
    sub_str = 'AB'.join(data[i:i+101])
    ans = max(ans, len(sub_str))

print(ans)