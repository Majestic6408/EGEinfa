def f(st, end):
    if st > end or st == 16:
        return 0
    if st == end:
        return 1
    if st < end:
        return f(st + 1, end) + f(st + 3, end) + f(st ** 2, end)

print(f(3, 20) * f(20, 26))