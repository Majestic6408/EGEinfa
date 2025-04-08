with open('26.txt') as file:
    N = file.readline()
    data = [int(i) for i in file]

data = sorted(data, reverse=1)
cnt = 0
ans = [data[0]]
for i in data[1:]:
    if ans[-1] - i >= 9:
        ans.append(i)

print(len(ans), min(ans))