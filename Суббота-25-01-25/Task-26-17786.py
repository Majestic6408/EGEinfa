with open('26_17786.txt') as file:
    N, V = map(int, file.readline().split())
    watermelons = [int(i) for i in file if 7000 <= int(i) <= 12000]

V *= 1000
watermelons = sorted(watermelons, reverse=True)

mass = 0
ans_1 = 0
ans_2 = 0
for watermelon in watermelons:
    if mass + watermelon <= V:
        mass += watermelon
        ans_1 += 1
        ans_2 = watermelon

print(ans_1, ans_2)