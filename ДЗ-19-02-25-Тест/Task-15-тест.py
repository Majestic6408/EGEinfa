def f(A):
    for x in range(90, 101):
        f = not(x & 79 == 0) and ((x & 31 == 0) <= (not(x & A == 0)))
        if not f:
            return 0
    return 1


for A in range(1, 10000):
    if f(A):
        print(A)
