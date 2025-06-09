def f(st, end):
    if st > end or st == 8:
        return 0
    if st == end:
        return 1
    return f(st + 1, end) + f(st + 2, end) + f(st * 2, end)

print(f(3, 14) * f(14, 18))
