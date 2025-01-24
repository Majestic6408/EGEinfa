def f(A):
    for x in range(90, 101):
        f = (x & 79 != 0) and ((x & 31 == 0) <= (x & A != 0))
        if not f:
            return 0
    return 1

for A in range(1000):
    if f(A):
        print(A)
        break
