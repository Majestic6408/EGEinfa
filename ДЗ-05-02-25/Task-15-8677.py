def f(A):
    for x in range(1, 1000):
        B = 80 <= x <= 100
        f = (x % 17 != 0) <= ((not B) or (A < x + 30))
        if not f:
            return 0
    return 1

for A in range(1, 1000):
    if f(A):
        print(A)