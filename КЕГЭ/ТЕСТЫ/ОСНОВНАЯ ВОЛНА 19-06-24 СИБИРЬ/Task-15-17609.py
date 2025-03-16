def f(A):
    for x in range(1, 10000):
        f = (x % 33 == 0) <= ((not (x % A == 0)) <= (not (x % 242 == 0)))
        if not f:
            return 0
    return 1

for A in range(1, 10000):
    if f(A):
        print(A)