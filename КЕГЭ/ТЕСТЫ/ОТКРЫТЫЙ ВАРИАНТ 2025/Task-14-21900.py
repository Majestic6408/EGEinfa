ans = []
for x in range(1, 2300):
    cnt = 0
    num = 7 ** 350 + 7 ** 150 - x
    while num:
        if num % 7 == 0:
            cnt += 1
        num //= 7
    if cnt == 200:
        ans.append(x)

print(max(ans))
