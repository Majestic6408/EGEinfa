def is_prime(num):
    if num < 2:
        return 0
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return 0
    return 1

def f(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            if is_prime(i): res.add(i)
            if is_prime(num // i): res.add(num // i)
    res = sorted(res)
    if len(res) >= 2:
        M = min(res) + max(res)
        if M > 2000 and str(M)[-1:] == '8':
            return M
    return 0

cnt = 0
for i in range(1200001, 100000000000000):
    res = f(i)
    if res:
        print(i, res)
        cnt += 1
        if cnt == 5:
            break