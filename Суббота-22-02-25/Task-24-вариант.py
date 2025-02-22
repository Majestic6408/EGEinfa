with open('24-1.txt') as file:
    data = file.readline()

data = data.replace('++', ' ').replace('**',' ')
data = data.replace('*+', ' ').replace('+*', ' ')

data = data.split()
ans = 0
for i in data:
    st = i.strip('+').strip('*')
    if eval(st) == 0:
        ans = max(ans, len(st))

print(ans)


