def f(st, end, A=False, C=False):
    if st > end:
        return 0
    if st == end:
        return 1
    if A or C:
        return f(st + 5, end) + (f(st * 2, end) or f(st + 2, end))
    return f(st + 2, end, True) + f(st + 5, end) + f(st * 2, end, True)

print(f(7, 23) * f(23, 35))