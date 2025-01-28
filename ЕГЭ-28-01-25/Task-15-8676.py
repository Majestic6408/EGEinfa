def f(B):
    for x in range(1, 10000):
        f = ((x & 500 != 0) and (x & 200 ==0)) <= (not(x & B == 0))
        if not f:
            return 0
    return 1

for B in range(1, 10000):
    if f(B):
        print(B)
        break