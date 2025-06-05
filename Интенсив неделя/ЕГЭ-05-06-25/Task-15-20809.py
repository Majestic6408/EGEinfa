def f(A):
    for x in range(1, 100):
        B = 60 <= x <= 80
        f = (x % A == 0) or (B <= (x % 22 != 0))
        if not f:
            return 0
    return 1

for A in range(1, 100):
    if f(A):
        print(A)