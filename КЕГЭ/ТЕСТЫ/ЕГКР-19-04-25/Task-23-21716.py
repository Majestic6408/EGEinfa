def f(st, end):
    if st > end or st == 56:
        return 0
    if st == end:
        return 1
    return f(st + 3, end) + f(st + 7, end) + f(st * 3, end)

print(f(12, 40) * f(40, 72) * f(72, 89))