def f(A):
    for x in range(300):
        for y in range(300):
            f = (5 < y) or (x > 32) or (x + (2 * y) < A)
            if not f:
                return 0
    return 1

for A in range(300):
    if f(A):
        print(A)