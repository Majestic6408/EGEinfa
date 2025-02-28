def f(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)
    if len(res) >= 2:
        M = res[-1] + res[-2]
        if str(M)[-4:] == '1214':
            return M
    return 0

for i in range(112_500_000, 112_550_001):
    N = f(i)
    if N:
        print(i)