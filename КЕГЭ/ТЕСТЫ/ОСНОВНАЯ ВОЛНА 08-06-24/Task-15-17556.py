def f(A):
    for x in range(1, 1000):
        B = 70 <= x <= 90
        f = (x % A == 0) or (B <= (not(x % 22 == 0)))
        if not f:
            return 0
    return 1

for A in range(1, 1000):
    if f(A):
        print(A)