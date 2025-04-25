def f(A):
    for x in range(100_000):
        f = ((x & 8375 != 0) or (x & 6743 != 0)) <= (x & A > 0)
        if not f:
            return 0
    return 1

for A in range(1, 100_000):
    if f(A):
        print(A)