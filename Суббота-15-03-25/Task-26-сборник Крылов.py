with open('file.txt') as file:
    N, M, K = map(int, file.readline().split())
    ships = [list(map(int, i.split())) for i in file]

ships = sorted(ships, key=lambda x: (x[1], -x[0]))

pole =[M + 1] * (K + 1)

for h, v in ships:
    pole[v] = h

ans = []
for i in range(1, len(pole) - 1):
    p1, p2 = pole[i:i + 2]
    ans.append([min(p1, p2) - 1, i])

print(max(ans))