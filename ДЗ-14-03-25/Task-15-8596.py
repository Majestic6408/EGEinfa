def f(A):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (x >= 11) or (3 * x < y) or (x * y < A)
            if not f:
                return 0
    return 1

for A in range(1, 10000):
    if f(A):
        print(A)