def f(A):
    for x in range(1000):
        f = ((x & 52 != 0) and (x & 48 == 0)) <=(x & A != 0)
        if not f:
            return 0
    return 1

for A in range(1000):
    if f(A):
        print(A)