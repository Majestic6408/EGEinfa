def f(A):
    for x in range(1, 10000):
        for y in range(1, 10000):
            f = (x - 3 * y < A) or (y > 400) or (x > 56)
            if not f:
                return 0
    return 1

for A in range(1, 100000):
    if f(A):
        print(A)