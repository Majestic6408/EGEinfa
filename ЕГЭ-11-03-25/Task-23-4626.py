def f(st, end):
    if st < end:
        return 0
    if st == end:
        return 1
    if st > end:
        return f(st - 2, end) + f(st // 2, end)

print(f(28, 10) * f(10, 1))