def f(st, end):
    if st > end or st == 9:
        return 0
    if st == end:
        return 1
    if st < end:
        return f(st + 1, end) + f(st * 2, end)

print(f(2, 12) * f(12, 42))