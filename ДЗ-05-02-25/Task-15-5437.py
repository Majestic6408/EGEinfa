def f(A):
    for x in range(1, 1000):
        for y in range(1, 1000):
            for z in range(1, 1000):
                f = ((z % 115 != 0) or (y % 78 != 0) or (x % 51 != 0)) <= (x % A != 0)
                if not f:
                    return 0
    return 1

for A in range(1, 1000):
    if f(A):
        print(A)

