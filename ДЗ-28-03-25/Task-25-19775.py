def is_prime(num):
    for i in range(2, int(num ** .5 ) + 1):
        if num % i == 0:
            return 0
    return 1

def f(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)
    if len(res) > 0:
        S = sum(map(int, res))
        if is_prime(S) and S % 145 == 0:
            return S
    return 0

cnt = 0
for i in range(32_500_001, 100_000_000):
    res = f(i)
    if res:
        print(i, res)
        cnt += 1
        if cnt == 7:
            break
