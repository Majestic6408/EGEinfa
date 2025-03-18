def f(st, end):
    if st < end or st == 24:
        return 0
    if st == end:
        return 1
    if st > end:
        return f(st - 1, end) + f(st - 6, end) + f(st // 2, end)

print(f(34, 29) * f(29, 19) * f(19, 6))