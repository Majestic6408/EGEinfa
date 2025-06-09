ans = []
for x in range(1, 3000):
    cnt = 0
    num = 4 ** 210 + 4 ** 110 - x
    while num:
        if num % 4 == 0:
            cnt += 1
        num //= 4
    ans.append([cnt, x])

print(sorted(ans))