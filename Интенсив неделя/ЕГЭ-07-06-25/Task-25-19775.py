def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return 0
    return 1

def f(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            if is_prime(i):
                res |= {i}
            if is_prime(num // i):
                res |= {num // i}
    res = sorted(res)

    for S in res:
        S = sum(res)
        if S != 0 and S % 145 == 0:
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
