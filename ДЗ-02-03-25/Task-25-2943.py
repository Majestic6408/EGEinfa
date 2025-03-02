def is_prime(num):
    if num == 1:
        return 0
    for i in range(2, int(num * .5) + 1):
        if num % i == 0:
            return 0
    return 1

def f(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)

    if len(res) >= 2:
        M = max(res) + min(res)
        if M > 220_000 and str(M)[-1:] == '4':
            return M
    return 0

cnt = 0
for i in range(1, 100000000000):
    res = f(i)
    if res:
        print(res)
        cnt += 1
        if cnt == 5:
            break