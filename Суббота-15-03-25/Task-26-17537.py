with open('26_17537.txt') as file:
    N, M, K = map(int, file.readline().split())
    place = [list(map(int, i.split())) for i in file]

place = sorted(place, key=lambda x: (x[1], -x[0]))

zal = [M + 1] * (K + 1)

for h, v in place:
    zal[v] = h

ans = []

for i in range(1, len(zal) - 1):
    p1, p2 = zal[i:i+2]
    ans.append([min(p1, p2) - 1, i + 1])

print(max(ans))


