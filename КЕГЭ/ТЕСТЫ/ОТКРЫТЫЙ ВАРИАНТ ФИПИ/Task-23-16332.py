def f(st, end):
    if st > end:
        return 0
    if st == end:
        return 1
    if st < end:
        return f(st + 1, end) + f(st + 2, end) + f(st * 2, end)

print(f(4, 11) * f(11, 13) * f(13, 15))