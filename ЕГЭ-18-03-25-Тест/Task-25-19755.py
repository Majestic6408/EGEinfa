def is_prime(num):
    for i in range(2, int(num ** .5) + 1):
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
        M = min(res) + max(res)
        if M > 2000 and str(M)[-1:] == '8':
            return M
    return 0

cnt = 0
for i in range(1_200_000, 10000000000):
    res = f(i)
    if res:
        print(i, res)
        cnt += 1
        if cnt == 5:
            break
