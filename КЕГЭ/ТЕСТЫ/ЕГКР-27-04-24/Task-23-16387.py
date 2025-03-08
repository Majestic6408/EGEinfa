def f(st, end):
    if st > end or st == 16:
        return 0
    if st == end:
        return 1
    if st < end:
        return f(st + 1, end) + f(st + 2, end) + f(st * 3, end)

print(f(2, 9) * f(9, 18))