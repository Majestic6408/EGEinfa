def f(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)

    for M in res:
        if str(M)[-1] == '7' and M != 7:
            return M
    return 0

cnt = 0
for i in range(1_125_001, 10_000_000):
    res = f(i)
    if res:
        print(i, res)
        cnt += 1
        if cnt == 5:
            break