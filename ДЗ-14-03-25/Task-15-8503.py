def f(A):
    for x in range(1, 1000):
        f = ((x & 52 != 0) and (x & 36 == 0)) <= (not(x & A == 0))
        if not f:
            return 0
    return 1

for A in range(1, 1000):
    if f(A):
        print(A)