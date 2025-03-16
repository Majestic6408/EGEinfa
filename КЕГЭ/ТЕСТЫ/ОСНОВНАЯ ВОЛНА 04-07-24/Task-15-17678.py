def f(A):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (x + y <= 24) or (y <= x - 2) or (y >= A)
            if not f:
                return 0
    return 1


for A in range(1, 100000):
    if f(A):
        print(A)