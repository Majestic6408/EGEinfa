def f(A):
    for x in range(1, 1000):
        f = ((x % 10 == 0) and (x % 26 == 0) and (x >= 300)) <= (A <= x)
        if not f:
            return 0
    return 1

for A in range(1, 1000):
    if f(A):
        print(A)