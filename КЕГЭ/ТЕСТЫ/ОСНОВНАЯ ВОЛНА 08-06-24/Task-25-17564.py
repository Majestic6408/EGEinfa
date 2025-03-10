def f(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)
    if len(res) >= 2:
        M = min(res) + max(res)
        if str(M)[-1:] == '4':
            return M
    return 0

cnt = 0
for i in range(700001, 1000000000):
    res = f(i)
    if res:
        print(i, res)
        cnt += 1
        if cnt == 5:
            break