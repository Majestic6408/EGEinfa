def f(A):
    for x in range(1, 10000):
        f = (not(x % A == 0)) <= ((x % 14 == 0) <= (not (x % 4 == 0)))
        if not f:
            return 0
    return 1

for A in range(1, 1000):
    if f(A):
        print(A)