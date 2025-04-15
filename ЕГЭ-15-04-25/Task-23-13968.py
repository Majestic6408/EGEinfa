def f(st, end):
    if st > end or st == 21:
        return 0
    if st == end:
        return 1
    if st < end:
        return f(st + 2, end) + f(st + 3, end) + f(st * 2, end)

print(f(7, 14) * f(14, 32))