def f(st, end, B=False):
    if st > end:
        return 0
    if st == end:
        return 1
    if B:
        return f(st + 2, end) + f(st * 3, end)
    return f(st + 2, end) + f(st ** 2, end, True) + f(st * 3,end)

print(f(2, 64))