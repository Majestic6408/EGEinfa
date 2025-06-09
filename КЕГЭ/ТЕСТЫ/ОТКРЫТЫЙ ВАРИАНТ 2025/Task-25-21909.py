def f(num):
    res = set()
    for i in range(1, int(num ** .5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)
    res = sum(res)
    if str(res)[-1] == '6':
        return res
    return 0
cnt = 0
for i in range(500_001, 10_000_000):
    res = f(i)
    if res:
        print(i, res)
        cnt += 1
        if cnt == 5:
            break