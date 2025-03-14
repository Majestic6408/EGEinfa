def f(st, end, A=False):
    if st > end + 1:
        return 0
    if st == end:
        return 1
    if A:
        return f(st * 2, end) + f(st * 3,end)
    return f(st - 1, end, True) + f(st * 2, end) + f(st * 3, end)

print(f(3, 15))