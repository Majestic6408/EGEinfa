def f(A):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = not((x < 7) or (y >= 3 * x + A - 20) or (x >= 34) or (y < 121))
            if f:
                return 0
    return 1

for A in range(1, 1000000):
    if f(A):
        print(A)