def f(A):
    for x in range(1, 10000):
        f = ((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40)
        if not f:
            return 0
    return 1


for A in range(1, 10000):
    if f(A):
        print(A)