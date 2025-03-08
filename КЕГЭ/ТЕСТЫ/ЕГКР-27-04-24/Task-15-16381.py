def f(A):
    for x in range(1, 1000):
        f = (not(x % A == 0)) <= ((x % 28 == 0) <= (not(x % 49 == 0)))
        if not f:
            return 0
    return 1


for A in range(1, 100000):
    if f(A):
        print(A)