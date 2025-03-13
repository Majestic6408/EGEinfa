def f(st, end):
    if st > end or st == 17:
        return 0
    if st == end:
        return 1
    if st < end:
        return f(st + 1, end) + f(st * 2, end)

print(f(1, 10) * f(10, 35))